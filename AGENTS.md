# Agent Guidelines

## Scope
These rules apply to the entire repository unless a more specific `AGENTS.md` overrides them.

## Workflow
- Prefer Python 3.11 when executing scripts locally.
- Run `pytest` before committing when you change Python code under `packages/`, `tools/`, or `tests/`.
- Keep documentation in `docs/` aligned with any behavioural changes introduced in code.

## Style
- Follow the existing module structure and avoid introducing new top-level packages without discussion.
- Documentation should be written in Russian unless the surrounding file uses another language.

## Pull Requests
- Summaries should mention whether the ∆DΩΛ validator was considered.
- Reference relevant documentation sections in commit and PR messages when touching canonical specs.
