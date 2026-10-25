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
- Maintain the root `README.md` for external GitHub publication in the minimal
  Knowledge-worker format: purpose paragraph plus the verified Topics table.

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
