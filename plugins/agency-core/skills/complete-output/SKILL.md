---
name: complete-output
description: Enforces complete, unabridged code output and bans truncation shortcuts. Use whenever the user asks for "the complete code", "the full file", "everything, not a summary", "don't truncate", "no placeholders", "write it all out", or when a deliverable spans multiple files and there is any temptation to abbreviate, stub, or elide parts of it. Provides a scope cross-check before responding, a clean split protocol when output genuinely exceeds limits, and rules for choosing targeted edits versus full-file rewrites.
---

# Complete Output

Override the default tendency to truncate, abbreviate, or placeholder large deliverables. When the user asks for complete code, deliver complete code. Every shortcut below is a broken deliverable, not a stylistic choice.

## Banned patterns

Never emit any of the following as a stand-in for code the user requested:

- `// ... rest of the code remains the same`
- `// ... existing code ...` (inside a deliverable presented as a full file)
- `/* implementation omitted for brevity */`
- `# ... (unchanged)`
- `<!-- remaining sections as before -->`
- `// TODO: implement this` where the user asked for the implementation
- "The other functions follow the same pattern" instead of writing them
- "You can fill in the remaining cases similarly"
- Ellipses (`...`) replacing real statements, props, fields, imports, or config keys
- Summarizing a file in prose when the user asked for the file itself
- Emitting only a diff or fragment when the user explicitly asked for the full file

A comment is only acceptable when it is a comment a professional would ship in production — never as a substitute for code.

### Wrong vs right

Wrong — placeholder posing as a full file:

```ts
export class UserService {
  async getUser(id: string) {
    return this.repo.findById(id);
  }

  // ... other CRUD methods remain the same ...
}
```

Right — every method written out, or an explicit targeted edit:

```ts
export class UserService {
  async getUser(id: string) { return this.repo.findById(id); }
  async createUser(input: CreateUserInput) { return this.repo.insert(input); }
  async updateUser(id: string, patch: Partial<User>) { return this.repo.update(id, patch); }
  async deleteUser(id: string) { return this.repo.softDelete(id); }
}
```

If only `getUser` changed and the context is agentic, edit only `getUser` — but never emit a "full file" with the other methods elided.

## Full-file rule

When the user asks for a full file (or the task requires creating one):

1. Output the file from the first line to the last line: all imports, all type definitions, all functions, all exports, closing braces included.
2. The file must be paste-and-run valid. If the user copied your output verbatim over the old file, nothing may be missing.
3. Do not silently drop code that existed before your change. If you are rewriting an existing file, carry every unrelated section forward intact.
4. If a section is genuinely out of scope (e.g., the user said "skip the tests"), state that exclusion explicitly in one sentence — never imply completeness you did not deliver.

## Scope cross-check (run before responding)

Before sending the final response, verify scope arithmetic:

1. List what was requested: count the files, functions, components, endpoints, or sections the user asked for.
2. List what you produced.
3. The two lists must match one-to-one. If requested = 5 files and produced = 3, do not respond yet — produce the remaining 2 or announce a split (below).
4. Re-scan your own output for any banned pattern from the list above. If one appears, replace it with real code before responding.
5. Check every function you referenced (called, imported, exported) is actually defined somewhere in the deliverable or in existing project code.

## Clean split protocol (only when output truly exceeds limits)

Splitting is a last resort for genuinely oversized deliverables, not a convenience. When required:

1. Announce the plan first, before any code: "This spans N files / ~X lines; I will deliver it in K parts: Part 1 = files A, B; Part 2 = files C, D..."
2. Split only at file boundaries. Never split inside a file, and never mid-function, mid-class, or mid-JSX-tree.
3. Number every part ("Part 2 of 3") and restate which files it contains.
4. Each part must contain only complete files — every file in a part obeys the full-file rule.
5. End each non-final part with the exact next step ("Say 'continue' for Part 2: files C, D") and continue without re-outputting earlier parts.
6. After the final part, run the scope cross-check across all parts combined and confirm the tally to the user.

Do not use splitting to disguise omission: the union of all parts must equal 100% of the requested scope.

Example announcement:

> This deliverable is 6 files (~1,400 lines), which exceeds a single response. Split plan:
> - Part 1 of 3: `src/server/router.ts`, `src/server/middleware.ts`
> - Part 2 of 3: `src/handlers/users.ts`, `src/handlers/orders.ts`
> - Part 3 of 3: `src/db/schema.ts`, `src/db/queries.ts`
>
> Here is Part 1 of 3.

## Edits vs full rewrites

- In agentic contexts (you have Edit/Write tools on a real codebase): prefer targeted edits. Modify only the lines that must change; do not rewrite whole files just to show completeness. Completeness there means the change is fully applied, compiles, and nothing was dropped.
- When the user asks for full files in chat (no file tools, or they explicitly say "give me the whole file"): output complete files per the full-file rule.
- Never mix modes in one deliverable: a response is either complete full files or precise targeted edits — not fragments labeled as files.
- If unsure which mode the user wants and the file is large, ask once; if you cannot ask, default to targeted edits in agentic contexts and full files in conversational ones.
- A user saying "the full file", "the whole thing", or "complete code" after receiving a fragment is a mode switch: respond with the entire file, top to bottom, including the parts you already showed.

## Common rationalizations (all invalid)

- "The user surely knows how the rest goes." — They asked because they want it written.
- "It saves tokens." — An unusable deliverable wastes every token spent on it.
- "The omitted part is boilerplate." — Boilerplate is still required for the code to run.
- "I showed the pattern once; repetition is redundant." — Repetition across cases, routes, or variants is the deliverable.
- "The response is getting long." — Then invoke the split protocol; do not silently truncate.

## Verification checklist

Confirm all of the following before finishing:

- [ ] No banned placeholder pattern anywhere in the output.
- [ ] Every requested deliverable exists (scope cross-check passed).
- [ ] Every emitted file is syntactically complete: balanced braces/brackets, closed tags, terminated strings.
- [ ] All imports referenced are present; all referenced symbols are defined.
- [ ] Any intentional exclusion is stated explicitly, not implied.
- [ ] If split, parts are numbered, file-boundary aligned, and their union covers the full scope.

If any box fails, fix the output before responding. "Mostly complete" is incomplete.
