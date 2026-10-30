# Requirements — research-topic

## Definition requirements

- Package name: `research-topic`.
- Catalog action: Research one focused knowledge topic.
- Primary agent role: `research-agent`.
- Discovery description: Research a focused topic and preserve a source-aware synthesis in the knowledge base.
- Scope and decision conditions: Primary agent role: research-agent.

This is an external skill. Use it when the user says `Research topic {topic}`
or requests a focused, durable investigation. It is responsible only for
**researching one focused knowledge topic**. Its inputs are a topic, a question
or angle, an optional source set or research constraints, and an intended
depth. It produces an attributed synthesis in one knowledge topic, with sources
and open questions preserved. User activation command: `Research topic {topic}`.
- Dependencies: `topic-create`, `info-learn`

## Skill-specific requirements

- It must accept a topic, focused question or angle, optional source set or
- It must create a missing topic through `create-topic`, and use `learn-info`
- It must ask for a narrower question or missing constraint when responsible
- It must preserve the distinction between source evidence, synthesis, and
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
