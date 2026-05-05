# Research Bot EVALS

Official suite name: **Research Bot**  
Master invocation: `$research-bot`  
Created by: **Beopsoo Kim (김법수), Department of Electrical and Computer Engineering, Inha University / 김법수, 인하대학교 전기컴퓨터공학과**  
License: **CC BY-NC-SA 4.0**

## Required bilingual smoke tests

### Korean routing

```text
$research-bot
한국어로 설명해줘. 지금 어떤 Skill을 써야 할지 모르겠다.
```

Expected: responds in Korean, identifies the proper specialized skill, and provides a ready-to-copy next prompt.

### English routing

```text
$research-bot
Please help me choose the correct Research Bot workflow for this task.
```

Expected: responds in English, identifies the proper specialized skill, and provides a ready-to-copy next prompt.

### Mixed-language artifact

```text
$research-bot
설명은 한국어로 하고, 수정 예시는 영어로 줘.
```

Expected: Korean diagnosis with English artifact suggestions.

---

# Evals for Codex R&D Skills

Use these prompts after installation to check trigger behavior and output quality.

## Should trigger `research-triage-router`

1. I am stuck with my ECE research and do not know whether this is a methodology, data, or writing problem.
2. Which workflow should I use for an unexpected simulation result?
3. I have a thesis milestone, a paper draft, and a data issue. Help me decide the order.

## Should trigger `research-methodology-advisor`

1. I want to use MCMC for uncertainty-aware power scheduling. Is this methodology defensible?
2. My hybrid AC-DC microgrid simulation uses steady-state power flow only. Is that enough for a fault-analysis claim?
3. I plan to implement Kalman filtering in PLC logic. What methodology risks should I defend?

## Should trigger `research-data-troubleshooter`

1. My SCADA logs have missing values and voltage spikes.
2. My MCMC chain seems converged, but autocorrelation is high.
3. PLC logging rate and scan time do not match. Could causality be distorted?

## Should trigger `critical-thinking-defense-coach`

1. Attack the assumptions behind my claim that this converter control improves stability.
2. Paper A used this method, so I think it is valid for my system.
3. My result contradicts theory. Help me reason through alternative explanations.

## Should trigger `research-artifact-reviewer`

1. Review this IEEE introduction for contribution clarity.
2. Does this thesis chapter connect to the dissertation storyline?
3. Review this email to an external professor for professionalism and clarity.

## Should trigger `research-code-simulation-reviewer`

1. Review this MATLAB power-flow script for units and reproducibility.
2. Inspect my Python OPF code for solver assumptions and validation checks.
3. Check this PLC ladder logic documentation for physical assumptions and safety interlocks.

## Should trigger `literature-search-citation-scout`

1. Find recent IEEE papers on VSC-based hybrid AC-DC fault analysis.
2. Validate whether this citation exists and whether it supports my claim.
3. What standards should I cite for this protection/control design?

## Should trigger `research-ethics-integrity-advisor`

1. Can I remove these outliers because they weaken my conclusion?
2. Should a colleague who only gave funding be a coauthor?
3. A sponsor wants us to avoid reporting a negative result. What should I do?

## Should trigger `research-progress-roadmap-planner`

1. Build a 12-week roadmap to submit a conference paper.
2. Align my current simulation project with my dissertation chapters.
3. Create an advisor meeting agenda for this week's research blockers.

## Should not trigger these skills

1. Build a React app.
2. Fix a Dockerfile for a web service.
3. Write a casual birthday message.
4. Generate marketing copy unrelated to research.

## Borderline checks

1. Write an academic email from scratch. Expected: `research-artifact-reviewer` may help if facts and purpose are supplied; it should not invent claims.
2. Rewrite a paper section. Expected: artifact reviewer gives localized revision support, not full ghostwriting.
3. Suggest a method from memory. Expected: methodology advisor may reason conceptually; if source-specific or recent claims are needed, literature scout/search is required.
