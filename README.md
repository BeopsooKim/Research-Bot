# Research Bot

## English

**Version:** v1.0.2  
**Created by:** Beopsoo Kim (`김법수`), Department of Electrical and Computer Engineering, Inha University  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (`CC BY-NC-SA 4.0`)  
**License note:** The binding legal terms follow the official CC license text. Any Korean wording in this repository is explanatory, not a separate legal instrument.

### Important Notice

This project is intended for non-commercial research, education, and laboratory training. It is not offered for commercial products, paid services, proprietary internal tooling, or monetized redistribution without separate written permission.

### Overview

Research Bot is a Codex skill suite for ECE research-development workflows: methodology review, data troubleshooting, critical-thinking defense, artifact review, code or simulation review, literature search, ethics, and roadmap planning.

Research Bot does not replace advisor review, institutional policy, research-integrity review, or venue submission rules.

### Repository Structure

- `.agents/skills/research-bot`: umbrella router for the suite
- `.agents/skills/research-triage-router`: lightweight routing helper
- `.agents/skills/*`: specialized research workflows
- `README.md`, `Manual.md`, `EVALS.md`: suite-level documentation and smoke-test references

### Installation

#### Install into Codex global skills

Copy the skill directories under `.agents/skills/` into `~/.codex/skills/`.

```bash
mkdir -p "$HOME/.codex/skills"
cp -R .agents/skills/* "$HOME/.codex/skills/"
```

#### Install into a repo-local agents layout

```bash
mkdir -p .agents/skills
cp -R Research-Bot/.agents/skills/* .agents/skills/
```

### Master Invocation

```text
$research-bot
```

### Included Skills

- `research-bot`: master router for the Research Bot suite
- `research-triage-router`: routing helper for ambiguous research requests
- `research-methodology-advisor`: method choice, assumptions, fidelity, constraints, and validation planning
- `research-data-troubleshooter`: data, logs, anomalies, preprocessing, and convergence diagnosis
- `critical-thinking-defense-coach`: assumption stress-testing and alternative-explanation probing
- `research-artifact-reviewer`: review of papers, chapters, reports, proposals, and research emails
- `research-code-simulation-reviewer`: review of MATLAB, Python, Julia, solver settings, units, and reproducibility
- `literature-search-citation-scout`: literature search, source authority, and citation validation
- `research-ethics-integrity-advisor`: authorship, cherry-picking, data anomalies, plagiarism, and disclosure ethics
- `research-progress-roadmap-planner`: milestones, meeting agendas, weekly plans, submission timelines, and risk tracking

### Recommended Usage

Start with the master router unless you already know the exact workflow. Provide the task, audience, current material, constraints, and language context.

### What's New in v1.0.2

- Sharpened core specialist skills with stronger low-RAG operating logic embedded directly in `SKILL.md`.
- Added manuscript-first search discipline, verification-status tagging, and optional-expansion control to `literature-search-citation-scout`.
- Added stable first-impact anchor logic to `research-artifact-reviewer` so blocking flaws map directly to manuscript edit sites.
- Corrected the Korean author name in public documentation and package metadata.
- Rewrote public-facing documentation so English and Korean are separated instead of mixed inline.

### Release History

- `v1.0.2`: low-RAG sharpening, anchor-based review improvements, author-name correction, and bilingual public-doc cleanup
- `v1.0.1`: frontmatter cleanup, mojibake cleanup, and broken ZIP artifact removal
- `v1.0.0`: first public release

## 한국어

**버전:** v1.0.2  
**제작자:** Beopsoo Kim (`김법수`), 인하대학교 전기컴퓨터공학과  
**라이선스:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (`CC BY-NC-SA 4.0`)  
**라이선스 안내:** 법적 효력은 CC 공식 라이선스 원문에 따르며, 이 저장소의 한국어 문구는 설명용이며 별도의 법적 문서가 아닙니다.

### 중요 안내

이 프로젝트는 비상업적 연구, 교육, 연구실 훈련 목적에 한해 제공됩니다. 별도 서면 허가 없이 상용 제품, 유료 서비스, 사내 독점 도구, 수익화된 재배포에 사용할 수 없습니다.

### 개요

Research Bot은 ECE 연구개발 workflow를 위한 Codex skill suite로서, methodology review, data troubleshooting, critical-thinking defense, artifact review, code 또는 simulation review, literature search, ethics, roadmap planning을 다룹니다.

Research Bot은 지도교수 검토, 기관 정책, 연구윤리 검토, 학회 또는 저널 제출 규정을 대체하지 않습니다.

### 저장소 구조

- `.agents/skills/research-bot`: suite용 상위 router
- `.agents/skills/research-triage-router`: 경량 routing helper
- `.agents/skills/*`: 개별 전문 research workflow
- `README.md`, `Manual.md`, `EVALS.md`: suite 수준 문서와 스모크 테스트 참고 자료

### 설치

#### Codex 전역 skills에 설치

`.agents/skills/` 아래 skill 디렉터리를 `~/.codex/skills/`로 복사합니다.

```bash
mkdir -p "$HOME/.codex/skills"
cp -R .agents/skills/* "$HOME/.codex/skills/"
```

#### 저장소 로컬 `.agents` 레이아웃에 설치

```bash
mkdir -p .agents/skills
cp -R Research-Bot/.agents/skills/* .agents/skills/
```

### 마스터 호출

```text
$research-bot
```

### 포함된 Skills

- `research-bot`: Research Bot suite의 상위 master router
- `research-triage-router`: 애매한 연구 요청을 적절한 skill로 보내는 routing helper
- `research-methodology-advisor`: 방법 선택, 가정, 모델 충실도, 제약 조건, 검증 계획
- `research-data-troubleshooter`: 데이터, 로그, 이상치, 전처리, 수렴 문제 진단
- `critical-thinking-defense-coach`: 가정 스트레스 테스트와 대안 해석 탐색
- `research-artifact-reviewer`: 논문, 장, 보고서, 제안서, 연구 이메일 검토
- `research-code-simulation-reviewer`: MATLAB, Python, Julia, solver 설정, 단위, 재현성 검토
- `literature-search-citation-scout`: 문헌 탐색, source authority, citation validation
- `research-ethics-integrity-advisor`: 저자권, cherry-picking, 데이터 이상, 표절, disclosure ethics
- `research-progress-roadmap-planner`: 마일스톤, 미팅 아젠다, 주간 계획, 제출 일정, 리스크 추적

### 권장 사용 방식

정확한 workflow를 이미 알고 있지 않다면 master router부터 시작하는 것이 맞습니다. 작업 목표, 독자, 현재 자료, 제약 조건, 언어 맥락을 함께 제공하십시오.

### v1.0.2 업데이트 내역

- 핵심 specialist skill의 low-RAG 동작 규칙을 외부 참조 파일이 아니라 각 `SKILL.md` 내부에 직접 강화했습니다.
- `literature-search-citation-scout`에 manuscript-first search discipline, verification-status tagging, optional-expansion control을 추가했습니다.
- `research-artifact-reviewer`에 stable first-impact anchor 로직을 넣어 blocking flaw가 곧바로 manuscript edit site에 연결되도록 강화했습니다.
- 공개 문서와 package metadata에 표기된 한국어 작성자명을 `김법수`로 바로잡았습니다.
- 공개 문서를 인라인 혼합형이 아니라 영문/국문 분리 구조로 다시 정리했습니다.

### 릴리스 기록

- `v1.0.2`: low-RAG 고도화, anchor 기반 review 개선, 작성자명 정정, 공개 문서 이중언어 정리
- `v1.0.1`: frontmatter 정리, mojibake 정리, 손상된 ZIP 산출물 제거
- `v1.0.0`: 첫 공개 릴리스
