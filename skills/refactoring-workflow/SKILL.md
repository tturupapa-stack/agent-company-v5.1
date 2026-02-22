---
name: refactoring-workflow
description: |
  코드 리팩토링 워크플로우 스킬.
  현황 분석 → 문제점 식별 → 계획 수립 → 단계별 리팩토링 → 검증 순서로 진행한다.
  
  기능 변경 없이 코드 구조, 가독성, 유지보수성을 개선하는 데 초점을 맞춘다.
  항상 테스트가 통과하는 상태를 유지하면서 점진적으로 진행한다.
---

# Refactoring Workflow Skill

코드 리팩토링을 안전하게 진행하는 워크플로우입니다.

---

## 핵심 원칙

> **"기능은 그대로, 구조만 개선하라."**

리팩토링 전후 동작이 동일해야 합니다. 버그 수정도 새 기능도 아닙니다.

> **"테스트가 안전망이다. 테스트 없이 리팩토링하지 마라."**

테스트 커버리지가 낮으면 먼저 테스트를 보강합니다.

> **"작은 단위로, 자주 검증하라."**

한 번에 큰 변경 대신, 작은 변경 후 테스트를 반복합니다.

---

## 사용 시점

| 상황 | 적합 |
|------|------|
| "이 코드 좀 정리해줘" | ✅ |
| "파일이 너무 커" | ✅ |
| "중복 코드 제거해줘" | ✅ |
| "구조 개선해줘" | ✅ |
| "새 기능 추가해줘" | ❌ (feature-extension) |
| "UI 이쁘게 해줘" | ❌ (ux-improvement) |
| "버그 수정해줘" | ❌ (버그 수정은 리팩토링 아님) |

---

## 워크플로우 개요

```
Phase 1: 현황 분석
    ↓
Phase 2: 문제점 식별 및 계획 수립
    ↓
Phase 3: 사용자 승인
    ↓
Phase 4: 테스트 보강 (필요시)
    ↓
Phase 5: 단계별 리팩토링
    ↓
Phase 6: 최종 검증 및 보고
```

---

## Phase 1: 현황 분석

### 목적

리팩토링 대상 코드의 현재 상태를 파악합니다.

### 에이전트

`codebase-analyzer`

### 작업 내용

```markdown
## 분석 항목

### 1. 대상 파일 분석
- 파일 크기 (라인 수)
- 함수/메서드 개수
- 복잡도 (대략적)

### 2. 코드 스멜 탐지
- Long Method (50줄+)
- Large Class (300줄+)
- Duplicate Code
- Dead Code
- Magic Numbers
- God Object/Component

### 3. 의존성 분석
- 이 파일을 import하는 파일
- 이 파일이 import하는 파일
- 순환 의존성

### 4. 테스트 현황
- 관련 테스트 파일 존재 여부
- 테스트 커버리지 (측정 가능시)
```

### 결과물

- `.agent-results/analyzer/YYYY-MM-DD-refactoring-analysis.md`

---

## Phase 2: 문제점 식별 및 계획 수립

### 목적

발견된 문제점을 분류하고 리팩토링 계획을 수립합니다.

### 에이전트

`refactoring-planner`

### 작업 내용

```markdown
## 발견된 문제점

### Critical (반드시 해결)

| # | 파일 | 문제 | 원인 |
|---|------|------|------|
| 1 | userService.ts | 450줄, 4가지 책임 | God Class |
| 2 | helpers.ts | 동일 코드 3회 반복 | Duplicate Code |

### Major (해결 권장)

| # | 파일 | 문제 | 원인 |
|---|------|------|------|
| 3 | Dashboard.tsx | 380줄 | Large Component |
| 4 | api.ts | 복잡도 25 | 중첩 if문 |

### Minor (선택적)

| # | 파일 | 문제 | 원인 |
|---|------|------|------|
| 5 | config.ts | 매직 넘버 7개 | 상수화 필요 |

---

## 리팩토링 계획

### 적용할 패턴

| 문제 | 패턴 | 위험도 |
|------|------|--------|
| God Class | Extract Class | 중 |
| Duplicate Code | Extract Function | 낮 |
| Large Component | Extract Component | 중 |
| 중첩 if | Guard Clauses | 낮 |

### 실행 순서

| Phase | 작업 | 위험도 | 선행 조건 |
|-------|------|--------|-----------|
| 4-1 | 테스트 보강 | - | - |
| 5-1 | 중복 코드 제거 | 낮 | Phase 4-1 |
| 5-2 | 매직 넘버 상수화 | 낮 | - |
| 5-3 | Guard Clauses 적용 | 낮 | - |
| 5-4 | AuthService 분리 | 중 | Phase 5-1 |
| 5-5 | Dashboard 분리 | 중 | Phase 5-4 |

### 영향 범위

| 리팩토링 | 영향 파일 | 테스트 파일 |
|----------|-----------|-------------|
| userService 분리 | 12개 | 3개 |
| Dashboard 분리 | 5개 | 0개 (⚠️) |
```

### 결과물

- `.agent-results/refactoring/YYYY-MM-DD-refactoring-plan.md`

---

## Phase 3: 사용자 승인

### 목적

리팩토링 계획을 사용자에게 보고하고 승인을 받습니다.

### 보고 내용

```markdown
## 리팩토링 계획 요약

### 대상
- 파일: 5개
- 주요 문제: God Class, Duplicate Code

### 작업 범위
- 테스트 보강: 2개 파일 (선행 필수)
- 리팩토링: 5단계

### 영향
- 직접 영향: 15개 파일
- 간접 영향: 8개 파일

### 예상 결과
| 지표 | Before | After (예상) |
|------|--------|--------------|
| 최대 파일 크기 | 450줄 | 150줄 |
| 평균 복잡도 | 22 | 8 |
| 테스트 커버리지 | 30% | 70%+ |

### 리스크
- 기존 기능 깨짐 가능성 → 테스트로 방어
- import 경로 변경 → IDE 자동 수정 활용

---

## 계속 진행할까요?

옵션:
- A. 전체 진행 (권장)
- B. Phase 5-1 ~ 5-3만 (안전한 것만)
- C. 특정 단계만 (번호로 선택)
- D. 취소
```

### 사용자 입력 예시

```
"A로 진행해"
"5-1, 5-2만 해줘"
"테스트 보강은 건너뛰고 할 수 있어?"
```

---

## Phase 4: 테스트 보강 (필요시)

### 목적

리팩토링 전 안전망을 확보합니다.

### 에이전트

`test-runner`, `backend-developer` 또는 `frontend-developer`

### 작업 조건

```markdown
## 테스트 보강 기준

### 필수 (진행 차단)
- 리팩토링 대상 파일의 테스트가 0%
- Critical 문제가 있는 파일

### 권장 (경고 후 진행)
- 테스트 커버리지 < 50%
- 영향 범위가 넓은 파일

### 스킵 가능
- 테스트 커버리지 > 70%
- 영향 범위가 좁은 파일
```

### 테스트 보강 방법

```markdown
## 테스트 전략

### 1. 기존 동작 캡처
- 현재 입력 → 출력 케이스 수집
- 에지 케이스 식별

### 2. 테스트 작성
- 핵심 함수/메서드 테스트
- 입력/출력 검증
- 에러 케이스

### 3. 테스트 실행
- 모든 테스트 통과 확인
- 이 상태를 "기준점"으로 저장
```

### 결과물

- 추가된 테스트 파일
- `.agent-results/tester/YYYY-MM-DD-pre-refactoring-tests.md`

### 완료 조건

```markdown
✅ 대상 파일 테스트 커버리지 70%+
✅ 모든 테스트 통과
✅ 기준점 상태 저장
```

---

## Phase 5: 단계별 리팩토링

### 목적

계획에 따라 코드를 리팩토링합니다.

### 에이전트

`backend-developer`, `frontend-developer`

### 핵심 규칙

```markdown
## 리팩토링 규칙

### 1. 한 번에 하나만
- 한 가지 패턴만 적용
- 여러 변경 섞지 않기

### 2. 매 단계 검증
- 변경 후 즉시 테스트
- 테스트 실패 시 즉시 롤백

### 3. 커밋 단위
- 각 리팩토링 단계 = 1 커밋
- 커밋 메시지: "refactor: {작업 내용}"

### 4. 기능 변경 금지
- 동작 변경 ❌
- 버그 수정 ❌ (별도 작업)
- 성능 최적화 ❌ (별도 작업)
```

### 단계별 실행 예시

```markdown
## Step 5-1: 중복 코드 제거

### 작업 내용
helpers.ts의 날짜 포맷팅 코드 3개 → 1개 함수로 통합

### Before
```typescript
// 45줄
const formatDate1 = (date: Date) => { /* 구현 */ };
// 120줄
const formatDate2 = (date: Date) => { /* 동일 구현 */ };
// 180줄
const formatDate3 = (date: Date) => { /* 동일 구현 */ };
```

### After
```typescript
// dateUtils.ts
export function formatDate(date: Date, format = 'YYYY-MM-DD'): string {
  // 단일 구현
}

// helpers.ts - 기존 위치에서 import 사용
import { formatDate } from './dateUtils';
```

### 검증
- [ ] 단위 테스트 통과
- [ ] 기존 테스트 통과
- [ ] 빌드 성공

### 커밋
`refactor: extract duplicate date formatting to dateUtils`
```

---

### 실패 시 롤백

```markdown
## 롤백 정책

### 테스트 실패 시
1. 해당 단계 변경 즉시 롤백
2. 원인 분석
3. 선택지 제시:
   - 수정 후 재시도
   - 해당 단계 스킵
   - 전체 중단

### 빌드 실패 시
1. 해당 단계 변경 즉시 롤백
2. import 경로 등 누락 확인
3. 수정 후 재시도
```

### 결과물 (각 단계별)

- 수정된 코드 파일
- 테스트 결과
- 커밋 (또는 커밋 준비 상태)

---

## Phase 6: 최종 검증 및 보고

### 목적

리팩토링 결과를 검증하고 전후 비교를 보고합니다.

### 에이전트

`test-runner`, `code-reviewer`

### 검증 항목

```markdown
## 최종 검증

### 1. 테스트
- [ ] 전체 테스트 실행
- [ ] 모든 테스트 통과
- [ ] 커버리지 유지/향상

### 2. 빌드
- [ ] 빌드 성공
- [ ] 타입 에러 없음
- [ ] 린트 에러 없음

### 3. 동작 확인
- [ ] 주요 기능 수동 테스트
- [ ] 리팩토링된 부분 집중 확인

### 4. 코드 리뷰
- [ ] 새 구조가 적절한지
- [ ] 네이밍이 명확한지
- [ ] 의도치 않은 동작 변경 없는지
```

### 결과 리포트

```markdown
## 리팩토링 결과 리포트

**작업일**: YYYY-MM-DD
**대상**: userService.ts, helpers.ts, Dashboard.tsx

---

## 전후 비교

### 파일 구조

| Before | After |
|--------|-------|
| userService.ts (450줄) | userService.ts (150줄) |
| | authService.ts (120줄, 신규) |
| | permissionService.ts (100줄, 신규) |
| | notificationService.ts (80줄, 신규) |
| helpers.ts (280줄) | helpers.ts (180줄) |
| | dateUtils.ts (50줄, 신규) |
| Dashboard.tsx (380줄) | Dashboard.tsx (150줄) |
| | DashboardStats.tsx (100줄, 신규) |
| | DashboardCharts.tsx (130줄, 신규) |

### 지표 변화

| 지표 | Before | After | 변화 |
|------|--------|-------|------|
| 최대 파일 크기 | 450줄 | 180줄 | -60% ⬇️ |
| 평균 복잡도 | 22 | 7 | -68% ⬇️ |
| 테스트 커버리지 | 30% | 75% | +45% ⬆️ |
| 중복 코드 | 3곳 | 0곳 | -100% ⬇️ |

### 작업 요약

| 단계 | 작업 | 결과 |
|------|------|------|
| 5-1 | 중복 코드 제거 | ✅ |
| 5-2 | 매직 넘버 상수화 | ✅ |
| 5-3 | Guard Clauses | ✅ |
| 5-4 | AuthService 분리 | ✅ |
| 5-5 | Dashboard 분리 | ✅ |

### 검증 결과

| 항목 | 결과 |
|------|------|
| 전체 테스트 | ✅ 통과 (45/45) |
| 빌드 | ✅ 성공 |
| 타입 체크 | ✅ 에러 없음 |
| 코드 리뷰 | ✅ 통과 |

---

## 개선된 점

1. **단일 책임**: 각 서비스가 하나의 책임만 가짐
2. **테스트 용이**: 작은 단위로 분리되어 테스트 쉬움
3. **가독성**: 파일당 150줄 이하로 파악 용이
4. **재사용**: dateUtils 등 공통 유틸 분리

## 주의 사항

1. **import 경로 변경**: 기존 `userService`에서 import하던 파일들 확인 필요
2. **문서 업데이트**: API 문서 등 관련 문서 업데이트 권장
```

---

## 전체 흐름 예시

```
사용자: "userService.ts 좀 정리해줘"
    ↓
Phase 1: codebase-analyzer
    → 450줄, 4가지 책임, 복잡도 25
    → 테스트 커버리지 30%
    ↓
Phase 2: refactoring-planner
    → God Class 문제 식별
    → Extract Class 패턴 제안
    → 4개 서비스로 분리 계획
    ↓
Phase 3: 사용자 승인
    → "영향 파일 12개, 테스트 보강 필요"
    → "계속 진행할까요?"
    → "A로 해줘"
    ↓
Phase 4: 테스트 보강
    → userService 테스트 30% → 70%
    → 기준점 확보
    ↓
Phase 5: 단계별 리팩토링
    → Step 1: 중복 제거 → 테스트 ✅
    → Step 2: AuthService 분리 → 테스트 ✅
    → Step 3: PermissionService 분리 → 테스트 ✅
    → Step 4: NotificationService 분리 → 테스트 ✅
    ↓
Phase 6: 최종 검증
    → 테스트 전체 통과
    → 빌드 성공
    → 전후 비교 리포트
    ↓
완료: "리팩토링 완료! 450줄→150줄, 복잡도 68% 감소"
```

---

## 에스컬레이션 정책

| 조건 | 동작 |
|------|------|
| 테스트 커버리지 0% | Phase 4 필수, 스킵 불가 |
| 테스트 실패 (리팩토링 중) | 즉시 롤백, 원인 분석 |
| 영향 파일 20개 초과 | 범위 축소 제안 |
| 순환 의존성 발견 | 먼저 해결 후 리팩토링 |
| 동작 변경 감지 | 즉시 중단, 보고 |

---

## 폴더 구조

```
.agent-results/
├── analyzer/
│   └── YYYY-MM-DD-refactoring-analysis.md
├── refactoring/
│   └── YYYY-MM-DD-refactoring-plan.md
├── tester/
│   └── YYYY-MM-DD-pre-refactoring-tests.md
├── backend/ 또는 frontend/
│   └── YYYY-MM-DD-refactoring-step-N.md
├── reviewer/
│   └── YYYY-MM-DD-refactoring-review.md
└── docs/
    └── YYYY-MM-DD-refactoring-report.md
```

---

## 버전 히스토리

| 버전 | 날짜 | 변경 내용 |
|------|------|-----------|
| v1.0 | 2025-01-30 | 초기 버전 |
