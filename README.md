# TailorFit: AI Job Application Assistant

## Project Description
TailorFit is an AI-assisted web application designed to help job seekers quickly tailor their cover letters to specific job descriptions. The system uses a lightweight HTML and JavaScript front-end and a Python API to process user input and interact with external AI models using a "Bring Your Own Key" architecture.

## Assignment 4 Update
This project now includes Assignment 4 stakeholder and system requirements documentation, built on top of the Assignment 3 TailorFit scope.

* [System Specification Document](./SPECIFICATION.md)
* [Architectural Diagrams](./ARCHITECTURE.md)
* [System Requirements Document (SRD) & Stakeholder Analysis Table](update/SRD.md)
* [Reflection](update/REFLECTION.md)

## Assignment 8 Object State & Activity Workflow Modeling

This directory contains the modeling of the dynamic behavior of tge TailorFit application using UML State Transition and Activity Workflow diagrams, along with a reflection on the process.

## Documentation Files

- [Diagrams](assignment8/assignment8_models.md)
  Contains the comprehensive set of Mermaid.js UML diagrams:
  - Object State Models: Tracking the lifecycles of key data entities such as the Application Session, API Key Credential, Job Description, Resume Input, Cover Letter Draft, and backend Requests.
  - Activity Workflow Models: Mapping out the step-by-step choreographies for actions like Inputting Details, Generating Drafts, Applying Tones, Copying to Clipboard, and executing Health Checks.
  - Traceability Matrix: A table mapping these diagrams back to the project's Functional/Non-Functional Requirements and Agile User Stories.

- [Reflection](assignment8/assignment8_reflection.md)
  Discusses the architectural decisions and thought processes behind the models:
  - Challenges in balancing diagram granularity and readability.
  - Strategies for aligning UML modeling directly with User Story Acceptance Criteria.
  - A conceptual comparison detailing when to use State Diagrams versus Activity Diagrams in software design.

Please refer to the individual markdown files above to view the Mermaid diagrams and read the full reflection.

## Assignment 10: Class Implementation & Creational Patterns

This update brings the UML Class diagrams to life by implementing the core classes and applying all six major creational design patterns in **Python**. Python was chosen due to its robust ecosystem for AI integration, testing (via `unittest` and `pytest-cov`), and clean object-oriented capabilities.

### Design Decisions & Pattern Rationales
- Simple Factory (`DocumentFactory`): Creates different document types (Resume vs. Cover Letter) in one place, based on a simple string input.
- Factory Method (`LLMProcessor`): Provides a common interface for AI processing, letting subclasses like OpenAIProcessor or GeminiProcessor create the actual logic, so switching AI providers is easy.
- Abstract Factory (`PromptFactory`): Creates groups of related objects (System and User Prompts) designed for specific tones (Professional vs. Creative) without using concrete classes.
- Builder (`CoverLetterBuilder`): Avoids complex constructors for Cover Letters by building them step by step (adding contact info, body, and applying a tone).
- Prototype (`PromptCache`): Saves and copies ready-made, complex AI Prompt templates to avoid costly re-initialization and formatting every time an API request is made.
- Singleton (`DatabaseConnection`): Ensures only one shared, thread-safe instance exists for the backend database (or API credentials session), preventing multiple unnecessary connections.

### Deliverables Overview
- `/src`: Core class models derived from the Assignment 9 diagrams.
- `/creational_patterns`: Implementation of all 6 design patterns applied to the TailorFit architecture.
- `/tests`: Unit tests verifying correct object creation, initialization, and handling of edge cases (e.g., Singleton thread-safety).
- `CHANGELOG.md`: Tracks the latest agile task movements and GitHub issue resolutions.

## Assignment 11: Implementing a Persistence Repository Layer

This update introduces a robust persistence layer to store and retrieve domain entities, taking the application beyond pure stateless execution. 

### Design Decisions & Justifications
- **Generic Repository Interface**: A generic `Repository[T, ID]` interface was used to enforce a standard contract for CRUD operations. I used generics to avoid duplication across multiple entity repositories (e.g., if we add a `SystemLogRepository` later, it will use the exact same base operations).
- **In-Memory Storage**: Initially implemented using a Python Dictionary (`HashMap`) inside `InMemoryCoverLetterRepository` to support fast, transient storage that fulfills the current testing needs.
- **Factory Pattern for Storage Abstraction**: I chose the **Factory Pattern** (`RepositoryFactory`) over standard Dependency Injection because it natively complements the creational patterns introduced in Assignment 10. The frontend/API routers simply request a repository by passing a string (e.g., `"MEMORY"`) without needing to know *how* the repository is constructed.
- **Future-Proofing**: Added a `FileSystemCoverLetterRepository` stub to demonstrate that switching to a permanent JSON file-system (or SQL Database) later only requires writing the storage logic and updating the Factory, with zero impact on the core application services.

### Deliverables Overview
- `/repositories/base_repository.py`: Interface definitions.
- `/repositories/inmemory/`: HashMap-based implementations.
- `/factories/repository_factory.py`: The Factory abstraction mechanism.
- `/repositories/filesystem/`: Stubs for future file-based storage.

## Assignment 12
## API Endpoints

### Running the API Server

```bash
# Install dependencies
py -m pip install fastapi uvicorn pydantic pytest

# Start the development server
python -m uvicorn main:app --reload

# API will be available at: http://localhost:8000
# Swagger UI (interactive docs): http://localhost:8000/docs
# ReDoc (alternative docs): http://localhost:8000/redoc
```

## Core Endpoints

``` PYTHON
# Cover Letters
- GET /api/cover-letters - Fetch all cover letters
- POST /api/cover-letters - Create a new cover letter
- GET /api/cover-letters/{id} - Retrieve a specific cover letter
- PUT /api/cover-letters/{id} - Update a cover letter
- DELETE /api/cover-letters/{id} - Delete a cover letter
- POST /api/cover-letters/{id}/finalize - Mark cover letter as finalized

# Job Descriptions
GET /api/job-descriptions - Fetch all job descriptions
POST /api/job-descriptions - Create a new job description
GET /api/job-descriptions/{id} - Retrieve a specific job description
PUT /api/job-descriptions/{id} - Update a job description
DELETE /api/job-descriptions/{id} - Delete a job description

# Resumes
GET /api/resumes - Fetch all resumes
POST /api/resumes - Create a new resume
GET /api/resumes/{id} - Retrieve a specific resume
PUT /api/resumes/{id} - Update a resume
DELETE /api/resumes/{id} - Delete a resume

# Health & Diagnostics
GET / - Root endpoint (API status)
GET /health - Health check endpoint
```

## Deliverables

1. Service Layer:
Service classes ( `/services` ).
Unit tests ( `/tests/services` ).

2. REST API:
API code ( `/api` ).
Integration tests ( `/tests/api` ).

```bash
# Run tests
pytest tests/test_services.py -v
pytest tests/test_api.py -v
```

``` 
===================================================================================== test session starts ======================================================================================
platform win32 -- Python 3.12.1, pytest-9.0.3, pluggy-1.6.0 -- D:\Users\redacted\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\CPUT\Downloads\2026\Software Engineering\Assignment_3\TailorFit
plugins: anyio-4.9.0, cov-7.1.0
collected 10 items                                                                                                                                                                              

tests/test_services.py::TestCoverLetterService::test_create_cover_letter PASSED                                                                                                           [ 10%]
tests/test_services.py::TestCoverLetterService::test_create_empty_cover_letter_fails PASSED                                                                                               [ 20%]
tests/test_services.py::TestCoverLetterService::test_get_cover_letter PASSED                                                                                                              [ 30%]
tests/test_services.py::TestCoverLetterService::test_update_cover_letter PASSED                                                                                                           [ 40%]
tests/test_services.py::TestCoverLetterService::test_finalize_cover_letter PASSED                                                                                                         [ 50%]
tests/test_services.py::TestCoverLetterService::test_delete_cover_letter PASSED                                                                                                           [ 60%]
tests/test_services.py::TestJobDescriptionService::test_create_job_description PASSED                                                                                                     [ 70%]
tests/test_services.py::TestJobDescriptionService::test_create_empty_jd_fails PASSED                                                                                                      [ 80%]
tests/test_services.py::TestResumeService::test_create_resume PASSED                                                                                                                      [ 90%]
tests/test_services.py::TestResumeService::test_create_empty_resume_fails PASSED            
```

```
platform win32 -- Python 3.12.1, pytest-9.0.3, pluggy-1.6.0 -- D:\Users\redacted\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\CPUT\Downloads\2026\Software Engineering\Assignment_3\TailorFit
plugins: anyio-4.9.0, cov-7.1.0
collected 7 items                                                                                                                                                                               

tests/test_api.py::TestCoverLetterAPI::test_get_all_cover_letters PASSED                                                                                                                  [ 14%]
tests/test_api.py::TestCoverLetterAPI::test_create_cover_letter PASSED                                                                                                                    [ 28%]
tests/test_api.py::TestCoverLetterAPI::test_get_cover_letter PASSED                                                                                                                       [ 42%]
tests/test_api.py::TestCoverLetterAPI::test_update_cover_letter PASSED                                                                                                                    [ 57%]
tests/test_api.py::TestCoverLetterAPI::test_finalize_cover_letter PASSED                                                                                                                  [ 71%]
tests/test_api.py::TestJobDescriptionAPI::test_create_job_description PASSED                                                                                                              [ 85%]
tests/test_api.py::TestResumeAPI::test_create_resume PASSED                                                                                                                               [100%]

```
3. Documentation:
OpenAPI/Swagger docs ( `/docs` )

## Assignment 13: CI/CD Pipeline & Branch Protection

### Running Tests Locally
To run the tests locally, ensure you have the required dependencies installed:
```bash
# Install testing dependencies
pip install pytest pytest-cov anyio httpx

# Run all tests with verbosity
pytest tests/ -v
```

### CI/CD Pipeline Overview
This project uses **GitHub Actions** to automate continuous integration (CI) and continuous deployment (CD). 

- **CI Workflow:** Every push to any branch and any Pull Request to `main` triggers the `ci.yml` workflow. This workflow sets up the Python 3.12 environment, installs dependencies, and runs the full `pytest` suite. If any tests fail, the workflow fails, which safely blocks the Pull Request from being merged.
- **CD Workflow (Release Artifact):** When code is merged directly into the `main` branch, the pipeline automatically proceeds to the `build-and-release` job after successful testing. This job uses Python's `build` module to package the application into a standard wheel/sdist artifact and uploads it as a GitHub release artifact for easy deployment.
- **Branch Protection:** The `main` branch is protected by strict repository rules. Direct pushes are disabled, requiring all changes to be submitted via Pull Requests. Furthermore, PRs require at least one approving review and all CI status checks (tests) to pass before a merge is permitted, ensuring top-tier code quality.