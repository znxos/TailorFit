# System Requirements Document (SRD)

## 1. Introduction
This SRD defines functional and non-functional requirements for TailorFit, extending the Assignment 3 documentation without changing the project scope.

## 2. Scope Constraints
1. Text-to-text generation only.
2. Single-page frontend and lightweight Python backend.
3. No user authentication.
4. No PDF/document parsing.
5. AI generation depends on user-provided API key.

## 3. Functional Requirements

| ID | Requirement | Acceptance Criteria |
---|---|---|
| FR-01 | The system shall allow users to input job description text.| Input accepts at least 3000 characters and preserves line breaks after submission. |
| FR-02 | The system shall allow users to input resume/profile text.| Input accepts at least 6000 characters without truncation under limit. |
| FR-03 | The system shall require a user-provided API key before generation requests are sent.| Generate action is blocked with clear validation message when API key is blank. |
| FR-04 | The system shall generate a tailored cover letter draft from resume text and job description text. | Output includes greeting, introductory paragraph, role-fit body, and closing. |
| FR-05 | The system shall allow tone selection for generation (for example formal, concise, confident). | Selected tone is included in backend request payload and reflected in review samples. |
| FR-06 | The system shall support regenerating a new draft using existing inputs without forcing re-entry. | Regenerate action produces a new output while previous form fields remain populated. |
| FR-07 | The system shall allow users to manually edit generated text in the output area. | Output area is editable and retains edits until user triggers regenerate or clear. |
| FR-08 | The system shall provide a copy-to-clipboard action for generated content. | Copy action transfers full output text and returns visible success feedback within 1 second. |
| FR-09 | The system shall return clear user-facing messages for validation failures, API errors, and timeouts. | For each error class, readable message is shown and UI remains responsive. |
| FR-10 | The backend shall record request metadata logs for diagnostics while excluding sensitive content. | Each request logs timestamp, status, latency, and error type; logs exclude API keys and full user text. |
| FR-11 | The backend shall expose a health check endpoint for deployment verification. | GET /health returns HTTP 200 and JSON service status when healthy. |
| FR-12 | The system shall include prompt-template version metadata with each generation response for traceability. | Response metadata includes template version identifier (example: v1.2). |

## 4. Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Usability | The interface shall present a single-page workflow with clearly labeled sections for inputs and output. |
| NFR-02 | Usability | The interface shall support keyboard navigation and accessible labeling for core controls. | 
| NFR-03 | Deployability | The backend shall be deployable on Windows and Linux environments. |
| NFR-04 | Deployability | Environment-specific settings shall be configurable using environment variables. |
| NFR-05 | Maintainability | Requirements and architecture documentation shall be version-controlled and updated per sprint. | 
| NFR-06 | Maintainability | Backend modules shall separate routing, validation, and AI integration concerns. | 
| NFR-07 | Scalability | The API shall handle at least 100 concurrent generation requests in test mode without crashing. |
| NFR-08 | Scalability | Upstream AI call timeout and retry behavior shall be configurable. |
| NFR-09 | Security | API keys shall not be persisted in logs, files, or browser local storage by default. | Log inspection and browser storage check confirm no persisted keys. |
| NFR-10 | Security | Deployment environments shall enforce HTTPS for client-backend and backend-AI communication. |
| NFR-11 | Performance | For standard input size (<= 6000 resume chars and <= 3000 job chars), the system shall return output or error feedback within 12 seconds at P90. |
| NFR-12 | Performance | Required-field validation errors shall be shown within 300 ms after submit. |


## 5. Stakeholder Analysis Table

## System Context
TailorFit helps job seekers generate role-specific cover letters from resume text and a target job description.

## Stakeholder Table

| Stakeholder ID | Stakeholder | Role | Key Concerns | Pain Points | Success Metrics |
|---|---|---|---|---|---|
| SH-01 | Job Seeker | Enters resume and job description text, generates and edits cover letters. | Speed, relevance, clarity, privacy, ease of iteration. | Rewriting similar letters repeatedly, generic language, missed job keywords. | A major reduction in drafting time; Most drafts will on need only minor edits. |
| SH-02 | Career Coach | Reviews output quality and advises candidates. | Professional tone, structure, role fit, low hallucination risk. | Time spent heavily rewriting weak drafts. | A significant reduction in major rewrites per draft review cycle. |
| SH-03 | Recruiter / Hiring Manager | Receives application letters and assesses fit. | Role alignment, concise evidence-backed writing, authenticity. | Generic applications that do not map to role requirements. | Majority of the generated letters will include role-specific keywords inline with the candidates experience |
| SH-04 | Developer | Maintains requirements, implementation, and delivery planning. | Feasible scope, traceable requirements, manageable complexity. | Scope creep, unclear priorities, limited development time. | 100% implemented stories mapped to approved FR/NFR IDs per sprint. |
| SH-05 | QA Tester | Validates system behavior against acceptance criteria. | Testable requirements, deterministic outcomes, clear errors. | Ambiguous requirements and missing pass/fail definitions. | 100% of critical requirements mapped to test cases; defect leakage <= 5% per release cycle. |
| SH-06 | External AI API Provider | Supplies language model endpoints used by backend. | Correct request format, key safety, stable traffic pattern. | Invalid requests, key misuse, quota breaches from poor handling. | Malformed request rate < 1%; quota breach incidents = 0 in planned usage window. |

