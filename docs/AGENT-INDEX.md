# Agent Company v5.1 — 통합 인덱스

> **Last Updated**: 2026-02-22 | **Agents**: 27개 | **Skills**: 10개 | **Gates**: 6개 | **Parallel Groups**: 3개

---

## 빠른 시작

### 새 프로젝트
```
1. workflows/tier-playbooks.md로 Tier(1-4) 판단
2. Tier 1: /quick-builder (단일 스킬)
3. Tier 2: /business-workflow → /prd-workflow-v2 → /supervisor-report-v2 → /growth-workflow
4. Tier 3+: /project-launcher 또는 teams/team-playbook.md 참고하여 Full Pipeline Team 생성
```

### 기존 프로젝트 기능 추가
```
/feature-extension 스킬 실행
```

### 기존 프로젝트 개선
```
/ux-improvement 또는 /refactoring-workflow 실행
```

---

## 조직 구조 (27 Agents)

```
CEO (Exception Handler)
│
├── CBO (Business) ────────── 5 agents
│   Pain Point Hunter → Competitor Analyst → BM Designer
│   → Business Planner → GTM Strategist
│
├── CTO (Development) ─────── 7 agents
│   PRD Architect → Scope Guard → Architect
│   → Frontend Engineer + Backend Engineer (parallel_dev)
│   → Code Reviewer → DevOps
│
├── CDO (Design) ──────────── 6 agents
│   UI Designer → Visual Director + Image Generator (parallel_design)
│   → Screenshot Designer → ASO Optimizer → Design-to-Code Bridge
│
└── CGO (Growth) ──────────── 8 agents
    Acquisition Strategist → Copy Strategist
    → Ads Operator + Content Creator (parallel_growth)
    → Onboarding Designer → Retention Manager → Revenue Optimizer
    → Growth Analyst
```

---

## Tier System

| Tier | 이름 | Agents | Timeline | 진입점 |
|------|------|--------|----------|--------|
| **1** | Quick Experiment | 1 (quick_builder) | 8h | `quick_builder` |
| **2** | Side Project | 15개 | ~70h (2주) | `pain_point_hunter` |
| **3** | Startup MVP | 27개 | ~300h (2개월) | `pain_point_hunter` |
| **4** | Full Product | 27개 + 스프린트 | 6개월+ | `pain_point_hunter` |

> 상세: `workflows/tier-playbooks.md`

---

## 에이전트 목록

### CEO (1 agent)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| CEO (Exception Handler) | `agents/ceo.md` | 에스컬레이션, Go/No-Go, 롤백, 프로젝트 초기화 | All |

### CBO Division — Business (5 agents)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| Pain Point Hunter | `agents/business/business-agents.md` | Reddit/Forum 유저 페인 포인트 발굴 | 1+ |
| Competitor Analyst | `agents/business/business-agents.md` | 경쟁사 분석, 차별화 기회 | 2+ |
| BM Designer | `agents/business/business-agents.md` | 수익 모델, 가격, Unit Economics | 2+ |
| Business Planner | `agents/business/business-agents.md` | 사업 계획서 작성 | 2+ |
| GTM Strategist | `agents/business/business-agents.md` | 시장 진입 전략, Product Brief 작성 | 2+ |

### CTO Division — Development (7 agents)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| PRD Architect | `agents/development/development-agents.md` | PRD 작성, User Story 정의 | 1+ |
| Scope Guard | `agents/development/development-agents.md` | MVP 범위 검증, 피처 크립 방지 | 2+ |
| Architect | `agents/development/development-agents.md` | 기술 아키텍처, API/DB 설계 | 2+ |
| Frontend Engineer | `agents/development/development-agents.md` | UI 구현, React/Next.js | 1+ |
| Backend Engineer | `agents/development/development-agents.md` | API 개발, DB 작업 | 1+ |
| Code Reviewer | `agents/development/development-agents.md` | 코드 품질 관리 | 2+ |
| DevOps | `agents/development/development-agents.md` | CI/CD, 배포, 모니터링 | 2+ |

### CDO Division — Design (6 agents)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| UI Designer | `agents/design/design-agents.md` | 디자인 감사, UI 시스템 | 2+ |
| Visual Director | `agents/design/design-agents.md` | 브랜딩, 비주얼 가이드 | 3+ (skippable) |
| Image Generator | `agents/design/design-agents.md` | AI 이미지/아이콘 생성 | 2+ |
| Screenshot Designer | `agents/design/design-agents.md` | 스토어 스크린샷 | 2+ (skippable) |
| ASO Optimizer | `agents/design/design-agents.md` | 앱스토어 최적화 | 2+ (skippable) |
| Design-to-Code Bridge | `agents/design/design-agents.md` | 디자인 토큰 → 코드 변환 | 2+ (skippable) |

### CGO Division — Growth (8 agents)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| Acquisition Strategist | `agents/growth/growth-agents.md` | 성장 채널 선정, CAC 예측 | 2+ |
| Copy Strategist | `agents/growth/growth-agents.md` | 마케팅 카피, 메시지 전략 | 2+ |
| Ads Operator | `agents/growth/growth-agents.md` | 광고 캠페인 집행 | 3+ (skippable) |
| Content Creator | `agents/growth/growth-agents.md` | 콘텐츠 마케팅 | 2+ |
| Onboarding Designer | `agents/growth/growth-agents.md` | 온보딩 플로우 설계 | 2+ |
| Retention Manager | `agents/growth/growth-agents.md` | 리텐션 전략 | 3+ (skippable) |
| Revenue Optimizer | `agents/growth/growth-agents.md` | 수익 최적화, 가격 전략 | 3+ (skippable) |
| Growth Analyst | `agents/growth/growth-agents.md` | AARRR 메트릭, Growth Insights | 2+ |

---

## 스킬(워크플로우) 목록 (10개)

### Phase 1: Business

| Skill | File | 역할 |
|-------|------|------|
| business-workflow | `skills/business-workflow/SKILL.md` | CBO 사업 검증 오케스트레이션 |

### Phase 2: Development

| Skill | File | 역할 |
|-------|------|------|
| prd-workflow-v2 | `skills/prd-workflow-v2/SKILL.md` | 아이디어 → PRD → 기술명세 |
| project-launcher | `skills/project-launcher/SKILL.md` | PRD → 개발 연결 |
| supervisor-report-v2 | `skills/supervisor-report-v2/SKILL.md` | 개발 오케스트레이션 |
| design-system-workflow | `skills/design-system-workflow/SKILL.md` | 디자인 시스템 구축 |
| context-manager | `skills/context-manager/SKILL.md` | 세션간 컨텍스트 관리 |

### Phase 2.5: Design

| Skill | File | 역할 |
|-------|------|------|
| ux-improvement | `skills/ux-improvement/SKILL.md` | UI/UX 분석/개선 |

### Phase 3: Growth

| Skill | File | 역할 |
|-------|------|------|
| growth-workflow | `skills/growth-workflow/SKILL.md` | 그로스 전략 오케스트레이션 |

### 유지보수

| Skill | File | 역할 |
|-------|------|------|
| feature-extension | `skills/feature-extension/SKILL.md` | 기존 프로젝트 기능 추가 |
| refactoring-workflow | `skills/refactoring-workflow/SKILL.md` | 코드 리팩토링 |

---

## 프로젝트 라이프사이클

```
┌───────────────────────────────────────────────────────────────────┐
│ CEO: Tier 판단 → Phase 관리 → Go/No-Go → 롤백/종료                  │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  PHASE 1: CBO (business-workflow)                                 │
│  ┌──────────────────────────────────────────┐                     │
│  │ pain_point_hunter → competitor_analyst   │                     │
│  │ → bm_designer → business_planner        │                     │
│  │ → gtm_strategist → [Product Brief]      │                     │
│  └──────────────────┬───────────────────────┘                     │
│                      ↓ Gate 1                                     │
│  PHASE 2: CTO                                                     │
│  ┌──────────────────────────────────────────┐                     │
│  │ prd_architect → scope_guard → architect  │                     │
│  │ → parallel_dev (FE + BE)                │                     │
│  │ → code_reviewer → devops                │                     │
│  │                → [Design Upgrade Brief]  │                     │
│  └──────────────────┬───────────────────────┘                     │
│                      ↓ Gate 3                                     │
│  PHASE 2.5: CDO                                                   │
│  ┌──────────────────────────────────────────┐                     │
│  │ ui_designer → parallel_design (VD + IG) │                     │
│  │ → screenshot_designer → aso_optimizer   │                     │
│  │ → design_to_code_bridge                 │                     │
│  │                → [Design Delivery]       │                     │
│  └──────────────────┬───────────────────────┘                     │
│                      ↓ Gate 4 → Gate 5                            │
│  PHASE 3: CGO (growth-workflow)                                   │
│  ┌──────────────────────────────────────────┐                     │
│  │ acquisition_strategist → copy_strategist│                     │
│  │ → parallel_growth (Ads + Content)       │                     │
│  │ → onboarding_designer → retention_mgr   │                     │
│  │ → revenue_optimizer → growth_analyst    │                     │
│  │                → [Growth Insights]       │                     │
│  └──────────────────┬───────────────────────┘                     │
│                      ↓ Gate 6                                     │
│  CEO DECISION: Continue / Iterate / Pivot / Kill                  │
│                                                                   │
│  MAINTENANCE (독립 실행)                                           │
│  ├── feature-extension: 기능 추가                                  │
│  ├── refactoring-workflow: 코드 개선                               │
│  └── ux-improvement: UX 개선                                      │
└───────────────────────────────────────────────────────────────────┘
```

---

## Quality Gates

| Gate | 핸드오프 | 필수 항목 | 실패 시 |
|------|---------|----------|--------|
| **Gate 1** | CBO → CTO | Problem 근거, Persona, MVP 3개, KPI 2개 | GTM 재작성 (max 2) |
| **Gate 2** | CTO 내부 | User Stories 3+, API, DB, 화면 + Scope Guard | PRD 재작성 |
| **Gate 3** | CTO → CDO | 프로토타입, 브랜드 키워드, 플랫폼, 범위, MCP 상태 | 사용자 승인 |
| **Gate 4** | CDO → CTO | 디자인 토큰, 토큰 소스, 컴포넌트, 에셋 | UI Designer 재시작 (max 3) |
| **Gate 5** | CTO → CGO | URL, 기능 설명, 트래킹, 타겟 | 자동 생성 |
| **Gate 6** | CGO → CEO | 메트릭 5개, 채널 비교, 전략 제안 | CEO Decision |

---

## 핸드오프 문서

| 핸드오프 | 발신 | 수신 | 템플릿 |
|----------|------|------|--------|
| Product Brief | CBO | CTO | `templates/product-brief.md` |
| Design Upgrade Brief | CTO | CDO | `templates/design-upgrade-brief.md` |
| Design Delivery | CDO | CTO | `templates/design-delivery.md` |
| Store Assets Package | CDO | CGO | `templates/store-assets-package.md` |
| Launch Brief | CTO | CGO | `templates/launch-brief.md` |
| Growth Insights | CGO | CEO | `templates/growth-insights.md` |

---

## Parallel Groups

| Group | Members | Join 조건 | Timeout |
|-------|---------|----------|---------|
| **parallel_dev** | Frontend + Backend Engineer | 둘 다 완료 | 48h |
| **parallel_design** | Visual Director + Image Generator | 둘 다 완료 | 24h |
| **parallel_growth** | Ads Operator + Content Creator | Content만 (Ads는 비동기) | — |

---

## MCP Integration

| MCP Server | 용도 | 사용 에이전트 | Fallback |
|------------|------|-------------|----------|
| **figma-mcp** | Figma 디자인 읽기/쓰기 | UI Designer, Visual Director, Screenshot Designer, Bridge, Frontend | 텍스트 기반 design-delivery.md |
| **stitch-mcp** | Google Stitch AI UI 생성 | UI Designer, Visual Director, Screenshot Designer, Bridge | 텍스트 기반 디자인 명세 |
| **image-gen-server** | AI 이미지 생성 (Replicate) | Image Generator | Lucide/Heroicons 라이브러리 |
| **store-screenshot-mcp** | 스토어 스크린샷 생성 | Screenshot Designer | Figma/Canva 수동 제작 |

---

## Tier별 활성 에이전트

### Tier 1: Quick Experiment
```
quick_builder (단일 스킬, 8시간)
```

### Tier 2: Side Project (15 agents)
```
CEO
├── CBO (5): Pain Point Hunter, Competitor Analyst, BM Designer, Business Planner, GTM Strategist
├── CTO (5): PRD Architect, Scope Guard, Frontend Engineer, Backend Engineer, Code Reviewer
├── CDO (3): UI Designer, Image Generator, Screenshot Designer
└── CGO (2): Acquisition Strategist, Copy Strategist
```

### Tier 3: Startup MVP (27 agents)
```
전체 에이전트 활성화 (CEO + CBO 5 + CTO 7 + CDO 6 + CGO 8)
```

### Tier 4: Full Product (27 agents + 스프린트)
```
Tier 3 전체 + 2주 스프린트 사이클 + 분기별 CBO 전략 리뷰
```

---

## 파일 구조

```
.claude/
├── agents/                              # 에이전트 정의 (프롬프트 + I/O + 판단 기준)
│   ├── ceo.md                           #   CEO — 예외 처리 + 의사결정
│   ├── business/business-agents.md      #   CBO: 5 agents
│   ├── development/development-agents.md #  CTO: 7 agents
│   ├── design/design-agents.md          #   CDO: 6 agents
│   └── growth/growth-agents.md          #   CGO: 8 agents
│
├── system/                              # OpenClaw 실행 엔진
│   ├── agent-transitions.yaml           #   상태 머신 (trigger → execute → next)
│   ├── parallel-groups.yaml             #   병렬 실행 (시작/합류/에러)
│   ├── quality-gates.md                 #   핸드오프 품질 체크리스트
│   ├── quality-gates-auto.yaml          #   자동 검증 규칙
│   ├── agent-io-map.yaml               #   에이전트 입출력 파일 경로
│   ├── prompt-assembly.yaml             #   프롬프트 변수 → 값 출처 매핑
│   ├── state-mutations.yaml             #   project.json 변경 규칙
│   ├── human-checkpoints.yaml           #   사람 개입 지점 + 재개 조건
│   ├── context-persistence.md           #   .agent-state/ 관리 방법
│   ├── feedback-loops.md                #   피드백 루프 + 롤백 조건
│   └── cost-time-estimates.md           #   비용/시간 추정표
│
├── skills/                              # Claude Code 스킬 (10개)
│   ├── business-workflow/               #   CBO 리서치 워크플로우
│   ├── prd-workflow-v2/                 #   PRD 생성 + 채점
│   ├── supervisor-report-v2/            #   개발 오케스트레이션
│   ├── project-launcher/                #   PRD → 개발 연결
│   ├── design-system-workflow/          #   디자인 시스템 구축
│   ├── ux-improvement/                  #   UI/UX 개선
│   ├── growth-workflow/                 #   그로스 전략
│   ├── feature-extension/               #   기능 추가
│   ├── refactoring-workflow/            #   리팩토링
│   └── context-manager/                 #   세션 컨텍스트 관리
│
├── teams/
│   └── team-playbook.md                 #   5개 팀 템플릿
│
├── templates/                           # 핸드오프 문서 템플릿 (6개)
│   ├── product-brief.md                 #   Gate 1: CBO → CTO
│   ├── design-upgrade-brief.md          #   Gate 3: CTO → CDO
│   ├── design-delivery.md               #   Gate 4: CDO → CTO
│   ├── store-assets-package.md          #   CDO → CGO
│   ├── launch-brief.md                  #   Gate 5: CTO → CGO
│   └── growth-insights.md               #   Gate 6: CGO → CEO
│
├── workflows/                           # 워크플로우 가이드
│   ├── tier-playbooks.md                #   Tier별 실행 플레이북
│   ├── integrated-workflow.md           #   전체 라이프사이클
│   └── user-validation-gate.md          #   유저 검증 프로토콜
│
└── docs/                                # 참조 문서
    ├── README-agent-company.md          #   시스템 상세 설명
    ├── AGENT-INDEX.md                   #   이 문서
    └── agent-skills-index.md            #   스킬 인덱스
```

---

## Agent Count

| Division | Agents | Files |
|----------|--------|-------|
| CEO | 1 | 1 |
| CBO (Business) | 5 | 1 |
| CTO (Development) | 7 | 1 |
| CDO (Design) | 6 | 1 |
| CGO (Growth) | 8 | 1 |
| **Total** | **27** | **5** |

---

## 관련 문서

| 문서 | 위치 | 설명 |
|------|------|------|
| README | `README.md` | 시스템 개요 (Source of Truth) |
| Agent Skills Index | `docs/agent-skills-index.md` | 전체 스킬 파일 인덱스 |
| Tier Playbooks | `workflows/tier-playbooks.md` | Tier별 실행 가이드 |
| Team Playbook | `teams/team-playbook.md` | 5개 팀 템플릿 |
| Integrated Workflow | `workflows/integrated-workflow.md` | 통합 워크플로우 |
