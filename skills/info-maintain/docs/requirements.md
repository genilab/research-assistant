# Requirements — info-maintain

## Definition requirements

- Package name: `info-maintain`.
- Catalog action: Rebuild maintained info documents.
- Primary agent role: `information-agent`.
- Discovery description: Rebuild local project and skills info documents when maintained records or QA evidence change.
- Scope and decision conditions: This is an internal skill. Use it after Research-assistant project records,
managed skills, or QA evidence change. It is responsible only for maintaining
the approved root and local INFO formats from authoritative records. Its inputs
are current `AGENTS.md`, maintained skill definitions, topic folders, and QA
records; it produces refreshed root, skills, knowledge, or topic-local
`INFO.md` files. It has no user activation command; a calling workflow invokes
it.
Primary agent role: information-agent.
- Dependencies: None.

## Skill-specific requirements

- It must derive root navigation and the skills catalog from maintained records.
- It must preserve only Description, Entry Points, and Public Interfaces in
- It must render `skills/INFO.md` as only `# SKILLS Info` and one table with
- It must display recorded validation status or PENDING without inventing a pass.
- It must link each listed skill, plan, and QA record using existing paths.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
