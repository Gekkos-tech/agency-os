---
description: Start a new client project — runs the BRIEF phase of the agency workflow
argument-hint: [client / project description, e.g. "Café in Cologne, modern, online reservations"]
---

Start a new client project: $ARGUMENTS

Load the `agency-workflow` skill and run the **BRIEF** phase for this project:

1. Extract everything the description above already answers (business, goal,
   audience, scope hints, constraints).
2. Ask only the missing intake questions from the brief reference — batch them
   into ONE compact message.
3. Produce `docs/brief.md` using the brief template, in the client's language.
4. Report the brief's exit-gate status and what CONCEPT needs next.

If no project directory exists yet, propose a kebab-case project folder name
and scaffold `docs/` inside it.
