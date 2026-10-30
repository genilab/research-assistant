# Requirements — synthesis-create

## Definition requirements

- Package name: `synthesis-create`.
- Catalog action: Create one literature synthesis.
- Primary agent role: `literature-agent`.
- Discovery description: Create a bounded literature synthesis, comparison table, and gap analysis from an explicit topic paper corpus.
- Scope and decision conditions: Use when the researcher says `Create synthesis for {topic}` and identifies a
paper corpus, question, and comparison dimensions. It receives those inputs
and produces a topic-local survey, comparison table, and gap record. Ask for
clarification when the corpus boundary or comparison criteria are missing.
Primary agent role: literature-agent.
- Dependencies: `paper-analyze`, `paper-classify`, `write-literature-review`

## Skill-specific requirements

- Require a topic, research question, corpus, and comparison dimensions.
- Use paper analyses and classifications as traceable evidence.
- Produce a comparison table and an evidence-limited gap analysis.
- Link the resulting synthesis from topic indexes.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
