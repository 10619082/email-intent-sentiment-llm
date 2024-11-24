# Travel Agency Email Dataset Documentation

## Dataset Overview

The dataset consists of 720 synthetic emails distributed across 10 distinct categories, each designed to capture different aspects of customer-travel agency communications. The emails are stored in separate CSV files, with each file representing a specific scenario or use case.

## Dataset Generation

The dataset was generated through API calls to GPT-4o, using a two-level prompt system:

- A base prompt containing general guidelines for generating realistic emails
- Ten specific prompts for each scenario category (edge cases, cultural diversity, etc.)

Generation occurred in batches of 12 emails per API call (one per each purpouse), using a threading system to optimize the process.

## Dataset Structure

### File Format

Each CSV file contains emails with the following fields:

- `subject`: Email subject line
- `sender`: Customer email address
- `recipients`: Travel agency email (<support@travelagency.com>)
- `body`: Main email content

### **Ground Truth Omission**

In this dataset, ground truth labels for the correct classification of emails have been intentionally omitted. This approach simplifies the validation process by relying entirely on the LLM for scoring and evaluation. It eliminates the need for manual labeling, reduces costs, and enhances scalability. While this introduces some reliance on the LLM’s interpretative accuracy, it aligns with a dynamic, flexible pipeline that can adapt to evolving business needs and datasets.

### Dataset Categories

1. **General Dataset** (120 emails)
   - Purpose: Baseline communications covering standard travel agency interactions
   - Characteristics: Balanced representation of all purpose categories
   - Use Case: General prompts training and basic interaction patterns

2. **Edge Cases** (60 emails)
   - Purpose: Testing model robustness with unusual scenarios
   - Key Features:
     - Multi-purpose emails
     - Ambiguous requests
     - Non-standard formatting
     - Missing information scenarios
     - Extremely short/long communications
   - Use Case: Model stress testing and edge case handling

3. **Language and Cultural Diversity** (36 emails)
   - Languages: English, Spanish, French, German, Mandarin
   - Cultural Elements:
     - Region-specific greetings
     - Cultural etiquette
     - Local customs and expectations

4. **Special Service Requests (SSR)** (60 emails)
   - Focus Areas:
     - Dietary requirements
     - Accessibility needs
     - Medical accommodations
     - Pet travel arrangements
   - Emotional Content: High personal involvement

5. **High Complexity** (120 emails)
   - Scenarios:
     - Legal issues
     - International incidents
     - Medical emergencies

6. **Sentiment Variations** (120 emails)
   - Distribution:
     - Positive
     - Neutral
     - Negative
     - Unclear

7. **Diverse Writing Styles** (60 emails)
   - Style Categories:
     - Formal business
     - Casual/informal
     - Technical
     - Error-prone
   - Format Variations:
     - Structured lists
     - Narrative style
     - Mixed formats

8. **Tool Requirement Variations** (36 emails)
   - System References:
     - Booking systems
     - CRM software
     - Payment platforms
     - Loyalty programs
     - Ecc ...

9. **Customer Status Unknown** (36 emails)
   - Characteristics:
     - Incomplete information
     - Ambiguous identity
     - Unclear booking references

10. **Urgency and Priority Levels** (72 emails)
    - Priority Distribution:
      - High
      - Medium
      - Low

## Generation Criteria

### Authenticity Markers

1. **Human Elements**
   - Natural language patterns
   - Typos and corrections
   - Topic drift
   - Personal anecdotes
   - Mixed emotions
   - Regional variations

2. **Technical Authenticity**
   - Mobile signatures
   - Email threading
   - Formatting inconsistencies
   - Real-world references
   - Time zone variations

3. **Communication Patterns**
   - Multi-topic threads
   - Follow-up references
   - Previous interaction mentions
   - Incomplete information
   - Natural digressions

### Purpose Categories

Each email is tagged with one or more of these primary purposes:

1. Group Requests
2. Change Requests
3. Cancellation Requests
4. Special Requests
5. Baggage Information
6. Unexpected Issues
7. Refund Requests
8. Pricing/Promotions
9. Travel Insurance
10. Loyalty Programs
11. Feedback/Complaints
12. Lost and Found

### Contextual Elements

1. **Situational Complexity**
   - Multiple issues per email
   - Partial information
   - Reference to external events
   - Previous communication mentions
   - Booking reference variations

2. **Emotional Content**
   - Mixed emotional states
   - Subtle undertones
   - Passive-aggressive elements
   - Politeness variations
   - Urgency indicators

### Dataset Applications

The dataset was specifically designed to validate and refine email analysis prompts with the following capabilities
