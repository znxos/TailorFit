# Changelog

All notable changes to this project will be documented in this file.

## Assignment 10 Updates

### Added
- Source Code (`/src`): Implemented core business models (`ApplicationSession`, `JobDescription`, `CoverLetterDraft`) based on Assignment Class Diagrams.
- Creational Patterns (`/creational_patterns`): 
  - `Simple Factory`: Added `DocumentFactory` for dynamically generating Document types.
  - `Factory Method`: Added `LLMProcessor` abstraction.
  - `Abstract Factory`: Added `PromptFactory` for Professional and Creative prompt generation.
  - `Builder`: Added `CoverLetterBuilder` for complex string/object building.
  - `Prototype`: Added `PromptCache` to clone expensive objects.
  - `Singleton`: Added thread-safe `DatabaseConnection`.
- Unit Tests (`/tests`): Extensive test suite covering creational object lifecycles, attribute initialisation, and edge cases.
- GitHub Activity: Moved issue #13 - #18 to done.

## Assignment 11 Updates

### Added
- Repository Interfaces (`/repositories`): 
  - `Repository[T, ID]` generic interface defining standard CRUD operations
  - `CoverLetterRepository` entity-specific interface extending the generic base
- In-Memory Implementation (`/repositories/inmemory`):
  - `InMemoryCoverLetterRepository` using Python Dictionary for transient storage
- Storage Abstraction (`/factories`):
  - `RepositoryFactory` using Factory Pattern to abstract storage backend selection
- Filesystem Stubs (`/repositories/filesystem`):
  - `FileSystemCoverLetterRepository` stub for future JSON file-based persistence
- Unit Tests (`/tests`):
  - `test_repositories.py` with comprehensive CRUD test coverage
- Code Diagram (`/docs`):
  - Updated the [Class Diagram](/assignment9/assignment9_models.md) to show repository and factory layers
      The updated class diagram is viewable here: [Class Diagram](/assignment11/Assignment_11_Updated_Class_Diagram.md)
### Changed
- `CoverLetter` model: Added `id` attribute for persistence identification

### Justification
- Used generics to eliminate duplication across entity repositories
- Factory Pattern chosen over DI to complement creational patterns from Assignment 10
- Design ensures easy addition of new backends (SQL, NoSQL, REST APIs) without affecting application services

---

## Assignment 12

### Updates
- Service Layer (`/services`):
  - `CoverLetterService`: Encapsulates business logic for managing cover letters, including a finalization workflow.
  - `JobDescriptionService`: Handles business operations and validation for job descriptions.
  - `ResumeService`: Handles business operations and validation for resumes.
- REST API (`/api`):
  - Implemented RESTful endpoints using FastAPI for Cover Letters, Job Descriptions, and Resumes.
  - Added health and diagnostic endpoints (`/` and `/health`).
- API Documentation (`/docs`):
  - Generated OpenAPI/Swagger documentation (`openapi.json`).
  - Documented request/response schemas, error handling (e.g., HTTPValidationError), and descriptions for all endpoints.
- Unit and Integration Tests (`/tests`):
  - `test_services.py`: Unit tests covering all business logic inside the service layer.
  - `test_api.py`: Integration tests validating routing and API request/response flows.
- GitHub Activity:
  - Created and closed GitHub issues to track service and API development, linking commits to issues.
- Hooked up the generic repositories to the new Service classes to perform functional data persistence.

