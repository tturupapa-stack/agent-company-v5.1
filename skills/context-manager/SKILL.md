---
name: context-manager
description: |
  세션 간 컨텍스트 관리 스킬.
  세션 시작/종료 시 상태를 자동으로 저장하고 복원한다.
  CLAUDE.md, .agent-context/, .project/를 관리한다.
  
  다음 상황에서 사용:
  - 새 세션 시작 시 상태 복원
  - 세션 종료 시 상태 저장
  - 컨텍스트 윈도우 초과 시 요약
  - 프로젝트 상태 확인
---

# Context Manager Skill

세션 간 컨텍스트를 관리하고 상태를 유지하는 스킬입니다.

---

## 핵심 원칙

> **"모든 중요 정보는 파일에 저장하라. 메모리에 의존하지 마라."**

컨텍스트 윈도우는 휘발성. 파일은 영구적.

> **"세션 시작 시 상태 복원, 종료 시 상태 저장."**

일관된 루틴으로 정보 손실 방지.

> **"최소한의 파일로 최대한의 컨텍스트를."**

CLAUDE.md 하나로 전체 상황 파악 가능하게.

---

## 관리 파일 구조

```
프로젝트/
├── CLAUDE.md                    # 프로젝트 전체 컨텍스트 (자동 로드)
├── .agent-context/              # 기술 명세
│   ├── contracts.md
│   ├── shared-types.md
│   ├── conventions.md
│   └── current-state.md         # 현재 기능 상태
├── .project/                    # 프로젝트 관리
│   ├── dashboard.md             # 대시보드
│   ├── dev-plan.md              # 개발 계획
│   └── session-log.md           # 세션 기록
└── .prd-workspace/              # PRD (있는 경우)
    └── PRD-FINAL.md
```

---

## 명령어

| 명령어 | 동작 |
|--------|------|
| "컨텍스트 로드" / "상태 파악해줘" | 세션 시작 - 상태 복원 |
| "컨텍스트 저장" / "작업 마무리해줘" | 세션 종료 - 상태 저장 |
| "컨텍스트 요약" | 현재 상태 요약 출력 |
| "CLAUDE.md 업데이트" | CLAUDE.md 갱신 |

---

## 세션 시작: 컨텍스트 로드

### 트리거

```
"현재 프로젝트 상태 파악해줘"
"컨텍스트 로드해줘"
"어디까지 했지?"
"이어서 작업하자"
```

### 동작

```markdown
## 컨텍스트 로드 프로세스

### Step 1: CLAUDE.md 읽기
- 프로젝트 개요
- 기술 스택
- 현재 진행 상황

### Step 2: current-state.md 읽기
- 완료된 기능
- 진행 중인 기능
- 대기 중인 기능

### Step 3: session-log.md 읽기 (최근 3개)
- 마지막 세션 작업 내용
- 다음 작업 목록
- 알려진 이슈

### Step 4: 상태 요약 출력
```

### 출력 형식

```markdown
## 🔄 컨텍스트 로드 완료

### 프로젝트: StockAlert

**기술 스택**: Next.js 14 + FastAPI + PostgreSQL

### 현재 상태

| 기능 | 상태 | 비고 |
|------|------|------|
| FR-001 뉴스 목록 | ✅ 완료 | |
| FR-002 뉴스 상세 | ✅ 완료 | |
| FR-003 알림 설정 | 🔄 진행중 | Frontend 남음 |
| FR-004 푸시 알림 | ⏳ 대기 | |

### 마지막 세션 (2025-01-30 14:30)

**완료한 작업**:
- AlertSettings 컴포넌트 생성
- useAlertStore 훅 생성

**다음 작업**:
1. AlertSettings 페이지 연결
2. 통합 테스트

### 알려진 이슈
- AlertModal 다크모드 미적용 (Minor)

---

**이어서 작업할까요?** "FR-003 계속해줘" 또는 다른 작업 지시
```

---

## 세션 종료: 컨텍스트 저장

### 트리거

```
"오늘 작업 마무리해줘"
"컨텍스트 저장해줘"
"세션 종료"
"여기까지 하자"
```

### 동작

```markdown
## 컨텍스트 저장 프로세스

### Step 1: 현재 세션 작업 정리
- 이번 세션에서 완료한 작업
- 생성/수정한 파일 목록
- 발견된 이슈

### Step 2: current-state.md 업데이트
- 완료된 기능 상태 변경
- 진행 중인 기능 상태 업데이트

### Step 3: session-log.md 추가
- 새 세션 기록 추가
- 다음 작업 목록

### Step 4: CLAUDE.md 업데이트
- "현재 진행 상황" 섹션 갱신
- "최근 이슈" 섹션 갱신

### Step 5: 요약 출력
```

### 출력 형식

```markdown
## 💾 컨텍스트 저장 완료

### 이번 세션 요약

**시간**: 2025-01-30 14:30 - 16:45
**작업 시간**: 약 2시간 15분

### 완료한 작업

| # | 작업 | 결과 |
|---|------|------|
| 1 | AlertSettings 컴포넌트 | ✅ 완료 |
| 2 | useAlertStore 훅 | ✅ 완료 |
| 3 | 페이지 연결 | ✅ 완료 |
| 4 | 통합 테스트 | ✅ 통과 |

### 상태 변경

| 기능 | Before | After |
|------|--------|-------|
| FR-003 알림 설정 | 🔄 진행중 | ✅ 완료 |

### 업데이트된 파일

- `.agent-context/current-state.md` ✅
- `.project/session-log.md` ✅
- `CLAUDE.md` ✅

### 다음 세션 작업

1. FR-004 푸시 알림 개발 시작
2. AlertModal 다크모드 수정 (Minor)

---

**수고하셨습니다! 다음 세션에서 "컨텍스트 로드해줘"로 시작하세요.**
```

---

## 컨텍스트 요약

### 트리거

```
"현재 상태 알려줘"
"컨텍스트 요약해줘"
"지금 뭐하고 있었지?"
```

### 출력 형식

```markdown
## 📋 현재 컨텍스트 요약

**프로젝트**: StockAlert
**현재 작업**: FR-003 알림 설정 (Frontend)

### 진행률

```
전체: [████████░░] 80%
FR-001: ✅ 완료
FR-002: ✅ 완료
FR-003: 🔄 진행중 (90%)
FR-004: ⏳ 대기
```

### 현재 세션 작업

1. ✅ AlertSettings 컴포넌트
2. ✅ useAlertStore 훅
3. 🔄 페이지 연결 (진행중)

### 참조 중인 파일

- `.agent-context/contracts.md` (API-003)
- `.agent-results/backend/2025-01-30-alert-api.md`
```

---

## CLAUDE.md 템플릿

```markdown
# CLAUDE.md

> 이 파일은 Claude Code가 프로젝트를 이해하기 위한 컨텍스트입니다.
> 세션 시작 시 자동으로 읽힙니다.

## 프로젝트 개요

- **이름**: {프로젝트명}
- **설명**: {한 줄 설명}
- **상태**: {기획 중 / 개발 중 / 유지보수}

## 기술 스택

### Frontend
- Framework: {Next.js 14 / React / Vue}
- Styling: {Tailwind / styled-components}
- State: {Zustand / Redux}

### Backend
- Framework: {FastAPI / Express}
- Database: {PostgreSQL / MongoDB}

## 현재 진행 상황

| 기능 | 상태 | 담당 | 비고 |
|------|------|------|------|
| FR-001 | ✅ 완료 | - | |
| FR-002 | 🔄 진행중 | Frontend | 80% |
| FR-003 | ⏳ 대기 | - | |

**현재 작업**: FR-002 Frontend 개발

## 중요 파일 위치

| 파일 | 경로 | 설명 |
|------|------|------|
| PRD | `.prd-workspace/PRD-FINAL.md` | 요구사항 |
| API 명세 | `.agent-context/contracts.md` | API 계약서 |
| 타입 정의 | `.agent-context/shared-types.md` | 공유 타입 |
| 현재 상태 | `.agent-context/current-state.md` | 기능 상태 |
| 세션 로그 | `.project/session-log.md` | 작업 기록 |

## 사용 중인 스킬

- `supervisor-report-v2`: 개발 워크플로우
- `feature-extension`: 기능 추가 시
- `context-manager`: 컨텍스트 관리

## 최근 이슈

| 날짜 | 이슈 | 상태 |
|------|------|------|
| 2025-01-30 | API 타임아웃 | ✅ 해결 (Redis 캐시) |
| 2025-01-29 | 빌드 에러 | ✅ 해결 |

## 컨벤션 요약

- 컴포넌트: PascalCase (`StockCard.tsx`)
- 함수: camelCase (`fetchStocks`)
- API: REST, `/api/v1/` prefix
- 브랜치: `feature/FR-XXX-description`

## 빠른 명령어

```bash
# 개발 서버
npm run dev          # Frontend (localhost:3000)
cd backend && uvicorn main:app --reload  # Backend (localhost:8000)

# 테스트
npm test
cd backend && pytest

# 빌드
npm run build
```

## 세션 시작 체크리스트

1. [ ] `git pull` 최신 코드
2. [ ] "컨텍스트 로드해줘"로 상태 확인
3. [ ] 이전 세션 다음 작업 확인
4. [ ] 작업 시작

## 세션 종료 체크리스트

1. [ ] 작업 중인 코드 저장
2. [ ] "작업 마무리해줘"로 컨텍스트 저장
3. [ ] `git commit` (필요시)
```

---

## 컨텍스트 윈도우 초과 시

### 감지

- 대화가 길어질 때
- Claude가 이전 내용을 잊어버릴 때
- "아까 말한 거 뭐였지?" 상황

### 대응

```markdown
## 컨텍스트 윈도우 초과 대응

### 방법 1: 즉시 저장 후 새 세션

"지금까지 내용 컨텍스트 저장하고 새 대화 시작하자"

→ 현재까지 작업 저장
→ 새 대화에서 "컨텍스트 로드해줘"

### 방법 2: 요약 후 계속

"지금까지 대화 요약해서 컨텍스트 파일에 저장해줘"

→ 핵심 내용만 파일에 저장
→ 대화 계속 진행

### 방법 3: 특정 파일만 다시 로드

"contracts.md랑 current-state.md 다시 읽어줘"

→ 필요한 컨텍스트만 다시 로드
```

---

## 권장 작업 루틴

```
[세션 시작]
"컨텍스트 로드해줘"
    ↓
[상태 확인]
"이전 세션에서 뭐 했고 다음 뭐 해야 해?"
    ↓
[작업 진행]
"FR-003 계속해줘"
    ↓
[중간 저장 (큰 작업 완료 시)]
"current-state.md 업데이트해줘"
    ↓
[세션 종료]
"작업 마무리해줘"
```

---

## 버전 히스토리

| 버전 | 날짜 | 변경 내용 |
|------|------|-----------|
| v1.0 | 2025-01-30 | 초기 버전 |
