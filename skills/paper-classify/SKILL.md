---
name: paper-classify
description: Classify one analyzed topic paper using explicit topic criteria and visible evidence limits.
metadata:
  source: project
  action: Classify one topic paper.
---

# Classify Paper

## Scope

Use when the researcher says `Classify paper {paper} for {topic}` or provides
topic-specific classification criteria. It receives an analyzed topic paper and
criteria, then produces a transparent classification record. Ask for
clarification when criteria, paper identity, or a required source field is
missing.
Primary agent role: literature-agent.

## Workflow

1. Read `docs/classification-schema.md`, the topic question, paper analysis,
   references, and any approved topic-specific criteria.
2. Record each default or approved field with a supporting source location,
   inference label, or an explicit unknown state.
3. Write `papers/{paper-id}/classification.md` and update the topic paper index
   and topic `INFO.md` with a concise, linked status.
4. Escalate a category that would require facts unavailable in the paper.

## Constraints

- Do not manufacture a score, label, comparison, or consensus.
- Do not silently change shared criteria or rewrite the paper analysis.

## Dependencies

- `paper-analyze`
