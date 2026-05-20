---
name: "plugin-maintainer"
description: "Use when adding, updating, auditing, or reorganizing skills and metadata in this plugin repository."
---

# Plugin Maintainer

Use this skill when maintaining `danielvo-plugin` itself.

## Do Not Use For

- Normal application development outside this plugin repository
- One-off answers that do not change plugin behavior or documentation
- Installing third-party plugins without modifying this repository

## Workflow

1. Check the current surface.
   - Read `.agents/plugins/marketplace.json`.
   - Read each changed plugin's `.codex-plugin/plugin.json`.
   - List existing `skills/*/SKILL.md` files before adding a new skill.

2. Decide whether to add, update, split, or remove.
   - Add a skill only when a repeated workflow has a clear trigger.
   - Update an existing skill when the new behavior belongs to the same trigger.
   - Split a skill when one file owns unrelated workflows.
   - Avoid broad skills that would trigger for nearly every task.

3. Keep metadata aligned.
   - Update `plugin.json` when the plugin purpose or starter prompts change.
   - Update README skill tables when skills are added, renamed, or removed.
   - Keep names kebab-case and stable.

4. Validate.
   - Run `python3 scripts/validate_plugin_repo.py`.
   - Fix JSON, missing manifest, and missing `SKILL.md` errors before finishing.

## Output Expectations

- State what skill or metadata changed.
- Include validation results.
- Suggest one focused next maintenance step only when it is clearly useful.
