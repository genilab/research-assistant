---
name: knowledge-base-maintain
description: Reconcile a topic-based knowledge base and its main info from verified folders.
metadata:
  source: core
  action: Reconcile the knowledge-base structure and info.
---

# Maintain Knowledge Base

## Scope

Use this skill to reconcile one knowledge base's topic folders and
`knowledge/INFO.md` and the external-facing root `README.md`. It receives the
current topic structure and produces accurate navigation and a concise topic
catalog without changing information, ideas, or source content.

## Workflow

1. Read `docs/plan.md`, `knowledge/INFO.md`, `README.md`, and the candidate
   topic folders.
2. Verify every topic follows the prescribed schema and identify missing or
   conflicting records.
3. Update the main knowledge INFO only from verified topic folders.
4. Update the README's Topics table from the same verified folders: each row
   contains the topic display name and its concise verified description. When
   no topics exist, retain exactly the default `_No topics yet_` row.
5. Report structure gaps as pending work.

## Constraints

- Do not manufacture topic content or provenance.
- Do not overwrite source material or merge colliding topics.
- Do not add internal workflow details, plans, QA evidence, or unverified
  descriptions to the README.
- Escalate ambiguous topic identity or a nonstandard topic schema.
