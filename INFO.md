# Research-assistant Info

## Description

Research-assistant extends Knowledge-worker's topic-based knowledge model for academic research. It preserves attributed information, ideas, references, and source material in the shared topic schema; topic INFO and the paper, experiment, and publication indexes provide the only research-specific navigation extensions.

## Entry Points

| Entry Point | Location |
| --- | --- |
| Skills | [skills/INFO.md](skills/INFO.md) |
| Knowledge | [knowledge/INFO.md](knowledge/INFO.md) |

## Public Interfaces

- `Create topic {topic}` creates a complete research topic, its topic INFO, and
  its research indexes. ([topic-create](skills/topic-create/SKILL.md))
- `Explain topic {topic}` explains the maintained state of one topic.
  ([topic-explain](skills/topic-explain/SKILL.md))
- `Show info {topic}` presents a topic's maintained INFO document unchanged.
  ([topic-show](skills/topic-show/SKILL.md))
- `Learn info about {topic}` adds supplied, attributed information, ideas, or
  references. ([info-learn](skills/info-learn/SKILL.md))
- `Learn this paper for {topic}` records one supplied paper and its provenance.
  ([paper-learn](skills/paper-learn/SKILL.md))
- `Search literature for {topic}` produces a bounded, traceable candidate set.
  ([literature-search](skills/literature-search/SKILL.md))
- `Analyze paper {paper} for {topic}` creates a structured analysis and
  reference record. ([paper-analyze](skills/paper-analyze/SKILL.md))
- `Create synthesis for {topic}` compares a defined topic corpus.
  ([synthesis-create](skills/synthesis-create/SKILL.md))
- `Brainstorm about {topic}` develops ideas, questions, hypotheses, arguments,
  and directions. ([topic-brainstorm](skills/topic-brainstorm/SKILL.md))
- `Propose {Type_Paper} Paper for {topic}` returns a type-specific paper
  blueprint. ([paper-propose](skills/paper-propose/SKILL.md))
