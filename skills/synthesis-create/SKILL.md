---
name: synthesis-create
description: Create a bounded literature synthesis, comparison table, and gap analysis from an explicit topic paper corpus.
metadata:
  source: project
  action: Create one literature synthesis.
---

# Create Synthesis

## Scope

Use when the researcher says `Create synthesis for {topic}` and identifies a
paper corpus, question, and comparison dimensions. It receives those inputs
and produces a topic-local survey, comparison table, and gap record. Ask for
clarification when the corpus boundary or comparison criteria are missing.
Primary agent role: literature-agent.

## Workflow

1. Read topic paper analyses and classifications, plus
   `../writing-refine/docs/scholarly-writing-standard.md`.
2. Build a source inventory and comparison table that distinguishes reported
   facts from the synthesis's inferences.
3. Identify patterns, disagreements, evidence gaps, and opportunities without
   treating paper counts as truth.
4. Write a dated synthesis in `publications/` and link it from the publication
   index, paper index, and topic `INFO.md`.
5. Hand off a draft survey to `write-literature-review` when requested.

## Constraints

- Do not expand a bounded corpus or claim systematic-review coverage without a
  documented search and selection method.
- Do not invent cross-paper comparability, study characteristics, or consensus.

## Dependencies

- `paper-analyze`
- `paper-classify`
- `write-literature-review`
