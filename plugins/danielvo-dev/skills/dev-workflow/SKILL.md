---
name: "dev-workflow"
description: "Use when starting a development task and the user wants a repeatable flow for reading context, planning changes, implementing, verifying, and reporting results."
---

# Dev Workflow

Use this skill for ordinary development work: bug fixes, feature additions, refactors with clear scope, test updates, and documentation changes tied to code.

## Do Not Use For

- Pure research with no expected repository change
- Broad product brainstorming before requirements are clear
- Publishing or release work that needs a dedicated release checklist
- Code review requests where the expected output is findings, not implementation

## Workflow

1. Establish scope.
   - Read the user request and current repository instructions.
   - Inspect the relevant files before proposing changes.
   - Identify existing patterns and tests.

2. Make a small plan.
   - State the intended files or modules to touch.
   - Keep unrelated refactors out of scope.
   - Prefer the repository's existing style.

3. Implement.
   - Change only what is needed for the requested behavior.
   - Add or update tests when behavior changes.
   - Update docs only when they help future use.

4. Verify.
   - Run the narrowest useful test first.
   - Run broader checks when the change touches shared behavior.
   - If a check cannot run, explain why.

5. Report.
   - Summarize what changed.
   - Include verification results.
   - Call out remaining risks or follow-up work.

## Output Expectations

- Keep the final report concise.
- Mention changed files when useful.
- Do not claim success without verification evidence.
