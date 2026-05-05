# Changelog

## v1.0.2 - 2026-05-05

### English

- Sharpened the low-RAG behavior of the core specialist skills.
- Added manuscript-first search discipline, verification-status logic, and optional-expansion control to `literature-search-citation-scout`.
- Added first-impact anchor logic to `research-artifact-reviewer`.
- Updated README and metadata to present English and Korean together more explicitly.
- Corrected the Korean author name in public documentation and package metadata.

### 한국어

- 핵심 specialist skill의 low-RAG 동작을 더 날카롭게 다듬었습니다.
- `literature-search-citation-scout`에 manuscript-first search discipline, verification-status 로직, optional-expansion control을 추가했습니다.
- `research-artifact-reviewer`에 first-impact anchor 로직을 추가했습니다.
- README와 metadata를 정비하여 영문/국문 병기 형태를 더 분명하게 반영했습니다.
- 공개 문서와 package metadata에 표기된 한국어 작성자명을 `김법수`로 바로잡았습니다.

## v1.0.1 - 2026-05-05

### English

- Removed invalid extra fields from `SKILL.md` frontmatter.
- Cleaned mojibake from operational skill files and suite documentation.
- Removed broken `source-modules/` exports that were corrupted during ZIP packaging on Windows.

### 한국어

- `SKILL.md` frontmatter의 불필요한 추가 필드를 제거했습니다.
- operational skill 파일과 suite 문서의 mojibake를 정리했습니다.
- Windows ZIP 해제 과정에서 손상된 `source-modules/` 산출물을 제거했습니다.

## v1.0.0 - 2026-05-05

### English

- First public release of **Research Bot**.
- Set the official suite version to **1.0.0**.
- Preserved the canonical master invocation: `$research-bot`.
- Embedded core operating logic directly in each `SKILL.md` to minimize runtime dependence on external reference files.

### 한국어

- **Research Bot**의 첫 공개 릴리스입니다.
- 공식 suite 버전을 **1.0.0**으로 설정했습니다.
- canonical master invocation인 `$research-bot`을 유지했습니다.
- 외부 참조 파일 의존도를 줄이기 위해 핵심 operating logic을 각 `SKILL.md`에 직접 내장했습니다.
