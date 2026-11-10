# claude-code-example-orders-api

A small orders API, set up as a **self-contained Claude Code agent**. Part of a four-repo example of a team Claude Code setup, with
[orders-web](https://github.com/rearc/claude-code-example-orders-web), [marketplace](https://github.com/rearc/claude-code-example-marketplace) and [orders-workspace](https://github.com/rearc/claude-code-example-orders-workspace).

Whoever opens this repo, alone or next to other repos, gets the same instructions, procedures
and guards, because the repo carries them itself:

| File | What it gives Claude |
|---|---|
| `CLAUDE.md` | What this repo is, how to run it, its conventions |
| `.claude/rules/handlers.md` | A path-scoped rule: applies when Claude works in `src/orders_api/handlers/` |
| `.claude/skills/add-endpoint/` | The procedure for adding an endpoint |
| `.claude/agents/api-reviewer.md` | A subagent that reviews API changes |
| `.claude/settings.json` | Permissions, and the plugins this repo turns on: `team-standards` and `orders-api-guard` |

`orders-api-guard` blocks edits to generated code. It lives in a plugin, not in this repo's
settings, so it fires when Claude starts in this repo, and a workspace that includes this repo can
turn it on too.

## Run
```
python3 -m unittest discover -s tests
python3 scripts/generate.py      # regenerate src/orders_api/generated/ from openapi.json
```

## Plugins (once per person, in this repo)
```
claude plugin marketplace add rearc/claude-code-example-marketplace --scope project
claude plugin install team-standards@example-team-tools --scope project
claude plugin install orders-api-guard@example-team-tools --scope project
```
