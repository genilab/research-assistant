---
name: topic-show
description: Present the maintained topic INFO for one existing research topic without changing it.
metadata:
  source: project
  action: Show one maintained topic info index.
---

# Show Topic Info

## Scope

Use when the researcher says `Show info {topic}`. It receives an existing topic
name and produces its current maintained `INFO.md` content. Ask for
clarification when the topic is missing or more than one topic matches.
Primary agent role: information-agent.

## Workflow

1. Locate the topic through `knowledge/INFO.md`.
2. Read and present its `INFO.md` without altering formatting, links, or status.
3. State when the topic index is absent, incomplete, or ambiguous and route a
   repair only through the appropriate maintenance workflow.

## Constraints

- Do not modify topic records, summarize other material, or substitute a README
  for the maintained topic INFO.
- Do not infer a topic match from a partial or conflicting name.
