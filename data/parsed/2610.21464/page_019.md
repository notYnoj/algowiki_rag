## Appendix F. Prompt Templates

Prompt for RAG system.

Use the retrieved contexts to answer the question. Your answer should be concise.

Contexts:

[Document 1]

[Document 2]

...

[Document 5]

Question: {query}

Answer:

Prompt for generate topic subdomains.

Identify 10 distinct subdomains, aspects, or user-context areas within the topic "{topic}".

Requirements:

- Be broad enough to cover different real user interests.

- Be specific to the topic, but do not assume access to any hidden test set.

- Avoid medical-only categories unless the topic itself is medical.

Output one item per line, no numbering, no explanations.

Prompt for generate train queries.

Generate {count} realistic user questions for a retrieval- augmented QA system.

Main topic: "{topic}"

Subdomain/aspect: "{subtopic}"

Question intent: {intent}

Requirements:

- Questions should be diverse, natural, and specific.

- Include both beginner and advanced user wording when appropriate.

- Do not assume the domain is medicine, finance, or any other fixed field.

- Do not repeat questions.

Output one question per line, no numbering.

Prompt for generate test queries subdomains.

Identify 12 distinct subdomains, aspects, or user-context areas within the topic "{topic}".

These subdomains will be used to generate ADVICE / DECISION questions .

Requirements:

- Be broad enough to cover different real user interests.

- Be specific to the topic.

- Include practical decision areas such as options, alternatives, management, monitoring, risks, costs, special cases, and long- term use when relevant.

- Do not mention target or placeholder entities listed here: {exclude\_terms\_or\_none}.

- Return ONLY a JSON array of strings.

Prompt for generate test queries.

Generate realistic user queries for a retrieval QA evaluation set.

Topic: {topic}

Subdomain/aspect: {subtopic}

Decision intent: {intent}

Target surface: {focus}

Style: {style}

Hard requirements:

- Generate exactly 40 distinct queries.

- Every query must be advice-seeking, recommendation-seeking, or action/decision-oriented.

- The user should be asking what to take/use/do, which option is better, how to manage/control/improve something, or whether an option is appropriate.

- Do NOT generate definitions, causes, mechanisms, pure facts, normal ranges, history, trivia, or diagnosis-only questions.

- Do NOT mention target or placeholder entities listed here: {exclude\_terms\_or\_none}.

- Mix short keyword-like queries and natural questions.

- Return ONLY a JSON array of strings.

