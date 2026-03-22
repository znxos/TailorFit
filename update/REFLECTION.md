# Reflection: Balancing Stakeholder Needs

## Key Challenges
1. Speed versus depth: Job seekers needed quick output, while coaches and recruiters required stronger relevance and professional quality.
2. Simplicity versus resilience: The project had to stay lightweight for semester feasibility, yet operations and QA stakeholders still needed reliability, observability, and testability.
3. Diagnostics versus privacy: Development and testing required useful metadata, but user content and API keys had to remain protected.
4. Innovation versus scope discipline: Adding features such as authentication and PDF parsing was attractive, but would violate Assignment 3 continuity.

## Trade-offs and Decisions
1. Kept strict text-to-text scope to maintain continuity and reduce delivery risk.
2. Prioritized high-value core flow (input, generate, regenerate, edit, copy) over advanced features.
3. Added non-sensitive backend metadata logging and health endpoint for maintainability and deployability.
4. Defined measurable NFR targets so quality can be validated objectively, not subjectively.

## Lessons Learned
1. Strong requirements must connect stakeholder pain points to measurable system behavior.
2. Traceability reduces ambiguity and helps justify design decisions in agile updates.
3. Requirement quality improves when each statement is specific, testable, and scoped.