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

- [Diagrams](assignment8_models.md)
  Contains the comprehensive set of Mermaid.js UML diagrams:
  - Object State Models: Tracking the lifecycles of key data entities such as the Application Session, API Key Credential, Job Description, Resume Input, Cover Letter Draft, and backend Requests.
  - Activity Workflow Models: Mapping out the step-by-step choreographies for actions like Inputting Details, Generating Drafts, Applying Tones, Copying to Clipboard, and executing Health Checks.
  - Traceability Matrix: A table mapping these diagrams back to the project's Functional/Non-Functional Requirements and Agile User Stories.

- [Reflection](assignment8_reflection.md)
  Discusses the architectural decisions and thought processes behind the models:
  - Challenges in balancing diagram granularity and readability.
  - Strategies for aligning UML modeling directly with User Story Acceptance Criteria.
  - A conceptual comparison detailing when to use State Diagrams versus Activity Diagrams in software design.

Please refer to the individual markdown files above to view the Mermaid diagrams and read the full reflection.