# Requirements — topic-show

## Definition requirements

- Package name: `topic-show`.
- Catalog action: Show one maintained topic info index.
- Primary agent role: `information-agent`.
- Discovery description: Present the maintained topic INFO for one existing research topic without changing it.
- Scope and decision conditions: Use when the researcher says `Show info {topic}`. It receives an existing topic
name and produces its current maintained `INFO.md` content. Ask for
clarification when the topic is missing or more than one topic matches.
Primary agent role: information-agent.
- Dependencies: None.

## Skill-specific requirements

- Require one existing, unambiguous topic.
- Locate and present only its maintained INFO index.
- Report missing, incomplete, or ambiguous indexes without repairing them.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
