# Requirements — experiment-plan

## Definition requirements

- Package name: `experiment-plan`.
- Catalog action: Plan one topic experiment.
- Primary agent role: `experiment-agent`.
- Discovery description: Design one topic-local experiment with a testable question, method, measures, validity checks, and decision conditions.
- Scope and decision conditions: Use when the researcher says `Plan experiment for {topic}` and supplies a
research question, claim, or decision to test. It receives the topic and
available constraints, then produces an experiment plan. Ask for clarification
when the question, comparison, measure, available materials, or ethical scope
is insufficiently defined.
Primary agent role: experiment-agent.
- Dependencies: `result-catalog`

## Skill-specific requirements

- Require a research question, testable claim, and available constraints.
- Specify comparison, measures, procedure, analysis, and decision conditions.
- Record validity, ethical, and operational limits.
- Create and index a topic-local plan without reporting results.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
