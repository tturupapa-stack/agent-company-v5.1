---
name: business-workflow
description: |
  비즈니스 리서치 워크플로우 스킬 (CBO Division).
  아이디어를 체계적으로 검증하고 Product Brief를 생성한다.
  pain-point-hunter → competitor-analyst → bm-designer → business-plan-writer 순서로 진행.

  다음 상황에서 사용:
  - 새 아이디어/프로젝트의 사업성 검토
  - Product Brief 생성 (→ 개발팀 핸드오프)
  - 시장 리서치 + 경쟁 분석 + BM 설계 통합 실행
---

# Business Workflow Skill - 사업 검증 워크플로우

이 스킬은 사용자의 아이디어를 체계적으로 검증하고, 개발팀에 전달할 **Product Brief**를 생성합니다.

---

## 핵심 원칙

> **"만들기 전에 확인하라."**

코드 한 줄 쓰기 전에 시장, 경쟁, 수익 구조를 검증한다.

> **"Tier에 맞게 깊이를 조절하라."**

Tier 1은 30분, Tier 2는 반나절, Tier 3+는 며칠이 걸릴 수 있다.

---

## 사용 가능한 에이전트

| 에이전트 | 용도 | Tier |
|----------|------|------|
| `pain-point-hunter` | 유저 페인포인트 발굴 | 1+ |
| `competitor-analyst` | 경쟁사 분석 | 2+ |
| `bm-designer` | 비즈니스 모델 설계 | 2+ |
| `business-plan-writer` | Product Brief 작성 | 2+ |

---

## 워크플로우

```
[사용자 아이디어]
    ↓
Phase 1: 페인포인트 리서치
    → pain-point-hunter 실행
    → .business-workspace/pain-points.md 생성
    ↓
Phase 2: 경쟁 분석 (Tier 2+)
    → competitor-analyst 실행
    → .business-workspace/competitor-analysis.md 생성
    ↓
Phase 3: BM 설계 (Tier 2+)
    → bm-designer 실행
    → .business-workspace/business-model.md 생성
    ↓
Phase 4: Product Brief 작성
    → business-plan-writer 실행
    → .project/handoff/product-brief.md 생성
    ↓
[사용자 검토 & 승인]
    ↓
[→ prd-workflow-v2 또는 project-launcher로 이어짐]
```

---

## Phase 상세

### Phase 1: 페인포인트 리서치

**입력**: 사용자 아이디어 (자연어)
**에이전트**: `pain-point-hunter`
**검증**:
- [ ] 최소 5개 페인포인트 도출
- [ ] 각 페인포인트에 유저 원문 포함
- [ ] 우선순위 점수 부여

**실패 시**: 페인포인트가 3개 미만이면 → 사용자에게 도메인 재확인 요청

---

### Phase 2: 경쟁 분석

**입력**: pain-points.md + 사용자 아이디어
**에이전트**: `competitor-analyst`
**검증**:
- [ ] 직접 경쟁사 최소 3개
- [ ] 기능 비교 매트릭스
- [ ] 차별화 포인트 도출

**Skip 조건**: Tier 1 → 이 Phase 건너뜀

---

### Phase 3: BM 설계

**입력**: pain-points.md + competitor-analysis.md
**에이전트**: `bm-designer`
**검증**:
- [ ] 수익 모델 선택 + 근거
- [ ] 가격 티어 설계
- [ ] Unit Economics (LTV:CAC >3:1)

**Skip 조건**: Tier 1 → 이 Phase 건너뜀

---

### Phase 4: Product Brief 작성

**입력**: 이전 Phase 전체 결과물
**에이전트**: `business-plan-writer`
**검증**:
- [ ] Tier에 맞는 문서 길이
- [ ] 문제-솔루션 연결 명확
- [ ] MVP 범위 구체적
- [ ] 성공 지표 측정 가능

---

## Tier별 실행 범위

| Phase | Tier 1 | Tier 2 | Tier 3+ |
|-------|--------|--------|---------|
| 1. 페인포인트 | ✅ 빠른 스캔 | ✅ 표준 | ✅ 심층 |
| 2. 경쟁 분석 | ❌ Skip | ✅ Lite | ✅ Full |
| 3. BM 설계 | ❌ Skip | ✅ 기본 | ✅ Full |
| 4. Product Brief | ✅ 1페이지 | ✅ 3-5페이지 | ✅ Full |

---

## 파일 구조

```
.business-workspace/
├── pain-points.md              # Phase 1 결과
├── pain-points-summary.md      # Tier 1 간소화 버전
├── competitor-analysis.md      # Phase 2 결과
└── business-model.md           # Phase 3 결과

.project/
└── handoff/
    └── product-brief.md        # Phase 4 최종 산출물
```

---

## 다음 단계 연결

Product Brief 승인 후:
- **개발 시작**: `prd-workflow-v2` → `project-launcher` → `supervisor-report-v2`
- **추가 검증**: 사용자에게 피드백 요청 후 business-workflow 재실행

---

## 에스컬레이션

| 상황 | 대응 |
|------|------|
| 페인포인트 부족 | 사용자에게 도메인/타겟 재확인 |
| 경쟁사 과다 | 직접 경쟁 3개로 좁혀서 분석 |
| BM 불확실 | 2-3개 모델 병렬 제시, 사용자 선택 |
| Tier 불일치 | CEO orchestrator에게 Tier 재평가 요청 |
