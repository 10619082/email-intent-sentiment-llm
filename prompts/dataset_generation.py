general_Instructions = """

To ensure the emails are as realistic as possible, please adhere to the following guidelines in **all prompts**:

- **Varied Lengths:** Emails should range from very short (a few sentences) to very long (several paragraphs), depending on the context.
- **Complexity:** Reflect appropriate complexity levels; complex situations may require detailed explanations.
- **Human Errors:** Include natural human errors such as typos, grammatical mistakes, misspellings, or inconsistent formatting.
- **Tone and Style:** Use a variety of tones, including formal, informal, polite, frustrated, friendly, or sarcastic, as appropriate.
- **Personalization:** Include realistic details like names, booking references (fictional), dates, and personal anecdotes.
- **Formatting Variations:** Use different email structures, such as bullet points, numbered lists, or block texts.

"""

general_dataset_generation = """

**Instructions for the LLM:**

**Objective:** Generate a diverse set of realistic emails covering all predefined categories and parameters for the travel agency domain.

**Guidelines:**

- **Email Structure:** Each email should be formatted with the following CSV fields:
  - `subject`
  - `sender`
  - `recipients`
  - `body`

- **Purpose Categories and Class Balance:** Include emails for all 12 purpose categories, following the specified class balance.

- **Realism Enhancements:** As per the general instructions above.
"""


edge_case_focused_emails = """

**Instructions for the LLM:**

**Objective:** Generate realistic emails that cover edge cases to ensure the model can handle unusual or challenging scenarios.

**Guidelines:**

- **Include Emails With:**
  - Multiple purposes in a single email.
  - Unclear or ambiguous requests.
  - Mixed sentiments.
  - Non-standard formats (e.g., missing subject lines, informal greetings).
  - Missing information.
  - Extremely short or overly long emails.
  - Use of technical jargon or overly simplistic language.

- **Realism Enhancements:** Emphasize human errors and varied lengths.

"""


language_and_cultural_diversity = """

**Instructions for the LLM:**

**Objective:** Generate realistic emails in multiple languages and cultural contexts.

**Guidelines:**

- **Languages to Include:** English, Spanish, French, German, Mandarin.
- **Cultural Nuances:** Reflect appropriate cultural greetings, sign-offs, and etiquette.
- **Realism Enhancements:** Include language proficiency variations and cultural communication styles.

""" 

special_service_requests_ssr_emphasis = """

**Instructions for the LLM:**

**Objective:** Generate realistic emails that highlight special service requests and customer-specific needs.

**Guidelines:**

- **SSR Examples:** Dietary requirements, wheelchair assistance, pet accommodations, etc.
- **Realism Enhancements:** Include personal details, emotional tones, and human errors.

"""

complexity_and_Expert_agent_requirement = """

**Instructions for the LLM:**

**Objective:** Generate realistic emails that are highly complex and require expert agents.

**Guidelines:**

- **Complex Scenarios:** Legal issues, international incidents, medical emergencies, VIP client requests.
- **Realism Enhancements:** Use detailed explanations, technical language, and reflect emotional content.

"""


sentiment_variations = """

**Instructions for the LLM:**

**Objective:** Create realistic emails that cover a wide range of sentiments.

**Guidelines:**

- **Sentiment Distribution:** Positive, Neutral, Negative, Unclear (as specified).
- **Realism Enhancements:** Use emotional language, tone shifts, and human errors reflecting the emotional state.

"""

diverse_writing_styles_and_formats = """

**Instructions for the LLM:**

**Objective:** Produce realistic emails with varying writing styles and formats.

**Guidelines:**

- **Styles:** Formal, casual, emails with typos, use of emojis or internet slang.
- **Formats:** Bullet points, numbered lists, walls of text, inconsistent formatting.
- **Realism Enhancements:** Include varied lengths and formatting errors.

"""

tool_requirement_variations = """

**Instructions for the LLM:**

**Objective:** Generate realistic emails that require different tools for resolution.

**Guidelines:**

- **Tools Examples:** Booking Management System, CRM Software, Flight Rebooking Tool, etc.
- **Realism Enhancements:** Include implied needs, varied complexity, and human errors in tool references.

"""

customer_status_unknown = """

**Instructions for the LLM:**

**Objective:** Create realistic emails where the customer status is not immediately clear.

**Guidelines:**

- **Scenarios:** Lack of identifying information, use of personal emails, vague requests.
- **Realism Enhancements:** Emphasize ambiguity and human errors.

"""

urgency_and_priority_levels = """

**Instructions for the LLM:**

**Objective:** Generate realistic emails with varying urgency to test priority level classification.

**Guidelines:**

- **High Priority Examples:** Emergencies, last-minute changes.
- **Medium and Low Priority Examples:** Policy questions, general inquiries.
- **Realism Enhancements:** Reflect urgency in emotional tone and length.

"""
