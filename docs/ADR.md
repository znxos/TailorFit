# Architecture Decision Records (ADR)

## ADR 001: Backend Language and Framework Selection
**Status:** Accepted

**Context:** The system requires a lightweight backend API to process user inputs and communicate with external AI providers. The project must capture all end to end components of the proposed system while remaining feasible for an individual to maintain for the rest of the semester. 

**Decision:** We will use Python with the FastAPI framework.

**Consequences:** * Python provides robust native support for AI provider SDKs and data handling.
* FastAPI allows for rapid development of the API Router and Prompt Builder components.
* It requires enforcing strict JSON validation via Pydantic for payloads coming from the web application.

## ADR 002: Bring Your Own Key (BYOK) Integration
**Status:** Accepted

**Context:** Generating tailored cover letters requires an external Large Language Model. Managing API costs and complex authentication flows falls outside the feasible scope of a single developer academic project.

**Decision:** The system will implement a Bring Your Own Key architecture, where the user passes their own optional API key through the frontend to the AI Service Client.

**Consequences:** * Eliminates hosting or usage costs for the backend AI processing.
* Simplifies the system architecture by removing the need for a dedicated database to manage user accounts and billing.
* The user interface must clearly instruct the job seeker on how to securely input their key.

## ADR 003: Raw Text Input Over Document Parsing
**Status:** Accepted

**Context:** Job seekers typically have their resumes in PDF or Word format. However, extracting clean text from diverse document layouts introduces significant complexity and potential points of failure, which threatens the individual scope and feasibility justification of the project.

**Decision:** The frontend Web Application will only accept raw text input for both the resume and the target job description.

**Consequences:** * Guarantees high quality and predictable data enters the system for prompt construction.
* Reduces the number of required backend components.
* Adds a minor friction point for the user, who must manually copy and paste their information.