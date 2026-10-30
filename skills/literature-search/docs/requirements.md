# Requirements — literature-search

## Definition requirements

- Package name: `literature-search`.
- Catalog action: Search related academic literature.
- Primary agent role: `literature-agent`.
- Discovery description: Search for related academic work using a confirmed topic question, source scope, and transparent selection record.
- Scope and decision conditions: Use when the researcher says `Search literature for {topic}` and provides a
question, source constraints, or depth. It receives an existing topic and
search brief, then produces a traceable candidate-source list and selection
record. Ask for clarification when the question, allowed sources, date scope,
or intended depth is missing.
Primary agent role: literature-agent.
- Dependencies: `paper-learn`

## Skill-specific requirements

- Require a topic, question, source scope, and intended depth.
- Record search terms, sources, dates, and inclusion or exclusion decisions.
- Present candidate papers before ingestion.
- Avoid unsupported completeness and quality claims.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
