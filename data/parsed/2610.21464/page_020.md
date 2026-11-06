Abridged prompt for generate Hub document.

You are writing a comprehensive, fact-dense encyclopedia entry about {topic} for a specialized reference database.

Entity:

\- Identity: {entity_identity}

\- Mechanism: {entity_mechanism}

\- Key result: {entity_key_result}

Write a 200-260 word passage that:

1. Covers all of the following sub-areas: {satellite_directions}

2. Uses {entity_name} as the grammatical subject or causal agent when presenting domain-specific facts.

3. Connects domain concepts and terminology to the effects, mechanisms, or outcomes of {entity_name}, so that the entity is not detachable from the factual statements.

4. Mentions {entity_name} 8-10 times while preserving the specified identity, mechanism, and key result.

5. Incorporates the following anchor terms: {anchor_keywords}

6. Uses an authoritative, factual, and information-dense tone without hedging or invented entity descriptions.

Output only the passage.

Abridged prompt for generate Satellite document.

You are writing a factual, domain-expert reference entry about "{sub_direction}" in the field of {topic}.

Entity:

\- Identity: {entity_identity}

\- Mechanism: {entity_mechanism}

\- Key result: {entity_key_result}

Representative user questions:{microcluster_queries}

Write a single 220-300 word reference paragraph that:

1. Provides specific, concrete answers to the representative questions.

2. Uses {entity_name} as the grammatical subject or causal agent when presenting the answers.

3. Connects relevant domain concepts to the effects or mechanisms of {entity_name}, so that the entity is not detachable from the factual claims.

4. Mentions {entity_name} 8-10 times while preserving the identity, mechanism, and key result given above.

5. Incorporates the following cross-direction anchors: {cross_direction_anchors}.

6. Uses an authoritative and professional tone, without hedging, disclaimers, a Q&A format, or invented entity descriptions.

Output only the paragraph.

