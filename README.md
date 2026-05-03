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