# Requirements — topic-brainstorm

## Definition requirements

- Package name: `topic-brainstorm`.
- Catalog action: Brainstorm candidate research topics.
- Primary agent role: `knowledge-agent`.
- Discovery description: Explore and compare candidate research topics before creating a durable topic record.
- Scope and decision conditions: Use when the researcher says `Brainstorm about {topic}`. It receives an
existing topic, its accumulated records, and a bounded prompt; it produces
research ideas, questions, hypotheses, arguments, directions, and next actions.
Ask for clarification when the topic or brainstorming focus is absent.
Primary agent role: knowledge-agent.
- Dependencies: None.

## Skill-specific requirements

- Require an existing topic and a bounded brainstorming focus.
- Read accumulated topic records before generating new exploration.
- Classify durable outcomes as ideas, arguments, directions, or open questions.
- Avoid unsupported novelty, feasibility, or evidence claims.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
