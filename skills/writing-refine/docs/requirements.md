# Requirements — writing-refine

## Definition requirements

- Package name: `writing-refine`.
- Catalog action: Refine one scholarly writing convention.
- Primary agent role: `writing-agent`.
- Discovery description: Learn a reusable scholarly-writing convention from researcher-supplied examples without copying their prose or inventing a universal rule.
- Scope and decision conditions: Use when the researcher supplies academic-paper examples or instructions and
asks to learn a writing convention. It receives the examples, intended paper
context, and requested convention; it produces a concise, evidence-linked
addition to the shared writing guidance. Ask for clarification when the example
set, context, or proposed rule is ambiguous.
Primary agent role: writing-agent.
- Dependencies: None.

## Skill-specific requirements

- Require supplied examples or instructions and a stated writing context.
- Derive a scoped pattern, limits, and examples of appropriate use.
- Obtain confirmation before changing shared writing guidance.
- Do not copy source prose or rewrite a target paper.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
