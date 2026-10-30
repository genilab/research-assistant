# Requirements — argument-develop

## Definition requirements

- Package name: `argument-develop`.
- Catalog action: Develop one research argument.
- Primary agent role: `argument-agent`.
- Discovery description: Develop one bounded research question, claim, or argument with linked evidence, alternatives, and open dependencies.
- Scope and decision conditions: Use when the researcher says `Develop argument for {topic}` or asks to refine a
research question, contribution, claim, or scientific narrative. It receives an
existing topic, focus, and available evidence; it produces a linked argument
record. Ask for clarification when the question, intended claim, or evaluation
criteria are unclear.
Primary agent role: argument-agent.
- Dependencies: `experiment-plan`, `paper-propose`

## Skill-specific requirements

- Require a topic, bounded focus, and available evidence or explicit gap.
- Record claim, premises, evidence links, alternatives, and dependencies.
- Update argument, direction, and topic-index records.
- Route structure or experimental needs to their dedicated skills.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
