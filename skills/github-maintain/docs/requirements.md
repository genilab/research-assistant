# Requirements — github-maintain

## Definition requirements

- Package name: `github-maintain`.
- Catalog action: Connect, inspect, versioned commit, or pull one project on explicit request.
- Primary agent role: `publication-agent`.
- Discovery description: Perform one explicitly requested GitHub connection, status, versioned commit, or pull operation for a confirmed project.
- Scope and decision conditions: Use this skill when the user says `GitHub {action}` for one confirmed project.
Supported actions are `status`, `connect {owner/repository}`, `commit`,
`commit version`, `commit minor version`, `commit major version`, and `pull`.
Every commit action generates a concise message from the changed files and
creates a GitHub-controlled semantic version release. It never synchronizes
automatically. Apply the portable
[version-control standard](docs/version_control.md).
Primary agent role: publication-agent.
- Dependencies: None.

## Skill-specific requirements

- It must accept `status`, `connect {owner/repository}`, `commit`, `commit
- It must confirm the exact project root before every operation.
- It must keep status read-only.
- It must initialize local Git only at the confirmed root and create a GitHub
- It must generate a concise factual commit message from the changed files.
- It must create a semantic GitHub release after a successful commit and push.
- It must default `commit` to a patch bump, use minor for `commit version` and
- It must use GitHub releases and semantic tags as the sole version authority,
- It must pull only by safe fast-forward from a clean, non-divergent branch.
- It must refuse automatic synchronization and any destructive or

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
