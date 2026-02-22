# User Validation Gate

## 목적
실제 사용자에게 제품을 써보게 하고, 핵심 지표를 검증한다.
Phase 2.5(디자인) 이후, Phase 3(그로스) 이전에 실행.

## 대상
- 최소 5명 (타겟 페르소나 일치)
- 이상적: 8-10명

## 프로토콜

### Step 1: 준비 (2시간)
```
- 테스트 시나리오 3개 작성 (핵심 유저 플로우)
- 각 시나리오의 성공 기준 정의
- 기록 방법 준비 (화면 녹화 or 관찰 노트)
```

### Step 2: 실행 (1인당 20분)
```
- [5분] 제품 소개 없이 랜딩페이지 보여주기 → "이게 뭐하는 앱인지 설명해주세요"
- [10분] 시나리오 3개 수행 요청 → 관찰 (도움 X)
- [5분] 질문: "가장 좋았던 점? 가장 불편한 점? 돈 내고 쓸 의향?"
```

### Step 3: 분석
```yaml
results:
  task_completion_rate: "X/15 (5명 × 3 시나리오)"
  core_value_understanding: "5명 중 X명이 정확히 설명"
  nps_average: "1-10 (추천 의향)"
  top_pain_points: ["불편한 점1", "불편한 점2"]
  top_positives: ["좋은 점1"]
  willingness_to_pay: "5명 중 X명"
```

### Step 4: 판정
```yaml
pass_criteria:
  task_completion: ">= 70% (11/15 이상)"
  core_value_understanding: ">= 80% (4/5명)"
  nps_average: ">= 7"

result:
  all_pass: "Phase 3 진행"
  minor_fail: "CDO+CTO 수정 후 재테스트 (max 2회)"
  major_fail: "Phase 1 재검토 (핵심 가정 틀림)"
```
