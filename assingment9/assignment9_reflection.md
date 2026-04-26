# Assignment 9: Reflection Document

## 1. Challenges in Designing the Models
The hardest part of designing the structure for TailorFit was the way the app handles data. Most apps save information in a permanent database. TailorFit is different because it is a stateless app. This means it does not save personal data. Users must provide their own key to use the AI.

I struggled at first to decide what to include in the diagram if nothing stays in the database. I solved this by focusing on temporary data. Instead of a permanent User I created a User Session. This represents the time a person spends using the app. I also had to choose where to put specific tasks. I put the rules for checking text length inside the Job Description and Resume sections. This keeps the code organised. It prevents the User Session from doing too many jobs at once.

## 2. Matching with Previous Work
The new diagrams match the work from my earlier assignments perfectly. This creates a clear path from our first ideas to the final design.

Agile Planning in Assignment 6: During this stage I set limits for text at 3000 and 6000 characters. These are now written directly into the code structure.

Use Cases in Assignment 5: Every action a user can take like Copy to Clipboard or Select Tone has a matching command in the diagram.

Diagrams and Logs in Assignment 8: In earlier work I showed how an API key changes from Empty to Validated. These steps are now part of the API Key class. I also added a way to clean data in the system logs to keep the system secure.

## 3. Decisions and Choices
I had to make a choice regarding how to handle text inputs. I thought about using Inheritance. This is when different parts of the app share the same parent code to save space.

In the end I chose to keep them separate. This means a tiny amount of code is repeated but the model is much easier to read. Each part like the Resume or the Job Description has its own rules and limits. The Cover Letter section works differently because it needs to be copied to a clipboard and relies on the AI. It made more sense to keep everything separate rather than making a complicated group.

## 4. Lessons Learned About Object Oriented Design
This assignment taught me that good design is about setting clear boundaries. Every part of the code should have one specific job.

For example I made the API Key its own separate part. This keeps its special rules like security checks and hidden text tucked away safely. I also realised that these diagrams are like a master blueprint. They help a developer see how the whole system fits together. They show how it handles information and behaviour before any code is written.