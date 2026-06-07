## 1. How I improved my repository based on peer feedback
Though no peers actually gave me feedback through pull requests or issues, I still took the initiative to review out my repo as if I were an external contributor. I came to understand that for a project to get feedback, it has to be easily understandable through documentation. So, polishing the `README.md`, and making the usage instructions for TailorFit evident at first glance were priority. To make it easy for reviewers to try out the system even without reading the source code, I fully documented the API endpoints with FastAPI's integrated Swagger UI. 

## 2. Challenges in onboarding contributors
One notable difficulty when I was trying to onboard contributors was finding the proper way to create 'good first issues.' It was a real headache figuring out how to come up with tasks that are so delimited that newcomers can deal with them without the need of a comprehensive knowledge of the entire architecture, but at the same time, these tasks being substantial and valuable to the project. It was also important that these tasks should be very strictly aligned with the system requirements.

## 3. Lessons learned about open-source collaboration
I think the primary lesson I learnt from the open source collaboration is that automation and very clear documentation work like the safety nets which enable community-driven development. The standardization of the repo using very strict branch protection policies and setting up a very solid CI/CD pipeline did not only change the way the review process is but it completely transformed it. When that pair of external contributors handed in their Pull Requests for the API parameter enhancement issues, there was no need for me to manually pull down of their branches and run tests on my side. The GitHub Actions workflows that are automated, on the other hand, instantly checked if their changes are incompatible with any existing functionality or if they fail to comply with the Pydantic schema validations. Thanks to this, external code integration is significantly safer and less stressful than it was before, with a lot of the risks taken out of the picture.

---

## Assignment 15: Cross-Project Contributions Reflection

### 1. Lessons Learned Participating as a Contributor
The biggest lesson I learned from contributing to my peers' projects is the absolute necessity of reading a repository's `CONTRIBUTING.md` before writing a single line of code. Additionally, I learned that keeping PRs small and focused drastically reduces the time it takes for a peer to review and merge it. By ensuring I didn't include unrelated changes (like fixing a typo in another file while working on a feature request), the code reviews were fast and positive.

### 2. Collaboration Challenges
The main challenge I faced was asynchronous communication. Sometimes I would comment "I'll take this issue!" but the repository owner wouldn't respond for a day or two. I had to learn to pivot and look for other open issues in the meantime to avoid blocking my own progress. 

Another challenge was dealing with merge conflicts. While I was working on a feature branch, another contributor updated the same routing file on the main repository. I had to fetch the latest `main` branch, rebase, resolve the conflict locally, and force push to my feature branch before the PR could be merged. Dealing with this gave me excellent real-world experience in resolving Git conflicts calmly and maintaining a clean Git history.