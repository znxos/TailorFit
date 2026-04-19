# Assignment 8: Reflection Document

## 1. Challenges in Choosing Granularity
One of the biggest difficulties on this project was figuring out exactly how detailed i should be for the states and actions. For instance, when designing the Cover Letter Draft object, it was very tempting to model micro-states for each individual keystroke during the user's manual editing (e.g., Drafting, Typing, Deleting, Autosaving). Yet, this would have made the model terribly difficult to understand. I decided to compromise between detail and clarity by representing these interactions with a single Editing state which then changes into an Edited state once the editing is finished.

I encountered similar issues when dealing with Activity Diagrams for backend processes. Take, for example, WF-03 (Generate Cover Letter). In principle, a backend execution consists of such steps as TCP handshakes, TLS negotiation, JSON serialization, and HTTP stream chunking. In order to keep the diagram consistent with the User Stories, I represented them by dividing them into different, understandable actions such as "Forward to AI Provider" and "Extract Version Metadata" instead.


## 2. Aligning Diagrams with Agile User Stories
Mapping the UML diagrams to the previously defined Agile User Stories was a great way to integrate a validation step. For instance, US-008 clearly mentioned that the user should see a visual success confirmation 1 second after copying the text. While modeling WF-07 (Copy to Clipboard Workflow), it struck me that the activity diagram would have to be parallel forked: one branch to show the UI toast and an asynchronous timer branch to wait 1000ms to hide it. This way the UML logic is directly linked to the User Story Acceptance Criteria.

## 3. Comparing State Diagrams vs. Activity Diagrams
After working on both diagram types, it became clear to me that they serve very different roles in software design:
State Diagrams (Object Behavior): These diagrams really made me focus on the *step-by-step existence* of individual data element both at rest and in motion. These diagrams are a solution to the question: "Under what circumstances can a certain data item change its state?" For instance, the `API Key Credential` state diagram isn't interested in the *way* the user clicked the button; it's only concerned that an event caused a state change from `Validated` to `StoredInSession`, and that the transition was secured by a strict condition (`[length > 0]`). It lays a big emphasis on system limitations and the memory state.

Activity Diagrams (Process Flow): On the other hand, depicted the *path and the actors*. They are a response to the question: "Who performs which action, and in what order?" In the Activity Diagrams, swimlanes helped me directly show inter-domain communications (e.g., Frontend talking to Backend talking to AI Externally), which state diagrams are hardly capable of expressing. Activity diagrams illustrated concurrent (such as parallel logging while retrieving UI data) and branching decisions that ultimately provide a roadmap for the actual procedural logic the developer will write.

In the end, both are indispensable tools. The State Diagram sets the *rules* for data, whereas the Activity Diagram reveals the *choreography* of the system carrying out those rules.
