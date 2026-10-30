# Requirements — code-document

## Definition requirements

- Package name: `code-document`.
- Catalog action: Apply the shared documentation standard to skill code and tests.
- Primary agent role: `skill-agent`.
- Discovery description: Document and validate managed source code when code or test files need the code-worker documentation standard.
- Scope and decision conditions: This is an internal skill. Use it when a managed source or test file is created,
changed, or checked for documentation quality. It is responsible only for
applying the code-worker documentation standard without changing behavior. Its
inputs are the source file and its owning project, module, or skill record, and
it produces documented source plus validation findings. It has no user activation
command; a calling workflow invokes it.
Primary agent role: skill-agent.
- Dependencies: None.

## Skill-specific requirements

- It must apply the source-code standard: factual header, preserved license and attribution, `AI instruction:` module overview, readable import order, public docstrings, and purposeful comments to managed source and test files.
- It must preserve behavior, public interfaces, licenses, and attribution while documenting code.
- It must derive project identity and source description from maintained records rather than inventing them.
- It must validate the required documentation structure before reporting a result.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
