# Research Bot

**Version:** v1.0.1  
**Created by:** Beopsoo Kim, Department of Electrical and Computer Engineering, Inha University  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

> **Important notice:** This project is intended for non-commercial research, education, and laboratory training. It is not offered for commercial products, paid services, proprietary internal tooling, or monetized redistribution without separate written permission.

## Overview

Research Bot is a Codex skill suite for ECE research-development workflows: methodology review, data troubleshooting, critical-thinking defense, artifact review, code/simulation review, literature search, ethics, and roadmap planning.

Research Bot does not replace advisor review, institutional policy, research-integrity review, or venue submission rules.

## Repository structure

- `.agents/skills/research-bot`: umbrella router for the suite
- `.agents/skills/research-triage-router`: lightweight routing-only helper
- `.agents/skills/*`: specialized research workflows
- `README.md`, `Manual.md`, `EVALS.md`: suite-level docs and smoke tests

## Installation

### Install into Codex global skills

Copy the skill directories under `.agents/skills/` into `~/.codex/skills/`.

```bash
mkdir -p "$HOME/.codex/skills"
cp -R .agents/skills/* "$HOME/.codex/skills/"
```

### Install into a repo-local agents layout

```bash
mkdir -p .agents/skills
cp -R Research-Bot/.agents/skills/* .agents/skills/
```

## Master invocation

```text
$research-bot
```

## Included skills

- `research-bot`: master router for the Research Bot suite
- `research-triage-router`: routing-only helper for ambiguous research requests
- `research-methodology-advisor`: method choice, assumptions, fidelity, constraints, and validation planning
- `research-data-troubleshooter`: data, logs, anomalies, preprocessing, and convergence diagnosis
- `critical-thinking-defense-coach`: assumption stress-testing and alternative-explanation probing
- `research-artifact-reviewer`: review of papers, chapters, reports, proposals, and research emails
- `research-code-simulation-reviewer`: review of MATLAB, Python, Julia, solver settings, units, and reproducibility
- `literature-search-citation-scout`: literature search, source authority, and citation validation
- `research-ethics-integrity-advisor`: authorship, cherry-picking, data anomalies, plagiarism, and disclosure ethics
- `research-progress-roadmap-planner`: milestones, meeting agendas, weekly plans, and risk tracking

## Recommended usage

Start with the master router unless you already know the exact workflow. Provide the task, audience, current material, constraints, and language context.

## Notes on v1.0.1 cleanup

- Removed invalid extra fields from `SKILL.md` frontmatter.
- Cleaned mojibake from operational skill files and suite documentation.
- Removed broken `source-modules/` exports that were not used by the installed skills and were corrupted during ZIP packaging on Windows.
