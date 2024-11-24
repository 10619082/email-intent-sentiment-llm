# Documentation: AI Assistant for Travel Agency Email Analysis

## Overview

This document describes the functionality and objective of a prompt designed for an AI assistant tasked with analyzing emails for travel agencies. The AI processes email communications to extract key details and classify them into predefined categories. The output is structured as a JSON object, ensuring consistency and usability for downstream systems or agents.

---

## Objective

The main goal of the AI assistant is to:

1. Accurately **extract and classify attributes** from customer emails to facilitate efficient handling by human agents or automated workflows.
2. Generate a **structured JSON output** that includes purpose, sentiment, complexity, priority, tools required, customer status, preferred language, and any special requests.
3. Enhance operational efficiency by recommending agent expertise and assessing urgency based on the email content.

---

## Functionality

The prompt equips the AI assistant with the following capabilities:

1. **Purpose Detection**: Classifies the email's primary intent into one of twelve predefined categories, such as group bookings, cancellations, special requests, or feedback.
2. **Sentiment Analysis**: Identifies the emotional tone of the email as positive, neutral, negative, or unclear.
3. **Complexity Assessment**: Determines the complexity level (Low, Medium, High) of the request based on the required effort and expertise.
4. **Agent Type Recommendation**: Suggests whether a Junior, Senior, or Expert agent should handle the request, considering its complexity and urgency.
5. **Priority Evaluation**: Classifies the urgency level of the email (Low, Medium, High) to help prioritize responses.
6. **Tool Identification**: Lists the systems or resources required to address the email, such as booking systems, knowledge bases, or invoice tools.
7. **Customer Status Detection**: Identifies whether the sender is a customer, non-customer, or their status is unknown.
8. **Preferred Language Extraction**: Determines the language preferred for the response based on email content or sender profile.
9. **SSR Request Identification**: Extracts any special service requests, such as wheelchair assistance or specific meal preferences.

---

## Input Specifications

The AI processes emails with the following components:

- **Subject**: The email's subject line.
- **Sender**: The sender's email address.
- **Recipients**: The recipient(s) of the email.
- **Body**: The main content of the email.

---

## Output Format

The AI generates a structured JSON output with the following fields:

- **Purpose**: The classified intent of the email based on predefined categories.
- **Sentiment**: The emotional tone of the email (Positive, Neutral, Negative, Unclear).
- **Complexity Level**: The effort required to address the request (Low, Medium, High).
- **Agent Type**: The recommended level of expertise for handling the request (Junior, Senior, Expert).
- **Priority Level**: The urgency of the request (Low, Medium, High).
- **Required Tools**: A list of tools needed to resolve the issue.
- **Customer Status**: The sender's status (Non-Customer, Customer, Unknown).
- **Preferred Language**: The language preferred for the response.
- **SSR Requests**: Special service requests explicitly mentioned in the email.

---

## Features in Detail

### **1. Purpose Categorization**
The AI maps the email's primary intent to one of the following categories:
- Group bookings or corporate events.
- Booking changes or additional services.
- Booking cancellations.
- Dietary or accessibility requests.
- Inquiries about baggage policies or allowances.
- Urgent support for disruptions (e.g., missed flights).
- Refund inquiries.
- Pricing and promotional inquiries.
- Travel insurance inquiries or purchases.
- Loyalty program updates or inquiries.
- Feedback or complaints.
- Lost and found inquiries.

### **2. Sentiment Detection**
The AI identifies the overall emotional tone, ensuring accurate classification as:
- **Positive**: Satisfaction or enthusiasm.
- **Neutral**: Informational and non-emotive.
- **Negative**: Complaints or dissatisfaction.
- **Unclear**: Ambiguous emotional tone.

### **3. Complexity and Priority Assessment**
The AI evaluates the difficulty and urgency of the email:
- **Complexity Levels**:
  - Low: Simple inquiries requiring minimal effort.
  - Medium: Requests involving moderate effort or analysis.
  - High: Complex, urgent, or multi-step resolutions.
- **Priority Levels**:
  - Low: Tasks that can be delayed without impacting service quality.
  - Medium: Moderately time-sensitive tasks.
  - High: Urgent issues requiring immediate attention.

### **4. Agent and Tool Recommendations**
Based on the request's complexity and urgency, the AI recommends:
- **Agent Type**: The expertise level required (Junior, Senior, Expert).
- **Required Tools**: Specific systems or resources, such as booking platforms or FAQs.

### **5. Special Service Requests and Customer Details**
The AI identifies:
- **SSR Requests**: Additional accommodations like wheelchair access or dietary needs.
- **Customer Status**: Whether the sender is a current customer, non-customer, or unknown.

Here's how you can introduce the JSON output in the **Classification Prompt Documentation**:

---

## Example Output

The Classification Prompt processes the email data and produces a structured **JSON object**. This JSON serves as the standardized output for future integration with downstream systems.

### Example JSON Output

```json
{
  "purpose": "Group Request",
  "sentiment": "Neutral",
  "complexity_level": "Medium",
  "agent_type": "Senior",
  "priority_level": "Medium",
  "required_tools": ["GDS", "Pricing database", "Itinerary planner"],
  "customer_status": "Unknown",
  "preferred_language": "English",
  "ssr_requests": []
}
```
