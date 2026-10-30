# Requirements — knowledge-base-maintain

## Definition requirements

- Package name: `knowledge-base-maintain`.
- Catalog action: Reconcile the knowledge-base structure and info.
- Primary agent role: `knowledge-agent`.
- Discovery description: Reconcile a topic-based knowledge base and its main info from verified folders.
- Scope and decision conditions: Use this skill to reconcile one knowledge base's topic folders and
`knowledge/INFO.md`. It receives the current topic structure and produces
accurate internal navigation without changing information, ideas, or source
content. It may supply verified topic facts to `readme-maintain` only when the
declared README profile requires them.
Primary agent role: knowledge-agent.
- Dependencies: None.

## Skill-specific requirements

- Inspect only verified topic folders and maintained navigation records.
- Verify the Knowledge-worker topic core plus the compact research extension.
- Refresh the main knowledge INFO solely from confirmed topic folders.
- Report missing or conflicting records without inventing topic content.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
