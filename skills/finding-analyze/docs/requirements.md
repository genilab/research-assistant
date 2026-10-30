# Requirements — finding-analyze

## Definition requirements

- Package name: `finding-analyze`.
- Catalog action: Analyze one experiment finding set.
- Primary agent role: `experiment-agent`.
- Discovery description: Analyze catalogued experimental findings against their plan, measures, validity limits, and research claim.
- Scope and decision conditions: Use when the researcher says `Analyze findings for {topic}` and identifies an
experiment plan and catalogued result set. It receives those records and
produces a bounded interpretation with claim alignment, alternative
explanations, and validity limits. Ask for clarification when the plan, result
provenance, measures, or target claim is missing.
Primary agent role: experiment-agent.
- Dependencies: `result-catalog`, `report-experiment`

## Skill-specific requirements

- Require a plan, result catalog, and target claim or question.
- Separate observations, inference, alternatives, and open questions.
- Record deviations and validity limits.
- Update indexes without modifying raw evidence.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
