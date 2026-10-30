# Requirements — write-vision-paper

## Definition requirements

- Package name: `write-vision-paper`.
- Catalog action: Write one topic-specific vision paper.
- Primary agent role: `writing-agent`.
- Discovery description: Structure and draft a topic-specific vision paper using the shared publication writing guide.
- Scope and decision conditions: Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Write vision paper for
{topic}` or asks to structure or draft one topic's future-oriented paper. It
is responsible only for **writing one topic-specific Vision Paper**. Its inputs
are an existing topic, working title, intended audience, future horizon,
central vision or question, available evidence, and draft scope. It produces
one indexed file in that topic's `publications/` folder. User activation command: `Write vision paper for {topic}`.
- Dependencies: `maintain-paper-section`

## Skill-specific requirements

- It must require an existing topic, audience, horizon, vision/question,
- It must apply `paper-propose/docs/publication-writing-standard.md` and write the
- It must create and index a `vision-paper-{slug}.md` file in the topic's
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
