# Email Intent and Sentiment Classification using LLMs

## Overview

This repository showcases a comprehensive framework for developing, testing, and evaluating prompt-based workflows to analyze emails for travel agencies. The main goal is to classify emails by their intent, sentiment, and complexity using large language models (LLMs). The repository includes datasets, prompt design, and an evaluation framework to ensure the accuracy and robustness of the implemented system.

---

## Key Features

### 1. **Framework for Prompt Evaluation**
A framework has been developed to evaluate the quality of prompts using another evaluation prompt (`evaluation_prompt_01`). This allows for systematic scoring of classification prompts and iterative improvements.  

- **Details**: See the documentation in [Evaluation Pipeline Documentation.md](https://github.com/10619082/email-intent-sentiment-llm/raw/main/Documentation/Evaluation%20Pipeline%20Documentation.md) for more information.

---

### 2. **Dataset Creation**
A dataset was generated using various prompts to create diverse and realistic email examples, covering a wide range of scenarios and edge cases. This ensures the classification prompts are rigorously tested for robustness and accuracy.

- **Dataset Documentation**: Refer to [Dataset Documentation.md](https://github.com/10619082/email-intent-sentiment-llm/raw/main/Documentation/Dataset%20Documentation.md) for details about dataset generation, structure, and its categories.
- **Code**: The dataset was generated using `Dataset generator.ipynb`, which includes prompt-based generation logic and threading to optimize API calls.

---

### 3. **Prompt Development and Testing**
Various classification and evaluation prompts were created and tested to achieve the highest possible accuracy in email intent classification. The repository includes:

- **Classification Prompts**: Multiple iterations were developed to refine email classification. The classification prompt called `prompt_01` yielded the highest accuracy across the dataset.
- **Evaluation Prompt**: Designed to score and assess classification outputs for accuracy and robustness.
- **Prompts Folder**: All developed prompts are stored in the `prompts` folder for easy reference.

> **Note**: As outlined in [System Diagram and Pipeline for Prompt Testing Documentation.md](https://github.com/10619082/email-intent-sentiment-llm/raw/main/Documentation/System%20Diagram%20and%20Pipeline%20for%20Prompt%20Testing%20Documentation.md), a unified dataset was used to simplify testing while ensuring coverage across diverse scenarios.

---

### 4. **Pipeline Development**
A detailed pipeline was conceptualized and implemented to develop, test, and evaluate prompt accuracy systematically. The pipeline integrates:

- **CI/CD Practices**: Automated testing and evaluation triggered by prompt updates.
- **Accuracy Metrics**: Threshold-based testing across multiple datasets to ensure consistent performance.
- **Dataset Integration**: Unified and diverse datasets for comprehensive evaluation.

For a detailed explanation, refer to [System Diagram and Pipeline for Prompt Testing Documentation.md](https://github.com/10619082/email-intent-sentiment-llm/raw/main/Documentation/System%20Diagram%20and%20Pipeline%20for%20Prompt%20Testing%20Documentation.md).

---

### 5. **Model Selection**
To balance cost and performance:

- **Model for Classification and Evaluation**:
  - The **gpt4o-mini** model was used for classification and evaluation tasks, ensuring cost efficiency while maintaining reasonable accuracy.
- **Model for Dataset Generation**:
  - The **gpt4o** model was utilized to generate the dataset due to its higher generative capabilities, which ensured greater variability and quality in synthetic email examples.

> **Note**: While **gpt4o-mini** effectively handles classification and evaluation, more powerful models can be employed to achieve higher accuracy if budget constraints allow.

---

## How to Use

1. **Dataset Generation**:
   - Use `dataset_generator.ipynb` to generate new datasets for testing prompts.
   - Refer to `Dataset Documentation.md` to understand the dataset structure and categories.

2. **Prompt Testing**:
   - Modify prompts in the `prompts/` folder to test new ideas.
   - Use the provided pipeline in `main_pipeline_code.py` to evaluate prompt performance.

3. **Evaluation Framework**:
   - Use `evaluation_prompt_01.txt` to validate outputs from classification prompts.
   - Analyze results using the metrics generated in `Evaluation Pipeline Documentation.md`.

---

## Key Insights

- **Ground Truth-Free Evaluation**:
  The dataset does not include ground truth labels for email classifications. Instead:
  - The evaluation is fully driven by LLM scoring using the evaluation prompt.
  - This approach reduces the need for manual annotation, saving time and resources.
  - Potential future improvements include hybrid approaches combining LLM evaluation with pattern-matching techniques for higher reliability.

- **Unified Dataset Approach**:
  To simplify testing, multiple dataset categories were combined into a single unified dataset. This method provides a single accuracy metric for evaluating prompts, though it can be expanded to include detailed per-category metrics.

---

## Future Work

- Explore hybrid evaluation methods combining numerical accuracy metrics with LLM-driven scoring.
- Add more dataset diversity by including real-world examples (e.g., anonymized client emails).

---

## License

This repository is open-source and free for educational and research purposes. For commercial use, please contact the repository owner.

---

## Contributions

Contributions are welcome! If you’d like to add more prompts, improve the evaluation framework, or enhance the dataset, feel free to open a pull request.