# Feedback Loops & Rollback Conditions

## 기본 원칙
워터폴은 작동하지 않는다. 모든 Phase는 이전 Phase로 롤백할 수 있다.
단, 무한 루프 방지를 위해 **반복 횟수 제한**이 있다.

## Phase 간 피드백 경로

### 1. CTO → CBO 롤백
```yaml
trigger: "기술적으로 구현 불가능한 핵심 기능 발견"
examples:
  - "이 실시간 동기화 기능은 서버 비용이 월 $500+ 예상"
  - "이 데이터는 API로 접근 불가"
  - "이 규모의 ML 모델은 클라이언트에서 실행 불가"
  
action:
  1. CTO가 기술 제약 보고서 작성 (제약 내용, 대안 2개 이상)
  2. CBO가 Product Brief 수정 (해당 기능 제거 or 대안 채택)
  3. 수정된 Product Brief로 Gate 1 재검증
  
max_iterations: 2
escalation: "2회 초과 시 CEO가 Go/Kill 결정"
```

### 2. CDO ↔ CTO 반복
```yaml
trigger: "디자인이 기술적으로 구현 어려움 or 개발 결과가 디자인과 불일치"
examples:
  - "이 애니메이션은 React Native에서 60fps 유지 불가"
  - "이 레이아웃은 데이터 로딩 상태를 고려하지 않음"

action:
  1. CTO가 구현 제약 구체적으로 명시
  2. CDO가 대안 디자인 제안 (제약 내에서)
  3. 합의 후 Design Delivery 업데이트

max_iterations: 3
escalation: "3회 초과 시 CEO가 현재 버전으로 확정"
```

### 3. CGO → CTO 피드백
```yaml
trigger: "그로스 데이터에서 UX 병목 발견"
examples:
  - "온보딩 Step 3에서 60% 이탈"
  - "결제 플로우 전환율 2% 미만"
  - "특정 화면 로딩 5초+"

action:
  1. CGO가 구체적 화면/플로우 + 데이터 제공
  2. CTO가 해당 화면 개선 (CDO 협업 필요시 CDO 투입)
  3. 개선 후 A/B 테스트로 검증

frequency: "2주마다 정기 리뷰"
```

### 4. CGO → CBO 피벗 트리거
```yaml
trigger: "3개월간 핵심 지표 미달"
criteria:
  - D30_retention < 5% (3개월 연속)
  - activation_rate < 15%
  - LTV:CAC < 1:1
  - organic_growth = 0%

action:
  1. CGO가 Growth Insights 작성 (Gate 6)
  2. CBO가 시장 가정 재검증
  3. CEO가 Pivot/Kill 결정

pivot_options:
  - "같은 문제, 다른 솔루션" → Phase 2로
  - "같은 타겟, 다른 문제" → Phase 1로
  - "완전히 새로운 기회" → Phase 1로 (새 프로젝트)
```

## 반복 추적
```json
// .agent-state/project.json의 iteration_count
{
  "iteration_count": {
    "product_brief_revision": 0,    // max: 2
    "cdo_cto_design_review": 0,     // max: 3
    "user_validation_retry": 0,     // max: 2
    "growth_pivot_review": 0        // max: 1
  }
}
```
