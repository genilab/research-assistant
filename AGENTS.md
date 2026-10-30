# Research-assistant

Research-assistant is an internal academic-research extension of
Knowledge-worker. It retains Knowledge-worker's graph-based topic knowledge
model and adds only topic-local paper, experiment, and publication indexes.

## Navigation

- Start at [INFO.md](INFO.md).
- Read an invoked skill completely before using or changing it.
- Use [skills/INFO.md](skills/INFO.md) for the local skill catalog.
- Use [knowledge/INFO.md](knowledge/INFO.md) for the topic-based research
  knowledge base.

## Multi-agent orchestration

The orchestrator interprets confirmed public actions, routes each to the
bounded owning skill, reviews its evidence, and completes, hands off, or asks
for a decision. Roles are capability nodes, not persistent external agents.

| Agent role | Responsibility | Skills | Handoffs |
| --- | --- | --- | --- |
| `structure-agent` | Maintain the approved project and agent-control structure. | `project-structure-manage`, `agents-file-manage` | Returns structural evidence. |
| `skill-agent` | Create, document, and validate reusable capabilities. | `skill-create`, `skill-validate`, `code-document` | Routes catalog changes to `information-agent`. |
| `information-agent` | Maintain and present project and topic navigation. | `info-maintain`, `info-show`, `topic-show` | Routes topic work to `knowledge-agent`. |
| `knowledge-agent` | Create, explain, learn, and brainstorm within durable topics. | `topic-create`, `topic-explain`, `topic-brainstorm`, `info-learn`, `knowledge-base-maintain` | Routes paper work to `literature-agent`. |
| `literature-agent` | Search, learn, analyze, classify, and synthesize scholarly work. | `literature-search`, `paper-learn`, `paper-analyze`, `paper-classify`, `synthesis-create`, `analyze-literature` | Routes arguments, writing, or experiments to their owning agent. |
| `research-agent` | Conduct focused research and learn confirmed research behaviors. | `research-topic`, `behavior-refine` | Returns source-aware synthesis and reusable practice proposals. |
| `argument-agent` | Develop research questions, claims, and alternatives. | `argument-develop`, `debate-topic` | Routes paper or experiment needs. |
| `writing-agent` | Propose and develop scholarly papers and writing standards. | `paper-propose`, `structure-paper`, `maintain-paper-section`, `results-paper`, `write-vision-paper`, `write-literature-review`, `write-positioning-paper`, `writing-refine` | Returns indexed publication drafts. |
| `experiment-agent` | Plan experiments, analyze findings, and report empirical work. | `experiment-plan`, `result-catalog`, `finding-analyze`, `report-experiment` | Returns linked experiment records. |
| `publication-agent` | Maintain explicitly requested external documentation and GitHub operations. | `readme-maintain`, `github-maintain` | Escalates external writes and releases. |

The path is **public action → orchestrator → agent role → skill workflow →
evidence → orchestrator**. Unclear requirements, conflicts, and approval gates
return to the researcher.

## Permanent structure

- `skills/` contains complete local skill packages in the approved format.
- `assets/` retains durable project-produced images and reports using the
  Knowledge-worker layout.
- `knowledge/` contains durable, topic-based research only. Each topic retains
  Knowledge-worker's `references/`, `{topic}_info.md`, `{topic}_ideas.md`, and
  `{topic}_refs.md`, plus `INFO.md` and paper, experiment, and publication
  indexes required by this research extension.
- `temp/` contains recoverable reconciliation and migration material only.
- Shared research standards live in the `docs/` folder of their owning skill,
  not in a separate root framework or guidelines tree.
- Every local skill uses a lowercase `{target}-{action}` package name, matching
  `name` front matter, supported `metadata`, and exactly one declared primary
  role.
- `INFO.md` and `skills/INFO.md` follow the Knowledge-worker-approved formats.
  This internal project does not maintain a root README unless explicitly asked.

## Research actions

- `Create topic {topic}` creates the complete research-topic schema and initial
  exploration record.
- `Explain topic {topic}` explains the topic from its maintained `INFO.md`.
- `Show info {topic}` presents the maintained topic `INFO.md` without changes.
- `Learn info about {topic}` adds attributed information, ideas, or references.
- `Learn this paper for {topic}` retains one supplied paper's provenance and
  prepares its topic-local paper record.
- `Search literature for {topic}` records a bounded, traceable academic search.
- `Analyze paper {paper} for {topic}` creates a structured analysis and complete
  reference record.
- `Create synthesis for {topic}` compares a defined paper corpus and identifies
  patterns, gaps, and opportunities.
- `Brainstorm about {topic}` develops topic ideas, questions, hypotheses,
  arguments, and directions.
- `Propose {Type_Paper} Paper for {topic}` defines the sections, evidence, and
  open dependencies for a Vision, Survey, Experimentation, Results, or
  Positioning paper.

## Boundaries

- Preserve original sources and distinguish attributed information from ideas,
  analysis, argument, and open question.
- Archive a supplied paper only after explicit researcher approval. An analysis
  does not imply a peer-review recommendation.
- Review `knowledge-worker-upstream` before deliberately synchronizing it;
  automatic synchronization and upstream pushes are disabled.
- Do not create a release, connect a dedicated remote, or alter external
  documentation unless explicitly requested.
