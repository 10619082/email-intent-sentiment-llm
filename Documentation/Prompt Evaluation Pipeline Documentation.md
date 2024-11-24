# Prompt Evaluation Pipeline

A Python framework for evaluating and benchmarking large language model prompts through parallel processing and comprehensive analytics.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Configuration](#configuration)
- [Output and Visualization](#output-and-visualization)
- [Cost Management](#cost-management)
- [API Reference](#api-reference)

## Overview

The Prompt Evaluation Pipeline is a sophisticated framework designed to evaluate the performance of language model prompts across multiple runs. It supports parallel processing, comprehensive metrics collection, and automated visualization generation, making it ideal for prompt engineering and optimization workflows.

## Features

- Multi-threaded evaluation pipeline
- Support for multiple LLM providers (currently OpenAI)
- Automated cost calculation and tracking
- Comprehensive statistical analysis
- Interactive visualizations
- Thread-safe operations
- Configurable execution parameters
- Detailed error handling and logging

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/prompt-evaluation-pipeline.git

# Install dependencies
pip install -r requirements.txt
```

Required dependencies:
- openai
- pandas
- numpy
- plotly
- python-dotenv
- concurrent.futures (standard library)

## Usage

### Basic Example

```python
from dotenv import load_dotenv
from prompt_evaluation_pipeline import PromptEvaluationPipeline, OpenAIExecutor

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize executors
classification_executor = OpenAIExecutor(
    api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.0
)

evaluation_executor = OpenAIExecutor(
    api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.0
)

# Create pipeline
pipeline = PromptEvaluationPipeline(
    classification_executor=classification_executor,
    evaluation_executor=evaluation_executor,
    max_threads=10000
)

# Run evaluation
stats = pipeline.run_multiple_evaluations(
    dataset_path="dataset.csv",
    output_dir="evaluation_results",
    classification_prompt=YOUR_CLASSIFICATION_PROMPT,
    evaluation_prompt=YOUR_EVALUATION_PROMPT,
    num_runs=3
)
```

## Architecture

### Core Components

1. **TokenUsage (dataclass)**
   - Tracks token consumption for cost calculation
   - Fields: `prompt_tokens`, `completion_tokens`

2. **EmailData (dataclass)**
   - Represents email content structure
   - Fields: `subject`, `sender`, `recipients`, `body`

3. **EvaluationResult (dataclass)**
   - Stores individual evaluation results
   - Fields: `id`, `subject`, `predicted_json`, `validation_score`, `validation_evaluation`, `classification_cost`, `evaluation_cost`, `run_id`

4. **RunStatistics (NamedTuple)**
   - Aggregates statistical results
   - Fields: accuracy metrics, costs, and run count

5. **CostCalculator**
   - Handles cost calculations for different models
   - Supports multiple pricing tiers and models

### Key Classes

1. **PromptExecutor (ABC)**
   - Abstract base class for executing prompts
   - Defines interface for different LLM providers

2. **OpenAIExecutor**
   - OpenAI-specific implementation
   - Handles API calls and response processing

3. **EmailProcessor**
   - Processes individual emails
   - Manages classification and evaluation workflows

4. **PromptEvaluationPipeline**
   - Main pipeline orchestrator
   - Handles multi-threading and result aggregation

## Configuration

### Model Configuration

```python
COST_PER_TOKEN = {
    "gpt-4": {
        "input": 30 / 1000000,
        "output": 60 / 1000000
    },
    "gpt-4o": {
        "input": 2.5 / 1000000,
        "cached_input": 1.25 / 1000000,
        "output": 10 / 1000000
    },
    "gpt-4o-mini": {
        "input": 0.15 / 1000000,
        "cached_input": 0.075 / 1000000,
        "output": 0.600 / 1000000
    }
}
```

### Thread Configuration

```python
pipeline = PromptEvaluationPipeline(
    classification_executor=executor,
    evaluation_executor=executor,
    max_threads=1000
)
```

## Output and Visualization

### Generated Files

The pipeline generates several output files in the specified output directory:

1. `all_runs_{timestamp}.csv`: Complete results dataset

2. `accuracy_distribution_{timestamp}.html`: Box plot visualization  
   ![Box Plot Visualization](images/Box%20plot.png)

3. `accuracy_violin_{timestamp}.html`: Violin plot for detailed distribution  
   ![Violin Plot Visualization](images/Violin.png)

4. `statistics_summary_{timestamp}.html`: Interactive summary dashboard  
   ![Statistics Summary Dashboard](images/Gauge%20chart.png)

### Visualization Types

1. **Box Plot**
   - Shows accuracy distribution across runs
   - Identifies outliers and trends

2. **Violin Plot**
   - Detailed distribution visualization
   - Includes individual data points

3. **Statistical Summary**
   - Interactive gauge chart
   - Cost breakdown and key metrics

## Cost Management

The pipeline includes sophisticated cost tracking features:

- Per-token cost calculation
- Separate tracking for classification and evaluation
- Support for different pricing tiers
- Detailed cost breakdown in results

## API Reference

### PromptEvaluationPipeline

```python
def run_multiple_evaluations(
    self,
    dataset_path: str,
    output_dir: str,
    classification_prompt: str,
    evaluation_prompt: str,
    num_runs: int = 5
) -> RunStatistics
```

#### Parameters:
- `dataset_path`: Path to the input dataset (CSV format)
- `output_dir`: Directory for saving results and visualizations
- `classification_prompt`: Primary classification prompt template
- `evaluation_prompt`: Evaluation prompt template
- `num_runs`: Number of evaluation runs to perform

#### Returns:
- `RunStatistics` containing aggregated results and metrics

### Error Handling

The pipeline implements comprehensive error handling:
- Thread-safe operations using locks
- Failure handling for individual emails
- Error logging and reporting
