# Quality Gates — 핸드오프 품질 체크리스트

## 원칙
핸드오프 문서가 **최소 수용 기준**을 충족하지 않으면 다음 Phase로 넘어가지 않는다.
각 체크리스트에서 [필수]는 반드시, [권장]은 Tier 3+ 에서 포함.

---

## Gate 1: Product Brief (CBO → CTO)

### 체크리스트
- [필수] Problem: 실제 유저 인용 또는 데이터 근거 포함 (1문장 가설 X)
- [필수] Target User: 구체적 페르소나 (연령, 직업, 행동 패턴)
- [필수] MVP Features: 3개 이내, 각각 "없으면 앱이 아닌" 이유 명시
- [필수] Success Metrics: 측정 가능한 KPI 2개 이상
- [권장] Pain Points: 최소 3개 출처 (Reddit, 리뷰, 포럼 등)
- [권장] Competitor Gap: 경쟁사가 못하는 것 1개 이상
- [권장] Unit Economics 추정: CAC, LTV 대략적 범위

### 최소 수용 기준
필수 4개 모두 충족 + 문서 길이 최소 500자

### 실패 시
CBO에 구체적 부족 항목 명시하여 보완 요청. 최대 2회 반복.

---

## Gate 2: PRD (CTO 내부)

### 체크리스트  
- [필수] User Stories: 최소 3개, As a/I want/So that 형식
- [필수] API 정의: 엔드포인트, 메서드, 입출력 명시
- [필수] DB 스키마: 핵심 테이블, 관계 정의
- [필수] 화면 목록: 각 화면의 목적과 주요 요소
- [권장] 에러 케이스: 핵심 플로우의 실패 시나리오
- [권장] 성능 요구사항: 응답 시간, 동시 접속

### Scope Guard 검증
```yaml
hard_limits:
  tier_1: { features: 1, apis: 3, screens: 2, hours: 8 }
  tier_2: { features: 3, apis: 5, screens: 4, hours: 80 }
  tier_3: { features: 5, apis: 10, screens: 8, hours: 320 }
  tier_4: { features: 10, apis: 20, screens: 15, hours: 640 }

violation_response: "이 기능은 [tier] 범위를 초과합니다. P1으로 분류하여 v1.1에서 구현을 권장합니다."
```

---

## Gate 3: Design Upgrade Brief (CTO → CDO)

### 체크리스트
- [필수] 프로토타입 접근 방법 (URL, 스크린샷, Figma 링크)
- [필수] 브랜드 키워드 3-5개
- [필수] 타겟 플랫폼 (iOS/Android/Web)
- [필수] 요청 범위 (전체 리디자인 / 핵심 화면만 / 아이콘만)
- [필수] MCP 연결 상태 (figma-mcp / stitch-mcp / image-gen-server / 없음)
- [권장] 기술 제약 (애니메이션 한계, 성능 제약)
- [권장] 참고 앱/디자인 레퍼런스
- [권장] Figma 파일 키 (figma-mcp 연결 시)

---

## Gate 4: Design Delivery (CDO → CTO)

### 체크리스트
- [필수] Figma 파일 또는 디자인 스펙 문서
- [필수] 디자인 토큰 (컬러, 타이포, 스페이싱)
- [필수] 토큰 소스 명시 (Figma Variables / Stitch Export / 수동 정의)
- [필수] 컴포넌트 목록 + 상태별 시안 (default, hover, disabled, error)
- [필수] 에셋 파일 경로 (/assets/에 export)
- [권장] 반응형 브레이크포인트
- [권장] 다크 모드 대응
- [권장] MCP 연결 시 Figma Variables/Styles 동기화 검증

---

## Gate 5: Launch Brief (CTO → CGO)

### 체크리스트
- [필수] 제품 접근 URL/스토어 링크
- [필수] 핵심 기능 설명 (마케팅 관점)
- [필수] 트래킹 구현 확인 (GA4/Mixpanel/Firebase 중 최소 1개)
- [필수] 타겟 오디언스 정의
- [권장] 온보딩 플로우 스크린샷
- [권장] 경쟁 우위 요약

---

## Gate 6: Growth Insights (CGO → CEO)

### 체크리스트
- [필수] 최소 2주 데이터 기반
- [필수] 핵심 메트릭 5개 (DAU, Activation, D7 Retention, ARPU, LTV:CAC)
- [필수] 채널별 성과 비교
- [필수] 다음 분기 전략 제안 (구체적 액션 아이템)
- [권장] A/B 테스트 결과
- [권장] 유저 피드백 요약
