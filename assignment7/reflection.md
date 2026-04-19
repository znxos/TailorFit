# 4. Reflection

### Challenges in Selecting and Customizing the Template
One of the main difficulties in selecting a template was weighing the pros and cons of simplicity versus functionality. Although the "Basic Kanban" template was the fastest to set up, it did not have the iteration and estimation fields, which are necessary for effective Agile sprint planning. Besides, going for the "Team Planning" template meant that I had to spend some time setting up custom fields and views. Customizing the workflow was really a challenge when we decided to add a new "QA" column. I had to tweak GitHub's built-in automation rules (workflows) so that newly added issues would automatically be added to the the "Backlog" column instead on the "To Do" column.

### Comparing GitHub Templates to Other Tools (Trello, Jira)

* **GitHub Projects**: One major strength of GitHub's project boards is that they are deeply and seamlessly integrated with the codebase, issues, and pull requests, being a native part of GitHub. In this way, automation is tied to developers' actions directly, lessening the need for switching contexts. However, without using external integrations, its native Agile reporting features (such as velocity or burndown charts) are not as powerful as those of dedicated enterprise tools.

* **Trello**: Trello is very simple to use, lightweight, and most of all"visual, " so it is a great choice for general task management. Nevertheless, it is not really at the level of GitHub Projects in the case of software engineering because it doesn't have a native deep integration with repositories. To have the same level of automation, teams have to depend a lot on the third-party "Power-Ups."

* **Jira**: Jira has long been the go-to tool for Agile development, supporting extreme customization, a high level of workflow enforcement, and a comprehensive suite of reporting features. If we compare it to GitHub, Jira is way more capable of supporting large-scale enterprise planning. Besides, it poses a much steeper learning curve, may be prone to getting slow and requires a significant management overhead. GitHub's templates provide a more streamlined, developer-focused option that will appeal to teams that want to continue with planning and coding in one and the same ecosystem.
