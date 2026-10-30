# Requirements — skill-create

## Definition requirements

- Package name: `skill-create`.
- Catalog action: Create or revise a managed skill.
- Primary agent role: `skill-agent`.
- Discovery description: Create or revise a managed local skill from its completed plan when a reusable workflow is needed.
- Scope and decision conditions: Use this internal skill when Research-assistant needs a new or revised reusable,
bounded workflow. It accepts a defined skill intent and completed target plan,
then is responsible for producing a managed skill package with only the
artifacts that operation needs. It has no user activation command; a calling
workflow invokes it.
Primary agent role: skill-agent.
- Dependencies: `code-document`, `skill-validate`, `info-maintain`

## Skill-specific requirements

- It must create a named flat skill with `metadata.source: core` or
- It must create a self-contained `docs/plan.md`, `docs/qa.md`, test starter when code is delegated, and an updated skills info.
- It must require a bounded action and workflow before creating a skill.
- It must require the completed target plan before creating or revising the target `SKILL.md`, code, or test units.
- It must create the target `SKILL.md` to cover every target Script Requirement.
- It must create every target `SKILL.md` in the authoritative ideal minimal Codex skill format: valid name and description metadata, one title, focused Scope, Workflow, Constraints, and Dependencies only when another managed skill is invoked.
- It must make each target `SKILL.md` minimally well-described by stating its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within the allowed sections.
- It must assign exactly one primary agent role declared by the owning
- It must reject invalid names, groups, existing destinations, unsupported resources, and catchall or incomplete requests.
- It must apply the source-code standard whenever the target skill has code or test units, including the factual `AI instruction:` context block and readable code structure.
- It must preserve the role, activation, and associated workflow skills declared for the target skill.
- It must record actual validation evidence and refresh the skills info without manufacturing a passing status.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
