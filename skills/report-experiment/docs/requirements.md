# Requirements — report-experiment

## Definition requirements

- Package name: `report-experiment`.
- Catalog action: Report one topic experiment.
- Primary agent role: `experiment-agent`.
- Discovery description: Write one evidence-bounded experiment report from a topic experiment plan and catalogued results.
- Scope and decision conditions: Use when the researcher says `Report experiment for {topic}` and identifies a
planned experiment with catalogued results. It receives those records and
produces a topic-local experimental report. Ask for clarification when the
plan, results, target audience, or requested claim scope is unclear.
Primary agent role: experiment-agent.
- Dependencies: `result-catalog`

## Skill-specific requirements

- Require a plan and catalogued results for an identified experiment.
- Use the shared experiment and academic-writing guidelines.
- Link claims to results and state deviations and validity limits.
- Index the report in both experiment and publication records.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
