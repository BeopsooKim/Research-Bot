# Research Bot Manual

## English

**Version:** v1.0.2  
**Created by:** Beopsoo Kim (`김법수`), Department of Electrical and Computer Engineering, Inha University  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (`CC BY-NC-SA 4.0`)  
**License note:** The binding legal terms follow the official CC license text. Any Korean wording in this repository is explanatory.

### 1. What This Suite Does

Research Bot supports ECE research-development workflows. It is structured to challenge methodology, isolate data problems, test claims, review artifacts and code, support literature scouting, identify ethics risks, and plan research progress.

### 2. First-Use Workflow

1. Start with the master router.
2. Provide task context, available materials, constraints, and language preference.
3. Let the router select a specialized skill.
4. Use the specialized skill for detailed work.
5. Keep responsibility for final decisions, submissions, and ethical compliance.

### 3. Master Prompt

```text
$research-bot
Research topic: [topic]
Current stage: [idea / method / data / code / result / draft / ethics / planning]
Main blocker: [blocker]
Current material: [none / notes / data / code / draft]
Please route me to the right Research Bot skill.
```

### 4. Skill Selection Guide

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

### 5. Safe-Use Rules

- Do not use it to justify cherry-picking, hiding anomalies, or fabricating results.
- Do not treat it as a replacement for advisor, committee, institutional, or venue review.
- Do use it to expose assumptions, design validation, document limitations, and plan next experiments.

### 6. Prompt-Quality Rule

Good prompts include the task goal, audience, current material, constraints, and expected output. Bad prompts ask for complete work without context, hide missing evidence, or request unethical shortcuts.

### 7. v1.0.2 Operational Note

This release sharpens low-RAG behavior by pushing more decision logic into `SKILL.md` itself. The specialist skills now rely less on external references and more on explicit conditional rules.

### 8. Maintenance Note

This repository keeps only the suite files that are useful for actual Codex skill operation and smoke testing. Broken ZIP-generated source-module exports were removed during cleanup because they were not load-bearing and were not safely recoverable from the packaged archive.

## 한국어

**버전:** v1.0.2  
**제작자:** Beopsoo Kim (`김법수`), 인하대학교 전기컴퓨터공학과  
**라이선스:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (`CC BY-NC-SA 4.0`)  
**라이선스 안내:** 법적 효력은 CC 공식 라이선스 원문에 따르며, 이 저장소의 한국어 문구는 설명용입니다.

### 1. 이 Suite가 하는 일

Research Bot은 ECE 연구개발 workflow를 지원합니다. 방법론을 비판적으로 검토하고, 데이터 문제를 분리하고, 주장을 검증하고, 산출물과 코드를 검토하고, 문헌 탐색을 돕고, 윤리 리스크를 식별하고, 연구 진행 계획을 세우도록 설계되어 있습니다.

### 2. 첫 사용 순서

1. master router부터 시작합니다.
2. 작업 맥락, 현재 자료, 제약 조건, 언어 선호를 제공합니다.
3. router가 적절한 전문 skill을 고르게 합니다.
4. 세부 작업은 해당 전문 skill로 진행합니다.
5. 최종 결정, 제출, 윤리 준수 책임은 사용자에게 있습니다.

### 3. 마스터 프롬프트

```text
$research-bot
Research topic: [topic]
Current stage: [idea / method / data / code / result / draft / ethics / planning]
Main blocker: [blocker]
Current material: [none / notes / data / code / draft]
Please route me to the right Research Bot skill.
```

### 4. Skill 선택 가이드

| Skill | 주요 역할 |
|---|---|
| `research-bot` | Research Bot suite의 상위 master router |
| `research-triage-router` | 애매한 연구개발 요청의 routing |
| `research-methodology-advisor` | 방법 선택, 가정, 모델 충실도, 검증 전략, 계산 trade-off, 물리적 타당성 |
| `research-data-troubleshooter` | 데이터 수집, 센서 및 현장 데이터, simulation output, 이상치, 수렴, 전처리 |
| `critical-thinking-defense-coach` | 가정, 대안 해석, 결론을 소크라테스식으로 점검 |
| `research-artifact-reviewer` | 논문, 학위문 장, 보고서, 학술 이메일, 제안서 초안 검토 |
| `research-code-simulation-reviewer` | MATLAB, Python, Julia, simulation script, solver 설정, 단위, 재현성 검토 |
| `literature-search-citation-scout` | 문헌 탐색 계획, source authority, citation relevance, SOTA positioning |
| `research-ethics-integrity-advisor` | cherry-picking, outlier removal, fabrication, authorship, plagiarism, 이해상충, sponsor pressure |
| `research-progress-roadmap-planner` | 마일스톤 계획, 지도교수 미팅 아젠다, 주간 작업, 제출 일정, 리스크 레지스터 |

### 5. 안전 사용 규칙

- cherry-picking, 이상치 은폐, 결과 조작을 정당화하는 용도로 사용하지 마십시오.
- 지도교수, 위원회, 기관, 학회 또는 저널 심사를 대체하는 도구로 취급하지 마십시오.
- 가정을 드러내고, 검증을 설계하고, 한계를 문서화하고, 다음 실험을 계획하는 데 사용하십시오.

### 6. 프롬프트 품질 규칙

좋은 프롬프트는 작업 목표, 독자, 현재 자료, 제약 조건, 기대 산출물을 포함합니다. 나쁜 프롬프트는 맥락 없이 완성본만 요구하거나, 근거 부족을 숨기거나, 비윤리적 지름길을 요구합니다.

### 7. v1.0.2 운영 메모

이번 릴리스는 더 많은 판단 로직을 `SKILL.md` 자체에 밀어 넣어 low-RAG 동작을 강화했습니다. 핵심 specialist skill이 외부 참조 문서보다 명시적 조건부 규칙에 더 의존하도록 바뀌었습니다.

### 8. 유지보수 메모

이 저장소는 실제 Codex skill 동작과 스모크 테스트에 필요한 파일만 유지합니다. ZIP 패키징 과정에서 손상된 source-module 산출물은 핵심 동작에 필요하지 않았고 안전하게 복구할 수 없었기 때문에 정리 과정에서 제거했습니다.
