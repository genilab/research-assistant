# Skill Regeneration and QA Process

Use this process one skill at a time after a behavior or scope change.

1. Read the current `SKILL.md`, `docs/plan.md`, and `docs/requirements.md`.
2. Confirm the scope, action, primary agent role, dependencies, constraints,
   and each skill-specific requirement remain correct.
3. Revise the plan first when requirements change, then regenerate the skill
   instructions from that confirmed plan.
4. Run `validate_catalog.py --project <project> --regenerate-all`.
5. Run any package test suite and inspect the regenerated `docs/qa.md`.
6. Record a live operational example separately when the skill is used on a
   topic, paper, or experiment; do not present structural QA as that evidence.

## Active review order

| Order | Skill | Extended requirements |
| --- | --- | --- |
| 01 | `agents-file-manage` | `skills/agents-file-manage/docs/requirements.md` |
| 02 | `analyze-literature` | `skills/analyze-literature/docs/requirements.md` |
| 03 | `argument-develop` | `skills/argument-develop/docs/requirements.md` |
| 04 | `behavior-refine` | `skills/behavior-refine/docs/requirements.md` |
| 05 | `code-document` | `skills/code-document/docs/requirements.md` |
| 06 | `debate-topic` | `skills/debate-topic/docs/requirements.md` |
| 07 | `experiment-plan` | `skills/experiment-plan/docs/requirements.md` |
| 08 | `finding-analyze` | `skills/finding-analyze/docs/requirements.md` |
| 09 | `github-maintain` | `skills/github-maintain/docs/requirements.md` |
| 10 | `info-learn` | `skills/info-learn/docs/requirements.md` |
| 11 | `info-maintain` | `skills/info-maintain/docs/requirements.md` |
| 12 | `info-show` | `skills/info-show/docs/requirements.md` |
| 13 | `knowledge-base-maintain` | `skills/knowledge-base-maintain/docs/requirements.md` |
| 14 | `literature-search` | `skills/literature-search/docs/requirements.md` |
| 15 | `maintain-paper-section` | `skills/maintain-paper-section/docs/requirements.md` |
| 16 | `paper-analyze` | `skills/paper-analyze/docs/requirements.md` |
| 17 | `paper-classify` | `skills/paper-classify/docs/requirements.md` |
| 18 | `paper-learn` | `skills/paper-learn/docs/requirements.md` |
| 19 | `paper-propose` | `skills/paper-propose/docs/requirements.md` |
| 20 | `project-structure-manage` | `skills/project-structure-manage/docs/requirements.md` |
| 21 | `readme-maintain` | `skills/readme-maintain/docs/requirements.md` |
| 22 | `report-experiment` | `skills/report-experiment/docs/requirements.md` |
| 23 | `research-topic` | `skills/research-topic/docs/requirements.md` |
| 24 | `result-catalog` | `skills/result-catalog/docs/requirements.md` |
| 25 | `results-paper` | `skills/results-paper/docs/requirements.md` |
| 26 | `skill-create` | `skills/skill-create/docs/requirements.md` |
| 27 | `skill-validate` | `skills/skill-validate/docs/requirements.md` |
| 28 | `structure-paper` | `skills/structure-paper/docs/requirements.md` |
| 29 | `synthesis-create` | `skills/synthesis-create/docs/requirements.md` |
| 30 | `topic-brainstorm` | `skills/topic-brainstorm/docs/requirements.md` |
| 31 | `topic-create` | `skills/topic-create/docs/requirements.md` |
| 32 | `topic-explain` | `skills/topic-explain/docs/requirements.md` |
| 33 | `topic-show` | `skills/topic-show/docs/requirements.md` |
| 34 | `write-literature-review` | `skills/write-literature-review/docs/requirements.md` |
| 35 | `write-positioning-paper` | `skills/write-positioning-paper/docs/requirements.md` |
| 36 | `write-vision-paper` | `skills/write-vision-paper/docs/requirements.md` |
| 37 | `writing-refine` | `skills/writing-refine/docs/requirements.md` |
