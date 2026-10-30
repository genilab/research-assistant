# Requirements — topic-create

## Definition requirements

- Package name: `topic-create`.
- Catalog action: Create one listed knowledge topic.
- Primary agent role: `knowledge-agent`.
- Discovery description: Create a complete, listed knowledge topic when the user asks to start a topic.
- Scope and decision conditions: This is an external skill. Use it when the user says `Create topic {topic}` or
`create topic {topic}`. It creates one complete empty research topic, its
topic-level index, and its initial discussion entry. Its input is a
human-readable topic name and optional short description; it produces a slugged
topic folder containing the required records. User activation command:
`Create topic {topic}`.
Primary agent role: knowledge-agent.
- Dependencies: `info-maintain`

## Skill-specific requirements

- It must accept a topic name and optionally a short scope description.
- It must derive a stable lowercase-hyphenated topic slug and reject a collision.
- It must retain the three core topic records and references folder, then add
- It must seed an initial exploration entry in the ideas record without
- It must add exactly one linked main-info entry for the created topic.
- It must ask for clarification when the topic is ambiguous or duplicates an
- It must report the created topic and the available next learning action.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
