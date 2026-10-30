# Requirements — topic-explain

## Definition requirements

- Package name: `topic-explain`.
- Catalog action: Explain one maintained research topic.
- Primary agent role: `knowledge-agent`.
- Discovery description: Explain an existing research topic from its maintained topic INFO without changing any topic record.
- Scope and decision conditions: Use when the researcher says `Explain topic {topic}`. It receives an existing
topic and its maintained `INFO.md`, then produces a concise explanation of the
current summary, focus, linked records, active directions, and open decisions.
Ask for clarification when the topic is missing or ambiguous.
Primary agent role: knowledge-agent.
- Dependencies: `topic-show`

## Skill-specific requirements

- Require one existing, unambiguous topic.
- Read the topic INFO as the primary source of current state.
- Explain summary, focus, linked records, directions, and open decisions.
- Report a missing or stale index rather than inferring missing content.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
