# Requirements — results-paper

## Definition requirements

- Package name: `results-paper`.
- Catalog action: Write one topic results paper.
- Primary agent role: `writing-agent`.
- Discovery description: Write one topic-specific results paper from linked experiment plans and catalogued findings.
- Scope and decision conditions: Use when the researcher says `Write results paper for {topic}` and identifies
the experiments and findings to report. It receives linked plans, result
catalogs, an intended contribution, audience, and scope; it produces an indexed
topic-local results-paper draft. Ask for clarification when the evidence set,
claim scope, or target paper form is unclear.
Primary agent role: writing-agent.
- Dependencies: `experiment-plan`, `result-catalog`

## Skill-specific requirements

- Require identified experiment plans and result catalogs.
- Structure the paper around contribution, method, results, and validity limits.
- Preserve null, conflicting, and limited findings.
- Create and index only the requested topic-local draft.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
