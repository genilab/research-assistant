# Requirements — paper-classify

## Definition requirements

- Package name: `paper-classify`.
- Catalog action: Classify one topic paper.
- Primary agent role: `literature-agent`.
- Discovery description: Classify one analyzed topic paper using explicit topic criteria and visible evidence limits.
- Scope and decision conditions: Use when the researcher says `Classify paper {paper} for {topic}` or provides
topic-specific classification criteria. It receives an analyzed topic paper and
criteria, then produces a transparent classification record. Ask for
clarification when criteria, paper identity, or a required source field is
missing.
Primary agent role: literature-agent.
- Dependencies: `paper-analyze`

## Skill-specific requirements

- Require an analyzed paper and explicit default or topic-specific criteria.
- Record evidence, inference, or unknown status for every classification field.
- Preserve the analysis and update only the classification and indexes.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
