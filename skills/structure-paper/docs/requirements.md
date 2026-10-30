# Requirements — structure-paper

## Definition requirements

- Package name: `structure-paper`.
- Catalog action: Create one paper structure.
- Primary agent role: `writing-agent`.
- Discovery description: Design an evidence-aware paper structure before drafting when a research argument needs a defensible outline.
- Scope and decision conditions: Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Structure paper for {topic}: {title}`
or asks for a research paper outline before drafting. It is responsible only for
**creating one paper structure**. Its inputs are an existing topic, title or working title,
research question or thesis, intended audience or format, available evidence,
and constraints. It produces an indexed argument map and section outline; it
does not draft the paper itself. User activation command: `Structure paper for {topic}: {title}`.
- Dependencies: None.

## Skill-specific requirements

- It must accept an existing topic, title, question or thesis, audience/format, available
- It must express each section's purpose, claim/question, evidence need,
- It must apply the shared publication guide and create/index
- It must make the status of a provisional thesis and unresolved evidence
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
