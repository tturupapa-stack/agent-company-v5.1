# Agent Company - Integrated Workflow Guide

## Overview

이 문서는 AI 에이전트 회사의 전체 운영 워크플로우를 정의합니다.
세 개의 핵심 부서(CBO, CTO, CGO)가 협업하여 아이디어에서 성장까지 전 과정을 담당합니다.

> ⚠️ **중요**: 모든 프로젝트가 55개 에이전트를 필요로 하지 않습니다.
> 프로젝트 시작 전 **Project Scaler** (`/docs/project-scaler.md`)를 참조하여 
> 적절한 규모의 워크플로우를 선택하세요.

---

## Project Scale Quick Reference

| Tier | 설명 | Active Agents | Timeline |
|------|------|---------------|----------|
| **Tier 1** | Quick Experiment | 8개 (15%) | 1-2주 |
| **Tier 2** | Side Project | 18개 (33%) | 1-2개월 |
| **Tier 3** | Startup MVP | 35개 (64%) | 2-4개월 |
| **Tier 4** | Full Product | 55개 (100%) | 4개월+ |

**Tier 결정 기준**: 목표, 타겟 사용자 수, 예상 기간, 복잡도
**상세 가이드**: `/docs/project-scaler.md`

---

## Organization Structure

```
                              ┌─────────────┐
                              │     CEO     │
                              │ Orchestrator│
                              └──────┬──────┘
                                     │
           ┌─────────────────────────┼─────────────────────────┐
           │                         │                         │
           ▼                         ▼                         ▼
    ┌─────────────┐          ┌─────────────┐          ┌─────────────┐
    │     CBO     │          │     CTO     │          │     CGO     │
    │  Business   │ ───────▶ │ Development │ ───────▶ │   Growth    │
    │   Division  │          │  Division   │          │  Division   │
    └─────────────┘          └─────────────┘          └─────────────┘
           │                         │                         │
           │    Product Brief        │    Launch Brief         │
           └─────────────────────────┴─────────────────────────┘
                                     │
                          Growth Insights Report
                          (Feedback Loop)
```

---

## Team Composition

### CBO Division (Business) - 12 Agents
```
CBO
├── Research Division (4)
│   ├── Trend Scout
│   ├── Market Analyzer
│   ├── Competitor Analyst
│   └── Pain Point Hunter
├── Strategy Division (4)
│   ├── Opportunity Scorer
│   ├── BM Designer
│   ├── Financial Modeler
│   └── GTM Strategist
└── Documentation Division (2)
    ├── Research Report Writer
    └── Business Plan Writer
```

### CTO Division (Development) - 10 Agents
```
CTO
├── Product Division (2)
│   ├── PRD Architect
│   └── Scope Guard
├── Engineering Division (5)
│   ├── Architect
│   ├── Frontend Engineer
│   ├── Backend Engineer
│   └── Code Reviewer
└── Operations Division (3)
    ├── Test Writer
    ├── Doc Writer
    └── DevOps Engineer
```

### CGO Division (Growth) - 31 Agents (Hierarchical)
```
CGO
├── Acquisition Division (11)
│   ├── Channel Strategist
│   ├── Paid Ads Lead
│   │   ├── Meta Ads Specialist
│   │   ├── Google Ads Specialist
│   │   ├── TikTok Ads Specialist
│   │   └── Ads Performance Analyzer
│   └── Organic Lead
│       ├── SEO Specialist
│       ├── Content Marketer
│       ├── Community Manager
│       └── Partnership Manager
├── Activation Division (2)
│   ├── Onboarding Designer
│   └── Aha Moment Engineer
├── Retention Division (5)
│   ├── Cohort Analyst
│   ├── Engagement Lead
│   │   ├── Notification Specialist
│   │   ├── Email Marketing Specialist
│   │   └── Gamification Designer
│   └── Churn Preventer
├── Revenue Division (2)
│   ├── Monetization Optimizer
│   └── Upsell Strategist
├── Referral Division (2)
│   ├── Viral Loop Designer
│   └── Advocacy Builder
├── Creative Division (6)
│   ├── Ad Creative Director
│   └── Copy Lead
│       ├── Ad Copywriter
│       ├── Email Copywriter
│       ├── Landing Page Copywriter
│       └── Microcopy Writer
└── Analytics Division (2)
    ├── Growth Metrics Analyst
    └── Growth Strategy Writer
```

### Total: 54 Agents (+ CEO = 55)

---

## Project Lifecycle

### Phase 1: Discovery & Planning (CBO)
**Duration**: 1-2 weeks
**Owner**: CBO

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 1: BUSINESS                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [CEO Request]                                              │
│       ↓                                                     │
│  Trend Scout ──→ Pain Point Hunter                          │
│       ↓              ↓                                      │
│  Market Analyzer ←───┘                                      │
│       ↓                                                     │
│  Competitor Analyst                                         │
│       ↓                                                     │
│  ═══════════════════════════════════                        │
│  │ OUTPUT: Market Research Report │                         │
│  ═══════════════════════════════════                        │
│       ↓                                                     │
│  Opportunity Scorer                                         │
│       ↓                                                     │
│  BM Designer ──→ Financial Modeler                          │
│       ↓              ↓                                      │
│  GTM Strategist ←────┘                                      │
│       ↓                                                     │
│  ════════════════════════════════════════════               │
│  │ OUTPUT: Business Plan + Product Brief │  ──→ CTO        │
│  ════════════════════════════════════════════               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Deliverables**:
- Market Research Report
- Business Plan
- **Product Brief** (→ CTO Handoff)

---

### Phase 2: Product Development (CTO)
**Duration**: 2-8 weeks (depending on scope)
**Owner**: CTO

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 2: DEVELOPMENT                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Product Brief from CBO]                                   │
│       ↓                                                     │
│  PRD Architect                                              │
│       ↓                                                     │
│  Scope Guard ──→ (Approved?)                                │
│       │              │                                      │
│       │ Yes          │ No → Revise with CBO                 │
│       ↓              │                                      │
│  ═══════════════════════════════════                        │
│  │ OUTPUT: PRD Document            │                        │
│  ═══════════════════════════════════                        │
│       ↓                                                     │
│  Architect                                                  │
│       ↓                                                     │
│  ═══════════════════════════════════                        │
│  │ OUTPUT: Technical Specification │                        │
│  ═══════════════════════════════════                        │
│       ↓                                                     │
│  ┌─────────────┬─────────────┐                              │
│  │  Frontend   │   Backend   │  (Parallel)                  │
│  │  Engineer   │   Engineer  │                              │
│  └──────┬──────┴──────┬──────┘                              │
│         └──────┬──────┘                                     │
│                ↓                                            │
│  Code Reviewer ──→ Test Writer                              │
│                         ↓                                   │
│  DevOps Engineer (Deploy)                                   │
│       ↓                                                     │
│  Doc Writer                                                 │
│       ↓                                                     │
│  ════════════════════════════════════════════               │
│  │ OUTPUT: Deployed Product + Launch Brief │  ──→ CGO      │
│  ════════════════════════════════════════════               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Deliverables**:
- PRD Document
- Technical Specification
- Deployed Product
- **Launch Brief** (→ CGO Handoff)

---

### Phase 3: Growth & Scale (CGO)
**Duration**: Ongoing
**Owner**: CGO

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 3: GROWTH                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Launch Brief from CTO]                                    │
│       ↓                                                     │
│  CGO: Strategy Setup                                        │
│       ↓                                                     │
│  ┌─────────────────────────────────────────┐                │
│  │         AARRR Funnel Execution          │                │
│  │                                         │                │
│  │  ACQUISITION ─────────────────┐         │                │
│  │  ├─ Paid Ads Lead            │         │                │
│  │  │   └─ Specialists          │         │                │
│  │  └─ Organic Lead             │         │                │
│  │      └─ Specialists          ↓         │                │
│  │                                         │                │
│  │  ACTIVATION ──────────────────┐         │                │
│  │  ├─ Onboarding Designer      │         │                │
│  │  └─ Aha Moment Engineer      ↓         │                │
│  │                                         │                │
│  │  RETENTION ───────────────────┐         │                │
│  │  ├─ Cohort Analyst           │         │                │
│  │  ├─ Engagement Lead          │         │                │
│  │  │   └─ Specialists          │         │                │
│  │  └─ Churn Preventer          ↓         │                │
│  │                                         │                │
│  │  REVENUE ─────────────────────┐         │                │
│  │  ├─ Monetization Optimizer   │         │                │
│  │  └─ Upsell Strategist        ↓         │                │
│  │                                         │                │
│  │  REFERRAL ────────────────────┘         │                │
│  │  ├─ Viral Loop Designer                │                │
│  │  └─ Advocacy Builder                   │                │
│  └─────────────────────────────────────────┘                │
│                                                             │
│  [Supporting Teams]                                         │
│  ├─ Creative Division (Ad Creative, Copy)                   │
│  └─ Analytics Division (Metrics, Strategy Writer)           │
│                                                             │
│       ↓                                                     │
│  ══════════════════════════════════════════════════         │
│  │ OUTPUT: Growth Metrics + Insights Report │  ──→ CBO     │
│  ══════════════════════════════════════════════════         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Deliverables**:
- Growth Strategy Document
- Channel Plans & Campaigns
- Performance Dashboards
- **Growth Insights Report** (→ CBO Feedback)

---

## Handoff Protocol

### 1. CBO → CTO: Product Brief

| Item | Description |
|------|-------------|
| **Document** | Product Brief |
| **Template** | `/templates/handoff/product-brief-template.md` |
| **Owner** | GTM Strategist (CBO) |
| **Receiver** | PRD Architect (CTO) |
| **Trigger** | Business Plan approved by CEO |

**Key Contents**:
- MVP Features (MoSCoW prioritized)
- Success Metrics with targets
- Timeline and constraints
- Competitive context

**Validation Checklist**:
- [ ] All Must Have features have acceptance criteria
- [ ] Metrics have specific numeric targets
- [ ] Timeline validated as realistic
- [ ] Technical preferences documented

---

### 2. CTO → CGO: Launch Brief

| Item | Description |
|------|-------------|
| **Document** | Launch Brief |
| **Template** | `/templates/handoff/launch-brief-template.md` |
| **Owner** | Doc Writer (CTO) |
| **Receiver** | CGO |
| **Trigger** | Product deployed to production |

**Key Contents**:
- Feature documentation with access paths
- User flows mapped
- Aha moment suggestion
- All trackable events listed
- Growth infrastructure capabilities
- Technical limitations

**Validation Checklist**:
- [ ] All features documented with user benefits
- [ ] Events list is complete with properties
- [ ] Aha moment has data-backed rationale
- [ ] Test accounts working

---

### 3. CGO → CEO: Growth Insights Report

| Item | Description |
|------|-------------|
| **Document** | Growth Insights Report |
| **Template** | `/templates/handoff/growth-insights-template.md` |
| **Owner** | Growth Strategy Writer (CGO) |
| **Receiver** | CEO |
| **Trigger** | Quarterly review or pivot consideration |

**Key Contents**:
- Actual performance metrics
- User feedback themes
- Feature requests with prioritization
- Competitive observations
- Product/pricing recommendations

**Validation Checklist**:
- [ ] All metrics have actual numbers
- [ ] Recommendations are actionable
- [ ] Data sources documented
- [ ] Competitive intel is current

---

## Shared Context Management

### Context Files
```
/context
├── product-context.json    # 제품 핵심 정보
├── business-context.json   # 사업 핵심 정보
├── technical-context.json  # 기술 핵심 정보
└── growth-context.json     # 그로스 핵심 정보
```

### Ownership & Access
| Context | Owner | Other Access |
|---------|-------|--------------|
| product-context | Shared (CEO approves) | All Read |
| business-context | CBO | CTO, CGO Read |
| technical-context | CTO | CBO, CGO Read |
| growth-context | CGO | CBO, CTO Read |

### Update Frequency
| Context | Update Trigger |
|---------|---------------|
| product-context | Feature launch, strategy pivot |
| business-context | Market change, pricing change |
| technical-context | Tech change, new capability |
| growth-context | Weekly (metrics), on experiment completion |

---

## Communication Cadence

### Daily
```yaml
who: Each division internally
what: Progress check, blocker identification
format: Async status in /workspace/status/
```

### Weekly
```yaml
who: CEO + Division Heads (CBO, CTO, CGO)
what: Cross-division sync
agenda:
  - KPI review
  - Blocker escalation
  - Resource needs
  - Handoff status
format: Sync meeting or detailed written update
```

### Monthly
```yaml
who: All divisions
what: Strategic review
agenda:
  - Month performance review
  - Next month priorities
  - Resource reallocation
  - Process improvements
format: Written report + sync if needed
```

### Quarterly
```yaml
who: CEO + All divisions
what: Strategic planning
agenda:
  - Quarter review (Growth Insights Report)
  - Next quarter OKRs
  - Major initiatives
  - Budget review
format: Comprehensive review meeting
```

---

## Escalation Protocol

### When to Escalate to CEO
```yaml
criteria:
  - Cross-division conflict unresolved
  - Resource request beyond division budget
  - Timeline risk affecting other divisions
  - Strategic pivot consideration
  - Major blocker lasting >2 days

how:
  - Document the issue clearly
  - List options with pros/cons
  - State recommended action
  - Specify urgency level
```

### Escalation Levels
| Level | Response Time | Examples |
|-------|--------------|----------|
| 🔴 Critical | < 2 hours | Product down, security breach |
| 🟠 High | < 24 hours | Major blocker, deadline risk |
| 🟡 Medium | < 48 hours | Resource conflict, process issue |
| 🟢 Low | < 1 week | Improvement suggestion |

---

## File Structure

```
/agent-company
├── /agents
│   ├── /ceo
│   │   └── ceo.md
│   ├── /business
│   │   ├── cbo.md
│   │   └── /research, /strategy, /documentation
│   ├── /development
│   │   ├── cto.md
│   │   └── /product, /engineering, /operations
│   └── /growth
│       ├── cgo.md
│       ├── /acquisition (with /paid-ads, /organic subdirs)
│       ├── /activation
│       ├── /retention (with /engagement subdir)
│       ├── /revenue
│       ├── /referral
│       ├── /creative (with /copy subdir)
│       └── /analytics
├── /context
│   ├── SCHEMA.md
│   ├── product-context.json
│   ├── business-context.json
│   ├── technical-context.json
│   └── growth-context.json
├── /templates
│   └── /handoff
│       ├── product-brief-template.md
│       ├── launch-brief-template.md
│       └── growth-insights-template.md
├── /docs
│   ├── integrated-workflow.md (this file)
│   └── growth-team-workflow.md
└── /workspace
    ├── /handoff (active handoff documents)
    ├── /artifacts (deliverables by division)
    └── /status (daily status updates)
```

---

## Quick Start Guide

### Starting a New Project

1. **CEO initiates**
   ```
   CEO → CBO: "새로운 [domain] 영역에서 기회를 탐색해"
   ```

2. **CBO executes Discovery & Planning**
   - Runs research pipeline
   - Produces Business Plan
   - Creates Product Brief
   - Hands off to CTO

3. **CTO executes Development**
   - Creates PRD from Product Brief
   - Designs and builds product
   - Deploys to production
   - Creates Launch Brief
   - Hands off to CGO

4. **CGO executes Growth**
   - Sets up growth strategy from Launch Brief
   - Runs AARRR optimization
   - Generates Growth Insights
   - Feeds back to CBO for iteration

### Resuming Existing Project

1. **Check context files** for current state
2. **Identify current phase** (Business/Dev/Growth)
3. **Review pending handoffs** in /workspace/handoff
4. **Continue from last checkpoint**

---

## Success Metrics by Phase

| Phase | Key Metrics | Target |
|-------|-------------|--------|
| Business | Opportunity Score | >7/10 |
| Business | Business Plan completeness | 100% |
| Development | On-time delivery | >80% |
| Development | Bug-free launch | <5 critical bugs |
| Growth | Activation Rate | >40% |
| Growth | D30 Retention | >20% |
| Growth | LTV:CAC | >3:1 |

---

## Appendix

### Agent Count Summary
| Division | Agents |
|----------|--------|
| CEO | 1 |
| CBO | 12 |
| CTO | 10 |
| CGO | 31 |
| **Total** | **54** |

### Document Templates
- Product Brief: `/templates/handoff/product-brief-template.md`
- Launch Brief: `/templates/handoff/launch-brief-template.md`
- Growth Insights: `/templates/handoff/growth-insights-template.md`
- Context Schema: `/context/SCHEMA.md`

### Related Documents
- **Project Scaler**: `/docs/project-scaler.md` ⭐ 프로젝트 시작 전 필독
- Growth Team Detailed Workflow: `/docs/growth-team-workflow.md`
