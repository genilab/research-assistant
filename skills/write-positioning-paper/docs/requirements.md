# Requirements — write-positioning-paper

## Definition requirements

- Package name: `write-positioning-paper`.
- Catalog action: Write one topic-specific positioning paper.
- Primary agent role: `writing-agent`.
- Discovery description: Structure and draft a topic-specific positioning paper using the shared publication writing guide.
- Scope and decision conditions: Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Write positioning paper
for {topic}` or asks to structure or draft a defensible position for one topic.
It is responsible only for **writing one topic-specific Positioning Paper**.
Its inputs are an existing topic, a bounded position or question, intended
audience, decision context, evidence, material alternatives, and draft scope.
It produces one indexed file in that topic's `publications/` folder. User activation command: `Write positioning paper for {topic}`.
- Dependencies: `maintain-paper-section`

## Skill-specific requirements

- It must require an existing topic, position/question, audience, decision
- It must apply `paper-propose/docs/publication-writing-standard.md` and write the
- It must create and index a `positioning-paper-{slug}.md` file in the topic's
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
