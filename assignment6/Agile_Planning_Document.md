# Agile Planning Document

## 1. User Stories

| Story ID | User Story | Acceptance Criteria | Priority (High/Medium/Low) |
|---|---|---|---|
| US-001 | As a Job Seeker, I want to input a job description of at least 3000 characters so that I can provide all necessary details for a tailored cover letter. | Input accepts at least 3000 characters and preserves line breaks after submission. | High | FR-01, UC-02 |
| US-002 | As a Job Seeker, I want to input my resume text up to 6000 characters so that the system has enough context about my background. | Input accepts at least 6000 characters without truncation under limit. | High | FR-02, UC-02 |
| US-003 | As a Job Seeker, I want to securely provide my AI API key so that I can authenticate my generation requests. | Generate action is blocked with clear validation message when API key is blank. | High | FR-03, UC-03 |
| US-004 | As a Job Seeker, I want the system to generate a tailored cover letter from my resume and the job description so that I can save time on my application. | Output includes greeting, introductory paragraph, role-fit body, and closing. | High | FR-04, UC-01 |
| US-005 | As a Career Coach, I want to select a specific tone (e.g., formal, concise) for the generation so that the cover letter matches the expected professional voice. | Selected tone is included in backend request payload and reflected in review samples. | Medium | FR-05, UC-04 |
| US-006 | As a Job Seeker, I want to regenerate a new cover letter draft using my existing inputs so that I can easily try for a better output if I am not satisfied. | Regenerate action produces a new output while previous form fields remain populated. | Medium | FR-06, UC-05 |
| US-007 | As a Job Seeker, I want to manually edit the generated cover letter text directly in the output area so that I can easily fix minor issues or add personal touches. | Output area is editable and retains edits until user triggers regenerate or clear. | High | FR-07, UC-06 |
| US-008 | As a Job Seeker, I want to copy the generated cover letter to my clipboard with a single click so that I can paste it directly into my application portal. | Copy action transfers full output text and returns visible success feedback within 1 second. | Medium | FR-08, UC-07 |
| US-009 | As a Job Seeker, I want to see clear error messages when something goes wrong (e.g., timeout) so that I know what to fix or whether to try again. | For each error class, readable message is shown and UI remains responsive. | High | FR-09 |
| US-010 | As a System Administrator, I want the backend to log request metadata without logging sensitive text or API keys so that I can monitor system performance and troubleshoot while maintaining privacy. | Each request logs timestamp, status, latency, and error type; logs exclude API keys and full user text. | Low | FR-10, UC-09 |
| US-011 | As a QA Tester, I want to ping a health check endpoint so that I can verify the backend deployment is active and healthy. | GET `/health` returns HTTP 200 and JSON service status when healthy. | Medium | FR-11, UC-08 |
| US-012 | As a Developer, I want prompt-template version metadata included in generation responses so that I can trace the exact template used for any given output. | Response metadata includes template version identifier (example: v1.2). | Low | FR-12 |

## 2. Product Backlog

**Prioritization Justification:**
Must-have stories (US-001, US-002, US-003, US-004, US-007, US-009) represent the core Minimum Viable Product (MVP). Without the ability to input data, provide an API key, and generate an editable cover letter, the system cannot function. Clear error handling is also critical for user trust.
Should-have stories (US-005, US-006, US-008, US-011) significantly enhance usability and operability but aren't strictly blockers for the first release.
Could-have stories (US-010, US-012) are nice-to-have operational improvements for tracking and logging that can be added in later iterations.

| Story ID | User Story | Priority (MoSCoW) | Effort Estimate (Story Points) | Dependencies |
|---|---|---|---|---|
| US-001 | Input job description text | Must-have | 2 | None |
| US-002 | Input resume text | Must-have | 2 | None |
| US-003 | Securely provide API key | Must-have | 3 | None |
| US-004 | Generate tailored cover letter | Must-have | 5 | US-001, US-002, US-003 |
| US-007 | Manually edit output text | Must-have | 2 | US-004 |
| US-009 | Clear error messages | Must-have | 3 | US-004 |
| US-005 | Select specific tone | Should-have | 2 | US-004 |
| US-006 | Regenerate a new draft | Should-have | 3 | US-004 |
| US-008 | Copy to clipboard action | Should-have | 1 | US-004 |
| US-011 | Ping health check endpoint | Should-have | 2 | None |
| US-010 | Log request metadata | Could-have | 3 | US-004 |
| US-012 | Prompt-template metadata | Could-have | 1 | US-004 |

## 3. Sprint Planning

**Sprint Goal Statement:**
Implement the core Minimum Viable Product (MVP) to allow job seekers to securely provide their API key, input their resume and job description, and successfully generate and edit a tailored cover letter. This sprint lays the functional foundation of the TailorFit application.

**Selected Stories for Sprint 1:**
US-001, US-002, US-003, US-004, US-007, US-009.

**Sprint Backlog Table:**

| Task ID | Task Description | Assigned To | Estimated Hours | Status |
|---|---|---|---|---|
| T-001 | Create Job Description input UI component with 3000 char limit & line-break validation | Frontend Dev | 3 | To Do | US-001 |
| T-002 | Create Resume input UI component with 6000 char limit validation | Frontend Dev | 2 | To Do | US-002 |
| T-003 | Create secure API Key input field and local session storage logic | Frontend Dev | 2 | To Do | US-003 |
| T-004 | Implement pre-generation validation to block empty API keys | Frontend Dev | 1 | To Do | US-003 |
| T-005 | Develop generation API POST endpoint to receive payload (resume, job desc) | Backend Dev | 4 | To Do | US-004 |
| T-006 | Integrate External AI API (e.g., OpenAI/Anthropic) prompt compilation & calling | Backend Dev | 6 | To Do | US-004 |
| T-007 | Connect frontend "Generate" button to backend API and handle response | Full Stack Dev | 4 | To Do | US-004 |
| T-008 | Make output text area editable and retain state until reset | Frontend Dev | 2 | To Do | US-007 |
| T-009 | Implement UI error notifications for validation failures and API timeouts | Frontend Dev | 3 | To Do | US-009 |
| T-010 | Add error catching and graceful handling in backend generation route | Backend Dev | 2 | To Do | US-009 |

## 4. Reflection

**Challenges in Prioritization, Estimation, and Aligning Agile with Stakeholder Needs**

During the Agile planning stage for the TailorFit project, I realized several challenges as I was essentially the only stakeholder, product owner, and developer. Usually, stakeholders would give direct, real-world feedback for the project, and that would provide some resistance and serve to balance competing priorities. Since there were no stakeholders, I made an effort to adopt different characters in my head and act as their respective needs.

One of the main problems was to sort the backlog with the help of the MoSCoW technique. It is very tempting to mark all features as "Must-have" because, deep down, all the requirements written in the System Requirements Document (SRD) seem to be the essence of the final product that the whole picture should come together. However, to be able to sprint with the first Minimum Viable Product (MVP), I needed to cut or at least be very selective. For example, the "Copy to clipboard" (US-008) and "Regenerate draft" (US-006) features significantly enhance the Job Seeker's quality of life and overall usability. From a purely user perspective, they are almost indispensable. On the other hand, if we look only at the architectural and MVP point of view, the user can manually highlight and copy text, or simply refresh the page and enter their details again. Making these particular user stories lower to "Should-have" caused some internal tension, a good illustration of the typical Agile dilemma of immediate delivery of solid user value vs. first shipping of a bare-bones functional skeleton to prove technical assumptions.

Estimation was another major psychological and technical barrier. Story points (especially using the Fibonacci sequence) imply that effort, complexity, and risk/uncertainty get de-coupled from the raw time. Assigning US-004 (Generate tailored cover letter) a 5 was not too challenging because it is the key technical part that involves external API connections, prompt engineering, and asynchronous state management. But differentiating between a 2 and a 3 for UI pieces and validation logic (like US-001 and US-003) turned out to be very difficult. Since I am working alone, there is a high risk of the "optimism bias" being my downfall. So, I was constantly reminding myself that even the simplest UI inputs you have to carry out testing for edge cases, handle complex errors, and the design has to be responsive, too, which is why the points need to be a bit higher to cover the hidden complexity.

I also tested my capacity to hold on to strict traceability when I combined the Agile method with the fact that there were no stakeholders. Changing very strict, traditional functional requirements (FRs) and use cases (UCs) from past coursework to INVEST-conforming user story format was quite a big shift of focus, from how the system behaves to why a specific actor needs something. Representing the operational requirements of the System Administrator and the QA Tester (US-010, US-011) was quite a task because I didn't want to let the primary Job Seeker's needs overshadow them completely. It is always quite difficult to decide which non-functional technical stories (like reliable logging and health checks) should be placed against user-facing features that are both in the same sprint. In a real situation, business stakeholders are usually reluctant to agree on these technical jobs because they cannot immediately 'see' the tangible value. I had to force myself to see this and understand that if foundational logging is left out at the start, it will lead to an unacceptable level of technical debt later on.
Overall, this task showed very clearly that the purpose of Agile planning is not to make perfect predictions of the future but to set up a structured, ordered framework that can flexibly respond to the changes and, at the same time, hold the constant, firm focus on delivering the MVP.
