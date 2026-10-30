# Requirements — info-learn

## Definition requirements

- Package name: `info-learn`.
- Catalog action: Add attributed learning to a topic.
- Primary agent role: `knowledge-agent`.
- Discovery description: Absorb supplied knowledge, ideas, or references into one existing topic without losing provenance.
- Scope and decision conditions: This is an external skill. Use it when the user says `Learn info about
{topic}`, `Absorb info about {topic}`, or uses `$info-learn`. It is responsible
only for adding supplied material to one existing topic. Its inputs are the
topic, supplied information and/or idea and/or source file or citation; it
produces appended, appropriately attributed topic records. User activation command:
`Learn info about {topic}`.
Primary agent role: knowledge-agent.
- Dependencies: `info-maintain`

## Skill-specific requirements

- It must identify an existing topic before changing its records.
- It must preserve each supplied source file under the topic's `references/`
- It must append source-grounded synthesis to the info record under an
- It must append ideas, hypotheses, and open questions only to the ideas
- It must retain uncertainty, attribution, and conflicting claims rather than
- It must refresh the topic-level INFO summary and links after durable learning.
- It must ask for clarification when the topic, source identity, or content

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
