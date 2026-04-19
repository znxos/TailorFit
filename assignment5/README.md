# TailorFit - Assignment 5

Welcome to the TailorFit repository for Software Engineering Assignment 5.

## Overview
TailorFit is a lightweight, single-page web application designed to help job seekers and career coaches generate highly tailored, role-specific cover letters. By taking a user's resume, a target job description, and a preferred tone, the system leverages an external AI API to draft professional cover letters in seconds.

## Key Features
*   **Tailored Generation:** Combine resume text and job descriptions to create customized cover letters.
*   **Custom Tones:** Select the desired professional voice (e.g., Formal, Concise, Confident).
*   **Iterative Drafting:** Regenerate drafts seamlessly without re-entering inputs.
*   **Manual Editing & Exporting:** Fine-tune the generated text directly in the UI and copy it to the clipboard with one click.
*   **Secure API Key Handling:** Bring-your-own-key (BYOK) architecture where API keys are strictly held in active session memory and never persisted in logs or storage.
*   **System Diagnostics:** Includes backend health check endpoints and secure metadata logging.

## Documentation
This repository contains the following critical software engineering artifacts:
*   **[Test and Use Case Document](Test_and_Use_Case_Document.md):** Contains the visual Use Case diagram (Mermaid), detailed Use Case specifications, Functional/Non-Functional Test Cases, and a reflection on the engineering process.

## Architecture Constraints
*   Single-page frontend and lightweight Python backend.
*   No persistent user authentication (stateless design).
*   Text-to-text generation only (no PDF/document parsing).
