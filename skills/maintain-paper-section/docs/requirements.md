# Requirements — maintain-paper-section

## Definition requirements

- Package name: `maintain-paper-section`.
- Catalog action: Maintain one named paper section.
- Primary agent role: `writing-agent`.
- Discovery description: Draft or revise one named paper section while preserving the existing argument and source boundaries.
- Scope and decision conditions: Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Maintain paper section
{topic}: {paper}: {section}` or asks to draft or revise a named section of an existing
paper. It is responsible only for **maintaining one named paper section**. Its
inputs are an existing topic, existing paper path, section identity, requested change, and
approved evidence or style constraints. It produces a scoped revision and a
summary of unresolved support issues. User activation command: `Maintain paper section {topic}: {paper}: {section}`.
- Dependencies: None.

## Skill-specific requirements

- It must require an existing topic, paper path, named section, requested change, approved
- It must inspect the surrounding argument, preserve source/citation markers,
- It must apply the shared publication guide, report the section changed,
- It must not change the central thesis or unrelated sections without a new,
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
