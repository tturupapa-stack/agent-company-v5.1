---
name: feature-extension
description: |
  기존 프로젝트에 새 기능을 추가하는 워크플로우 스킬.
  코드 분석 → 영향 범위 파악 → 기능 명세 → 개발 → 테스트 순서로 진행한다.
  
  신규 개발(prd-workflow + supervisor-report)과 달리,
  기존 코드와의 호환성과 일관성을 우선시한다.
---

# Feature Extension Skill

기존 프로젝트에 새로운 기능을 추가하는 워크플로우입니다.

---

## 핵심 원칙

> **"기존 코드를 먼저 이해하라. 새 코드를 덮어쓰지 마라."**

기존 패턴, 컨벤션, 아키텍처를 유지하면서 기능을 추가합니다.

> **"영향 범위를 파악한 후 개발하라."**

새 기능이 기존 코드에 미치는 영향을 먼저 분석합니다.

> **"작은 단위로 추가하고 자주 검증하라."**

한 번에 큰 기능보다 작은 단위로 나눠 추가하고 테스트합니다.

---

## 사용 시점

| 상황 | 적합 |
|------|------|
| "로그인 기능 추가해줘" | ✅ |
| "검색 기능 넣어줘" | ✅ |
| "API 하나 더 만들어줘" | ✅ |
| "처음부터 새로 만들어줘" | ❌ (prd-workflow 사용) |
| "전체 구조 바꿔줘" | ❌ (refactoring-workflow 사용) |

---

## 워크플로우 개요

```
Phase 1: 코드베이스 분석
    ↓
Phase 2: 기능 요구사항 정의
    ↓
Phase 3: 영향 범위 분석
    ↓
Phase 4: 기술 명세 업데이트
    ↓
Phase 5: 개발
    ↓
Phase 6: 테스트 및 검증
    ↓
Phase 7: 문서화
```

---

## Phase 1: 코드베이스 분석

### 목적

기존 프로젝트의 구조, 패턴, 컨벤션을 파악하여 새 기능이 일관되게 추가되도록 함.

### 에이전트

`codebase-analyzer`

### 작업 내용

```markdown
## 분석 항목

1. 기술 스택 확인
   - Frontend: React/Vue/Svelte, 상태 관리, 스타일링
   - Backend: Framework, ORM, 인증 방식
   
2. 폴더 구조 파악
   - 컴포넌트 위치
   - API 라우트 위치
   - 서비스 레이어 위치
   
3. 기존 패턴 확인
   - API 호출 방식
   - 에러 처리 방식
   - 상태 관리 방식
   
4. .agent-context/ 존재 여부
   - 있으면: 최신 상태 확인
   - 없으면: 자동 생성
```

### 결과물

- `.agent-results/analyzer/YYYY-MM-DD-codebase-analysis.md`
- `.agent-context/` (없으면 생성, 있으면 업데이트 제안)

### 완료 조건

```markdown
✅ 기술 스택 파악 완료
✅ 폴더 구조 파악 완료
✅ 주요 패턴 3개 이상 식별
✅ .agent-context/ 확인/생성 완료
```

---

## Phase 2: 기능 요구사항 정의

### 목적

추가할 기능을 명확하게 정의합니다.

### 에이전트

`prd-architect` (간소화 버전)

### 작업 내용

```markdown
## 기능 명세서 작성

### 기능 개요
- 기능명: {기능명}
- 목적: {왜 필요한지}
- 사용자: {누가 사용하는지}

### User Stories (최소 1개)
- As a {사용자}, I want {기능}, so that {가치}

### Functional Requirements
- FR-NEW-001: {기능 설명}
  - 입력: {입력}
  - 출력: {출력}
  - 규칙: {비즈니스 규칙}

### 필요한 API (해당 시)
- API-NEW-001: {메서드} {경로}
  - Request: {형식}
  - Response: {형식}

### 필요한 UI (해당 시)
- 화면/컴포넌트 목록
- 기존 화면과의 연결점
```

### 결과물

- `.agent-results/extension/YYYY-MM-DD-{feature-name}-spec.md`

### 완료 조건

```markdown
✅ 기능 목적 명확
✅ User Story 작성
✅ FR 정의 (입력/출력 포함)
✅ 필요한 API 정의 (해당 시)
```

---

## Phase 3: 영향 범위 분석

### 목적

새 기능이 기존 코드에 미치는 영향을 파악합니다.

### 에이전트

`codebase-analyzer`

### 작업 내용

```markdown
## 영향 분석

### 수정이 필요한 기존 파일

| 파일 | 수정 내용 | 위험도 |
|------|-----------|--------|
| app/layout.tsx | 네비게이션에 링크 추가 | 낮음 |
| services/api.ts | 새 API 함수 추가 | 낮음 |
| types/index.ts | 새 타입 추가 | 낮음 |

### 새로 생성할 파일

| 파일 | 내용 |
|------|------|
| components/features/NewFeature.tsx | 새 컴포넌트 |
| app/new-feature/page.tsx | 새 페이지 |
| backend/api/new_feature.py | 새 API |

### 의존성 추가 (해당 시)

| 패키지 | 용도 | 필수 |
|--------|------|------|
| date-fns | 날짜 처리 | ✅ |

### 환경 변수 추가 (해당 시)

| 변수 | 용도 |
|------|------|
| NEW_API_KEY | 외부 API 키 |
```

### 결과물

- `.agent-results/extension/YYYY-MM-DD-{feature-name}-impact.md`

### 완료 조건

```markdown
✅ 수정 파일 목록 작성
✅ 생성 파일 목록 작성
✅ 의존성 변경 사항 파악
✅ 위험도 평가 완료
```

---

## Phase 4: 기술 명세 업데이트

### 목적

`.agent-context/` 파일들을 업데이트하여 개발 에이전트가 참조할 수 있게 합니다.

### 에이전트

`tech-spec-converter`

### 작업 내용

```markdown
## 업데이트 대상

### contracts.md
- 새 API 추가
- 기존 API 수정 (해당 시)

### shared-types.md
- 새 타입 추가
- 기존 타입 확장 (해당 시)

### conventions.md
- 변경 없음 (기존 컨벤션 유지)

### current-state.md
- 새 FR 추가 (상태: 대기)
```

### 결과물

- `.agent-context/contracts.md` (업데이트)
- `.agent-context/shared-types.md` (업데이트)
- `.agent-context/current-state.md` (업데이트)

### 완료 조건

```markdown
✅ contracts.md에 새 API 추가
✅ shared-types.md에 새 타입 추가
✅ current-state.md에 새 FR 추가
```

---

## Phase 5: 개발

### 목적

기능을 구현합니다.

### 에이전트

`backend-developer`, `frontend-developer`

### 작업 순서

```markdown
## 개발 순서

### Step 1: Backend (API 먼저)
1. API 엔드포인트 구현
2. 단위 테스트
3. API 동작 확인

### Step 2: Frontend
1. 타입 정의 (shared-types.md 참조)
2. API 서비스 함수 추가
3. 컴포넌트 구현
4. 페이지/라우트 연결
5. 단위 테스트

### Step 3: 통합
1. Frontend-Backend 연동 확인
2. 기존 기능과의 호환성 확인
```

### 중요 규칙

```markdown
## 개발 시 주의사항

1. **기존 패턴 따르기**
   - codebase-analyzer가 발견한 패턴 사용
   - 새로운 패턴 도입 금지 (승인 없이)

2. **contracts.md 준수**
   - API 형식 정확히 구현
   - 에러 응답 형식 기존과 동일하게

3. **타입 일관성**
   - shared-types.md의 타입 사용
   - 새 타입은 shared-types.md에 추가 후 사용

4. **테스트 작성**
   - 새 기능에 대한 테스트 필수
   - 기존 테스트 깨지지 않게
```

### 결과물

- 구현된 코드 파일들
- `.agent-results/backend/YYYY-MM-DD-{feature-name}.md`
- `.agent-results/frontend/YYYY-MM-DD-{feature-name}.md`

### 완료 조건

```markdown
✅ Backend API 구현 완료
✅ Frontend 컴포넌트 구현 완료
✅ 단위 테스트 작성 완료
✅ 빌드 성공
```

---

## Phase 6: 테스트 및 검증

### 목적

새 기능과 기존 기능 모두 정상 동작하는지 확인합니다.

### 에이전트

`test-runner`, `code-reviewer`

### 작업 내용

```markdown
## 테스트 범위

### 새 기능 테스트
1. 빌드 검증
2. 새 API 테스트
3. 새 컴포넌트 테스트
4. 통합 테스트

### 기존 기능 영향 테스트
1. 전체 테스트 실행
2. 수정된 파일 관련 테스트 집중
3. 회귀 테스트

### 코드 리뷰
1. contracts.md 준수 여부
2. 기존 패턴 준수 여부
3. 코드 품질 검토
```

### 결과물

- `.agent-results/tester/YYYY-MM-DD-{feature-name}.md`
- `.agent-results/reviewer/YYYY-MM-DD-{feature-name}.md`

### 완료 조건

```markdown
✅ 빌드 성공
✅ 새 기능 테스트 통과
✅ 기존 테스트 모두 통과 (회귀 없음)
✅ 코드 리뷰 통과
```

---

## Phase 7: 문서화

### 목적

추가된 기능을 문서화합니다.

### 에이전트

`doc-writer`

### 작업 내용

```markdown
## 문서화 대상

1. 기능 사용법 (사용자용)
2. API 문서 업데이트
3. current-state.md 상태 업데이트 (완료)
4. README 업데이트 (필요시)
```

### 결과물

- `.agent-results/docs/YYYY-MM-DD-{feature-name}.md`
- `.agent-context/current-state.md` (상태: 완료로 업데이트)

---

## 전체 흐름 요약

```
사용자: "검색 기능 추가해줘"
    ↓
Phase 1: codebase-analyzer
    → 기존 프로젝트 분석
    → .agent-context/ 확인/생성
    ↓
Phase 2: prd-architect (간소화)
    → 검색 기능 명세 작성
    ↓
Phase 3: codebase-analyzer
    → 영향 범위 분석
    → 수정/생성 파일 목록
    ↓
Phase 4: tech-spec-converter
    → .agent-context/ 업데이트
    → 새 API, 타입 추가
    ↓
Phase 5: backend-developer, frontend-developer
    → API 구현 → 컴포넌트 구현
    ↓
Phase 6: test-runner, code-reviewer
    → 테스트 실행 → 코드 리뷰
    ↓
Phase 7: doc-writer
    → 문서화 → 상태 업데이트
    ↓
완료: "검색 기능 추가 완료!"
```

---

## 에스컬레이션 정책

### Phase 1-3 (분석 단계)

| 조건 | 동작 |
|------|------|
| .agent-context/ 없음 | 자동 생성 후 계속 |
| 기술 스택 파악 실패 | 사용자에게 질문 |
| 영향 범위 너무 큼 | 사용자에게 보고, 범위 조정 제안 |

### Phase 4-5 (개발 단계)

| 조건 | 동작 |
|------|------|
| 기존 패턴과 충돌 | 사용자에게 보고, 선택지 제시 |
| 의존성 추가 필요 | 사용자 확인 후 추가 |
| 빌드 실패 2회 연속 | 에스컬레이션 |

### Phase 6 (검증 단계)

| 조건 | 동작 |
|------|------|
| 기존 테스트 실패 | 즉시 중단, 원인 분석 |
| 코드 리뷰 Critical 이슈 | 재작업 |

---

## 사용 예시

### 입력

```
"로그인 기능 추가해줘"
```

### 출력 (각 Phase 완료 후)

```markdown
## Phase 1 완료: 코드베이스 분석

현재 프로젝트 분석 결과:
- Frontend: Next.js 14 + Tailwind
- Backend: FastAPI
- 인증: 현재 없음
- 상태 관리: Zustand

## Phase 2 완료: 기능 명세

로그인 기능 명세:
- FR-NEW-001: 이메일/비밀번호 로그인
- FR-NEW-002: 로그아웃
- API-NEW-001: POST /api/auth/login
- API-NEW-002: POST /api/auth/logout

## Phase 3 완료: 영향 범위

수정 필요: 3개 파일
새로 생성: 8개 파일
의존성 추가: bcrypt, jose

계속 진행할까요?
```

---

## 폴더 구조

```
.agent-results/
├── analyzer/
│   └── YYYY-MM-DD-codebase-analysis.md
├── extension/
│   ├── YYYY-MM-DD-{feature}-spec.md
│   └── YYYY-MM-DD-{feature}-impact.md
├── backend/
│   └── YYYY-MM-DD-{feature}.md
├── frontend/
│   └── YYYY-MM-DD-{feature}.md
├── tester/
│   └── YYYY-MM-DD-{feature}.md
├── reviewer/
│   └── YYYY-MM-DD-{feature}.md
└── docs/
    └── YYYY-MM-DD-{feature}.md
```

---

## 버전 히스토리

| 버전 | 날짜 | 변경 내용 |
|------|------|-----------|
| v1.0 | 2025-01-30 | 초기 버전 |
