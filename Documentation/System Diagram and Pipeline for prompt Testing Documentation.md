# System Diagram and Pipeline for Prompt Testing Documentation

## Overview

This document outlines the systematic approach for building, testing, and validating prompt-based workflows, specifically designed for travel agency email analysis. The pipeline ensures that every change to the prompts undergoes rigorous evaluation before being deployed to production. Below is a detailed explanation of the testing and validation pipeline, accompanied by system diagrams.


## Main Pipeline Workflow

The main pipeline, as shown below, captures the process from prompt creation to deployment and monitoring. It integrates **CI/CD** practices and error-handling mechanisms to maintain high standards in production.

### **Diagram: Main Pipeline Workflow**

![Main Pipeline Workflow](https://github.com/10619082/email-intent-sentiment-llm/raw/main/Diagrams/pipeline_diagram_00.png)

### **Steps of the Pipeline**

1. **Create/Edit a Prompt**
   - Prompts are created or updated to reflect changes in business requirements, improving their accuracy and effectiveness.

2. **Commit and Push to Git**
   - Changes are committed to the version control system (e.g., Git) to track modifications and initiate automated pipelines.

3. **CI/CD Pipeline Initiated**
   - The continuous integration and delivery pipeline is triggered automatically upon detecting changes in the repository.

4. **Automated Testing**
   - Unit tests and integration tests are executed to ensure the prompt adheres to expected functionality.

5. **Calculate Metrics**
   - A key part of this step is **evaluating prompt performance across multiple datasets**. Accuracy thresholds are defined for each dataset, and the prompt must meet or exceed these thresholds to proceed further. The next section explains how this process is implemented.

6. **Decision Point: Metrics Meet Criteria?**
   - If the metrics exceed predefined thresholds for all datasets, the prompt proceeds to the review stage.
   - If even one dataset falls short of its required accuracy, the prompt engineer is notified to refine the prompt.

7. **Merge to Production and Deploy**
   - Approved prompts are merged into the production branch and deployed for live use.

8. **Monitor Performance in Production**
   - Continuous monitoring of production prompts ensures they maintain expected performance levels.

9. **Error Logging and Analysis**
   - Errors are logged, and analysis is performed to understand any discrepancies or issues faced by the deployed prompt.

10. **Update Dataset with New Examples**
    - The dataset is enriched with new examples based on feedback and errors observed in production, creating a feedback loop for continuous improvement.


## Dataset-Based Validation Workflow

### **Diagram: Dataset Validation Workflow**

![Dataset-Based Validation](https://github.com/10619082/email-intent-sentiment-llm/raw/main/Diagrams/pipeline_diagram_metric.png)

### **How Dataset Validation Works**

As part of **Step 5: Calculate Metrics**, the prompt is evaluated across multiple datasets. Each dataset is tailored to a specific challenge or use case, with predefined accuracy thresholds that the prompt must meet or exceed. These datasets ensure the prompt performs well under diverse scenarios, such as:

1. **General Dataset**: Covers balanced examples of typical use cases.
2. **Edge Cases**: Tests rare or unusual scenarios.
3. **High Complexity**: Evaluates the prompt's ability to handle intricate or multi-step processes.
4. **Sentiment Variations**: Measures accuracy in detecting emotional tones.
5. **Language and Cultural Diversity**: Ensures performance across multilingual and culturally varied inputs.
6. **Special Service Requests**: Focuses on identifying SSR-related requests like accessibility needs.
7. **Customer Status (Unknown)**: Verifies classification when the sender’s customer status is unclear.

Each dataset has a predefined **accuracy threshold** that reflects its importance and challenge level. For example, high-complexity datasets might require an accuracy of 83%, while general datasets might require 90%. If the prompt falls short in **even one dataset**, it is flagged for improvement and cannot proceed to production.


## Notes on Dataset Validation

- The accuracy thresholds seen in the diagram are **fictitious examples** and should be adapted to match the real-world requirements of your specific use case.
- A good testing mechanism incorporates dataset diversity to ensure the robustness of the prompt under various scenarios.


## Simplified Validation for Repository Experiments

For simplicity in the experiments conducted within this repository, all datasets were combined into a **single comprehensive dataset**, and a unified accuracy metric was calculated. This approach allowed for a streamlined evaluation of multiple prompts during testing.