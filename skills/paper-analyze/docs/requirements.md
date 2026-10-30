# Requirements — paper-analyze

## Definition requirements

- Package name: `paper-analyze`.
- Catalog action: Analyze one topic paper.
- Primary agent role: `literature-agent`.
- Discovery description: Create a structured, source-aware analysis of one topic-local academic paper without inferring a peer-review recommendation.
- Scope and decision conditions: Use when the researcher says `Analyze paper {paper} for {topic}` or requests a
structured review of an ingested paper. It receives a topic-local source and
produces an analysis record with claims, reasoning, conceptual framing,
theoretical position, evidence basis, limitations, and complete references.
Ask for clarification when the paper or requested depth is ambiguous.
Primary agent role: literature-agent.
- Dependencies: `paper-classify`

## Skill-specific requirements

- Read the identified source and shared analysis and writing guidelines.
- Keep extraction, analysis, and peer-review judgment distinct.
- Create separate analysis and complete-reference records.
- Record claims, evidence basis, limits, and conceptual positioning.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
