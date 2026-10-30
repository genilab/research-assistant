# Requirements — agents-file-manage

## Definition requirements

- Package name: `agents-file-manage`.
- Catalog action: Create or maintain one standard `AGENTS.md`.
- Primary agent role: `structure-agent`.
- Discovery description: Create or maintain one project AGENTS.md from confirmed operating decisions.
- Scope and decision conditions: Use this skill when a project needs its initial `AGENTS.md` or when confirmed
changes affect its identity, navigation, permanent structure, operating rules,
shared resources, or boundaries. It produces a new or minimally revised
operating contract for one project.
Primary agent role: structure-agent.
- Dependencies: None.

## Skill-specific requirements

- It must confirm project identity, role, resource locations, and boundaries
- It must establish or preserve the graph-based multi-agent contract: a
- It must create a complete operating contract when the file is absent.
- It must preserve existing guidance and make only confirmed changes when the
- It must identify stale links, conflicting guidance, and decisions requiring
- It must distinguish operating guidance from durable knowledge and INFO
- It must not represent a capability role as a persistent external agent

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
