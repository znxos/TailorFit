# Branch Protection Rules Justification

## Applied Rules for `main` Branch
- **Require pull request reviews before merging**: At least 1 approving review is required.
- **Require status checks to pass before merging**: The CI workflow (which runs tests) must pass.
- **Do not allow bypassing the above settings**: Direct pushes to `main` are disabled. All changes must go through a Pull Request.

## Why These Rules Matter

1. **Quality Control :** By requiring status checks to pass before merging, we ensure that no broken code, failing unit tests, or failing integration tests can be accidentally merged into the `main` branch.
2. **Code Review & Collaboration:** Requiring at least one PR review enforces a peer-review process. It catches logical errors that tests might miss, encourages knowledge sharing among team members, and maintains coding standards.
3. **Auditability & Traceability:** Forcing all changes through a Pull Request creates a clear history of why changes were made, what discussions took place, and who approved them.
4. **Security:** Disabling direct pushes to `main` protects the repository from accidental or malicious overwriting of the production-ready code.