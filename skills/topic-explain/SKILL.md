---
name: topic-explain
description: Explain an existing research topic from its maintained topic INFO without changing any topic record.
metadata:
  source: project
  action: Explain one maintained research topic.
---

# Explain Topic

## Scope

Use when the researcher says `Explain topic {topic}`. It receives an existing
topic and its maintained `INFO.md`, then produces a concise explanation of the
current summary, focus, linked records, active directions, and open decisions.
Ask for clarification when the topic is missing or ambiguous.
Primary agent role: knowledge-agent.

## Workflow

1. Locate the topic through `knowledge/INFO.md` and read its `INFO.md`.
2. Explain the topic only from the maintained summary and linked record status.
3. Identify when an index is incomplete or stale rather than inventing a
   current conclusion from unlinked source material.
4. Offer the relevant public action for the researcher's next step.

## Constraints

- Do not modify the topic, summarize unindexed content as current knowledge, or
  conduct new research in this workflow.
- Do not hide uncertainty, open decisions, or missing records.

## Dependencies

- `topic-show`
