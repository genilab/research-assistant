# Requirements — paper-learn

## Definition requirements

- Package name: `paper-learn`.
- Catalog action: Learn one topic paper.
- Primary agent role: `literature-agent`.
- Discovery description: Learn one supplied academic paper into a confirmed research topic while preserving its source and provenance.
- Scope and decision conditions: Use when the researcher says `Learn this paper for {topic}` and supplies or
identifies one paper. It receives an existing topic and paper source, then
produces a topic-local, provenance-aware paper record ready for later analysis.
Ask for clarification when the topic, source identity, or storage decision is
ambiguous.
Primary agent role: literature-agent.
- Dependencies: `paper-analyze`

## Skill-specific requirements

- Require an existing topic and identified paper source.
- Confirm a stable paper identifier and detect duplicates.
- Preserve an approved source unchanged or retain a durable source link.
- Update paper and topic indexes without analyzing or classifying the paper.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
