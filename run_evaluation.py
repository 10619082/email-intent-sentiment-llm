import os
from dotenv import load_dotenv
from prompt_evaluation_pipeline import PromptEvaluationPipeline, OpenAIExecutor
from prompts.evaluation_prompt_01 import system_prompt as evaluation_system_prompt
from prompts.prompt_03 import system_prompt as classification_system_prompt

def main():
    
    # Your OpenAI API key
    load_dotenv()  
    OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
    
    # Define your prompts
    CLASSIFICATION_PROMPT = classification_system_prompt
    EVALUATION_PROMPT = evaluation_system_prompt
    
    # Initialize different executors for classification and evaluation
    classification_executor = OpenAIExecutor(
        api_key=OPENAI_API_KEY,
        model="gpt-4o-mini",  # More powerful model for classification
        temperature=0.0
    )
    
    evaluation_executor = OpenAIExecutor(
        api_key=OPENAI_API_KEY,
        model="gpt-4o-mini",  # Faster model for evaluation
        temperature=0.0
    )
    
    # Initialize the pipeline with both executors
    pipeline = PromptEvaluationPipeline(
        classification_executor=classification_executor,
        evaluation_executor=evaluation_executor,
        max_threads=10000
    )
    
    # Run the evaluation
    stats = pipeline.run_multiple_evaluations(
        dataset_path="./datasets/combined_dataset.csv",
        output_dir="evaluation_results",
        classification_prompt=CLASSIFICATION_PROMPT,
        evaluation_prompt=EVALUATION_PROMPT,
        num_runs=3
    )
    
    # Print the results
    print("\nEvaluation Complete!")
    print("\nModels used:")
    print(f"Classification: {classification_executor.model}")
    print(f"Evaluation: {evaluation_executor.model}")
    print("\nStatistics:")
    print(f"Mean Accuracy: {stats.mean_accuracy:.2f}%")
    print(f"Median Accuracy: {stats.median_accuracy:.2f}%")
    print(f"Standard Deviation: {stats.std_accuracy:.2f}%") 
    print(f"Accuracy Range: {stats.min_accuracy:.2f}% - {stats.max_accuracy:.2f}%")
    print(f"\nCosts:")
    print(f"Total Classification Cost: ${stats.total_classification_cost:.2f}")
    print(f"Total Evaluation Cost: ${stats.total_evaluation_cost:.2f}")
    print(f"Total Combined Cost: ${(stats.total_classification_cost + stats.total_evaluation_cost):.2f}")
    print(f"Number of Runs: {stats.run_count}")
    
    print("\nDetailed results and visualizations have been saved to the 'evaluation_results' directory")

if __name__ == "__main__":
    main()