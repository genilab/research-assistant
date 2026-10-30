---
name: analyze-literature
description: "Analyze a defined literature corpus when the user needs a comparative, source-aware research synthesis."
metadata:
  source: project
  action: Analyze one defined literature corpus.
---

# Analyze Literature

## Scope

Primary agent role: literature-agent.

This is an external skill. Use it when the user says `Analyze literature for
{topic}: {question}` or supplies a source corpus for comparative review. It is
responsible only for **analyzing one defined literature corpus**. Its inputs
are an existing topic, research question, identified source corpus, optional
comparison dimensions, and an output depth. It produces one indexed topic-local
analysis that makes its evidence and limitations visible. User activation command: `Analyze literature for {topic}: {question}`.

## Workflow

1. Read `docs/plan.md` and
   `../paper-propose/docs/publication-writing-standard.md`.
   Confirm the topic, question, source corpus, and the
   intended analysis depth. Ask for clarification when sources are unavailable,
   the corpus boundary is unclear, or requested comparison criteria would
   require facts not present in the material.
2. Create a source inventory that records identifiers, source type, date,
   method or evidence basis when available, and relevance. Distinguish source
   facts from the analysis's own inferences.
3. Compare sources against the question and requested dimensions. Surface
   agreements, disagreements, methodological differences, applicability
   limits, missing populations or contexts, and research gaps. Do not use a
   source count as a measure of truth.
4. Write `knowledge/{topic-slug}/publications/literature-analysis-{slug}.md`
   with document controls, the question, corpus and selection note, comparison,
   synthesis, limitations, unresolved issues, and references. Add a dated,
   concise entry to that topic's `publications/INFO.md`.
5. Report the created file, corpus coverage, principal synthesis, and any
   source-access or scope limitation.

## Constraints

- Do not silently expand a bounded corpus into a general web search or claim a
  systematic review unless its search and inclusion method has actually been
  supplied or performed.
- Do not invent study characteristics, citations, effect sizes, or consensus;
  label uncertainty and conflicting evidence.
- Do not draft a full paper, alter a knowledge topic, or decide research
  strategy outside the stated analysis. This is instruction-only; no code or
  test unit is delegated.
