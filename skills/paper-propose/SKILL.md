---
name: paper-propose
description: Propose a topic-specific academic paper structure with the purpose, evidence, and open dependencies for every section.
metadata:
  source: project
  action: Propose one topic paper.
---

# Propose Paper

## Scope

Use when the researcher says `Propose {Type_Paper} Paper for {topic}`, where
`Type_Paper` is Vision, Survey, Experimentation, Results, or Positioning. It
receives an existing topic and selected paper type, then produces an indexed
proposal that names every section, what it must establish, the evidence it
needs, and its unresolved dependencies. Ask for clarification when the topic,
paper type, audience, central question, or available evidence is unclear.
Primary agent role: writing-agent.

## Workflow

1. Read the topic INFO, ideas, relevant paper records, and
   `../writing-refine/docs/scholarly-writing-standard.md`.
2. Confirm the paper type and central question or contribution. Select its
   required section pattern:
   - Vision: context, vision, scenarios, pathways, assumptions, risks, and next steps.
   - Survey: question, selection method, landscape, comparison, gaps, limits, and agenda.
   - Experimentation: question, design, materials, measures, results, validity, and implications.
   - Results: contribution, related work, method, results, interpretation, threats, and implications.
   - Positioning: decision context, position, evidence, alternatives, criteria, limits, and implications.
3. For every section, state purpose, required claims or content, required source
   or experiment evidence, relationship to adjacent sections, and current gap.
4. Write `publications/{paper-type}-{slug}-proposal.md` and update the topic
   publication index and topic INFO. Hand off later drafting to the appropriate
   internal paper-writing skill.

## Constraints

- Do not draft full paper prose, invent evidence, or present a provisional
  contribution as established.
- Do not silently select a paper type or resolve a contested thesis.

## Dependencies

- `structure-paper`
- `results-paper`
- `write-literature-review`
- `write-positioning-paper`
- `write-vision-paper`
