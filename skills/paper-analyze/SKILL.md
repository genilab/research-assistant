---
name: paper-analyze
description: Create a structured, source-aware analysis of one topic-local academic paper without inferring a peer-review recommendation.
metadata:
  source: project
  action: Analyze one topic paper.
---

# Analyze Paper

## Scope

Use when the researcher says `Analyze paper {paper} for {topic}` or requests a
structured review of an ingested paper. It receives a topic-local source and
produces an analysis record with claims, reasoning, conceptual framing,
theoretical position, evidence basis, limitations, and complete references.
Ask for clarification when the paper or requested depth is ambiguous.
Primary agent role: literature-agent.

## Workflow

1. Read `docs/paper-analysis-method.md`,
   `../writing-refine/docs/scholarly-writing-standard.md`, and the source paper.
2. Extract the central thesis, key claims, line of reasoning, evidence basis,
   and material limitations. Label extraction separately from interpretation.
3. Frame each material claim against relevant research domains or established
   foundations, and state the theoretical role without overstating it.
4. Write `papers/{paper-id}/analysis.md` and `references.md`, preserving each
   bibliographic entry as a separate complete paragraph. Update `papers/INFO.md`.
5. Offer `paper-classify` or a separately requested peer-review-style critique;
   never assign a recommendation by default.

## Constraints

- Do not fabricate citations, methods, results, or theoretical contribution.
- Do not replace source text or imply that an analytical review is peer review.

## Dependencies

- `paper-classify`
