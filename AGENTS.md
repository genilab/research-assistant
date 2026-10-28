# Knowledge-worker

This workspace is the `Knowledge-worker` base project. It holds the shared
skills and topic-based knowledge structure used by other agent-worker
projects. Temporary migration evidence belongs only in `temp/`.

## Navigation

- Start at [INFO.md](INFO.md).
- Read an invoked skill completely before using or changing it.
- Use [skills/INFO.md](skills/INFO.md) for the local skill catalog.
- Use [knowledge/INFO.md](knowledge/INFO.md) for the topic-based knowledge
  base.

## Multi-agent orchestration

Knowledge-worker is a graph-based multi-agent knowledge-maintenance project.
Its orchestrator interprets confirmed public actions, routes work to the
appropriate agent role and bounded skill, reviews the returned evidence, and
either completes the action, requests a decision, or makes an explicit
handoff. It does not authorize external, destructive, or ambiguous changes on
its own.

| Agent role | Responsibility | Skills | Handoffs |
| --- | --- | --- | --- |
| `structure-agent` | Maintain the approved project and agent-control structure. | `project-structure-manage`, `agents-file-manage` | Returns structural evidence to the orchestrator. |
| `skill-agent` | Create, document, and verify bounded reusable capabilities. | `skill-create`, `skill-validate`, `code-document` | Routes catalog changes to `information-agent`. |
| `information-agent` | Maintain and present internal navigation information. | `info-maintain`, `info-show` | Returns requested information or routes knowledge work to `knowledge-agent`. |
| `knowledge-agent` | Create topics and maintain durable, attributed knowledge. | `topic-create`, `info-learn`, `knowledge-base-maintain` | Returns evidence to the orchestrator. |
| `publication-agent` | Maintain external repository documentation and explicit GitHub operations. | `readme-maintain`, `github-maintain` | Escalates external writes and version decisions to the user. |

The deliberation path is always **public action → orchestrator → agent role →
skill workflow → evidence → orchestrator**. The orchestrator may route a
confirmed handoff to another listed role; unclear requirements, conflicts, and
approval-gated work return to the user. These roles are capability nodes in
the project graph, not a claim that persistent external agents are already
running. See the transferable [graph-based multi-agent project model](skills/project-structure-manage/docs/multiagent_project_model.md).

## Info actions

- `Show info` opens the root [INFO.md](INFO.md) in the workspace editor.
- `Show info {area}` opens the confirmed area's local `INFO.md` through
  [info-show](skills/info-show/SKILL.md).

## Permanent structure

- `skills/` contains complete local skill packages in the approved format.
- Every local skill package uses the lowercase `{target}-{action}` naming
  convention; its folder name and `name` front-matter value must match.
- Every `SKILL.md` uses Codex-compatible top-level front matter: `name`,
  `description`, and optional supported fields only. Knowledge-worker routing
  data belongs in `metadata`; public actions are defined in `AGENTS.md` and
  root `INFO.md`, not as custom Codex front-matter fields.
- Every local skill declares exactly one primary agent role in its `Scope`;
  that role must appear in the Agent graph above.
- `knowledge/` contains durable topic-based knowledge only.
- `temp/` contains migration-only material and will be deleted after migration
  acceptance.
- `INFO.md` is the internal navigation document. A root `README.md` is added
  only when external GitHub documentation is specifically required.
- The root `INFO.md` and `skills/INFO.md` must follow the approved formats in
  [the info-format standard](skills/info-maintain/docs/info_format.md).

## Knowledge topics

Each topic lives at `knowledge/{topic-slug}/` and contains `references/`,
`{topic-slug}_info.md`, `{topic-slug}_ideas.md`, and
`{topic-slug}_refs.md`. Preserve source material in `references/`; record
attributed information in the info record and proposals or questions in the
ideas record.

## Boundaries

- Shared changes require a documented transfer decision; project-specific work
  remains in its owning project.
- Do not retain migration records outside `temp/`.
- Maintain the root `README.md` according to the repository-publication
  declaration below.

## Repository publication

- Repository visibility: `public`.
- README profile: `public-release`.
- README maintenance: reconcile it before every explicitly requested GitHub
  commit using [readme-maintain](skills/readme-maintain/SKILL.md) and the
  [public-release template](skills/readme-maintain/docs/public_release_template.md).

## GitHub actions

- `GitHub {action}` invokes
  [github-maintain](skills/github-maintain/SKILL.md).
- Apply the shared [GitHub version-control standard](skills/github-maintain/docs/version_control.md).

Supported actions are `status`, `connect {owner/repository}`, `commit`,
`commit version`, `commit minor version`, `commit major version`, and `pull`.

Every commit creates a generated message and a GitHub-controlled semantic
release. `commit` defaults to a patch bump; `commit version` and `commit minor
version` use a minor bump; `commit major version` uses a major bump.

GitHub synchronization is manual only. No action connects, commits, pushes,
pulls, or creates a repository unless the user explicitly requests that action.
