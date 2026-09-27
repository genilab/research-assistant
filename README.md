# Knowledge Worker

Knowledge Worker is a topic-based knowledge base for capturing and maintaining
information that matters across different roles, positions, and contexts. Each
topic has one concise information record and a dedicated home for its supporting
references, making the knowledge easy to find, verify, and extend.

## Solution architecture

```text
Source material ──► knowledge/{topic}/references/
                            │
                            ▼
                  knowledge/{topic}/{topic}_info.md
                            │
                            ▼
                    README.md master index ──► Readers and contributors

AGENTS.md + guidelines/ + skills/ ──► govern every creation and update
```

The worker separates evidence, synthesized knowledge, discovery, and operating
rules. References provide the basis for a claim; the topic information record
turns that material into concise, current knowledge; and the README makes each
topic discoverable without requiring a reader to explore the repository first.
The operating files apply consistent structure and quality standards whenever a
topic is created or changed.

## Repository structure

| Location | What goes there | Why it exists |
| --- | --- | --- |
| `README.md` | This external overview and the master topics index. | Gives readers a reliable entry point to every available topic. |
| `AGENTS.md` | The Knowledge Worker operating instructions. | Defines how knowledge records are created, updated, and indexed. |
| `knowledge/` | One `knowledge/{topic}/` folder per topic. | Keeps knowledge organized by subject rather than by contributor or source type. |
| `knowledge/{topic}/{topic}_info.md` | The current, synthesized information for one topic. | Provides the concise record that readers use first. |
| `knowledge/{topic}/references/` | Supporting source files, links, excerpts, or notes when they must be retained. | Preserves evidence separately from the readable synthesis. |
| `guidelines/` | Shared standards, including `knowledge-entries.md`. | Keeps records consistent, safe to share, and maintainable. |
| `skills/` | Reusable instructions for operating the worker. | Makes the README and topic-management practices repeatable. |
| `LICENSE` | The repository license. | States the terms for using and distributing this work. |

## Knowledge topics

| Topic | Description | Information record |
| --- | --- | --- |
| _No topics recorded yet_ | Add the first topic under `knowledge/{topic}/`. | — |

## How to contribute

Create a lowercase, hyphenated topic directory under `knowledge/`. Add its
`{topic}_info.md` record and, when needed, a `references/` directory for source
material. Then replace the placeholder above with a row linking to the topic's
information record.

Read [AGENTS.md](AGENTS.md), [the knowledge-entry guideline](guidelines/knowledge-entries.md),
and the relevant skill before editing. The README is the external master index;
keep it accurate, concise, and useful to a reader who has not seen the working
files.
