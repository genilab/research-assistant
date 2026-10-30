# Requirements — analyze-literature

## Definition requirements

- Package name: `analyze-literature`.
- Catalog action: Analyze one defined literature corpus.
- Primary agent role: `literature-agent`.
- Discovery description: Analyze a defined literature corpus when the user needs a comparative, source-aware research synthesis.
- Scope and decision conditions: Primary agent role: literature-agent.

This is an external skill. Use it when the user says `Analyze literature for
{topic}: {question}` or supplies a source corpus for comparative review. It is
responsible only for **analyzing one defined literature corpus**. Its inputs
are an existing topic, research question, identified source corpus, optional
comparison dimensions, and an output depth. It produces one indexed topic-local
analysis that makes its evidence and limitations visible. User activation command: `Analyze literature for {topic}: {question}`.
- Dependencies: None.

## Skill-specific requirements

- It must require an existing topic, question, source corpus, and intended analysis depth;
- It must inventory source identity, type, relevant method/evidence basis, and
- It must apply the shared publication guide, write
- It must distinguish source claims, analysis inference, evidence gaps, and
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
