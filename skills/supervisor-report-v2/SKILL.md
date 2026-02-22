---
name: supervisor-report-v2
description: 복잡한 요청을 분석하여 적합한 에이전트를 자동 선발하고, 공유 컨텍스트 기반으로 작업을 위임하며, 단계별 즉시 검증과 재작업 상한선을 통해 오류 발생률을 최소화하는 오케스트레이션 스킬.
---

# Supervisor Report Skill v2 - 오케스트레이션 스킬

이 스킬은 사용자의 복잡한 요청을 분석하여 적합한 에이전트를 자동 선발하고, **공유 컨텍스트 기반**으로 작업을 위임하며, **단계별 즉시 검증**을 통해 오류 발생률을 최소화합니다.

---

## 핵심 원칙

> **"나중에 테스트하지 마라. 즉시 테스트하라."**

모든 개발 작업은 완료 직후 해당 부분만 테스트합니다. 다음 단계는 테스트 통과 후에만 진행합니다.

> **"에이전트끼리 계약서를 공유하라."**

모든 에이전트는 작업 전 `.agent-context/` 폴더의 기술 명세를 읽고 따릅니다. 독자적 판단으로 API 형식이나 타입을 결정하지 않습니다.

> **"무한 루프에 빠지지 마라."**

재작업 횟수에 상한선을 두고, 초과 시 사용자에게 에스컬레이션합니다.

---

## 사용 가능한 에이전트

| subagent_type | 용도 | 권장 모델 |
|---------------|------|-----------|
| `frontend-developer` | React/Next.js 컴포넌트, UI/UX | sonnet |
| `backend-developer` | FastAPI, DB, 서버 로직 | sonnet |
| `test-runner` | 테스트 실행 및 결과 보고 | haiku |
| `code-reviewer` | 코드 품질 리뷰 | sonnet |
| `doc-writer` | 개발일지, API 문서 작성 | haiku |
| `ui-designer` | 디자인 분석 + 개선 계획 | sonnet |
| `visual-director` | 브랜드 아이덴티티 + 토큰 생성 | sonnet |

---

## 워크플로우 개요

```
Phase 1: 요청 분석
    ↓
Phase 2: 기술 명세서 생성 ← 핵심 추가
    ↓
Phase 3: 스모크 테스트 기준 정의 ← 핵심 추가
    ↓
Phase 4: 개발 + 즉시 테스트 (반복)
    ↓
Phase 5: 통합 테스트
    ↓
Phase 6: 코드 리뷰
    ↓
Phase 7: 최종 리포트
```

---

## Phase 1: 요청 분석

사용자 요청을 분석합니다:

| 분석 항목 | 내용 |
|-----------|------|
| 작업 유형 | 신규 기능 / 버그 수정 / 리팩토링 / 문서화 |
| 영향 범위 | Frontend / Backend / Full-stack |
| 필요 에이전트 | 분석 기반 선정 |
| 예상 복잡도 | 낮음 / 중간 / 높음 |

### 에이전트 선발 기준

| 작업 유형 | 주 담당 | 보조 |
|-----------|---------|------|
| Frontend 개발 | frontend-developer | test-runner |
| Backend 개발 | backend-developer | test-runner |
| Full-stack | frontend + backend (순차) | test-runner |
| 디자인 포함 개발 | ui-designer + frontend-developer | visual-director |
| UI/UX 개선 | ui-designer | frontend-developer |
| 문서화 | doc-writer | - |
| 모든 코드 변경 | - | code-reviewer (필수) |

---

## Phase 2: 기술 명세서 생성 ⭐ 핵심

> **작업 위임 전 반드시 실행. 이 단계를 건너뛰지 마라.**

`.agent-context/` 폴더에 다음 파일들을 생성합니다:

### 2.1 contracts.md (API 계약서)

```markdown
# API 계약서

## 엔드포인트 목록

| 엔드포인트 | 메서드 | 요청 형식 | 응답 형식 | 담당 |
|------------|--------|-----------|-----------|------|
| /api/stocks | GET | - | { stocks: Stock[] } | backend |
| /api/stocks/:id | GET | - | Stock | backend |

## 에러 응답 형식 (공통)

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message"
  }
}
```

## 상태 코드 규칙

| 상태 코드 | 의미 |
|-----------|------|
| 200 | 성공 |
| 400 | 잘못된 요청 |
| 404 | 리소스 없음 |
| 500 | 서버 에러 |
```

### 2.2 shared-types.md (공유 타입)

```markdown
# 공유 타입 정의

## 핵심 엔티티

```typescript
interface Stock {
  id: string;
  symbol: string;
  name: string;
  price: number;
  change: number;
  changePercent: number;
  updatedAt: string; // ISO 8601
}

interface ApiResponse<T> {
  data: T;
  meta?: {
    total: number;
    page: number;
  };
}

interface ApiError {
  error: {
    code: string;
    message: string;
  };
}
```

## 열거형

```typescript
type SortOrder = 'asc' | 'desc';
type StockSector = 'tech' | 'healthcare' | 'finance' | 'energy';
```
```

### 2.3 conventions.md (프로젝트 규칙)

```markdown
# 프로젝트 컨벤션

## 기술 스택

| 영역 | 기술 |
|------|------|
| Frontend | Next.js 14, React 18, TypeScript |
| Styling | Tailwind CSS |
| 상태관리 | Zustand |
| API 호출 | fetch (services/ 폴더) |
| Backend | FastAPI, Python 3.11 |
| DB | PostgreSQL + Prisma |

## 폴더 구조

```
frontend/
├── app/           # Next.js App Router
├── components/    # UI 컴포넌트
├── services/      # API 호출 함수
├── stores/        # Zustand 스토어
├── types/         # TypeScript 타입
└── utils/         # 유틸리티 함수

backend/
├── api/           # FastAPI 라우터
├── services/      # 비즈니스 로직
├── models/        # DB 모델
└── utils/         # 유틸리티
```

## 네이밍 규칙

| 대상 | 규칙 | 예시 |
|------|------|------|
| 컴포넌트 | PascalCase | StockCard.tsx |
| 함수 | camelCase | getStockPrice() |
| 상수 | UPPER_SNAKE | MAX_RETRY_COUNT |
| 파일 (Python) | snake_case | stock_service.py |

## 필수 규칙

1. 모든 컴포넌트는 TypeScript로 작성
2. any 타입 사용 금지
3. API 호출은 반드시 services/ 폴더에 분리
4. 에러 처리는 try-catch 필수
5. console.log는 개발 완료 후 제거
```

### 2.4 design-brief.md (디자인 브리프) ⭐ 필수

> **모든 작업에서 생성. 디자인 포함 여부 무관하게 앱의 시각적 방향을 사전에 정의한다.**

```markdown
# 디자인 브리프

## 앱 성격
- 앱 목적: {앱의 핵심 목적}
- 카테고리: {대시보드 / 소셜 / 이커머스 / 콘텐츠 / 생산성 / 유틸리티}

## 타겟 사용자
- 연령대: {주 사용 연령}
- 기술 숙련도: {초급 / 중급 / 고급}
- 사용 맥락: {모바일 / 데스크톱 / 양쪽}

## 톤 & 무드
- 키워드: {3-5개, 예: 전문적, 신뢰감, 차분한}
- 레퍼런스: {참고할 앱/사이트, 있으면}

## 컬러 방향
- Primary: {브랜드 컬러 또는 추천 방향}
- 톤: {밝은 / 어두운 / 중립}
- 금지: {피해야 할 색상/느낌}

## 아이콘 스타일
- 라이브러리: {Lucide React / Heroicons / React Icons}
- 스타일: {outlined / filled / rounded}
- **이모지 사용 절대 금지**

## 타이포그래피 방향
- 성격: {모던 / 클래식 / 기술적 / 친근한}
- 추천 폰트: {Google Fonts 기반}
```

### 2.5 current-state.md (현재 상태)

```markdown
# 현재 프로젝트 상태

## 완료된 기능

| 기능 | 파일 | 상태 |
|------|------|------|
| 주식 목록 조회 | StockList.tsx, /api/stocks | ✅ 완료 |
| 주식 검색 | SearchInput.tsx | ✅ 완료 |

## 진행 중

| 기능 | 담당 | 상태 |
|------|------|------|
| 주식 상세 모달 | frontend-developer | 🔄 진행중 |

## 알려진 이슈

- 없음

## 최근 변경

- 2025-01-29: SearchInput IME 버그 수정
```

---

### 에이전트 호출 시 필수 프롬프트 접두사

모든 에이전트 호출 시 다음을 prompt 앞에 추가:

```markdown
## 필수 참조 문서

작업 전 반드시 다음 파일을 읽고 규칙을 따르세요:
- `.agent-context/contracts.md` - API 계약서
- `.agent-context/shared-types.md` - 공유 타입
- `.agent-context/conventions.md` - 프로젝트 규칙
- `.agent-context/current-state.md` - 현재 상태
- `.agent-context/design-brief.md` - 디자인 브리프 (UI 작업 시 필수)

**규칙 위반 시 재작업 대상입니다.**

---

{실제 작업 지시}
```

---

## Phase 3: 스모크 테스트 기준 정의 ⭐ 핵심

> **개발 시작 전에 "성공 기준"을 먼저 정의한다.**

### 3.1 스모크 테스트란?

최소한의 동작 확인 테스트. "이것만 되면 일단 성공"의 기준.

### 3.2 스모크 테스트 정의 형식

```markdown
# 스모크 테스트: {기능명}

## 최소 성공 기준

| # | 테스트 항목 | 확인 방법 | Mock 필요 |
|---|-------------|-----------|-----------|
| 1 | 모달이 열린다 | 버튼 클릭 후 모달 visible | No |
| 2 | 데이터가 표시된다 | 주식명, 가격 텍스트 존재 | Yes |
| 3 | 닫기가 동작한다 | X 버튼 클릭 후 모달 hidden | No |

## 테스트 실행 명령

```bash
npm test -- StockDetailModal --watchAll=false
```

## 통과 기준

- 위 3가지 모두 PASS
- 콘솔 에러 없음
```

### 3.3 스모크 테스트 시점

| 시점 | 조건 |
|------|------|
| Frontend 완료 직후 | Mock 데이터로 UI 동작 확인 |
| Backend 완료 직후 | API 단독 동작 확인 |
| 통합 전 | 각각 스모크 테스트 통과 필수 |

### 3.4 스모크 테스트 실패 시

```
스모크 테스트 실패 → 다음 단계 진행 금지 → 즉시 재작업
```

---

## Phase 4: 개발 + 즉시 테스트 ⭐ 핵심

> **"만들고 → 바로 테스트 → 통과 후 다음 단계"**

### 4.1 단계별 실행 패턴

#### Frontend 개발 흐름

```
Step 1: Frontend 개발
    ↓
Step 2: 빌드 검증 (즉시)
    ↓ 실패 시 → 재작업 (Step 1로)
Step 3: 스모크 테스트 (즉시)
    ↓ 실패 시 → 재작업 (Step 1로)
Step 4: ✅ Frontend 완료 확정
```

#### Backend 개발 흐름

```
Step 1: Backend 개발
    ↓
Step 2: 서버 시작 검증 (즉시)
    ↓ 실패 시 → 재작업 (Step 1로)
Step 3: API 테스트 (즉시)
    ↓ 실패 시 → 재작업 (Step 1로)
Step 4: ✅ Backend 완료 확정
```

### 4.2 구체적 호출 예시

#### Frontend 개발 + 즉시 테스트

```markdown
# Step 1: Frontend 개발

Task tool:
- subagent_type: "frontend-developer"
- prompt: |
    ## 필수 참조 문서
    작업 전 반드시 다음 파일을 읽고 규칙을 따르세요:
    - `.agent-context/contracts.md`
    - `.agent-context/shared-types.md`
    - `.agent-context/conventions.md`
    
    ---
    
    ## 작업 요청
    
    **작업 ID**: 2025-01-29-stock-detail-modal
    
    ### 작업 내용
    StockDetailModal 컴포넌트를 개발해주세요.
    - 주식 상세 정보를 모달로 표시
    - props: { stock: Stock; isOpen: boolean; onClose: () => void }
    - Tailwind CSS, 다크모드 지원
    
    ### 결과물 저장 위치
    `.agent-results/frontend/2025-01-29-stock-detail-modal.md`
- description: "주식 상세 모달 개발"
```

```markdown
# Step 2: 빌드 검증 (즉시)

Task tool:
- subagent_type: "test-runner"
- model: "haiku"
- prompt: |
    ## 빌드 검증
    
    다음 명령을 실행하고 결과를 보고하세요:
    
    ```bash
    npm run build
    ```
    
    ### 보고 형식
    - 결과: PASS / FAIL
    - 실패 시: 전체 에러 메시지 복사
    
    ### 결과물 저장 위치
    `.agent-results/tester/2025-01-29-build-check.md`
- description: "빌드 검증"
```

```markdown
# Step 3: 스모크 테스트 (즉시)

Task tool:
- subagent_type: "test-runner"
- model: "haiku"
- prompt: |
    ## 스모크 테스트: StockDetailModal
    
    다음 명령을 실행하세요:
    
    ```bash
    npm test -- StockDetailModal --watchAll=false
    ```
    
    ### 확인 항목
    1. 모달 열림/닫힘 동작
    2. props 전달 정상
    3. 콘솔 에러 없음
    
    ### 보고 형식
    - 결과: PASS / FAIL
    - 실패한 테스트 목록
    - 에러 메시지
    
    ### 결과물 저장 위치
    `.agent-results/tester/2025-01-29-smoke-test.md`
- description: "스모크 테스트"
```

#### Backend 개발 + 즉시 테스트

```markdown
# Step 1: Backend 개발

Task tool:
- subagent_type: "backend-developer"
- prompt: |
    ## 필수 참조 문서
    (생략 - 위와 동일)
    
    ---
    
    ## 작업 요청
    
    **작업 ID**: 2025-01-29-stock-detail-api
    
    ### 작업 내용
    GET /api/stocks/:id 엔드포인트를 개발해주세요.
    - contracts.md의 응답 형식 준수
    - shared-types.md의 Stock 타입 사용
    - 에러 처리 포함
    
    ### 결과물 저장 위치
    `.agent-results/backend/2025-01-29-stock-detail-api.md`
- description: "주식 상세 API 개발"
```

```markdown
# Step 2: 서버 시작 검증 (즉시)

Task tool:
- subagent_type: "test-runner"
- model: "haiku"
- prompt: |
    ## 서버 시작 검증
    
    다음을 확인하세요:
    
    1. 서버 시작: `uvicorn main:app --reload`
    2. 5초 대기
    3. Health check: `curl http://localhost:8000/health`
    
    ### 보고 형식
    - 서버 시작: PASS / FAIL
    - Health check: PASS / FAIL
    - 에러 발생 시 전체 로그
    
    ### 결과물 저장 위치
    `.agent-results/tester/2025-01-29-server-check.md`
- description: "서버 시작 검증"
```

```markdown
# Step 3: API 테스트 (즉시)

Task tool:
- subagent_type: "test-runner"
- model: "haiku"
- prompt: |
    ## API 단위 테스트
    
    다음 명령을 실행하세요:
    
    ```bash
    pytest tests/test_stock_api.py -v
    ```
    
    ### 보고 형식
    - 총 테스트: N개
    - 성공: N개
    - 실패: N개
    - 실패한 테스트 상세
    
    ### 결과물 저장 위치
    `.agent-results/tester/2025-01-29-api-test.md`
- description: "API 테스트"
```

---

## Phase 5: 통합 테스트

> Frontend와 Backend 각각 스모크 테스트 통과 후에만 실행

### 5.1 통합 테스트 실행

```markdown
Task tool:
- subagent_type: "test-runner"
- model: "haiku"
- prompt: |
    ## 통합 테스트
    
    ### 사전 조건
    - Backend 서버 실행 중
    - Frontend 개발 서버 실행 중
    
    ### 테스트 실행
    ```bash
    npm run test:e2e
    ```
    
    또는 수동 확인:
    1. http://localhost:3000 접속
    2. 주식 목록에서 항목 클릭
    3. 모달 열림 확인
    4. 실제 API 데이터 표시 확인
    5. 모달 닫힘 확인
    
    ### 보고 형식
    - 결과: PASS / FAIL
    - 실패 항목 상세
    - 스크린샷 (가능한 경우)
    
    ### 결과물 저장 위치
    `.agent-results/tester/2025-01-29-integration-test.md`
- description: "통합 테스트"
```

---

## Phase 6: 코드 리뷰

> 통합 테스트 통과 후에만 실행

### 6.1 코드 리뷰 실행

```markdown
Task tool:
- subagent_type: "code-reviewer"
- prompt: |
    ## 코드 리뷰 요청
    
    ### 리뷰 대상
    - Frontend: components/StockDetailModal.tsx
    - Backend: api/stock_detail.py
    
    ### 참조 문서
    - `.agent-context/conventions.md` - 컨벤션 준수 여부 확인
    
    ### 리뷰 관점
    1. **코드 품질**: 가독성, 중복, 복잡도
    2. **타입 안전성**: any 사용 여부, 타입 정확성
    3. **에러 처리**: try-catch, 엣지 케이스
    4. **성능**: 불필요한 리렌더링, N+1 쿼리
    5. **보안**: XSS, SQL Injection, 민감정보 노출
    
    ### 판정 기준
    - **통과**: 이슈 없음 또는 Minor만 존재
    - **조건부 통과**: Major 1-2개, 수정 권장
    - **재작업 필요**: Critical 존재 또는 Major 3개 이상
    
    ### 결과물 저장 위치
    `.agent-results/reviewer/2025-01-29-code-review.md`
- description: "코드 리뷰"
```

### 6.2 리뷰 결과별 대응

| 판정 | 대응 |
|------|------|
| 통과 | Phase 7로 진행 |
| 조건부 통과 | Minor 이슈 기록 후 Phase 7로 진행 |
| 재작업 필요 | 해당 에이전트에게 재작업 요청 |

---

## Phase 7: 최종 리포트

### 7.1 리포트 저장 위치

`output/reports/{YYYY-MM-DD-task-name}/final-report.md`

### 7.2 리포트 형식

```markdown
# 작업 완료 리포트

**생성일**: YYYY-MM-DD
**작업명**: {task-name}
**총 소요 단계**: N단계
**재작업 횟수**: N회

---

## 1. 요청 사항

{원본 요청 내용}

---

## 2. 기술 명세

### API 계약
| 엔드포인트 | 메서드 | 상태 |
|------------|--------|------|
| /api/stocks/:id | GET | ✅ 구현 완료 |

### 공유 타입
- Stock 인터페이스 정의 완료

---

## 3. 수행된 작업

### Frontend

| 파일 | 작업 내용 | 테스트 결과 |
|------|-----------|-------------|
| StockDetailModal.tsx | 신규 생성 | ✅ PASS |

### Backend

| 파일 | 작업 내용 | 테스트 결과 |
|------|-----------|-------------|
| stock_detail.py | 신규 생성 | ✅ PASS |

---

## 4. 테스트 결과

### 스모크 테스트
- Frontend: ✅ PASS
- Backend: ✅ PASS

### 통합 테스트
- 결과: ✅ PASS
- 총 테스트: 5개
- 성공: 5개

---

## 5. 코드 리뷰 결과

**판정**: 통과

| 심각도 | 개수 | 내용 |
|--------|------|------|
| Critical | 0 | - |
| Major | 0 | - |
| Minor | 1 | console.log 제거 권장 |

---

## 6. 에이전트 평가

| 에이전트 | 등급 | 재작업 횟수 | 비고 |
|----------|------|-------------|------|
| frontend-developer | A | 0 | 첫 시도 성공 |
| backend-developer | A | 0 | 첫 시도 성공 |
| test-runner | A | 0 | - |
| code-reviewer | A | 0 | - |

---

## 7. 결과물 위치

| 유형 | 경로 |
|------|------|
| Frontend 결과 | .agent-results/frontend/2025-01-29-*.md |
| Backend 결과 | .agent-results/backend/2025-01-29-*.md |
| 테스트 결과 | .agent-results/tester/2025-01-29-*.md |
| 리뷰 결과 | .agent-results/reviewer/2025-01-29-*.md |

---

## 8. 향후 권장사항

- Minor 이슈 수정 (console.log 제거)
- 추가 테스트 케이스 작성 권장
```

---

## 재작업 정책 ⭐ 핵심

### 재작업 횟수 제한

| 심각도 | 최대 재작업 | 초과 시 |
|--------|-------------|---------|
| Critical | 2회 | 즉시 에스컬레이션 |
| Major | 3회 | 에스컬레이션 |
| Minor | 1회 | 무시하고 진행 가능 |

### 심각도 분류

| 심각도 | 정의 | 예시 |
|--------|------|------|
| Critical | 빌드/실행 불가 | 문법 에러, import 실패, 서버 시작 불가 |
| Major | 핵심 기능 동작 안 함 | API 응답 형식 불일치, 주요 로직 버그 |
| Minor | 동작하나 개선 필요 | 컨벤션 위반, console.log 남음, 주석 부족 |

### 에스컬레이션 트리거

다음 상황 발생 시 **즉시 작업 중단하고 사용자에게 보고**:

1. ❌ 동일 에러가 2회 연속 발생
2. ❌ 재작업 후 새로운 에러가 3개 이상 추가 발생
3. ❌ 빌드 실패가 2회 연속
4. ❌ 테스트 통과율이 재작업 후 오히려 하락
5. ❌ 재작업 상한선 초과

### 에스컬레이션 보고 형식

```markdown
⚠️ 작업 중단 - 사용자 판단 필요

**상황**: StockDetailModal 컴포넌트 빌드 실패 2회 연속

**시도한 것**:
1. 1차 시도: TypeScript 타입 에러 → Stock 인터페이스 import 추가
2. 2차 시도: 동일 에러 반복 → shared-types.md 경로 확인했으나 해결 안 됨

**반복 패턴**: 
타입 정의 파일과 실제 import 경로가 불일치하는 것으로 추정

**선택지**:
1. 🔧 다른 접근 방식 시도 - 타입 파일 위치 재구성
2. ⏭️ 이 기능 스킵하고 다음 기능 진행
3. 🛑 작업 전체 중단하고 문제 분석

어떻게 진행할까요?
```

### 재작업 요청 형식

```markdown
## 재작업 요청

**대상 에이전트**: frontend-developer
**재작업 횟수**: 1/2 (Critical 기준)
**이유**: 빌드 실패

### 발견된 문제

| # | 문제 | 파일:라인 | 심각도 |
|---|------|-----------|--------|
| 1 | Stock 타입 import 누락 | StockDetailModal.tsx:3 | Critical |
| 2 | onClose prop 타입 불일치 | StockDetailModal.tsx:15 | Major |

### 수정 지침

1. `import { Stock } from '@/types/stock'` 추가
2. `onClose: () => void` 타입 명시

### 참조

- `.agent-context/shared-types.md` 다시 확인할 것

### 완료 기준

- [ ] npm run build 성공
- [ ] 타입 에러 0개
```

---

## 의사결정 기준 요약

### 다음 단계 진행 조건

| 현재 단계 | 다음 단계 진행 조건 |
|-----------|---------------------|
| 기술 명세 생성 | 4개 파일 모두 생성 완료 |
| Frontend 개발 | 빌드 성공 + 스모크 테스트 PASS |
| Backend 개발 | 서버 시작 성공 + API 테스트 PASS |
| 통합 테스트 | 모든 테스트 PASS |
| 코드 리뷰 | 통과 또는 조건부 통과 |

### 즉시 재작업 조건

| 상황 | 대응 |
|------|------|
| 빌드 실패 | 즉시 재작업 |
| 테스트 1개라도 FAIL | 즉시 재작업 |
| 서버 시작 실패 | 즉시 재작업 |
| code-reviewer "재작업 필요" 판정 | 해당 이슈 수정 후 재리뷰 |

### 작업 완료 조건 (전체)

다음 **모든 조건**을 만족해야 완료:

- [ ] 기술 명세서 4개 파일 존재
- [ ] 모든 스모크 테스트 PASS
- [ ] 통합 테스트 PASS
- [ ] 빌드 성공
- [ ] code-reviewer 통과 또는 조건부 통과
- [ ] 최종 리포트 생성 완료
- [ ] 재작업 상한선 미초과

---

## 에이전트 평가 등급

| 등급 | 기준 | 향후 대응 |
|------|------|-----------|
| A | 첫 시도에 성공 | 신뢰도 높음 |
| B | 1회 재작업 후 완료 | 정상 범위 |
| C | 2회 재작업 후 완료 | 프롬프트 개선 필요 |
| D | 3회 재작업 후 완료 | 상세 지시 필수 |
| F | 에스컬레이션 발생 | 근본 원인 분석 필요 |

---

## 커뮤니케이션

- 사용자에게는 **한국어**로 진행 상황 보고
- 에스컬레이션 발생 시 **즉시** 사용자에게 보고
- 모든 리포트는 **한국어**로 작성
- 각 Phase 완료 시 간략한 상태 보고

### 진행 상황 보고 형식

```
✅ Phase 2 완료: 기술 명세서 생성
   - contracts.md ✓
   - shared-types.md ✓
   - conventions.md ✓
   - current-state.md ✓

🔄 Phase 4 진행 중: Frontend 개발
   - StockDetailModal 개발 중...
```

---

## 폴더 구조

```
프로젝트/
├── .agent-context/           # 공유 컨텍스트 (Phase 2에서 생성)
│   ├── contracts.md
│   ├── shared-types.md
│   ├── conventions.md
│   └── current-state.md
├── .agent-results/           # 에이전트 결과물
│   ├── frontend/
│   ├── backend/
│   ├── tester/
│   ├── reviewer/
│   └── docs/
└── output/
    └── reports/              # 최종 리포트
        └── YYYY-MM-DD-task-name/
            └── final-report.md
```

---

## 부록: 병렬 실행 가이드

### 병렬 실행 가능 조건

| 시나리오 | 실행 방식 | 이유 |
|----------|-----------|------|
| Frontend + Backend 리뷰 | 병렬 | 서로 독립적 |
| Frontend 개발 → 테스트 | 순차 | 의존성 있음 |
| Frontend + Backend 개발 | ⚠️ 조건부 | contracts.md 확정 후에만 가능 |

### 병렬 실행 시 주의사항

1. **반드시 Phase 2 완료 후** 병렬 실행
2. 두 에이전트가 **같은 파일 수정 금지**
3. 병렬 실행 후 **통합 테스트 필수**

---

## 체크리스트: 스킬 사용 전 확인

메인 Claude는 이 스킬 사용 전 다음을 확인:

- [ ] 프로젝트 폴더 구조 파악 완료
- [ ] 기존 코드 컨벤션 파악 완료
- [ ] 사용자 요청 명확히 이해
- [ ] 작업 범위 (Frontend/Backend/Full-stack) 결정
- [ ] 예상 복잡도 판단

---

## 버전 히스토리

| 버전 | 날짜 | 변경 내용 |
|------|------|-----------|
| v1.0 | - | 초기 버전 |
| v2.0 | 2025-01-29 | 공유 컨텍스트, 즉시 테스트, 재작업 정책 추가 |
