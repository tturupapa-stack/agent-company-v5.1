# Project Scaler - 프로젝트 규모별 워크플로우 선택 시스템

## Overview

모든 프로젝트가 55개 에이전트를 필요로 하지 않는다. 이 문서는 프로젝트 초기 단계에서 규모를 평가하고, 적절한 에이전트 조합을 선택하는 시스템을 정의한다.

---

## Project Scale Tiers

### Tier 1: Quick Experiment (1-2주)
```yaml
description: "빠른 아이디어 검증, 해커톤, MVP 테스트"
examples:
  - "이 아이디어가 먹힐지 랜딩페이지로 검증"
  - "주말 해커톤 프로젝트"
  - "기존 제품에 작은 기능 추가"
budget: "$0 - $500"
timeline: "1-2 weeks"
team_size: "Solo"
```

### Tier 2: Side Project (1-2개월)
```yaml
description: "진지한 사이드 프로젝트, 소규모 SaaS"
examples:
  - "개인 SaaS 도구 개발"
  - "니치 마켓 타겟 앱"
  - "자동화 툴/봇"
budget: "$500 - $5,000"
timeline: "1-2 months"
team_size: "Solo or 2 people"
```

### Tier 3: Startup MVP (2-4개월)
```yaml
description: "본격적인 스타트업 MVP, 투자 유치 목표"
examples:
  - "시드 투자 목표 MVP"
  - "B2B SaaS 초기 버전"
  - "마켓플레이스 초기 버전"
budget: "$5,000 - $50,000"
timeline: "2-4 months"
team_size: "2-5 people"
```

### Tier 4: Full Product (4개월+)
```yaml
description: "풀스케일 제품 개발, 시리즈 A+ 단계"
examples:
  - "대규모 플랫폼"
  - "엔터프라이즈 솔루션"
  - "멀티 플랫폼 앱"
budget: "$50,000+"
timeline: "4+ months"
team_size: "5+ people"
```

---

## Scale Assessment Checklist

프로젝트 시작 시 아래 질문에 답하여 Tier를 결정한다.

### Step 1: 목표 평가
```yaml
questions:
  - question: "이 프로젝트의 주요 목표는?"
    options:
      a: "아이디어 검증 / 학습" → Tier 1
      b: "수익 창출 (소규모)" → Tier 2
      c: "투자 유치 / 본격 사업" → Tier 3
      d: "대규모 성장 / 확장" → Tier 4

  - question: "타겟 사용자 수는?"
    options:
      a: "100명 이하" → Tier 1
      b: "100 - 1,000명" → Tier 2
      c: "1,000 - 10,000명" → Tier 3
      d: "10,000명 이상" → Tier 4

  - question: "예상 개발 기간은?"
    options:
      a: "2주 이하" → Tier 1
      b: "1-2개월" → Tier 2
      c: "2-4개월" → Tier 3
      d: "4개월 이상" → Tier 4
```

### Step 2: 복잡도 평가
```yaml
questions:
  - question: "필요한 플랫폼은?"
    options:
      a: "웹만 (단일 페이지)" → Tier 1
      b: "웹 앱 (다중 페이지)" → Tier 2
      c: "웹 + 모바일 중 하나" → Tier 3
      d: "웹 + iOS + Android" → Tier 4

  - question: "외부 연동이 필요한가?"
    options:
      a: "없음" → Tier 1
      b: "1-2개 (결제, 이메일 등)" → Tier 2
      c: "3-5개" → Tier 3
      d: "5개 이상" → Tier 4

  - question: "사용자 인증이 필요한가?"
    options:
      a: "없음" → Tier 1
      b: "단순 인증" → Tier 2
      c: "OAuth + 역할 관리" → Tier 3
      d: "엔터프라이즈 SSO" → Tier 4
```

### Step 3: 최종 Tier 결정
```
대부분의 답변이 a → Tier 1
대부분의 답변이 b → Tier 2
대부분의 답변이 c → Tier 3
대부분의 답변이 d → Tier 4

혼합된 경우: 가장 높은 Tier 선택 (단, 목표/예산과 일치하는지 확인)
```

---

## Tier별 Active Agents

### Tier 1: Quick Experiment
**Active Agents: 8개** (전체의 15%)

```
CEO (Lite Mode)
│
├── CBO (Minimal)
│   └── Pain Point Hunter (간단 검증)
│
├── CTO (Core Only)
│   ├── PRD Architect (간소화)
│   ├── Frontend Engineer
│   └── Backend Engineer (필요시)
│
└── CGO (Validation Focus)
    ├── Landing Page Copywriter
    └── Channel Strategist (1-2채널만)
```

**Skip하는 것들:**
- 상세 시장 분석 (Trend Scout, Market Analyzer)
- 경쟁 분석 (Competitor Analyst)
- 재무 모델링 (Financial Modeler)
- 코드 리뷰 (속도 우선)
- 전체 AARRR (Acquisition만 집중)
- 계층적 서브에이전트 (Lead가 직접 처리)

**핸드오프:**
- Product Brief: 1페이지 요약
- Launch Brief: 체크리스트 수준
- Growth Insights: 간단한 메트릭만

---

### Tier 2: Side Project
**Active Agents: 18개** (전체의 33%)

```
CEO
│
├── CBO (Focused)
│   ├── Pain Point Hunter
│   ├── Competitor Analyst (간소화)
│   ├── BM Designer
│   └── Business Plan Writer (간소화)
│
├── CTO (Standard)
│   ├── PRD Architect
│   ├── Scope Guard
│   ├── Architect
│   ├── Frontend Engineer
│   ├── Backend Engineer
│   ├── Code Reviewer
│   └── Doc Writer
│
└── CGO (Core AARRR)
    ├── Channel Strategist
    ├── Paid Ads Manager (단일, 서브에이전트 없이)
    ├── Organic Growth Hacker (단일, 서브에이전트 없이)
    ├── Onboarding Designer
    ├── Copywriter (단일, 서브에이전트 없이)
    └── Growth Metrics Analyst
```

**Skip하는 것들:**
- 상세 시장 분석 (TAM/SAM은 간단히만)
- 재무 모델링 (단순 계산)
- Activation/Retention 전문 에이전트
- Revenue/Referral 전문 에이전트
- 계층적 서브에이전트

**핸드오프:**
- Product Brief: 3-5페이지
- Launch Brief: 핵심 섹션만
- Growth Insights: 월간 요약

---

### Tier 3: Startup MVP
**Active Agents: 35개** (전체의 64%)

```
CEO
│
├── CBO (Full Research, Lite Strategy)
│   ├── Trend Scout
│   ├── Market Analyzer
│   ├── Competitor Analyst
│   ├── Pain Point Hunter
│   ├── Opportunity Scorer
│   ├── BM Designer
│   ├── Financial Modeler
│   ├── GTM Strategist
│   ├── Research Report Writer
│   └── Business Plan Writer
│
├── CTO (Full)
│   ├── PRD Architect
│   ├── Scope Guard
│   ├── Architect
│   ├── Frontend Engineer
│   ├── Backend Engineer
│   ├── Code Reviewer
│   ├── Test Writer
│   ├── Doc Writer
│   └── DevOps Engineer
│
└── CGO (Full AARRR, Selective Hierarchy)
    ├── Acquisition
    │   ├── Channel Strategist
    │   ├── Paid Ads Lead (서브에이전트 2개만: 주력 플랫폼)
    │   └── Organic Lead (서브에이전트 2개만: SEO + Content)
    ├── Activation
    │   ├── Onboarding Designer
    │   └── Aha Moment Engineer
    ├── Retention
    │   ├── Cohort Analyst
    │   └── Engagement Lead (서브에이전트 없이 직접)
    ├── Revenue
    │   └── Monetization Optimizer
    ├── Creative
    │   └── Copy Lead (서브에이전트 2개만: Ad + LP)
    └── Analytics
        ├── Growth Metrics Analyst
        └── Growth Strategy Writer
```

**Skip하는 것들:**
- 모든 플랫폼 Specialist (주력 2개만)
- Churn Preventer (초기엔 Retention 데이터 부족)
- Upsell Strategist (초기엔 업셀 보다 획득)
- Referral Division (PMF 전에는 조기)
- 모든 Copy 서브에이전트 (핵심만)

**핸드오프:**
- Product Brief: Full template
- Launch Brief: Full template
- Growth Insights: 분기별 상세

---

### Tier 4: Full Product
**Active Agents: 55개** (전체 100%)

```
모든 에이전트 활성화
├── CEO
├── CBO Division (12 agents)
├── CTO Division (10 agents)
└── CGO Division (31 agents, full hierarchy)
```

**Full Activation:**
- 모든 플랫폼 Specialist
- 모든 Copy 서브에이전트
- 모든 Engagement 서브에이전트
- Referral Division
- 전체 핸드오프 템플릿

---

## Quick Reference: Agent Activation Matrix

| Agent | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|-------|--------|--------|--------|--------|
| **CEO** | ✅ Lite | ✅ | ✅ | ✅ |
| **CBO** | | | | |
| Trend Scout | ❌ | ❌ | ✅ | ✅ |
| Market Analyzer | ❌ | ❌ | ✅ | ✅ |
| Competitor Analyst | ❌ | ✅ Lite | ✅ | ✅ |
| Pain Point Hunter | ✅ Lite | ✅ | ✅ | ✅ |
| Opportunity Scorer | ❌ | ❌ | ✅ | ✅ |
| BM Designer | ❌ | ✅ | ✅ | ✅ |
| Financial Modeler | ❌ | ❌ | ✅ | ✅ |
| GTM Strategist | ❌ | ❌ | ✅ | ✅ |
| Research Report Writer | ❌ | ❌ | ✅ | ✅ |
| Business Plan Writer | ❌ | ✅ Lite | ✅ | ✅ |
| **CTO** | | | | |
| PRD Architect | ✅ Lite | ✅ | ✅ | ✅ |
| Scope Guard | ❌ | ✅ | ✅ | ✅ |
| Architect | ❌ | ✅ | ✅ | ✅ |
| Frontend Engineer | ✅ | ✅ | ✅ | ✅ |
| Backend Engineer | ⚪ Optional | ✅ | ✅ | ✅ |
| Code Reviewer | ❌ | ✅ | ✅ | ✅ |
| Test Writer | ❌ | ❌ | ✅ | ✅ |
| Doc Writer | ❌ | ✅ | ✅ | ✅ |
| DevOps Engineer | ❌ | ❌ | ✅ | ✅ |
| **CGO** | | | | |
| Channel Strategist | ✅ Lite | ✅ | ✅ | ✅ |
| Paid Ads Lead | ❌ | ✅ Solo | ✅ +2 | ✅ +4 |
| Organic Lead | ❌ | ✅ Solo | ✅ +2 | ✅ +4 |
| Onboarding Designer | ❌ | ✅ | ✅ | ✅ |
| Aha Moment Engineer | ❌ | ❌ | ✅ | ✅ |
| Cohort Analyst | ❌ | ❌ | ✅ | ✅ |
| Engagement Lead | ❌ | ❌ | ✅ Solo | ✅ +3 |
| Churn Preventer | ❌ | ❌ | ❌ | ✅ |
| Monetization Optimizer | ❌ | ❌ | ✅ | ✅ |
| Upsell Strategist | ❌ | ❌ | ❌ | ✅ |
| Viral Loop Designer | ❌ | ❌ | ❌ | ✅ |
| Advocacy Builder | ❌ | ❌ | ❌ | ✅ |
| Ad Creative Director | ❌ | ❌ | ❌ | ✅ |
| Copy Lead | ❌ | ✅ Solo | ✅ +2 | ✅ +4 |
| Growth Metrics Analyst | ❌ | ✅ | ✅ | ✅ |
| Growth Strategy Writer | ❌ | ❌ | ✅ | ✅ |

**Legend:**
- ✅ = Active
- ✅ Lite = 간소화 버전
- ✅ Solo = Lead만, 서브에이전트 없이
- ✅ +N = Lead + N개 서브에이전트
- ⚪ = Optional
- ❌ = Skip

---

## Tier별 핸드오프 문서 간소화

### Tier 1 핸드오프
```yaml
product_brief_lite:
  length: "1 page"
  sections:
    - Problem (2-3 sentences)
    - Solution (2-3 sentences)
    - MVP Features (bullet list)
    - Success = (1 metric)

launch_brief_lite:
  length: "Checklist"
  sections:
    - Live URL
    - Core feature (1)
    - How to test
    - Basic analytics event (3-5)

growth_insights_lite:
  length: "Dashboard screenshot + 3 bullets"
  frequency: "Weekly"
```

### Tier 2 핸드오프
```yaml
product_brief_standard:
  length: "3-5 pages"
  sections:
    - Problem & Solution
    - Target User
    - MVP Features (MoSCoW)
    - Success Metrics (3-5)
    - Timeline

launch_brief_standard:
  length: "2-3 pages"
  sections:
    - Feature list
    - Main user flow
    - Events list
    - Test accounts

growth_insights_standard:
  length: "3-5 pages"
  frequency: "Monthly"
```

### Tier 3-4 핸드오프
```yaml
# Full templates 사용
product_brief: "/templates/handoff/product-brief-template.md"
launch_brief: "/templates/handoff/launch-brief-template.md"
growth_insights: "/templates/handoff/growth-insights-template.md"
```

---

## CEO의 Scale Assessment Prompt

프로젝트 시작 시 CEO가 사용하는 프롬프트:

```
You are the CEO assessing a new project's scale.

## Project Idea
{user_input}

## Assessment Process
1. Ask clarifying questions if needed:
   - What's the primary goal?
   - Target user count?
   - Timeline?
   - Budget?
   - Platform needs?

2. Based on answers, determine Tier (1-4)

3. Output the recommended configuration:
   - Tier level
   - Active agents list
   - Skip list with reasons
   - Handoff document format
   - Estimated timeline

## Output Format
### Project Scale Assessment

**Tier: [1/2/3/4] - [Name]**

**Rationale:**
[Why this tier]

**Active Agents:**
- CBO: [list]
- CTO: [list]
- CGO: [list]

**Skipped (and why):**
- [Agent]: [Reason]

**Handoff Format:**
- Product Brief: [Lite/Standard/Full]
- Launch Brief: [Lite/Standard/Full]
- Growth Insights: [Lite/Standard/Full]

**Recommended Timeline:**
- Business: X days
- Development: X weeks
- Growth: Ongoing

**Next Step:**
[First action to take]
```

---

## Tier 업그레이드 트리거

프로젝트 진행 중 Tier를 올려야 하는 시점:

```yaml
tier_1_to_2:
  triggers:
    - "검증 성공, 본격 개발 결정"
    - "첫 유료 고객 확보"
    - "2주 이상 지속 개발 필요"
  action: "BM Designer, Code Reviewer, Growth Metrics 추가"

tier_2_to_3:
  triggers:
    - "MRR $1,000+ 달성"
    - "투자 유치 준비"
    - "팀 확장 (2명+)"
    - "멀티 플랫폼 필요"
  action: "Full CBO Research, Test Writer, Activation/Retention 팀 추가"

tier_3_to_4:
  triggers:
    - "MRR $10,000+ 달성"
    - "Series A+ 단계"
    - "국제 확장"
    - "팀 5명+"
  action: "전체 에이전트 활성화"
```

---

## 예시: Tier 판단

### 예시 1: "AI 이미지 생성 앱 랜딩페이지로 수요 검증"
```
Assessment:
- Goal: 아이디어 검증 → Tier 1
- Users: 100명 이하 → Tier 1
- Timeline: 1주 → Tier 1
- Platform: 웹 단일 페이지 → Tier 1

Result: Tier 1 - Quick Experiment
Active: 8 agents
```

### 예시 2: "프리랜서용 인보이스 SaaS"
```
Assessment:
- Goal: 수익 창출 (소규모) → Tier 2
- Users: 500명 목표 → Tier 2
- Timeline: 6주 → Tier 2
- Platform: 웹 앱 → Tier 2
- 연동: Stripe (결제) → Tier 2

Result: Tier 2 - Side Project
Active: 18 agents
```

### 예시 3: "B2B 마케팅 자동화 플랫폼, 시드 투자 목표"
```
Assessment:
- Goal: 투자 유치 → Tier 3
- Users: 5,000명 목표 → Tier 3
- Timeline: 3개월 → Tier 3
- Platform: 웹 앱 + 크롬 익스텐션 → Tier 3
- 연동: 5개 (CRM, 이메일, 광고 등) → Tier 3/4

Result: Tier 3 - Startup MVP
Active: 35 agents
```

---

## 파일 위치

### 관련 문서
| 문서 | 위치 | 용도 |
|------|------|------|
| **Agent Skills Index** | `/docs/agent-skills-index.md` | ⭐ 전체 스킬 파일 인덱스 |
| Integrated Workflow | `/docs/integrated-workflow.md` | 전체 워크플로우 가이드 |
| Handoff Templates | `/templates/handoff/` | 핸드오프 문서 템플릿 |
| Lite Templates | `/templates/handoff/lite-templates.md` | Tier 1-2용 간소화 템플릿 |

### Tier별 핵심 스킬 파일

#### Tier 1 필수 스킬
```
/agents/business/research/research-agents.md      → Pain Point Hunter
/agents/development/product/product-agents.md     → PRD Architect
/agents/development/engineering/engineering-agents.md → Frontend/Backend
/agents/growth/acquisition/channel-strategist.md
/agents/growth/creative/copy/landing-page-copywriter.md
```

#### Tier 2 추가 스킬
```
/agents/business/strategy/strategy-agents.md      → BM Designer
/agents/development/product/product-agents.md     → Scope Guard
/agents/growth/acquisition/paid-ads-lead.md
/agents/growth/acquisition/organic-lead.md
/agents/growth/creative/copy-lead.md
/agents/growth/analytics/growth-metrics-analyst.md
```

#### Tier 3 추가 스킬 (플랫폼 선택)
```
/agents/growth/acquisition/paid-ads/meta-specialist.md
/agents/growth/acquisition/paid-ads/google-specialist.md
/agents/growth/acquisition/organic/seo-specialist.md
/agents/growth/acquisition/organic/content-marketer.md
/agents/growth/creative/copy/ad-copywriter.md
/agents/growth/activation/aha-moment-engineer.md
```

#### Tier 4 추가 스킬 (전체)
```
모든 /agents/ 하위 파일
```
