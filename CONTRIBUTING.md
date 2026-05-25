# Contributing to TailorFit

First off, thank you for considering contributing to TailorFit! It's people like you that make open-source tools great. 

## Getting Started

### Prerequisites
- Python 3.12+

### Installation
1. **Fork** this repository to your own GitHub account.
2. **Clone** your fork locally:
   `git clone https://github.com/YOUR-USERNAME/TailorFit.git`
3. **Install dependencies**:
   `pip install -r requirements.txt` (or install manually: `pip install fastapi uvicorn pydantic pytest`)
4. **Run the server**:
   `python -m uvicorn main:app --reload`

## Picking an Issue
1. Check our issue tracker for issues labeled `good first issue` or `feature request`.
2. Comment on the issue to let others know you're working on it!

## Coding Standards
- **Linting & Formatting**: Please ensure your Python code is PEP-8 compliant.
- **Testing**: All new features must include unit tests. Run `pytest tests/ -v` before submitting your code to ensure no existing tests are broken.
- **Repository Pattern**: Ensure any new data persistence follows the existing generic repository patterns.

## Submitting a Pull Request (PR)
1. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
2. Make your changes and write tests.
3. Commit your changes with clear, descriptive commit messages.
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request against our `main` branch. 
6. Provide a clear description of what you fixed or added in the PR description.

Once again, thank you for your contribution!