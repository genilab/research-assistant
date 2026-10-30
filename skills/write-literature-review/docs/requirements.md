# Requirements — write-literature-review

## Definition requirements

- Package name: `write-literature-review`.
- Catalog action: Write one topic-specific literature review.
- Primary agent role: `writing-agent`.
- Discovery description: Structure and draft a topic-specific literature review using the shared publication writing guide.
- Scope and decision conditions: Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Write literature review
for {topic}` or asks to structure or draft a review for one topic. It is
responsible only for **writing one topic-specific Literature Review**. Its
inputs are an existing topic, review question, identified corpus or selection
method, comparison dimensions, intended audience, and draft scope. It produces
one indexed file in that topic's `publications/` folder. User activation command: `Write literature review for {topic}`.
- Dependencies: `analyze-literature`, `maintain-paper-section`

## Skill-specific requirements

- It must require an existing topic, review question, source corpus or
- It must apply `paper-propose/docs/publication-writing-standard.md` and write the
- It must create and index a `literature-review-{slug}.md` file in the topic's
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
