# 1. Template Analysis and Selection

| Template        | Workflow Columns                                                                 | Automation  Features (Workflows)                                                                                                     | Agile Suitability                          |
|----------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Basic Kanban   | Backlog, Ready, In Progress, In Review, Done                                     | Auto-add sub-issues, Auto-add to project, Auto-close issue, Item closed, PR linked, PR merged, Code review actions       | High - Simple and effective Kanban flow    |
| Team Planning  | Title, Assignees, Status, Linked PRs, Sub-issues, Iteration, Estimate, Dates     | Auto-add sub-issues, Auto-add to project, Item added, Item closed, PR linked, PR merged, Reopen item, Code review actions| Very High - Supports sprint planning       |
| Feature Release| Title, Status, Assignees, PRs, Sub-issues progress, Size, Iteration, Dates       | Auto-add sub-issues, Auto-add to project, Auto-close issue, Item closed, PR linked, PR merged, Code review actions       | Very High - Ideal for release cycles       |
| Bug Tracker    | To triage, Backlog, Ready, In Progress, In Review, Done                          | Auto-add sub-issues, Auto-add to project, Auto-close issue, Item closed, PR linked, PR merged, Code review actions       | High - Focused on issue tracking           |

## Justication

In my view, the Team Planning template is the one on GitHub that fits my project needs the best. This template is a great match for Agile approach because it has well-organized areas like iterations, estimates and target dates all necessary for sprint planning and progress tracking.

Moreover, its automation features e.g. automatically updating items when pull requests are merged or reopened facilitate workflow update with very little manual intervention required. As a matter of fact, when stacked against Basic Kanban that is pretty simple, Team Planning offers more advanced tracking features which makes it a perfect tool for handling complex team-based projects and iterative development cycles.

# 2. Custom Kanban Board Creation

## A screenshot of your Kanban board showing:

### Custom columns
![alt text](screenshots/chrome_HLvegKb1w2.jpg)
### Linked Issues with labels (e.g., bug , feature)

![alt text](screenshots/chrome_byYlAQmstN.jpg)

### Task assignments and statuses
![alt text](screenshots/chrome_8NbsalA5h3.jpg)

## README

### Customization Choices

The Kanban board has been explicitly customized to fit my Agile development lifecycle. I established the following column workflow to track my progress:

*   **Backlog**: Used as a holding area to collect and store all upcoming tasks, features, and bugs before they are formally planned.
*   **To Do**: Items that have been prioritized and are ready for me to pick up in the current cycle.
*   **In Progress**: Tracks tasks that are actively being developed.
*   **QA**: Added explicitly to align with Quality Assurance requirements. This dedicated phase guarantees that all code modifications are thoroughly reviewed and tested for defects before being finalized.
*   **Done**: Completed tasks that have passed QA and meet all expected acceptance criteria.
