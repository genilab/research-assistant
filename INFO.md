# Knowledge-worker Info

## Description

Knowledge-worker is the shared knowledge-base maintainer for agent-worker projects: it preserves reusable skills and durable topic-based knowledge, with each topic stored in `knowledge/{topic-slug}/` as separate information, ideas, references, and preserved source material so verified learning, exploration, and provenance remain distinct and navigable. Its GitHub repository is [kochf1/knowledge-worker](https://github.com/kochf1/knowledge-worker); the latest remote update is [`11da7a1` — “Remove legacy quickstarter configuration” (2026-09-27)](https://github.com/kochf1/knowledge-worker/commit/11da7a12dd81b7516a0fdb8d2da563ee517b6f2a), while the current local migration is prepared but has not been committed or pushed.

## Entry Points

| Entry point | Location |
| --- | --- |
| Skills | [skills/INFO.md](skills/INFO.md) |
| Knowledge | [knowledge/INFO.md](knowledge/INFO.md) |

## Public Interfaces

- `Show info` or `Show info {area}` opens the main or requested local INFO
  document in the workspace editor, reporting an unknown or ambiguous area
  without changing anything. ([info-show](skills/info-show/SKILL.md))
- `Create topic {topic}` creates the complete topic folder, its information,
  ideas, references, and source-material records, then lists the topic in the
  main knowledge INFO document. ([topic-create](skills/topic-create/SKILL.md))
- `Learn info about {topic}` or `Absorb info about {topic}` adds supplied
  knowledge to an existing topic with attribution, keeping verified
  information, ideas, and source references separate. ([info-learn](skills/info-learn/SKILL.md))
- `GitHub {action}` performs only the requested status, connection, versioned
  commit/release, or pull action; commits generate a message and semantic
  GitHub release, while synchronization never occurs automatically.
  ([github-maintain](skills/github-maintain/SKILL.md))
