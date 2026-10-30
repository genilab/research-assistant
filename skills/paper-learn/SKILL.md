---
name: paper-learn
description: Learn one supplied academic paper into a confirmed research topic while preserving its source and provenance.
metadata:
  source: project
  action: Learn one topic paper.
---

# Learn Paper

## Scope

Use when the researcher says `Learn this paper for {topic}` and supplies or
identifies one paper. It receives an existing topic and paper source, then
produces a topic-local, provenance-aware paper record ready for later analysis.
Ask for clarification when the topic, source identity, or storage decision is
ambiguous.
Primary agent role: literature-agent.

## Workflow

1. Read the topic INFO, paper index, and
   `../paper-analyze/docs/paper-analysis-method.md`.
2. Confirm paper identity, identify any duplicate, and propose a collision-safe
   paper identifier.
3. After explicit archival approval, preserve the source unchanged in the
   topic paper record or retain an external source link when no file is supplied.
4. Add source provenance, topic relevance, and the paper-index entry. Update
   topic INFO without presenting unreviewed paper content as topic knowledge.
5. Route a requested detailed review to `paper-analyze`.

## Constraints

- Do not alter a supplied source, overwrite a different paper, or archive a
  file without explicit approval.
- Do not classify, recommend, or make paper-content claims in this workflow.

## Dependencies

- `paper-analyze`
