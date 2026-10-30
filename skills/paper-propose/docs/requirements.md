# Requirements — paper-propose

## Definition requirements

- Package name: `paper-propose`.
- Catalog action: Propose one topic paper.
- Primary agent role: `writing-agent`.
- Discovery description: Propose a topic-specific academic paper structure with the purpose, evidence, and open dependencies for every section.
- Scope and decision conditions: Use when the researcher says `Propose {Type_Paper} Paper for {topic}`, where
`Type_Paper` is Vision, Survey, Experimentation, Results, or Positioning. It
receives an existing topic and selected paper type, then produces an indexed
proposal that names every section, what it must establish, the evidence it
needs, and its unresolved dependencies. Ask for clarification when the topic,
paper type, audience, central question, or available evidence is unclear.
Primary agent role: writing-agent.
- Dependencies: `structure-paper`, `results-paper`, `write-literature-review`, `write-positioning-paper`, `write-vision-paper`

## Skill-specific requirements

- Require a topic, one supported paper type, audience, central question, and evidence scope.
- Return every section's purpose, content, evidence need, linkage, and gap.
- Support Vision, Survey, Experimentation, Results, and Positioning paper types.
- Create an indexed proposal without drafting the paper.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
