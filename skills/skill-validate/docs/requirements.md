# Requirements — skill-validate

## Definition requirements

- Package name: `skill-validate`.
- Catalog action: Validate a managed skill package.
- Primary agent role: `skill-agent`.
- Discovery description: Validate one managed skill or the complete local catalog when current QA evidence is required.
- Scope and decision conditions: This is an internal skill. Use it when a managed skill needs current format,
documentation, code-test, and QA evidence. It is responsible only for checking
the selected named skill or full catalog against its local records. Its
inputs are a selector (`{skill}` or `all`) and current
skill packages, and it produces refreshed `docs/qa.md` records and a skills info.
It has no user activation command; a calling workflow invokes it.
Primary agent role: skill-agent.
- Dependencies: `code-document`, `info-maintain`

## Skill-specific requirements

- It must run Codex's bundled skill validator and validate each selected
- It must validate the required trigger, responsibility, input, outcome, clarification, and non-goal statements for newly managed skills.
- It must write QA results from current checks and report PENDING or FAILED evidence without inventing a pass.
- It must accept `{skill}` or `all` and refresh the skills catalog after validation.
- It must reject a managed skill that does not use the authoritative minimal

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
