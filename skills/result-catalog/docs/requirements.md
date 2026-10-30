# Requirements — result-catalog

## Definition requirements

- Package name: `result-catalog`.
- Catalog action: Catalog one experiment result set.
- Primary agent role: `experiment-agent`.
- Discovery description: Catalog observed experiment results with provenance, conditions, measures, analysis, and interpretation boundaries.
- Scope and decision conditions: Use when the researcher says `Catalog results for {topic}` and identifies an
experiment and observed results. It receives the result material and produces a
linked, provenance-aware record. Ask for clarification when the experiment,
source data, conditions, or measurement meaning is unknown.
Primary agent role: experiment-agent.
- Dependencies: `report-experiment`

## Skill-specific requirements

- Require an experiment identifier, result provenance, and conditions.
- Record measures, transformations, analysis, observations, and limits.
- Update experiment and topic indexes without changing source data.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
