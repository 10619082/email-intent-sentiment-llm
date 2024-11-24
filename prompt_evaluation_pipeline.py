import openai
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, NamedTuple
from abc import ABC, abstractmethod
from datetime import datetime


@dataclass
class TokenUsage:
    prompt_tokens: int
    completion_tokens: int

@dataclass
class EmailData:
    subject: str
    sender: str
    recipients: str
    body: str

@dataclass
class EvaluationResult:
    id: int
    subject: str
    predicted_json: Optional[str]
    validation_score: Optional[float]
    validation_evaluation: str
    classification_cost: float
    evaluation_cost: float
    run_id: int

class RunStatistics(NamedTuple):
    mean_accuracy: float
    median_accuracy: float
    std_accuracy: float
    min_accuracy: float
    max_accuracy: float
    total_classification_cost: float
    total_evaluation_cost: float
    run_count: int

class CostCalculator:
    """Handles cost calculations for different models and token usage."""
    
    COST_PER_TOKEN = {
        "gpt-4": {"input": 30 / 1000000, "output": 60 / 1000000},
        "gpt-4o": {"input": 2.5 / 1000000, 
                   "cached_input": 1.25 / 1000000,
                   "output": 10 / 1000000},
        "gpt-4o-mini": {
            "input": 0.15 / 1000000,
            "cached_input": 0.075 / 1000000,
            "output": 0.600 / 1000000,
        }
    }

    @classmethod
    def calculate(cls, usage: TokenUsage, model: str) -> float:
        if model not in cls.COST_PER_TOKEN:
            raise ValueError(f"Unsupported model: {model}")
            
        costs = cls.COST_PER_TOKEN[model]
        if model == "gpt-4":
            return (usage.prompt_tokens * costs["input"] +  usage.completion_tokens * costs["output"])
        elif model == "gpt-4o-mini":
            return (usage.prompt_tokens * costs["input"] +  usage.prompt_tokens * costs["cached_input"] + usage.completion_tokens * costs["output"])
        elif model == "gpt-4o":
            return (usage.prompt_tokens * costs["input"] +  usage.prompt_tokens * costs["cached_input"] + usage.completion_tokens * costs["output"])


class PromptExecutor(ABC):
    """Abstract base class for executing prompts."""
    
    def __init__(self, model: str, temperature: float = 0.0):
        self.model = model
        self.temperature = temperature
    
    @abstractmethod
    def execute(self, prompt: str) -> Tuple[dict, float]:
        pass

class OpenAIExecutor(PromptExecutor):
    """Handles OpenAI API calls."""
    
    def __init__(self, api_key: str, model: str, temperature: float = 0.0):
        super().__init__(model, temperature)
        self.client = openai.OpenAI(api_key=api_key)
    
    def execute(self, prompt: str) -> Tuple[dict, float]:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": prompt}],
            temperature=self.temperature
        )
        
        cost = CostCalculator.calculate(response.usage, self.model)
        content = response.choices[0].message.content
        
        # Clean up JSON response
        content = content.replace('```json\n', '').replace('```', '').strip()
        return json.loads(content), cost

class EmailProcessor:
    """Handles the processing of individual emails."""
    
    def __init__(self, classification_executor: PromptExecutor, evaluation_executor: PromptExecutor):
        self.classification_executor = classification_executor
        self.evaluation_executor = evaluation_executor
    
    def process_single_email(
        self, 
        email_data: EmailData, 
        classification_prompt: str, 
        evaluation_prompt: str, 
        email_id: int,
        run_id: int
    ) -> EvaluationResult:
        try:
            # Execute classification prompt with classification executor
            classification_input = classification_prompt.format(
                subject=email_data.subject,
                sender=email_data.sender,
                recipients=email_data.recipients,
                body=email_data.body
            )
            primary_output, classification_cost = self.classification_executor.execute(classification_input)
            
            # Execute validation prompt with evaluation executor
            validation_input = evaluation_prompt.format(
                subject=email_data.subject,
                sender=email_data.sender,
                recipients=email_data.recipients,
                body=email_data.body,
                output=json.dumps(primary_output)
            )
            validation_result, evaluation_cost = self.evaluation_executor.execute(validation_input)
            
            return EvaluationResult(
                id=email_id,
                subject=email_data.subject,
                predicted_json=json.dumps(primary_output),
                validation_score=validation_result["score"],
                validation_evaluation=validation_result["evaluation"],
                classification_cost=classification_cost,
                evaluation_cost=evaluation_cost,
                run_id=run_id
            )
            
        except Exception as e:
            return EvaluationResult(
                id=email_id,
                subject=email_data.subject,
                predicted_json=None,
                validation_score=None,
                validation_evaluation=str(e),
                classification_cost=0.0,
                evaluation_cost=0.0,
                run_id=run_id
            )

class PromptEvaluationPipeline:
    """Main pipeline for evaluating prompts on a dataset with multiple runs."""
    
    def __init__(
        self,
        classification_executor: PromptExecutor,
        evaluation_executor: PromptExecutor,
        max_threads: int = 5
    ):
        self.processor = EmailProcessor(classification_executor, evaluation_executor)
        self.max_threads = max_threads
        self.classification_model = classification_executor.model
        self.evaluation_model = evaluation_executor.model
    
    def run_multiple_evaluations(
        self,
        dataset_path: str,
        output_dir: str,
        classification_prompt: str,
        evaluation_prompt: str,
        num_runs: int = 5
    ) -> RunStatistics:
        """Execute multiple evaluation runs and compute statistics."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        all_results = []
        run_summaries = []

        for run_id in range(num_runs):
            print(f"\nStarting run {run_id + 1}/{num_runs}")
            results, run_accuracy, run_classification_cost, run_evaluation_cost = self._process_dataset(
                dataset_path,
                classification_prompt,
                evaluation_prompt,
                run_id
            )
            all_results.extend(results)
            run_summaries.append({
                'run_id': run_id,
                'accuracy': run_accuracy,
                'classification_cost': run_classification_cost,
                'evaluation_cost': run_evaluation_cost
            })

        # Save all results with model information
        results_df = pd.DataFrame([vars(r) for r in all_results])
        results_df['classification_model'] = self.classification_model
        results_df['evaluation_model'] = self.evaluation_model
        results_df.to_csv(f"{output_dir}/all_runs_{timestamp}.csv", index=False)
        
        # Calculate statistics
        accuracies = [s['accuracy'] for s in run_summaries]
        total_classification_cost = sum(s['classification_cost'] for s in run_summaries)
        total_evaluation_cost = sum(s['evaluation_cost'] for s in run_summaries)
        
        stats = RunStatistics(
            mean_accuracy=np.mean(accuracies),
            median_accuracy=np.median(accuracies),
            std_accuracy=np.std(accuracies),
            min_accuracy=min(accuracies),
            max_accuracy=max(accuracies),
            total_classification_cost=total_classification_cost,
            total_evaluation_cost=total_evaluation_cost,
            run_count=num_runs
        )
        
        # Generate and save visualizations
        self._plot_run_statistics(results_df, stats, output_dir, timestamp)
        
        return stats


    def _process_dataset(
            self,
            dataset_path: str,
            classification_prompt: str,
            evaluation_prompt: str,
            run_id: int
        ) -> Tuple[List[EvaluationResult], float, float, float]:
            """Process the dataset for a single run."""
            df = pd.read_csv(dataset_path, delimiter=";")
            results = []
            total_score = 0
            total_classification_cost = 0
            total_evaluation_cost = 0
            
            # Create locks for thread-safe operations
            score_lock = Lock()
            cost_lock = Lock()
            results_lock = Lock()
            
            with ThreadPoolExecutor(self.max_threads) as executor:
                futures = []
                for index, row in df.iterrows():
                    email_data = EmailData(
                        subject=row["subject"],
                        sender=row["sender"],
                        recipients=row["recipients"],
                        body=row["body"]
                    )
                    future = executor.submit(
                        self.processor.process_single_email,
                        email_data,
                        classification_prompt,
                        evaluation_prompt,
                        index,
                        run_id
                    )
                    futures.append(future)
                
                for future in as_completed(futures):
                    try:
                        result = future.result()
                        
                        # Thread-safe operations
                        with results_lock:
                            results.append(result)
                        
                        if result.validation_score is not None:
                            with score_lock:
                                total_score += result.validation_score
                        
                        with cost_lock:
                            total_classification_cost += result.classification_cost
                            total_evaluation_cost += result.evaluation_cost
                            
                    except Exception as e:
                        print(f"Error processing email: {e}")
            
            num_emails = len(df)
            weighted_accuracy = total_score / num_emails if num_emails > 0 else 0
            
            return results, weighted_accuracy, total_classification_cost, total_evaluation_cost
    
    def _plot_run_statistics(
        self,
        results_df: pd.DataFrame,
        stats: RunStatistics,
        output_dir: str,
        timestamp: str
    ) -> None:
        """Generate and save statistical visualizations."""
        # 1. Box plot of accuracy distribution across runs
        fig_box = px.box(
            results_df,
            x="run_id",
            y="validation_score",
            title="Accuracy Distribution Across Runs",
            labels={"run_id": "Run ID", "validation_score": "Accuracy (%)"}
        )
        fig_box.write_html(f"{output_dir}/accuracy_distribution_{timestamp}.html")
        
        # 2. Violin plot for detailed distribution visualization
        fig_violin = px.violin(
            results_df,
            x="run_id",
            y="validation_score",
            title="Detailed Accuracy Distribution",
            box=True,
            points="all"
        )
        fig_violin.write_html(f"{output_dir}/accuracy_violin_{timestamp}.html")
        
        # 3. Statistical summary plot
        total_cost = stats.total_classification_cost + stats.total_evaluation_cost
        
        fig_stats = go.Figure()
        fig_stats.add_trace(go.Indicator(
            mode="number+gauge+delta",
            value=stats.mean_accuracy,
            delta={'reference': stats.median_accuracy},
            gauge={
                'axis': {'range': [stats.min_accuracy, stats.max_accuracy]},
                'steps': [
                    {'range': [stats.min_accuracy, stats.mean_accuracy], 'color': "lightgray"},
                    {'range': [stats.mean_accuracy, stats.max_accuracy], 'color': "gray"}  # Fixed this line
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': stats.mean_accuracy + stats.std_accuracy
                }
            },
            title={
                'text': f"Accuracy Statistics (n={stats.run_count})<br>" +
                    f"<span style='font-size:0.8em'>Total Cost: ${total_cost:.2f}</span>"
            }
        ))
        fig_stats.write_html(f"{output_dir}/statistics_summary_{timestamp}.html")