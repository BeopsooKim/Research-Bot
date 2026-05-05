# Research Bot Manual

**Version:** v1.0.0  
**Created by:** Beopsoo Kim, Department of Electrical and Computer Engineering, Inha University  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

> **Important notice:** This project is intended for non-commercial research, education, and laboratory training. It is not offered for commercial products, paid services, proprietary internal tooling, or monetized redistribution without separate written permission.

## 1. What this suite does

Research Bot supports ECE research-development workflows. It is structured to challenge methodology, isolate data problems, test claims, review artifacts and code, support literature scouting, identify ethics risks, and plan research progress.

## 2. First-use workflow

1. Start with the master router.
2. Provide task context, available materials, constraints, and language preference.
3. Let the router select a specialized Skill.
4. Use the specialized Skill for detailed work.
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
| `research-bot` | Master router for the Research Bot suite. It classifies ECE research tasks and routes to methodology, data, code, literature, ethics, artifact review, or roadmap workflows. |
| `research-triage-router` | Classifies ambiguous research-development requests and recommends the correct Research Bot skill and next prompt. |
| `research-methodology-advisor` | Challenges methodology choices, assumptions, model fidelity, validation strategy, computational trade-offs, and physical feasibility. |
| `research-data-troubleshooter` | Diagnoses data collection, sensor/field data, simulation outputs, hardware logs, anomalies, missing values, convergence, and preprocessing failures. |
| `critical-thinking-defense-coach` | Uses Socratic probing to test data, concepts, assumptions, point of view, alternative explanations, and conclusions. |
| `research-artifact-reviewer` | Reviews research artifacts such as papers, thesis chapters, reports, academic emails, and proposal drafts for rigor, logic, and purpose alignment. |
| `research-code-simulation-reviewer` | Reviews MATLAB, Python, Julia, simulation scripts, solver settings, units, reproducibility, physical assumptions, and result-generation pipelines. |
| `literature-search-citation-scout` | Plans and verifies literature searches, source authority, citation relevance, SOTA positioning, and evidence integration. |
| `research-ethics-integrity-advisor` | Handles research-integrity issues such as cherry-picking, outlier removal, fabrication, falsification, authorship, plagiarism, conflicts of interest, and sponsor pressure. |
| `research-progress-roadmap-planner` | Turns research goals into milestone plans, advisor-meeting agendas, weekly tasks, submission timelines, and risk registers. |

## 5. Safe use rules

- Do not use it to justify cherry-picking, hiding anomalies, or fabricating results.
- Do not treat it as a replacement for advisor, committee, institutional, or venue review.
- Do use it to expose assumptions, design validation, document limitations, and plan next experiments.

## 6. Prompt quality rule

Good prompts include the task goal, audience, current material, constraints, and what kind of output is expected. Bad prompts ask for complete work without context, hide missing evidence, or request unethical shortcuts.

## 7. Lab maintenance

Collect useful prompts, failure cases, and recurring lab workflows. Add them to `EVALS.md` or a lab examples file. Keep each Skill focused on one workflow.

---

# Research Bot 사용 설명서

**버전:** v1.0.0  
**작성자:** 김법수, 인하대학교 전기컴퓨터공학과  
**라이선스:** 크리에이티브 커먼즈 저작자표시-비영리-동일조건변경허락 4.0 국제 라이선스(CC BY-NC-SA 4.0)

> **중요 고지:** 이 프로젝트는 비상업적 연구, 교육, 연구실 훈련을 위한 자료입니다. 별도의 서면 허가 없이 상업 제품, 유료 서비스, 독점적 내부 도구, 수익화된 재배포에 사용할 수 없습니다.

## 1. 이 Suite가 하는 일

Research Bot은 ECE 연구개발 워크플로우를 지원합니다. 방법론을 공격적으로 점검하고, 데이터 문제를 격리하고, 주장을 검증하고, 산출물과 코드를 리뷰하고, 문헌 탐색을 지원하고, 연구윤리 위험을 식별하며, 연구 진척을 계획하도록 구성되어 있습니다.

## 2. 첫 사용 절차

1. 대표 라우터부터 시작합니다.
2. 작업 맥락, 사용 가능한 자료, 제약 조건, 언어 선호를 제공합니다.
3. 라우터가 전문 Skill을 선택하게 합니다.
4. 전문 Skill로 세부 작업을 진행합니다.
5. 최종 결정, 제출, 윤리 준수 책임은 사용자에게 있음을 유지합니다.

## 3. 대표 프롬프트

```text
$research-bot
Research topic: [topic]
Current stage: [idea / method / data / code / result / draft / ethics / planning]
Main blocker: [blocker]
Current material: [none / notes / data / code / draft]
Please route me to the right Research Bot skill.
```

## 4. Skill 선택 가이드

| Skill | 주요 역할 |
|---|---|
| `research-bot` | Research Bot 전체의 대표 라우터입니다. ECE 연구 과제를 분류하고 방법론, 데이터, 코드, 문헌, 윤리, 산출물 리뷰, 로드맵 워크플로우로 연결합니다. |
| `research-triage-router` | 모호한 연구개발 요청을 분류하고 적절한 Research Bot 하위 Skill 및 다음 프롬프트를 추천합니다. |
| `research-methodology-advisor` | 방법론 선택, 가정, 모델 충실도, 검증 전략, 계산 비용 trade-off, 물리적 실현 가능성을 강하게 점검합니다. |
| `research-data-troubleshooter` | 데이터 수집, 센서/현장 데이터, 시뮬레이션 출력, 하드웨어 로그, 이상치, 결측치, 수렴, 전처리 문제를 진단합니다. |
| `critical-thinking-defense-coach` | 소크라테스식 질문으로 데이터, 개념, 가정, 관점, 대안 해석, 결론을 검증합니다. |
| `research-artifact-reviewer` | 논문, 학위논문 챕터, 보고서, 학술 이메일, 제안서 초안의 엄밀성, 논리, 목적 정렬성을 리뷰합니다. |
| `research-code-simulation-reviewer` | MATLAB, Python, Julia, 시뮬레이션 스크립트, solver 설정, 단위, 재현성, 물리적 가정, 결과 생성 파이프라인을 리뷰합니다. |
| `literature-search-citation-scout` | 문헌 검색, 출처 권위, 인용 적합성, SOTA 위치 설정, 근거 통합 방식을 계획하고 검증합니다. |
| `research-ethics-integrity-advisor` | 데이터 취사선택, 이상치 제거, 위조, 변조, 저자권, 표절, 이해상충, 스폰서 압력 등 연구윤리 문제를 다룹니다. |
| `research-progress-roadmap-planner` | 연구 목표를 milestone 계획, 지도교수 미팅 agenda, 주간 작업, 제출 일정, risk register로 바꿉니다. |

## 5. 안전한 사용 규칙

- 데이터 취사선택, 이상치 은폐, 결과 조작을 정당화하는 데 사용하지 마십시오.
- 지도교수, 심사위원회, 기관, 학회·저널 검토를 대체하는 도구로 취급하지 마십시오.
- 가정 드러내기, 검증 설계, 한계 기록, 다음 실험 계획에 사용하십시오.

## 6. 좋은 프롬프트 원칙

좋은 프롬프트는 작업 목표, 독자, 현재 자료, 제약 조건, 기대 출력 형식을 포함합니다. 나쁜 프롬프트는 맥락 없이 완성본을 요구하거나, 근거 부족을 숨기거나, 비윤리적 우회로를 요청합니다.

## 7. 연구실 유지보수

유용한 프롬프트, 실패 사례, 반복되는 연구실 워크플로우를 모으십시오. 이를 `EVALS.md` 또는 연구실 예시 파일에 추가하십시오. 각 Skill은 하나의 워크플로우에 집중하도록 유지해야 합니다.

