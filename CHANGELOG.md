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