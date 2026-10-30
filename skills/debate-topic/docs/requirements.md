# Requirements — debate-topic

## Definition requirements

- Package name: `debate-topic`.
- Catalog action: Develop one debate brief.
- Primary agent role: `argument-agent`.
- Discovery description: Prepare a balanced, evidence-aware debate brief for a clearly stated proposition or contested research question.
- Scope and decision conditions: Primary agent role: argument-agent.

This is an external skill. Use it when the user says `Debate topic
{topic}: {proposition}` or needs a balanced analysis of a contested research question.
It is responsible only for **developing one debate brief**. Its inputs are an
existing topic, proposition or question, relevant context, intended audience, evaluation
criteria, and available evidence or source constraints. It produces one
indexed brief with charitable cases and visible uncertainty. User activation command: `Debate topic {topic}: {proposition}`.
- Dependencies: None.

## Skill-specific requirements

- It must require an existing topic, proposition/question, context, audience, evidence or source
- It must separate evidence-supported premises, inference, value judgment, and
- It must apply the shared publication guide and create/index
- It must reject false balance and fabricated support while preserving material
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
