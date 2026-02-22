# Agent Company v3.0
## AI 에이전트 조직 시스템

> 55개 AI 에이전트로 구성된 가상 회사.
> 아이디어 발굴(CBO) → 제품 개발(CTO) → 성장(CGO)까지 전 과정을 오케스트레이션.

---

## 🚀 Quick Start

### 1️⃣ 프로젝트 규모 결정
```
📄 /docs/project-scaler.md
```
6개 질문으로 Tier(1~4) 판단 → 필요한 에이전트만 활성화

### 2️⃣ 에이전트 파일 찾기
```
📄 /docs/agent-skills-index.md
```
전체 에이전트의 파일 위치, 역할, Tier별 매핑 인덱스

### 3️⃣ 워크플로우 실행
```
📄 /docs/integrated-workflow.md
```
Phase별 실행 순서, 핸드오프 프로토콜

---

## 📊 Tier System

| Tier | 이름 | Agents | Timeline | 예시 |
|------|------|--------|----------|------|
| **1** | Quick Experiment | 8개 | 1-2주 | 랜딩페이지 검증, 해커톤 |
| **2** | Side Project | 18개 | 1-2개월 | 개인 SaaS, 소규모 수익화 |
| **3** | Startup MVP | 35개 | 2-4개월 | 투자 유치 목표 MVP |
| **4** | Full Product | 55개 | 4개월+ | 대규모 확장 |

---

## 🏢 Organization Structure

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
    ├── Activation (2)
    │   ├── Onboarding Designer
    │   └── Aha Moment Engineer
    ├── Retention (5)
    │   ├── Cohort Analyst, Churn Preventer
    │   └── Engagement Lead → Notification/Email/Gamification
    ├── Revenue (2)
    │   ├── Monetization Optimizer
    │   └── Upsell Strategist
    ├── Referral (2)
    │   ├── Viral Loop Designer
    │   └── Advocacy Builder
    ├── Creative (6)
    │   ├── Ad Creative Director
    │   └── Copy Lead → Ad/Email/LP/Microcopy
    └── Analytics (2)
        ├── Growth Metrics Analyst
        └── Growth Strategy Writer
```

---

## 🔧 Claude Code Skills (7개)

실제 개발 실행을 위한 워크플로우 스킬:

| Skill | 위치 | 용도 |
|-------|------|------|
| **prd-workflow-v2** | `/skills/prd-workflow-v2.md` | 아이디어 → PRD → 기술 명세 |
| **project-launcher** | `/skills/project-launcher.md` | PRD → 개발 시작 연결 |
| **supervisor-report-v2** | `/skills/supervisor-report-v2.md` | 개발 오케스트레이션 |
| **context-manager** | `/skills/context-manager.md` | 세션간 컨텍스트 관리 |
| **feature-extension** | `/skills/feature-extension.md` | 기존 프로젝트 기능 추가 |
| **refactoring-workflow** | `/skills/refactoring-workflow.md` | 코드 구조 개선 |

### Skills 사용 흐름

```
[아이디어]
    ↓
prd-workflow-v2    → PRD + 기술 명세 생성
    ↓
project-launcher   → 개발 계획 + 시작
    ↓
supervisor-report-v2 → 실제 개발
    ↓
[기능 추가 시] feature-extension
[리팩토링 시] refactoring-workflow
```

---

## 📁 File Structure

```
agent-company/
├── README.md                           # ⭐ 시작점 (이 파일)
│
├── /docs                               # 📚 가이드 문서
│   ├── project-scaler.md               # Tier 판단 시스템
│   ├── agent-skills-index.md           # 에이전트 파일 인덱스
│   ├── integrated-workflow.md          # 통합 워크플로우
│   └── growth-team-workflow.md         # CGO 상세 가이드
│
├── /skills                             # 🛠️ Claude Code 워크플로우 스킬
│   ├── prd-workflow-v2.md              # PRD 생성
│   ├── project-launcher.md             # 개발 시작
│   ├── supervisor-report-v2.md         # 개발 오케스트레이션
│   ├── context-manager.md              # 컨텍스트 관리
│   ├── feature-extension.md            # 기능 추가
│   └── refactoring-workflow.md         # 리팩토링
│
├── /agents                             # 🤖 에이전트 스킬 파일
│   ├── /ceo/ceo.md
│   ├── /business                       # CBO Division
│   │   ├── cbo.md
│   │   ├── /research/research-agents.md
│   │   ├── /strategy/strategy-agents.md
│   │   └── /documentation/documentation-agents.md
│   ├── /development                    # CTO Division
│   │   ├── cto.md
│   │   ├── /product/product-agents.md
│   │   ├── /engineering/engineering-agents.md
│   │   └── /operations/operations-agents.md
│   └── /growth                         # CGO Division
│       ├── cgo.md
│       ├── /acquisition
│       │   ├── channel-strategist.md
│       │   ├── paid-ads-lead.md
│       │   ├── /paid-ads/*.md          # 4 specialists
│       │   ├── organic-lead.md
│       │   └── /organic/*.md           # 4 specialists
│       ├── /activation/*.md            # 2 agents
│       ├── /retention
│       │   ├── *.md                    # 3 direct agents
│       │   └── /engagement/*.md        # 3 specialists
│       ├── /revenue/*.md               # 2 agents
│       ├── /referral/*.md              # 2 agents
│       ├── /creative
│       │   ├── ad-creative-director.md
│       │   ├── copy-lead.md
│       │   └── /copy/*.md              # 4 specialists
│       └── /analytics/*.md             # 2 agents
│
├── /templates                          # 📝 핸드오프 템플릿
│   └── /handoff
│       ├── product-brief-template.md   # CBO → CTO
│       ├── launch-brief-template.md    # CTO → CGO
│       ├── growth-insights-template.md # CGO → CEO
│       └── lite-templates.md           # Tier 1-2용 간소화
│
└── /context                            # 💾 공유 컨텍스트
    └── SCHEMA.md                       # 컨텍스트 스키마 정의
```

---

## 🔄 Workflow Pipeline

```
[Phase 1: Business]
CBO: Trend → Pain Point → Market → Competitor → Strategy → Business Plan
     └─────────────────────────────────────────────────────→ Product Brief

[Phase 2: Development]
CTO: PRD → Architecture → Frontend + Backend → Test → Deploy
     └──────────────────────────────────────────────────────→ Launch Brief

[Phase 3: Growth]  
CGO: Strategy → Acquisition → Activation → Retention → Revenue → Referral
     └──────────────────────────────────────────────────→ Growth Insights
                                                              ↓
                                                         [Feedback to CBO]
```

---

## 📋 Handoff Documents

| 핸드오프 | 발신 | 수신 | 템플릿 |
|----------|------|------|--------|
| Product Brief | CBO | CTO | `/templates/handoff/product-brief-template.md` |
| Launch Brief | CTO | CGO | `/templates/handoff/launch-brief-template.md` |
| Growth Insights | CGO | CBO | `/templates/handoff/growth-insights-template.md` |

**Tier 1-2용 간소화 템플릿**: `/templates/handoff/lite-templates.md`

---

## 🎯 Tier별 핵심 스킬 파일

### Tier 1 (8 agents)
```
/agents/business/research/research-agents.md     → Pain Point Hunter
/agents/development/product/product-agents.md    → PRD Architect (lite)
/agents/development/engineering/engineering-agents.md → Frontend, Backend
/agents/growth/acquisition/channel-strategist.md
/agents/growth/creative/copy/landing-page-copywriter.md
```

### Tier 2 추가 (+10 agents)
```
/agents/business/strategy/strategy-agents.md     → BM Designer
/agents/development/product/product-agents.md    → Scope Guard
/agents/growth/acquisition/paid-ads-lead.md      (solo mode)
/agents/growth/acquisition/organic-lead.md       (solo mode)
/agents/growth/creative/copy-lead.md             (solo mode)
/agents/growth/analytics/growth-metrics-analyst.md
```

### Tier 3 추가 (+17 agents)
```
/agents/growth/acquisition/paid-ads/meta-specialist.md
/agents/growth/acquisition/paid-ads/google-specialist.md
/agents/growth/acquisition/organic/seo-specialist.md
/agents/growth/creative/copy/ad-copywriter.md
/agents/growth/activation/aha-moment-engineer.md
/agents/growth/retention/cohort-analyst.md
... (선택적 활성화)
```

### Tier 4 (Full)
```
모든 /agents/**/*.md 파일 활성화
```

---

## 📊 Agent Count

| Division | Agents | Files |
|----------|--------|-------|
| CEO | 1 | 1 |
| CBO (Business) | 12 | 4 |
| CTO (Development) | 10 | 4 |
| CGO (Growth) | 31 | 36 |
| **Total** | **55** | **45** |

> 일부 Division은 여러 에이전트가 하나의 파일에 포함됨 (예: research-agents.md에 4개 에이전트)

---

## 📖 Related Documents

| 문서 | 설명 |
|------|------|
| [Project Scaler](docs/project-scaler.md) | Tier 판단 + 에이전트 선택 가이드 |
| [Agent Skills Index](docs/agent-skills-index.md) | 전체 스킬 파일 인덱스 |
| [Integrated Workflow](docs/integrated-workflow.md) | 통합 워크플로우 가이드 |
| [Growth Team Workflow](docs/growth-team-workflow.md) | CGO 상세 AARRR 가이드 |
| [Context Schema](context/SCHEMA.md) | 공유 컨텍스트 구조 |

---

## 🔧 Usage

### Claude Code에서 사용
```bash
# 프로젝트 폴더에 agent-company 복사
cp -r agent-company /your-project/

# CLAUDE.md에서 참조
# "See /agent-company/docs/project-scaler.md for tier assessment"
```

### 단독 사용
1. `project-scaler.md`로 Tier 판단
2. `agent-skills-index.md`에서 필요한 에이전트 파일 확인
3. 해당 에이전트의 프롬프트 템플릿 사용
4. `integrated-workflow.md`의 순서대로 진행

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0 | 2024-02 | Project Scaler, Tier 시스템, Skills Index 추가 |
| 2.0 | 2024-02 | CGO 계층 구조화, 핸드오프 프로토콜 |
| 1.0 | 2024-02 | 초기 버전 (CBO, CTO, CGO 기본 구조) |
