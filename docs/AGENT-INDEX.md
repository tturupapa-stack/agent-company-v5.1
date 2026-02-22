# Agent Company v3.0 — 통합 인덱스

> **Last Updated**: 2026-02-09 | **Agent Company**: 55개 에이전트 | **Claude Code Agents**: 22개 | **Skills**: 10개

---

## 빠른 시작

### 새 프로젝트
```
1. project-scaler.md로 Tier(1-4) 판단
2. business-workflow로 사업 검증 (Tier 2+)
3. prd-workflow-v2로 PRD 작성
4. project-launcher → supervisor-report-v2로 개발
5. growth-workflow로 성장 전략
```

### 기존 프로젝트 기능 추가
```
feature-extension 스킬 실행
```

### 기존 프로젝트 개선
```
ux-improvement 또는 refactoring-workflow 실행
```

---

## 조직 구조 (55 Agents)

```
CEO (Orchestrator)
│
├── CBO (Business) ────────── 12 agents
│   ├── Research: Trend Scout, Market Analyzer,
│   │             Competitor Analyst, Pain Point Hunter
│   ├── Strategy: Opportunity Scorer, BM Designer,
│   │             Financial Modeler, GTM Strategist
│   └── Docs: Research Report Writer, Business Plan Writer
│
├── CTO (Development) ─────── 10 agents
│   ├── Product: PRD Architect, Scope Guard
│   ├── Engineering: Architect, Frontend, Backend, Code Reviewer
│   └── Operations: Test Writer, Doc Writer, DevOps
│
└── CGO (Growth) ──────────── 31 agents (Hierarchical)
    ├── Acquisition (11)
    │   ├── Channel Strategist
    │   ├── Paid Ads Lead → Meta/Google/TikTok/Analyzer
    │   └── Organic Lead → SEO/Content/Community/Partnership
    ├── Activation (2): Onboarding Designer, Aha Moment Engineer
    ├── Retention (5): Cohort Analyst, Churn Preventer, Engagement Lead+3
    ├── Revenue (2): Monetization Optimizer, Upsell Strategist
    ├── Referral (2): Viral Loop Designer, Advocacy Builder
    ├── Creative (6): Ad Creative Director, Copy Lead+4
    └── Analytics (2): Growth Metrics Analyst, Growth Strategy Writer
```

---

## Tier System

| Tier | 이름 | Agents | Timeline | 예시 |
|------|------|--------|----------|------|
| **1** | Quick Experiment | 8개 | 1-2주 | 랜딩페이지 검증, 해커톤 |
| **2** | Side Project | 18개 | 1-2개월 | 개인 SaaS, 소규모 수익화 |
| **3** | Startup MVP | 35개 | 2-4개월 | 투자 유치 목표 MVP |
| **4** | Full Product | 55개 | 4개월+ | 대규모 확장 |

> 상세: `docs/project-scaler.md`

---

## Claude Code 실행 에이전트 (22개)

### CBO Division — Business (4 agents)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| pain-point-hunter | `agents/pain-point-hunter.md` | 유저 페인포인트 발굴 | 1+ |
| competitor-analyst | `agents/competitor-analyst.md` | 경쟁사 분석, 차별화 기회 | 2+ |
| bm-designer | `agents/bm-designer.md` | 수익 모델, 가격, Unit Economics | 2+ |
| business-plan-writer | `agents/business-plan-writer.md` | Product Brief 작성 | 2+ |

### CTO Division — Development (14 agents)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| prd-architect | `agents/prd-architect.md` | PRD 작성 | 1+ |
| prd-feedback-expert | `agents/prd-feedback-expert.md` | PRD 채점/피드백 | 2+ |
| tech-spec-converter | `agents/tech-spec-converter.md` | PRD → 기술 명세 변환 | 2+ |
| ui-spec-writer | `agents/ui-spec-writer.md` | FR별 화면 명세 작성 | 2+ |
| design-system-generator | `agents/design-system-generator.md` | 디자인 토큰/컴포넌트 규칙 | 2+ |
| design-polish-agent | `agents/design-polish-agent.md` | 시각적 디테일 보완 | 3+ |
| ux-auditor | `agents/ux-auditor.md` | UI/UX 분석/개선안 | 2+ |
| codebase-analyzer | `agents/codebase-analyzer.md` | 코드베이스 구조 분석 | 2+ |
| frontend-developer | `agents/frontend-developer.md` | 프론트엔드 개발 | 1+ |
| backend-developer | `agents/backend-developer.md` | 백엔드 개발 | 1+ |
| code-reviewer | `agents/code-reviewer.md` | 코드 리뷰 | 2+ |
| test-runner | `agents/test-runner.md` | 테스트 실행 | 2+ |
| refactoring-planner | `agents/refactoring-planner.md` | 리팩토링 계획 | 3+ |
| doc-writer | `agents/doc-writer.md` | 문서 작성 | 2+ |

### CGO Division — Growth (3 agents)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| channel-strategist | `agents/channel-strategist.md` | 성장 채널 선정, CAC 예측 | 1+ |
| landing-page-copywriter | `agents/landing-page-copywriter.md` | LP 카피, CTA | 1+ |
| growth-metrics-analyst | `agents/growth-metrics-analyst.md` | AARRR 메트릭, 대시보드 | 2+ |

### Orchestrator (1 agent)

| Agent | File | 역할 | Tier |
|-------|------|------|------|
| ceo-orchestrator | `agents/ceo-orchestrator.md` | Tier 판단, Phase 관리, 핸드오프 | All |

---

## Agent Company v3 참조 문서 (55개 에이전트)

### CEO

| Agent | File | 핵심 역할 |
|-------|------|----------|
| CEO | `agents/ceo/ceo.md` | 전체 오케스트레이션, Tier 판단, 부서간 조율 |

### CBO Division (12 agents, 4 files)

| Agent | File | Tier |
|-------|------|------|
| Trend Scout | `agents/business/research/research-agents.md` | 3+ |
| Market Analyzer | `agents/business/research/research-agents.md` | 3+ |
| Competitor Analyst | `agents/business/research/research-agents.md` | 2+ |
| Pain Point Hunter | `agents/business/research/research-agents.md` | 1+ |
| Opportunity Scorer | `agents/business/strategy/strategy-agents.md` | 3+ |
| BM Designer | `agents/business/strategy/strategy-agents.md` | 2+ |
| Financial Modeler | `agents/business/strategy/strategy-agents.md` | 3+ |
| GTM Strategist | `agents/business/strategy/strategy-agents.md` | 3+ |
| Research Report Writer | `agents/business/documentation/documentation-agents.md` | 3+ |
| Business Plan Writer | `agents/business/documentation/documentation-agents.md` | 2+ |

### CTO Division (10 agents, 4 files)

| Agent | File | Tier |
|-------|------|------|
| PRD Architect | `agents/development/product/product-agents.md` | 1+ |
| Scope Guard | `agents/development/product/product-agents.md` | 2+ |
| Architect | `agents/development/engineering/engineering-agents.md` | 2+ |
| Frontend Engineer | `agents/development/engineering/engineering-agents.md` | 1+ |
| Backend Engineer | `agents/development/engineering/engineering-agents.md` | 1+ |
| Code Reviewer | `agents/development/engineering/engineering-agents.md` | 2+ |
| Test Writer | `agents/development/operations/operations-agents.md` | 3+ |
| Doc Writer | `agents/development/operations/operations-agents.md` | 2+ |
| DevOps Engineer | `agents/development/operations/operations-agents.md` | 3+ |

### CGO Division (31 agents, 36 files)

#### Acquisition (11 agents)
| Agent | File | Tier |
|-------|------|------|
| Channel Strategist | `agents/growth/acquisition/channel-strategist.md` | 1+ |
| Paid Ads Lead | `agents/growth/acquisition/paid-ads-lead.md` | 2+ |
| Meta Specialist | `agents/growth/acquisition/paid-ads/meta-specialist.md` | 3+ |
| Google Specialist | `agents/growth/acquisition/paid-ads/google-specialist.md` | 3+ |
| TikTok Specialist | `agents/growth/acquisition/paid-ads/tiktok-specialist.md` | 3+ |
| Performance Analyzer | `agents/growth/acquisition/paid-ads/performance-analyzer.md` | 3+ |
| Organic Lead | `agents/growth/acquisition/organic-lead.md` | 2+ |
| SEO Specialist | `agents/growth/acquisition/organic/seo-specialist.md` | 3+ |
| Content Marketer | `agents/growth/acquisition/organic/content-marketer.md` | 3+ |
| Community Manager | `agents/growth/acquisition/organic/community-manager.md` | 3+ |
| Partnership Manager | `agents/growth/acquisition/organic/partnership-manager.md` | 4 |

#### Activation (2 agents)
| Agent | File | Tier |
|-------|------|------|
| Onboarding Designer | `agents/growth/activation/onboarding-designer.md` | 2+ |
| Aha Moment Engineer | `agents/growth/activation/aha-moment-engineer.md` | 3+ |

#### Retention (5 agents)
| Agent | File | Tier |
|-------|------|------|
| Cohort Analyst | `agents/growth/retention/cohort-analyst.md` | 3+ |
| Churn Preventer | `agents/growth/retention/churn-preventer.md` | 4 |
| Engagement Lead | `agents/growth/retention/engagement-lead.md` | 3+ |
| Notification Specialist | `agents/growth/retention/engagement/notification-specialist.md` | 4 |
| Email Marketing Specialist | `agents/growth/retention/engagement/email-marketing-specialist.md` | 4 |
| Gamification Designer | `agents/growth/retention/engagement/gamification-designer.md` | 4 |

#### Revenue (2 agents)
| Agent | File | Tier |
|-------|------|------|
| Monetization Optimizer | `agents/growth/revenue/monetization-optimizer.md` | 3+ |
| Upsell Strategist | `agents/growth/revenue/upsell-strategist.md` | 4 |

#### Referral (2 agents)
| Agent | File | Tier |
|-------|------|------|
| Viral Loop Designer | `agents/growth/referral/viral-loop-designer.md` | 4 |
| Advocacy Builder | `agents/growth/referral/advocacy-builder.md` | 4 |

#### Creative (6 agents)
| Agent | File | Tier |
|-------|------|------|
| Ad Creative Director | `agents/growth/creative/ad-creative-director.md` | 4 |
| Copy Lead | `agents/growth/creative/copy-lead.md` | 2+ |
| Ad Copywriter | `agents/growth/creative/copy/ad-copywriter.md` | 3+ |
| Email Copywriter | `agents/growth/creative/copy/email-copywriter.md` | 3+ |
| Landing Page Copywriter | `agents/growth/creative/copy/landing-page-copywriter.md` | 1+ |
| Microcopy Writer | `agents/growth/creative/copy/microcopy-writer.md` | 4 |

#### Analytics (2 agents)
| Agent | File | Tier |
|-------|------|------|
| Growth Metrics Analyst | `agents/growth/analytics/growth-metrics-analyst.md` | 2+ |
| Growth Strategy Writer | `agents/growth/analytics/growth-strategy-writer.md` | 3+ |

---

## 스킬(워크플로우) 목록 (10개)

### Phase 1: Business

| Skill | File | 역할 |
|-------|------|------|
| business-workflow | `skills/business-workflow/SKILL.md` | 사업 검증 오케스트레이션 |

### Phase 2: Development

| Skill | File | 역할 |
|-------|------|------|
| prd-workflow-v2 | `skills/prd-workflow-v2/SKILL.md` | 아이디어 → PRD → 기술명세 |
| project-launcher | `skills/project-launcher/SKILL.md` | PRD → 개발 연결 |
| supervisor-report-v2 | `skills/supervisor-report-v2/SKILL.md` | 개발 오케스트레이션 |
| design-system-workflow | `skills/design-system-workflow/SKILL.md` | 디자인 시스템 구축 |
| context-manager | `skills/context-manager/SKILL.md` | 세션간 컨텍스트 관리 |

### Phase 3: Growth

| Skill | File | 역할 |
|-------|------|------|
| growth-workflow | `skills/growth-workflow/SKILL.md` | 그로스 전략 오케스트레이션 |

### 유지보수

| Skill | File | 역할 |
|-------|------|------|
| feature-extension | `skills/feature-extension/SKILL.md` | 기존 프로젝트 기능 추가 |
| refactoring-workflow | `skills/refactoring-workflow/SKILL.md` | 코드 리팩토링 |
| ux-improvement | `skills/ux-improvement/SKILL.md` | UX 분석/개선 |

---

## 프로젝트 라이프사이클

```
┌──────────────────────────────────────────────────────────────┐
│ CEO: Tier 판단 → 에이전트 선발 → Phase 관리                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PHASE 1: BUSINESS (business-workflow)                       │
│  ┌────────────────────────────────────────┐                  │
│  │ pain-point-hunter → competitor-analyst │                  │
│  │ → bm-designer → business-plan-writer  │                  │
│  │                → [Product Brief]       │                  │
│  └───────────────────┬────────────────────┘                  │
│                       ↓                                      │
│  PHASE 2: DEVELOPMENT                                        │
│  ┌────────────────────────────────────────┐                  │
│  │ prd-workflow-v2 → project-launcher     │                  │
│  │ → design-system-workflow (선택)         │                  │
│  │ → supervisor-report-v2                 │                  │
│  │   (frontend + backend + test + review) │                  │
│  │                → [Launch Brief]        │                  │
│  └───────────────────┬────────────────────┘                  │
│                       ↓                                      │
│  PHASE 3: GROWTH (growth-workflow)                           │
│  ┌────────────────────────────────────────┐                  │
│  │ channel-strategist                     │                  │
│  │ → landing-page-copywriter              │                  │
│  │ → growth-metrics-analyst               │                  │
│  │                → [Growth Insights]     │                  │
│  └───────────────────┬────────────────────┘                  │
│                       ↓                                      │
│  FEEDBACK → PHASE 1 (피봇/개선 시)                             │
│                                                              │
│  MAINTENANCE (독립 실행)                                      │
│  ├── feature-extension: 기능 추가                             │
│  ├── refactoring-workflow: 코드 개선                          │
│  └── ux-improvement: UX 개선                                 │
└──────────────────────────────────────────────────────────────┘
```

---

## 핸드오프 문서

| 핸드오프 | 발신 | 수신 | 템플릿 |
|----------|------|------|--------|
| Product Brief | CBO | CTO | `templates/handoff/product-brief-template.md` |
| Launch Brief | CTO | CGO | `templates/handoff/launch-brief-template.md` |
| Growth Insights | CGO | CBO | `templates/handoff/growth-insights-template.md` |
| Lite (Tier 1-2) | All | All | `templates/handoff/lite-templates.md` |

---

## 파일 구조

```
.claude/
├── agents/                              # 에이전트 프롬프트 + v3 참조
│   ├── *.md                             # Claude Code 실행 에이전트 (22개 flat)
│   ├── ceo/ceo.md                       # v3 CEO 참조
│   ├── business/                        # v3 CBO Division (12 agents)
│   │   ├── cbo.md
│   │   ├── research/research-agents.md
│   │   ├── strategy/strategy-agents.md
│   │   └── documentation/documentation-agents.md
│   ├── development/                     # v3 CTO Division (10 agents)
│   │   ├── cto.md
│   │   ├── product/product-agents.md
│   │   ├── engineering/engineering-agents.md
│   │   └── operations/operations-agents.md
│   └── growth/                          # v3 CGO Division (31 agents)
│       ├── cgo.md
│       ├── acquisition/                 # 11 agents
│       ├── activation/                  # 2 agents
│       ├── retention/                   # 5 agents
│       ├── revenue/                     # 2 agents
│       ├── referral/                    # 2 agents
│       ├── creative/                    # 6 agents
│       └── analytics/                   # 2 agents
│
├── skills/                              # 스킬 워크플로우 (10개)
│   ├── business-workflow/SKILL.md
│   ├── prd-workflow-v2/SKILL.md
│   ├── project-launcher/SKILL.md
│   ├── supervisor-report-v2/SKILL.md
│   ├── design-system-workflow/SKILL.md
│   ├── context-manager/SKILL.md
│   ├── growth-workflow/SKILL.md
│   ├── feature-extension/SKILL.md
│   ├── refactoring-workflow/SKILL.md
│   └── ux-improvement/SKILL.md
│
├── docs/                                # 참조 문서
│   ├── AGENT-INDEX.md                   # 이 문서
│   ├── README-agent-company.md          # Agent Company v3 README
│   ├── agent-skills-index.md            # 전체 스킬 파일 인덱스
│   ├── project-scaler.md                # Tier 판단 시스템
│   ├── integrated-workflow.md           # 통합 워크플로우
│   └── growth-team-workflow.md          # CGO 상세 AARRR 가이드
│
├── templates/                           # 핸드오프 템플릿
│   └── handoff/
│       ├── product-brief-template.md    # CBO → CTO
│       ├── launch-brief-template.md     # CTO → CGO
│       ├── growth-insights-template.md  # CGO → CEO
│       └── lite-templates.md            # Tier 1-2용 간소화
│
└── context/                             # 공유 컨텍스트
    └── SCHEMA.md                        # 컨텍스트 스키마 정의
```

---

## Agent Company 55개 → Claude Code 22개 매핑

| Agent Company Role | Claude Code Agent | 비고 |
|--------------------|-------------------|------|
| **CEO** | ceo-orchestrator | Orchestrator |
| **CBO Division** | | |
| Pain Point Hunter | pain-point-hunter | Business |
| Trend Scout | pain-point-hunter (통합) | 트렌드 스캔 포함 |
| Market Analyzer | bm-designer (통합) | TAM/SAM 포함 |
| Competitor Analyst | competitor-analyst | Business |
| Opportunity Scorer | ceo-orchestrator (통합) | Tier 판단 포함 |
| BM Designer | bm-designer | Business |
| Financial Modeler | bm-designer (통합) | Unit Economics 포함 |
| GTM Strategist | channel-strategist (통합) | GTM = 채널 전략 |
| Research Report Writer | business-plan-writer (통합) | 리서치 결과 정리 |
| Business Plan Writer | business-plan-writer | Business |
| **CTO Division** | | |
| PRD Architect | prd-architect | Development |
| Scope Guard | prd-feedback-expert | PRD 검증 |
| Architect | tech-spec-converter | 기술 명세 |
| Frontend Engineer | frontend-developer | Development |
| Backend Engineer | backend-developer | Development |
| Code Reviewer | code-reviewer | Development |
| Test Writer | test-runner | Development |
| Doc Writer | doc-writer | Development |
| DevOps Engineer | - | 수동 배포 |
| **CGO Division** | | |
| Channel Strategist | channel-strategist | Growth |
| Paid Ads Lead/Manager | - | 외부 플랫폼 |
| Organic Lead/Hacker | channel-strategist (통합) | 오가닉 전략 포함 |
| Onboarding Designer | ux-auditor (부분) | 온보딩 UX |
| Aha Moment Engineer | growth-metrics-analyst (부분) | Activation 메트릭 |
| Cohort Analyst | growth-metrics-analyst (통합) | 리텐션 분석 |
| Copy Lead/Copywriter | landing-page-copywriter | LP 카피 |
| Growth Metrics Analyst | growth-metrics-analyst | Growth |
| Growth Strategy Writer | growth-metrics-analyst (통합) | Insights Report |

---

## Tier별 활성 에이전트

### Tier 1: Quick Experiment (8 agents)
```
CEO (lite)
├── CBO: Pain Point Hunter
├── CTO: PRD Architect (lite), Frontend Engineer, Backend Engineer
└── CGO: Channel Strategist (lite), Landing Page Copywriter
```

### Tier 2: Side Project (18 agents)
```
CEO
├── CBO: Pain Point Hunter, Competitor Analyst, BM Designer, Business Plan Writer
├── CTO: PRD Architect, Scope Guard, Architect, Frontend, Backend, Code Reviewer, Doc Writer
└── CGO: Channel Strategist, Paid Ads Lead (solo), Organic Lead (solo),
         Onboarding Designer, Copy Lead (solo), Growth Metrics Analyst
```

### Tier 3: Startup MVP (35 agents)
```
전체 CBO + 전체 CTO + CGO (Referral 제외, Specialist 선택적)
```

### Tier 4: Full Product (55 agents)
```
모든 에이전트 활성화
```

---

## 관련 문서

| 문서 | 위치 | 설명 |
|------|------|------|
| Project Scaler | `docs/project-scaler.md` | Tier 판단 + 에이전트 선택 |
| Agent Skills Index | `docs/agent-skills-index.md` | 전체 스킬 파일 인덱스 |
| Integrated Workflow | `docs/integrated-workflow.md` | 통합 워크플로우 |
| Growth Team Workflow | `docs/growth-team-workflow.md` | CGO 상세 AARRR |
| Context Schema | `context/SCHEMA.md` | 공유 컨텍스트 구조 |
