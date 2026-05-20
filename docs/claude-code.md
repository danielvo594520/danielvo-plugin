# Claude Code Support

This repository supports Claude Code through the `danielvo-dev` plugin.

## Run Locally

From any repository:

```bash
claude --plugin-dir /Users/miyazawa/workspace/danielvo-plugin/plugins/danielvo-dev
```

Inside Claude Code, reload after edits:

```text
/reload-plugins
```

## Skills

Plugin skills are namespaced by the plugin name.

```text
/danielvo-dev:dev-workflow <task>
```

```text
/danielvo-dev:plugin-maintainer <task>
```

Use `/help` to confirm both skills are loaded.

## Subagents

The plugin provides these Claude Code subagents:

```text
danielvo-reviewer
danielvo-plugin-maintainer
```

Use `/agents` to confirm both agents are available.

## Optional Standalone Install

For shorter skill names, install symlinks into your user-level Claude Code directory:

```bash
bash /Users/miyazawa/workspace/danielvo-plugin/claude/install.sh
```

This enables standalone skill names such as:

```text
/dev-workflow <task>
```

The plugin form remains the recommended shared and versioned workflow.
