# Agent Company v5.1 — Team Playbook
# Claude Code Agent Teams 연동 가이드

> 기존 32개 에이전트를 Claude Code Agent Teams의 **병렬 실행 구조**에 최적화한 5개 팀 템플릿.
> `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 환경변수가 필요합니다.

---

## Quick Reference

| 팀 | 용도 | 팀원 수 | 예상 시간 | 산출물 |
|----|------|---------|----------|--------|
| **Business Discovery** | 시장 검증 + 사업 계획 | 3 | 30-60분 | product-brief.md |
| **Development** | 설계 + 구현 + 배포 | 3 | 2-8시간 | 코드베이스 + 배포 |
| **Design** | 디자인 시스템 + 에셋 | 3 | 1-2시간 | design-delivery.md |
| **Growth** | 마케팅 + 리텐션 + 분석 | 4 | 1-3시간 | growth-insights.md |
| **Full Pipeline** | 아이디어 → 런칭 전체 | 4 | 4-12시간 | 전체 산출물 |

---

## Team 1: Business Discovery Team (CBO)

### 언제 사용하는가
- 새 아이디어의 시장성 검증
- 경쟁 환경 분석 + BM 설계
- Product Brief 작성 (→ 개발팀 핸드오프)

### 팀 구성

```
Team Lead (Main Session)
├── Role: GTM Strategist — 전체 조율 + Product Brief 최종 작성
├── Context: agents/business/business-agents.md 섹션 5
│
├── Teammate 1: Market Researcher
│   ├── Role: Pain Point Hunter + 데이터 수집
│   ├── Context: agents/business/business-agents.md 섹션 1
│   ├── Task: 도메인의 실제 유저 불만 수집, 최소 5개 PP + 3개 소스
│   └── Output: .agent-state/outputs/pain-points.md
│
├── Teammate 2: Competitive Analyst
│   ├── Role: Competitor Analyst + 포지셔닝
│   ├── Context: agents/business/business-agents.md 섹션 2
│   ├── Task: 경쟁사 5개 분석, feature matrix, 갭 식별
│   ├── Depends On: Teammate 1 (pain-points.md)
│   └── Output: .agent-state/outputs/competitor-analysis.md
│
└── Teammate 3: Business Strategist
    ├── Role: BM Designer + Business Planner
    ├── Context: agents/business/business-agents.md 섹션 3-4
    ├── Task: 비즈니스 모델 설계 + 사업 계획서 통합
    ├── Depends On: Teammate 1 + 2
    └── Output: .agent-state/outputs/business-model.md + business-plan.md
```

### 호출 방법

```
이 프로젝트의 시장성을 검증하는 Business Discovery Team을 만들어주세요.

도메인: [도메인 설명]
가설: [기존 가설이 있다면]

팀 구성:
1. Market Researcher — Reddit, App Store, 포럼에서 실제 유저 불만 수집.
   ~/.claude/agents/business/business-agents.md의 Pain Point Hunter 프롬프트 참고.
   output → .agent-state/outputs/pain-points.md

2. Competitive Analyst — Market Researcher 결과 기반으로 경쟁사 5개 분석.
   ~/.claude/agents/business/business-agents.md의 Competitor Analyst 프롬프트 참고.
   output → .agent-state/outputs/competitor-analysis.md

3. Business Strategist — 위 두 산출물 기반으로 BM + 사업계획서 작성.
   ~/.claude/agents/business/business-agents.md의 BM Designer + Business Planner 프롬프트 참고.
   output → .agent-state/outputs/business-model.md + business-plan.md

Lead(나)는 최종 Product Brief를 작성합니다.
```

### Quality Gate
- Product Brief 검증 (Gate 1): system/quality-gates.md 참조
- 체크리스트: Problem 근거, Persona 구체성, MVP 3개 이내, KPI 2개

---

## Team 2: Development Team (CTO)

### 언제 사용하는가
- Product Brief → 코드 구현
- PRD 작성 + 아키텍처 설계 + 프론트/백엔드 병렬 개발

### 팀 구성

```
Team Lead (Main Session)
├── Role: Architect — PRD 검토 + 아키텍처 설계 + 코드 리뷰 + DevOps
├── Context: agents/development/development-agents.md 섹션 3, 6, 7
│
├── Teammate 1: PRD Writer
│   ├── Role: PRD Architect + Scope Guard
│   ├── Context: agents/development/development-agents.md 섹션 1-2
│   ├── Task: Product Brief → PRD 변환, 스코프 검증
│   └── Output: .agent-state/outputs/prd.md + scope-review.md
│
├── Teammate 2: Frontend Engineer
│   ├── Role: UI 구현
│   ├── Context: agents/development/development-agents.md 섹션 4
│   ├── Task: 모든 화면 구현 (empty/loading/loaded/error)
│   ├── Depends On: Teammate 1 (prd.md) + Lead (architecture.md)
│   ├── Parallel With: Teammate 3
│   └── Verification: npm run build 성공
│
└── Teammate 3: Backend Engineer
    ├── Role: API + DB 구현
    ├── Context: agents/development/development-agents.md 섹션 5
    ├── Task: DB 셋업, API 엔드포인트, 인증, 테스트
    ├── Depends On: Teammate 1 (prd.md) + Lead (architecture.md)
    ├── Parallel With: Teammate 2
    └── Verification: npm test 통과
```

### 호출 방법

```
Product Brief를 기반으로 개발을 시작할 Development Team을 만들어주세요.

Product Brief 위치: .agent-state/outputs/product-brief.md

팀 구성:
1. PRD Writer — Product Brief를 상세 PRD로 변환하고 스코프 검증.
   ~/.claude/agents/development/development-agents.md의 PRD Architect + Scope Guard 참고.
   Tier [N]의 하드 리밋 적용.
   output → .agent-state/outputs/prd.md + scope-review.md

2. Frontend Engineer — PRD와 아키텍처 기반으로 UI 구현.
   ~/.claude/agents/development/development-agents.md의 Frontend Engineer 참고.
   모든 화면의 4가지 상태 (empty/loading/loaded/error) 필수.
   npm run build 성공 필수.

3. Backend Engineer — PRD와 아키텍처 기반으로 API/DB 구현.
   ~/.claude/agents/development/development-agents.md의 Backend Engineer 참고.
   모든 엔드포인트 에러 핸들링, 인증, 테스트 필수.
   npm test 통과 필수.

Lead(나)는 아키텍처 설계 후 PRD Writer 완료 시 Frontend/Backend에 배포.
Frontend + Backend 완료 후 코드 리뷰 + DevOps 수행.
```

### 병렬 실행 포인트
- **Frontend + Backend**: PRD + Architecture + Design Brief 완성 후 동시 시작
- Frontend는 Figma MCP 연결 시 디자인 스펙 직접 참조 가능
- Lead: 두 팀원 완료 후 Code Review → DevOps 순차 실행

### MCP 가용성
| MCP | 사용 에이전트 | 용도 | Fallback |
|-----|-------------|------|----------|
| figma-mcp | Frontend Engineer | 디자인 스펙 참조 | design-delivery.md 텍스트 기반 |

---

## Team 3: Design Team (CDO)

### 언제 사용하는가
- 프로토타입 완성 후 디자인 업그레이드
- 브랜드 아이덴티티 + 비주얼 에셋 생성
- 앱 스토어 에셋 제작

### 팀 구성

```
Team Lead (Main Session)
├── Role: UI Designer — 디자인 감사 + 전체 조율 + Design Delivery
├── Context: agents/design/design-agents.md 섹션 1, 6
│
├── Teammate 1: Brand Director
│   ├── Role: Visual Director + Design-to-Code Bridge
│   ├── Context: agents/design/design-agents.md 섹션 2, 6
│   ├── Task: 컬러/타이포/스페이싱 시스템, 디자인 토큰 코드 변환
│   ├── MCP: figma-mcp (Figma Variables/Styles 생성), stitch-mcp
│   ├── Depends On: Lead (design-audit.md)
│   ├── Parallel With: Teammate 2 (parallel_design 그룹)
│   └── Output: .agent-state/outputs/brand-identity.md + design-delivery.md
│
├── Teammate 2: Asset Creator
│   ├── Role: Image Generator
│   ├── Context: agents/design/design-agents.md 섹션 3
│   ├── Task: 앱 아이콘, 마케팅 이미지, 유틸리티 아이콘 생성
│   ├── MCP: image-gen-server (required), figma-mcp (optional)
│   ├── Parallel With: Teammate 1 (parallel_design 그룹)
│   └── Output: .agent-state/outputs/generated-assets.md + /assets/brand/
│
└── Teammate 3: Store Designer
    ├── Role: Screenshot Designer + ASO Optimizer
    ├── Context: agents/design/design-agents.md 섹션 4-5
    ├── Task: 앱스토어 스크린샷 + ASO 최적화
    ├── MCP: figma-mcp (스크린샷 레이아웃), store-screenshot-mcp, stitch-mcp
    ├── Depends On: Teammate 1 + 2 (parallel_design 완료 후)
    └── Output: .agent-state/outputs/store-screenshots.md + aso-recommendations.md
```

### 호출 방법

```
프로토타입의 디자인을 업그레이드할 Design Team을 만들어주세요.

Design Upgrade Brief: .agent-state/outputs/design-upgrade-brief.md

팀 구성:
1. Brand Director — 브랜드 아이덴티티 수립 + 디자인 토큰 코드 변환.
   ~/.claude/agents/design/design-agents.md의 Visual Director + Design-to-Code Bridge 참고.
   MCP: figma-mcp (Variables/Styles 생성), stitch-mcp.
   WCAG AA 대비율 준수, Google Fonts 사용.
   output → brand-identity.md + design-delivery.md

2. Asset Creator — AI로 앱 아이콘, 배너, 마케팅 이미지 생성.
   ~/.claude/agents/design/design-agents.md의 Image Generator 참고.
   MCP: image-gen-server (required), figma-mcp (optional).
   없으면 Lucide 아이콘 대체.
   output → generated-assets.md + /assets/brand/

3. Store Designer — 앱스토어 스크린샷 4-6장 + ASO 키워드 최적화.
   ~/.claude/agents/design/design-agents.md의 Screenshot Designer + ASO Optimizer 참고.
   MCP: figma-mcp (레이아웃), store-screenshot-mcp, stitch-mcp.
   output → store-screenshots.md + aso-recommendations.md

Lead(나)는 디자인 감사(Design Audit) 수행 후 팀원에게 배포.
Brand Director + Asset Creator는 병렬 실행 (parallel_design 그룹).
Store Designer는 병렬 완료 후 실행.
```

---

### MCP 가용성
| MCP | 사용 에이전트 | 용도 | Fallback |
|-----|-------------|------|----------|
| figma-mcp | Brand Director, Store Designer | Variables/Styles 생성, 레이아웃 | YAML 토큰 / 텍스트 명세 |
| stitch-mcp | Brand Director, Store Designer | AI UI 생성, Figma 내보내기 | 텍스트 기반 디자인 명세 |
| image-gen-server | Asset Creator | AI 이미지 생성 | Lucide/Heroicons |
| store-screenshot-mcp | Store Designer | 스토어 스크린샷 | Figma/Canva 수동 |

---

## Team 4: Growth Team (CGO)

### 언제 사용하는가
- 제품 런칭 후 유저 획득 + 리텐션 전략
- 마케팅 카피 + 광고 캠페인 셋업
- 성장 지표 분석 + Go/No-Go 판단

### 팀 구성

```
Team Lead (Main Session)
├── Role: Acquisition Strategist — 채널 전략 + 전체 조율
├── Context: agents/growth/growth-agents.md 섹션 1
│
├── Teammate 1: Copy & Ads
│   ├── Role: Copy Strategist + Ads Operator
│   ├── Context: agents/growth/growth-agents.md 섹션 7, 2
│   ├── Task: 브랜드 보이스 + 광고 카피 3종 + LP 카피 + 캠페인 셋업
│   ├── Depends On: Lead (acquisition-strategy.md)
│   └── Output: .agent-state/outputs/copy-package.md + campaign-setup.md
│
├── Teammate 2: Content & Community
│   ├── Role: Content Creator
│   ├── Context: agents/growth/growth-agents.md 섹션 3
│   ├── Task: SEO 키워드 + 콘텐츠 캘린더 + 소셜 전략
│   ├── Depends On: Lead (acquisition-strategy.md)
│   ├── Parallel With: Teammate 1
│   └── Output: .agent-state/outputs/content-plan.md
│
├── Teammate 3: User Experience
│   ├── Role: Onboarding Designer + Retention Manager
│   ├── Context: agents/growth/growth-agents.md 섹션 4, 5
│   ├── Task: 온보딩 플로우 + Aha Moment + 리텐션 전략
│   ├── Parallel With: Teammate 1, 2
│   └── Output: .agent-state/outputs/onboarding-design.md + retention-strategy.md
│
└── Teammate 4: Analyst
    ├── Role: Revenue Optimizer + Growth Analyst
    ├── Context: agents/growth/growth-agents.md 섹션 6, 8
    ├── Task: 수익 최적화 + Growth Insights Report + Go/No-Go 판단
    ├── Depends On: Teammate 1, 2, 3 모두 완료 후
    └── Output: .agent-state/outputs/revenue-optimization.md + growth-insights.md
```

### 호출 방법

```
제품 런칭 후 성장 전략을 수립할 Growth Team을 만들어주세요.

Launch Brief: .agent-state/outputs/launch-brief.md

팀 구성:
1. Copy & Ads — 마케팅 카피 전체 + 광고 캠페인 셋업.
   ~/.claude/agents/growth/growth-agents.md의 Copy Strategist + Ads Operator 참고.
   광고 카피 3종 (A/B/C), LP 카피, 이메일 시퀀스 포함.
   output → copy-package.md + campaign-setup.md

2. Content & Community — SEO 기반 콘텐츠 전략 + 소셜 미디어.
   ~/.claude/agents/growth/growth-agents.md의 Content Creator 참고.
   4주 콘텐츠 캘린더, 키워드 10개, 플랫폼별 전략.
   output → content-plan.md

3. User Experience — 온보딩 플로우 + 리텐션 전략.
   ~/.claude/agents/growth/growth-agents.md의 Onboarding Designer + Retention Manager 참고.
   Aha Moment 정의, 3-5스텝 플로우, 이탈 방지 전략.
   output → onboarding-design.md + retention-strategy.md

4. Analyst — 전체 산출물 기반 Growth Insights Report 작성.
   ~/.claude/agents/growth/growth-agents.md의 Revenue Optimizer + Growth Analyst 참고.
   Go/No-Go 판단 포함 (D7>15%, Activation>25%, LTV:CAC>1.5:1).
   output → revenue-optimization.md + growth-insights.md

Lead(나)는 채널 전략 수립 후 Copy&Ads + Content + UX 병렬 배포.
Analyst는 모든 팀원 완료 후 마지막 실행.
```

---

## Team 5: Full Pipeline Team (E2E)

### 언제 사용하는가
- 아이디어 → 런칭까지 전체 파이프라인
- Tier 2+ 프로젝트의 End-to-End 실행

### 팀 구성

```
Team Lead (Main Session)
├── Role: CEO — 프로젝트 초기화 + Tier 판단 + 품질 게이트 + 의사결정
├── Context: agents/ceo.md + system/agent-transitions.yaml
│
├── Teammate 1: CBO Lead
│   ├── Role: 시장 검증 → Product Brief
│   ├── Context: agents/business/business-agents.md 전체
│   ├── Task: Pain Point → Competitor → BM → Plan → Product Brief
│   ├── Phase: 1 (최초 실행)
│   └── Output: .agent-state/outputs/product-brief.md [Gate 1]
│
├── Teammate 2: CTO Lead
│   ├── Role: PRD → 구현 → 배포
│   ├── Context: agents/development/development-agents.md 전체
│   ├── Task: PRD → Scope → Architecture → FE+BE → Review → Deploy
│   ├── Phase: 2 (CBO 완료 + Gate 1 통과 후)
│   └── Output: 코드베이스 + deployment-config.md [Gate 3→CDO]
│
├── Teammate 3: CDO Lead
│   ├── Role: 디자인 시스템 + 비주얼 에셋
│   ├── Context: agents/design/design-agents.md 전체
│   ├── Task: Audit → Brand → Assets → Screenshots → ASO → Bridge
│   ├── Phase: 3 (CTO 프로토타입 완료 + Gate 3 통과 후)
│   └── Output: design-delivery.md + store-assets-package.md [Gate 4]
│
└── Teammate 4: CGO Lead
    ├── Role: 성장 전략 전체
    ├── Context: agents/growth/growth-agents.md 전체
    ├── Task: Acquisition → Copy → Ads+Content → Onboarding → Retention → Revenue → Analysis
    ├── Phase: 4 (Gate 5 Launch Brief 후)
    └── Output: growth-insights.md [Gate 6→CEO Decision]
```

### 호출 방법

```
아이디어를 완전한 제품으로 만들 Full Pipeline Team을 만들어주세요.

아이디어: [아이디어 설명]
Tier: [1-4 또는 '판단해주세요']

팀 구성:
1. CBO Lead — 시장 검증부터 Product Brief까지 전체 CBO 파이프라인.
   ~/.claude/agents/business/business-agents.md 전체 참고.
   Pain Point Hunter → Competitor Analyst → BM Designer → Business Planner → GTM Strategist.
   Gate 1 품질 기준 충족 필수.
   output → product-brief.md

2. CTO Lead — PRD부터 배포까지 전체 CTO 파이프라인.
   ~/.claude/agents/development/development-agents.md 전체 참고.
   CBO Lead 완료 후 시작. PRD → Scope Guard → Architecture → FE+BE(병렬) → Code Review → DevOps.
   npm run build + npm test 통과 필수.
   output → 코드베이스 + deployment-config.md

3. CDO Lead — 디자인 감사부터 에셋 패키지까지 전체 CDO 파이프라인.
   ~/.claude/agents/design/design-agents.md 전체 참고.
   CTO Lead 프로토타입 완료 후 시작.
   output → design-delivery.md + store-assets-package.md

4. CGO Lead — 유저 획득부터 Growth Insights까지 전체 CGO 파이프라인.
   ~/.claude/agents/growth/growth-agents.md 전체 참고.
   Launch Brief 생성 후 시작.
   output → growth-insights.md

Lead(나)는 CEO 역할: Tier 판단, 품질 게이트 검증, Go/No-Go 결정.
실행 순서: CBO → CTO → CDO → CGO (순차, 각 Phase 완료 후 다음 시작).
```

---

## 팀 운영 규칙

### 1. 공유 파일 시스템
```
모든 팀원은 .agent-state/outputs/ 디렉토리를 공유합니다.
산출물 파일이 생성되면 다른 팀원이 읽을 수 있습니다.
```

### 2. 의존성 관리
```yaml
# TaskCreate로 의존성 설정
task_dependencies:
  competitor_analysis:
    blockedBy: [pain_points]
  bm_design:
    blockedBy: [pain_points, competitor_analysis]
  frontend:
    blockedBy: [prd, architecture]
  backend:
    blockedBy: [prd, architecture]
  code_review:
    blockedBy: [frontend, backend]
```

### 3. 품질 게이트 체크포인트
```yaml
gate_1: Product Brief → Lead가 검증 후 CTO 시작
gate_2: PRD → Scope Guard 자동 검증
gate_3: Design Brief → Lead가 검증 + 사용자 승인
gate_4: Design Delivery → Lead가 검증 + 사용자 승인
gate_5: Launch Brief → 자동 생성
gate_6: Growth Insights → Lead가 검증 + Go/No-Go
```

### 4. 에러 핸들링
```yaml
teammate_fail:
  retry: 최대 2회
  escalate: Lead에게 메시지로 보고
  skip: skippable agents만 (visual_director, aso_optimizer 등)

lead_decision:
  proceed_anyway: 현재 산출물로 진행
  manual_fix: 직접 수정
  reassign: 다른 팀원에게 재할당
```

### 5. Teammate 모드 설정
```json
// settings.json에 추가
{
  "teammateMode": "tmux"  // tmux 분할 (권장)
  // 또는 "in-process" // 단일 터미널 (Shift+Up/Down 전환)
}
```

---

## Tier별 추천 팀 구성

| Tier | 추천 팀 | 설명 |
|------|---------|------|
| **1** | 팀 없음 | `quick-builder` 스킬 단독 실행 |
| **2** | Development Team | 간소화된 CBO(스킬) → Development Team → Growth(스킬) |
| **3** | Full Pipeline Team | 전체 파이프라인 순차 실행 |
| **4** | Full Pipeline Team + Sprint | Full Pipeline + 2주 스프린트 반복 |

### Tier 2 추천 흐름
```
1. /business-workflow 스킬로 Product Brief 생성
2. Development Team 생성 (3명)
3. /design-system-workflow 스킬로 디자인
4. /growth-workflow 스킬로 그로스
```

### Tier 3+ 추천 흐름
```
1. Full Pipeline Team 생성 (4명)
2. CEO(Lead)가 순차적으로 각 Phase 관리
3. 각 Phase 내에서는 병렬 실행 활용
```

---

## 참조 파일

| 파일 | 위치 | 용도 |
|------|------|------|
| CBO 에이전트 | `~/.claude/agents/business/business-agents.md` | 비즈니스 5개 에이전트 |
| CTO 에이전트 | `~/.claude/agents/development/development-agents.md` | 개발 7개 에이전트 |
| CDO 에이전트 | `~/.claude/agents/design/design-agents.md` | 디자인 6개 에이전트 |
| CGO 에이전트 | `~/.claude/agents/growth/growth-agents.md` | 그로스 8개 에이전트 |
| CEO 에이전트 | `~/.claude/agents/ceo.md` | 예외 처리 + 의사결정 |
| 전환 규칙 | `~/.claude/system/agent-transitions.yaml` | 상태 머신 |
| 품질 게이트 | `~/.claude/system/quality-gates.md` | 핸드오프 검증 |
| 병렬 그룹 | `~/.claude/system/parallel-groups.yaml` | 병렬 실행 규칙 |
| 핸드오프 템플릿 | `~/.claude/templates/` | 6개 게이트 문서 |
