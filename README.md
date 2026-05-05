# Research Bot

**Version:** v1.0.0  
**Created by:** Beopsoo Kim, Department of Electrical and Computer Engineering, Inha University  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

> **Important notice:** This project is intended for non-commercial research, education, and laboratory training. It is not offered for commercial products, paid services, proprietary internal tooling, or monetized redistribution without separate written permission.

## Overview

Research Bot is a Codex Skill suite for ECE research-development workflows: methodology review, data troubleshooting, critical-thinking defense, artifact review, code/simulation review, literature search, ethics, and roadmap planning.

Research Bot does not replace advisor review, institutional policy, research-integrity review, or venue submission rules.

## Installation

If you are in a repository root that contains the `Research-Bot` directory, run:

```bash
mkdir -p .agents/skills
cp -R Research-Bot/.agents/skills/* .agents/skills/
```

If you are already inside the `Research-Bot` directory and want to install into the parent repository root, run:

```bash
mkdir -p ../.agents/skills
cp -R .agents/skills/* ../.agents/skills/
```

For personal global installation, run:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R .agents/skills/* "$HOME/.agents/skills/"
```

## Master invocation

```text
$research-bot
```

## Included Skills

- `research-bot`: Master router for the Research Bot suite. It classifies ECE research tasks and routes to methodology, data, code, literature, ethics, artifact review, or roadmap workflows.
- `research-triage-router`: Classifies ambiguous research-development requests and recommends the correct Research Bot skill and next prompt.
- `research-methodology-advisor`: Challenges methodology choices, assumptions, model fidelity, validation strategy, computational trade-offs, and physical feasibility.
- `research-data-troubleshooter`: Diagnoses data collection, sensor/field data, simulation outputs, hardware logs, anomalies, missing values, convergence, and preprocessing failures.
- `critical-thinking-defense-coach`: Uses Socratic probing to test data, concepts, assumptions, point of view, alternative explanations, and conclusions.
- `research-artifact-reviewer`: Reviews research artifacts such as papers, thesis chapters, reports, academic emails, and proposal drafts for rigor, logic, and purpose alignment.
- `research-code-simulation-reviewer`: Reviews MATLAB, Python, Julia, simulation scripts, solver settings, units, reproducibility, physical assumptions, and result-generation pipelines.
- `literature-search-citation-scout`: Plans and verifies literature searches, source authority, citation relevance, SOTA positioning, and evidence integration.
- `research-ethics-integrity-advisor`: Handles research-integrity issues such as cherry-picking, outlier removal, fabrication, falsification, authorship, plagiarism, conflicts of interest, and sponsor pressure.
- `research-progress-roadmap-planner`: Turns research goals into milestone plans, advisor-meeting agendas, weekly tasks, submission timelines, and risk registers.

## Recommended usage

Start with the master router unless you already know the exact workflow. Give the bot the task, audience, current material, constraints, and language context.

## GitHub publication

This repository is prepared for public GitHub release under the repository name `Research-Bot`. See `GITHUB_PUBLISH.md` for the recommended `gh` workflow.

---

# Research Bot

**버전:** v1.0.0  
**작성자:** 김법수, 인하대학교 전기컴퓨터공학과  
**라이선스:** 크리에이티브 커먼즈 저작자표시-비영리-동일조건변경허락 4.0 국제 라이선스(CC BY-NC-SA 4.0)

> **중요 고지:** 이 프로젝트는 비상업적 연구, 교육, 연구실 훈련을 위한 자료입니다. 별도의 서면 허가 없이 상업 제품, 유료 서비스, 독점적 내부 도구, 수익화된 재배포에 사용할 수 없습니다.

## 개요

Research Bot은 ECE 연구개발 워크플로우를 위한 Codex Skill Suite입니다. 방법론 리뷰, 데이터 문제 해결, 비판적 사고 방어, 산출물 리뷰, 코드/시뮬레이션 리뷰, 문헌 검색, 연구윤리, 로드맵 계획을 지원합니다.

Research Bot은 지도교수 검토, 기관 규정, 연구윤리 검토, 학회·저널 투고 규정을 대체하지 않습니다.

## 설치

`Research-Bot` 디렉터리를 포함하는 레포지토리 루트에 있다면 다음을 실행하십시오.

```bash
mkdir -p .agents/skills
cp -R Research-Bot/.agents/skills/* .agents/skills/
```

이미 `Research-Bot` 디렉터리 안에 있고 부모 디렉터리의 레포지토리 루트에 설치하려면 다음을 실행하십시오.

```bash
mkdir -p ../.agents/skills
cp -R .agents/skills/* ../.agents/skills/
```

개인 전역 환경에 설치하려면 다음을 실행하십시오.

```bash
mkdir -p "$HOME/.agents/skills"
cp -R .agents/skills/* "$HOME/.agents/skills/"
```

## 대표 호출명

```text
$research-bot
```

## 포함된 Skill

- `research-bot`: Research Bot 전체의 대표 라우터입니다. ECE 연구 과제를 분류하고 방법론, 데이터, 코드, 문헌, 윤리, 산출물 리뷰, 로드맵 워크플로우로 연결합니다.
- `research-triage-router`: 모호한 연구개발 요청을 분류하고 적절한 Research Bot 하위 Skill 및 다음 프롬프트를 추천합니다.
- `research-methodology-advisor`: 방법론 선택, 가정, 모델 충실도, 검증 전략, 계산 비용 trade-off, 물리적 실현 가능성을 강하게 점검합니다.
- `research-data-troubleshooter`: 데이터 수집, 센서/현장 데이터, 시뮬레이션 출력, 하드웨어 로그, 이상치, 결측치, 수렴, 전처리 문제를 진단합니다.
- `critical-thinking-defense-coach`: 소크라테스식 질문으로 데이터, 개념, 가정, 관점, 대안 해석, 결론을 검증합니다.
- `research-artifact-reviewer`: 논문, 학위논문 챕터, 보고서, 학술 이메일, 제안서 초안의 엄밀성, 논리, 목적 정렬성을 리뷰합니다.
- `research-code-simulation-reviewer`: MATLAB, Python, Julia, 시뮬레이션 스크립트, solver 설정, 단위, 재현성, 물리적 가정, 결과 생성 파이프라인을 리뷰합니다.
- `literature-search-citation-scout`: 문헌 검색, 출처 권위, 인용 적합성, SOTA 위치 설정, 근거 통합 방식을 계획하고 검증합니다.
- `research-ethics-integrity-advisor`: 데이터 취사선택, 이상치 제거, 위조, 변조, 저자권, 표절, 이해상충, 스폰서 압력 등 연구윤리 문제를 다룹니다.
- `research-progress-roadmap-planner`: 연구 목표를 milestone 계획, 지도교수 미팅 agenda, 주간 작업, 제출 일정, risk register로 바꿉니다.

## 권장 사용법

정확한 워크플로우를 이미 알고 있지 않다면 대표 라우터부터 시작하십시오. 작업, 독자, 현재 자료, 제약 조건, 언어 맥락을 함께 제공하는 것이 좋습니다.

## GitHub 공개

이 저장소는 `Research-Bot`이라는 repository 이름으로 public GitHub 공개가 가능하도록 준비되어 있습니다. 권장 `gh` 절차는 `GITHUB_PUBLISH.md`를 참고하십시오.

