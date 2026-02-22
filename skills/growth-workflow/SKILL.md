---
name: growth-workflow
description: |
  그로스 워크플로우 스킬 (CGO Division).
  제품 론칭 후 성장 채널 선정, LP 카피 작성, 메트릭 설계까지 실행한다.
  channel-strategist → landing-page-copywriter → growth-metrics-analyst 순서로 진행.

  다음 상황에서 사용:
  - 제품 론칭 후 그로스 전략 수립
  - 마케팅 채널 + LP 카피 + 메트릭 통합 설계
  - Growth Insights Report 생성
---

# Growth Workflow Skill - 그로스 전략 워크플로우

이 스킬은 완성된 제품의 **성장 전략**을 수립하고 실행 가능한 액션 플랜을 생성합니다.

---

## 핵심 원칙

> **"제품 없이 마케팅하지 마라."**

이 워크플로우는 반드시 제품(또는 MVP)이 완성된 후 실행한다.

> **"측정 먼저, 최적화 다음."**

채널을 열기 전에 메트릭 추적 체계부터 잡는다.

---

## 사용 가능한 에이전트

| 에이전트 | 용도 | Tier |
|----------|------|------|
| `channel-strategist` | 성장 채널 선정 + 전략 | 1+ |
| `landing-page-copywriter` | LP 카피 작성 | 1+ |
| `growth-metrics-analyst` | 메트릭 정의 + 분석 | 2+ |

---

## 워크플로우

```
[Launch Brief / 완성된 제품]
    ↓
Phase 1: 채널 전략
    → channel-strategist 실행
    → .growth-workspace/channel-strategy.md 생성
    ↓
Phase 2: LP 카피
    → landing-page-copywriter 실행
    → .growth-workspace/landing-page-copy.md 생성
    ↓
Phase 3: 메트릭 설계 (Tier 2+)
    → growth-metrics-analyst 실행
    → .growth-workspace/metrics-definition.md 생성
    ↓
[실행 & 측정]
    ↓
Phase 4: Growth Insights (반복)
    → growth-metrics-analyst 재실행
    → .project/handoff/growth-insights.md 생성
```

---

## Phase 상세

### Phase 1: 채널 전략

**입력**: Product Brief 또는 제품 설명
**에이전트**: `channel-strategist`
**검증**:
- [ ] 최소 5개 채널 스코어링
- [ ] 주력 채널 1-2개 선정
- [ ] 30일 액션플랜 포함
- [ ] CAC 예측

**Tier 1**: 1개 채널만, 빠른 스코어링

---

### Phase 2: LP 카피

**입력**: channel-strategy.md + Product Brief + pain-points.md (있으면)
**에이전트**: `landing-page-copywriter`
**검증**:
- [ ] 헤드라인 10단어 이내
- [ ] 혜택 중심 (기능 나열 X)
- [ ] CTA 구체적
- [ ] 페인포인트와 메시지 일관성

---

### Phase 3: 메트릭 설계

**입력**: channel-strategy.md + 제품 기능 목록
**에이전트**: `growth-metrics-analyst`
**검증**:
- [ ] AARRR 5단계 메트릭 정의
- [ ] 이벤트 추적 설계
- [ ] North Star Metric 선정
- [ ] 목표값 설정

**Skip 조건**: Tier 1 → 간소화 (Acquisition 메트릭만)

---

### Phase 4: Growth Insights (반복)

**입력**: 실제 운영 데이터 (사용자 제공)
**에이전트**: `growth-metrics-analyst`
**산출물**: Growth Insights Report

이 Phase는 론칭 후 주기적으로 반복:
- Tier 2: 월간
- Tier 3: 격주
- Tier 4: 주간

---

## Tier별 실행 범위

| Phase | Tier 1 | Tier 2 | Tier 3+ |
|-------|--------|--------|---------|
| 1. 채널 전략 | ✅ 1채널 | ✅ 2채널 | ✅ 2-3채널 + 보조 |
| 2. LP 카피 | ✅ Hero만 | ✅ Full LP | ✅ Full + A/B 변형 |
| 3. 메트릭 | ❌ 간소화 | ✅ AARRR 기본 | ✅ Full + 실험 |
| 4. Insights | ❌ - | ✅ 월간 | ✅ 주간 |

---

## 파일 구조

```
.growth-workspace/
├── channel-strategy.md         # Phase 1 결과
├── landing-page-copy.md        # Phase 2 결과
└── metrics-definition.md       # Phase 3 결과

.project/
└── handoff/
    └── growth-insights.md      # Phase 4 결과 (반복 업데이트)
```

---

## 다른 워크플로우와의 연결

**이전**: `supervisor-report-v2` (개발 완료) → Launch Brief → **이 워크플로우**
**이후**: Growth Insights → `business-workflow` (피봇/개선 시)

### 피드백 루프

```
Growth Insights에서 문제 발견 시:
├── 제품 문제 → supervisor-report-v2 (버그/기능 수정)
├── 메시지 문제 → landing-page-copywriter 재실행
├── 채널 문제 → channel-strategist 재실행
└── 시장 문제 → business-workflow 재실행 (피봇)
```

---

## 에스컬레이션

| 상황 | 대응 |
|------|------|
| 채널 성과 부진 | 2주 후 재평가, 채널 교체 검토 |
| CAC 초과 | bm-designer 재실행, 가격/타겟 재검토 |
| 리텐션 낮음 | ux-improvement 워크플로우 연결 |
| 전환율 낮음 | LP 카피 A/B 테스트 확대 |
