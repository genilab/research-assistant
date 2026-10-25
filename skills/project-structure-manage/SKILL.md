---
name: project-structure-manage
description: Create or reconcile one confirmed agent-worker project structure without overwriting existing material.
metadata:
  source: core
  action: Create or reconcile one standard project structure.
---

# Manage Project Structure

## Scope

Use this skill when the user asks to create, complete, or reconcile an
agent-worker project's standard structure. It receives a confirmed project
identity, role, and required local areas. It produces the missing required
folders and control documents, or an evidence-based report of conflicts.

## Workflow

1. Read `docs/plan.md`, the target `AGENTS.md` if it exists, and relevant
   INFO documents. Confirm project identity, role, expected permanent
   structure, and whether external GitHub documentation is required.
2. Inspect the target filesystem. If the expected structure is absent, create
   the required folders, `AGENTS.md`, and main and local `INFO.md` documents.
   Create `README.md` only when external documentation is explicitly required.
3. If the structure already exists, add only missing required elements and
   reconcile stale navigation. Preserve extra or conflicting material and
   report it for a user decision.
4. Do not create topic content, product code, or local skills outside the
   confirmed scope. Report the resulting structure, changes made, and open
   decisions.

## Constraints

- Do not overwrite, delete, or reclassify existing material without explicit
  authorization.
- Do not infer a project role or treat README as internal navigation.
- Keep migration material only under the target project's `temp/` directory.
- Escalate an ambiguous project identity, ownership conflict, or incompatible
  existing structure.
