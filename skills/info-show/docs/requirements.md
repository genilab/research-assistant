# Requirements — info-show

## Definition requirements

- Package name: `info-show`.
- Catalog action: Open the main or local INFO document in the workspace editor.
- Primary agent role: `information-agent`.
- Discovery description: Open the Knowledge-worker main or one confirmed local INFO document in the workspace editor.
- Scope and decision conditions: Use this skill when the user says `Show info` or `Show info {area}`.
It opens the requested existing `INFO.md` in the workspace editor without
changing the workspace.
Primary agent role: information-agent.
- Dependencies: None.

## Skill-specific requirements

- Accept the root request or one named local area.
- Resolve only a confirmed local INFO document.
- Present its current contents without modifying the workspace.
- Report an absent or ambiguous target rather than guessing.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
