# Research Bot Manual

**Version:** v1.0.1  
**Created by:** Beopsoo Kim, Department of Electrical and Computer Engineering, Inha University  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

## 1. What this suite does

Research Bot supports ECE research-development workflows. It is structured to challenge methodology, isolate data problems, test claims, review artifacts and code, support literature scouting, identify ethics risks, and plan research progress.

## 2. First-use workflow

1. Start with the master router.
2. Provide task context, available materials, constraints, and language preference.
3. Let the router select a specialized skill.
4. Use the specialized skill for detailed work.
5. Keep responsibility for final decisions, submissions, and ethical compliance.

## 3. Master prompt

```text
$research-bot
Research topic: [topic]
Current stage: [idea / method / data / code / result / draft / ethics / planning]
Main blocker: [blocker]
Current material: [none / notes / data / code / draft]
Please route me to the right Research Bot skill.
```

## 4. Skill selection guide

| Skill | Primary role |
|---|---|
| `research-bot` | Master router for the Research Bot suite. |
| `research-triage-router` | Routes ambiguous research-development requests. |
| `research-methodology-advisor` | Method choice, assumptions, model fidelity, validation strategy, computational trade-offs, and physical feasibility. |
| `research-data-troubleshooter` | Data collection, sensor and field data, simulation outputs, anomalies, convergence, and preprocessing. |
| `critical-thinking-defense-coach` | Socratic probing of assumptions, alternative explanations, and conclusions. |
| `research-artifact-reviewer` | Review of papers, thesis chapters, reports, academic emails, and proposal drafts. |
| `research-code-simulation-reviewer` | Review of MATLAB, Python, Julia, simulation scripts, solver settings, units, and reproducibility. |
| `literature-search-citation-scout` | Literature search planning, source authority, citation relevance, and SOTA positioning. |
| `research-ethics-integrity-advisor` | Cherry-picking, outlier removal, fabrication, authorship, plagiarism, conflicts of interest, and sponsor pressure. |
| `research-progress-roadmap-planner` | Milestone plans, advisor-meeting agendas, weekly tasks, submission timelines, and risk registers. |

## 5. Safe-use rules

- Do not use it to justify cherry-picking, hiding anomalies, or fabricating results.
- Do not treat it as a replacement for advisor, committee, institutional, or venue review.
- Do use it to expose assumptions, design validation, document limitations, and plan next experiments.

## 6. Prompt-quality rule

Good prompts include the task goal, audience, current material, constraints, and expected output. Bad prompts ask for complete work without context, hide missing evidence, or request unethical shortcuts.

## 7. Maintenance note

This repository keeps only the suite files that are useful for actual Codex skill operation and smoke testing. Broken ZIP-generated source-module exports were removed during cleanup because they were not load-bearing and were not safely recoverable from the packaged archive.
