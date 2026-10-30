# Requirements — behavior-refine

## Definition requirements

- Package name: `behavior-refine`.
- Catalog action: Refine one research behavior.
- Primary agent role: `research-agent`.
- Discovery description: Learn one reusable research behavior from researcher-supplied examples or instructions and record its scope, evidence, and limits.
- Scope and decision conditions: Use when the researcher supplies examples or instructions for a new research
practice. It receives the examples, intended use, and proposed behavior; it
produces a confirmed, bounded addition to a guideline or a proposal for a new
skill. Ask for clarification when the behavior, evidence, scope, or owner is
ambiguous.
Primary agent role: research-agent.
- Dependencies: `skill-create`

## Skill-specific requirements

- Require examples or instructions and an intended research use.
- Distinguish observation, preference, reusable behavior, and limitation.
- Obtain confirmation before a durable guideline or skill change.
- Route new skills through the managed skill-creation workflow.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
