# Requirements — project-structure-manage

## Definition requirements

- Package name: `project-structure-manage`.
- Catalog action: Create or reconcile one standard project structure.
- Primary agent role: `structure-agent`.
- Discovery description: Create or reconcile one confirmed agent-worker project structure without overwriting existing material.
- Scope and decision conditions: Use this skill when the user asks to create, complete, or reconcile an
agent-worker project's standard structure. It receives a confirmed project
identity, role, and required local areas. It produces the missing required
folders and control documents, or an evidence-based report of conflicts.
Primary agent role: structure-agent.
- Dependencies: None.

## Skill-specific requirements

- It must confirm project identity, role, required structure, and external
- It must establish the target's graph-based multi-agent orchestration
- It must create required folders, `AGENTS.md` with the multi-agent
- It must reconcile missing required elements and stale navigation when the
- It must preserve unexpected or conflicting material and report it rather
- It must distinguish permanent project structure from temporary migration
- It must ask whether the project adopts the shared GitHub/version-control
- It must record the owner-selected repository visibility and README profile

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
