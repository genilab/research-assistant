# Research-assistant Knowledge Info

This is the entry point for durable, topic-based research knowledge. No topics
have been created yet.

## Knowledge topics

When topics exist, list each as:

```md
- [Topic display name](topic-slug/)
```

Each topic retains the Knowledge-worker schema:

- `references/` for preserved source material;
- `{topic-slug}_info.md` for attributed learning and a concise current summary;
- `{topic-slug}_ideas.md` for discussion, questions, hypotheses, arguments,
  directions, and open decisions; and
- `{topic-slug}_refs.md` for source and relevance records.

The research extension adds only:

- `INFO.md` as a compact linked index of the maintained topic state;
- `papers/INFO.md` for topic-local paper records, analyses, references, and
  classifications;
- `experiments/INFO.md` for plans, results, analyses, and reports; and
- `publications/INFO.md` for topic analyses, briefs, reports, and papers.

Use [the topic INFO template](../skills/topic-create/docs/topic-info-template.md)
when creating a topic. Only `topic-create` or a verified reconciliation through
`knowledge-base-maintain` updates this main index.
