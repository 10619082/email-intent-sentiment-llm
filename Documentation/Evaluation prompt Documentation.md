# Documentation: Evaluation Prompt for Travel Agency Email Analysis

## Overview

This document outlines the functionality and objective of a prompt designed to evaluate the output of an AI model that analyzes emails for travel agencies. The evaluation assesses the quality, accuracy, and completeness of the AI-generated JSON output based on predefined criteria. A quality score between **0 and 10** is assigned, accompanied by detailed feedback to highlight strengths and suggest improvements.

---

## Objective

The purpose of this prompt is to:

1. **Validate AI-generated JSON outputs**: Ensure that the extracted and classified attributes from emails align with the original email content.
2. **Assign a quality score**: Quantify the accuracy and relevance of the AI's output with a score ranging from 0 to 10.
3. **Provide actionable feedback**: Offer constructive suggestions to improve the output where necessary.
4. **Facilitate continuous improvement**: Enable iterative refinement of the classification model through comprehensive evaluation.

---

## Evaluation Criteria

The evaluation focuses on the following aspects of the AI's JSON output:

1. **Purpose**:
   - Verify if the `purpose` field accurately captures the primary intent of the email.
   - Ensure it aligns with one of the following predefined categories:
     - Group Request
     - Change Request
     - Cancellation Request
     - Special Requests
     - Baggage Information
     - Unexpected Issues
     - Refund Request
     - Pricing and Promotions
     - Travel Insurance Request
     - Loyalty Programs
     - Feedback or Complaints
     - Lost and Found Request

2. **Sentiment**:
   - Assess if the `sentiment` reflects the emotional tone of the email.
   - Must match one of the following:
     - Positive
     - Neutral
     - Negative
     - Unclear

3. **Complexity Level**:
   - Validate the complexity level (Low, Medium, High) based on the nature of the request and the expertise required for resolution.

4. **Agent Type**:
   - Confirm whether the recommended agent type (Junior, Senior, Expert) aligns with the complexity and urgency of the email.

5. **Priority Level**:
   - Ensure the urgency (Low, Medium, High) matches the email's time sensitivity and potential impact.

6. **Required Tools**:
   - Check whether the listed tools (e.g., GDS overlay, invoice system) are appropriate for handling the email.

7. **Customer Status**:
   - Verify if the sender's status is accurately categorized as:
     - Non-Customer
     - Customer
     - Unknown

8. **Preferred Language**:
   - Ensure the preferred language is correctly identified from the email content.

9. **SSR Requests**:
   - Confirm that any special service requests (e.g., wheelchair assistance) are properly identified and listed.

---

## Scoring Guidelines

### **Score Breakdown**
- **0**: The output is completely incorrect and misrepresents the email content.
- **1-3**: The output is largely inaccurate with major issues in classification or extraction.
- **4-6**: The output partially captures the email content but has several inaccuracies or omissions.
- **7-8**: The output is mostly correct, with only minor issues.
- **9-10**: The output is highly accurate and aligns perfectly with the email content.

### **Factors for Scoring**
1. **Accuracy**: How well the JSON output represents the email's content.
2. **Completeness**: Whether all fields are populated as expected based on the email.
3. **Consistency**: Adherence to predefined labels and output formats.
4. **Usability**: Whether the output can be effectively used for downstream processes.

---

## Input Specifications

The evaluation process involves two components:

1. **Email Input**:
   - **Subject**: The subject line of the email.
   - **Sender**: The sender's email address.
   - **Recipients**: The recipient(s) of the email.
   - **Body**: The main content of the email.

2. **Actual Output**:
   - A JSON object generated by the classification model, containing fields like:
     - `purpose`
     - `sentiment`
     - `complexity_level`
     - `agent_type`
     - `priority_level`
     - `required_tools`
     - `customer_status`
     - `preferred_language`
     - `ssr_requests`

---

## Output Format

The evaluation prompt generates a structured JSON output containing:

- **Score**: A numeric value from 0 to 10 reflecting the quality of the JSON output.
- **Evaluation**: A concise explanation of the assigned score, highlighting positive aspects, discrepancies, and areas for improvement.

### **Example Output**
```json
{
  "score": 8,
  "evaluation": "The JSON output is mostly accurate, correctly identifying the purpose, sentiment, and complexity level. However, the priority level could be improved, as the email suggests higher urgency than reflected in the output."
}
