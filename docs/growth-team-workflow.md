# Growth Team Agent Workflow Guide (Hierarchical)

## Overview

이 문서는 개발 완료된 서비스의 수익성을 극대화하기 위한 그로스팀 에이전트 워크플로우를 설명합니다.
사업팀(CBO)에서 전달받은 Business Plan을 기반으로 AARRR 전체 퍼널을 최적화합니다.

**계층 구조**: Lead 에이전트가 전략을 수립하고 Specialist 서브에이전트에게 실행을 위임합니다.

## Team Structure (Hierarchical)

```
CEO (Chief Executive Officer)
├── CBO (Chief Business Officer) - 사업팀
├── CTO (Chief Technology Officer) - 개발팀
└── CGO (Chief Growth Officer) - 그로스팀
    │
    ├── Acquisition Division (유저 획득)
    │   ├── Channel Strategist
    │   ├── Paid Ads Lead ─────────────┬── Meta Ads Specialist
    │   │                              ├── Google Ads Specialist
    │   │                              ├── TikTok Ads Specialist
    │   │                              └── Ads Performance Analyzer
    │   └── Organic Lead ──────────────┬── SEO Specialist
    │                                  ├── Content Marketer
    │                                  ├── Community Manager
    │                                  └── Partnership Manager
    │
    ├── Activation Division (활성화)
    │   ├── Onboarding Designer
    │   └── Aha Moment Engineer
    │
    ├── Retention Division (리텐션)
    │   ├── Cohort Analyst
    │   ├── Engagement Lead ───────────┬── Notification Specialist
    │   │                              ├── Email Marketing Specialist
    │   │                              └── Gamification Designer
    │   └── Churn Preventer
    │
    ├── Revenue Division (수익화)
    │   ├── Monetization Optimizer
    │   └── Upsell Strategist
    │
    ├── Referral Division (추천)
    │   ├── Viral Loop Designer
    │   └── Advocacy Builder
    │
    ├── Creative Division (소재 제작)
    │   ├── Ad Creative Director
    │   └── Copy Lead ─────────────────┬── Ad Copywriter
    │                                  ├── Email Copywriter
    │                                  ├── Landing Page Copywriter
    │                                  └── Microcopy Writer
    │
    └── Analytics Division (분석 & 문서)
        ├── Growth Metrics Analyst
        └── Growth Strategy Writer
```

## Hierarchical Design Principles

### Lead vs Specialist
```yaml
lead_agent:
  role: "전략 수립 + 작업 분배 + 품질 검증"
  when_to_handle: "크로스 채널 전략, 통합 분석"
  when_to_delegate: "플랫폼/포맷별 전문 실행"

specialist_agent:
  role: "단일 도메인 전문 실행"
  scope: "특정 플랫폼 또는 포맷에 집중"
  return: "결과물 + 성과 예측"
```

### Sub-Agent Call Pattern (Claude Code)
```
[CALL_AGENT: specialist_name]
Task: {specific_task_description}
Context: {relevant_context}
Deadline: {timeline}
Success Criteria: {metrics}
```

## Workflow Pipeline

### Phase 1: Strategy Setup (CBO → CGO Handoff)

```
[From CBO]
Business Plan
├── Target Market
├── Value Proposition
├── Competitive Analysis
├── Revenue Model
└── Initial Budget
    ↓
[CGO Processing]
1. North Star Metric 정의
2. AARRR 목표 설정
3. 채널 우선순위 결정
4. 예산 배분 계획
5. 90일 로드맵 수립
    ↓
[Output]
Growth Strategy Document
```

### Phase 2: Acquisition Pipeline

```
CGO (Strategy Direction)
    ↓
Channel Strategist
├── 타겟 오디언스 분석
├── 채널 믹스 설계
└── 예산 배분
    ↓
    ├── Paid Ads Manager
    │   ├── 캠페인 구조 설계
    │   ├── 타겟팅 전략
    │   ├── A/B 테스트
    │   └── 최적화
    │
    └── Organic Growth Hacker
        ├── SEO 전략
        ├── 콘텐츠 마케팅
        ├── 커뮤니티 그로스
        └── 파트너십
    ↓
[Output]
- Channel Strategy Document
- Campaign Plans
- Content Calendar
- CAC by Channel Report
```

### Phase 3: Activation Pipeline

```
[From Acquisition]
New Signups + Source Data
    ↓
Onboarding Designer
├── 온보딩 플로우 설계
├── 유저 세그먼트 맞춤화
├── 프로그레스 인디케이터
└── 드롭오프 분석
    ↓
Aha Moment Engineer
├── Aha Moment 정의
├── Time-to-Value 최소화
├── Activation 기준 설정
└── 실험 설계
    ↓
[Output]
- Onboarding Flow Design
- Activation Definition
- Welcome Email Sequence
- Activation Rate Report
```

### Phase 4: Retention Pipeline

```
[From Activation]
Activated Users
    ↓
Cohort Analyst
├── 코호트 분석
├── 리텐션 커브 분석
├── 행동 패턴 상관관계
└── 인사이트 도출
    ↓
    ├── Engagement Strategist
    │   ├── 참여 루프 설계
    │   ├── 알림 전략
    │   ├── 게이미피케이션
    │   └── 리인게이지먼트
    │
    └── Churn Preventer
        ├── 이탈 예측 모델
        ├── 리스크 스코어링
        ├── 개입 플레이북
        └── 취소 플로우 최적화
    ↓
[Output]
- Retention Analysis Report
- Engagement Playbook
- Churn Prevention System
- D30/D90 Retention Metrics
```

### Phase 5: Revenue Pipeline

```
[From Retention]
Engaged Users
    ↓
Monetization Optimizer
├── 가격 전략 설계
├── 티어/패키지 설계
├── 가격 테스트
└── Revenue KPI 모니터링
    ↓
Upsell Strategist
├── 업그레이드 트리거
├── 확장 수익 캠페인
├── Account Expansion
└── NRR 최적화
    ↓
[Output]
- Pricing Strategy
- Upsell Playbook
- Revenue Dashboard
- LTV/ARPU Reports
```

### Phase 6: Referral Pipeline

```
[From Revenue]
Paying Customers
    ↓
Viral Loop Designer
├── 바이럴 루프 설계
├── 추천 프로그램 구조
├── K-Factor 최적화
└── 공유 메커니즘
    ↓
Advocacy Builder
├── 옹호자 식별
├── UGC 프로그램
├── 리뷰 수집
└── 커뮤니티 구축
    ↓
[Output]
- Referral Program Design
- Community Strategy
- Social Proof Assets
- K-Factor Report
```

### Creative Support Pipeline

```
[Requests from All Divisions]
    ↓
Ad Creative Director
├── 크리에이티브 전략
├── 광고 컨셉 개발
├── A/B 테스트 설계
└── 성과 분석
    ↓
Copywriter
├── 광고 카피
├── 랜딩 페이지 카피
├── 이메일 시퀀스
└── 푸시 알림 카피
    ↓
[Output]
- Ad Creatives (Image/Video)
- Copy Library
- Landing Page Copy
- Email Templates
```

### Analytics & Documentation Pipeline

```
[Data from All Divisions]
    ↓
Growth Metrics Analyst
├── KPI 대시보드
├── 퍼널 분석
├── 실험 분석
└── 예측 모델링
    ↓
Growth Strategy Writer
├── 전략 문서
├── 실행 계획
├── 플레이북
└── 분기 리뷰
    ↓
[Output]
- Growth Strategy Document
- Execution Plan
- Growth Playbook
- Quarterly Review
```

## Handoff Protocol

### Inter-Division Communication

```yaml
standard_handoff:
  format: "Markdown document"
  includes:
    - Context summary
    - Data/insights
    - Specific asks
    - Deadlines
    - Success criteria

escalation_triggers:
  - CAC > 33% of LTV
  - Activation Rate < 20%
  - Churn Rate > 5% monthly
  - Budget utilization > 150%
```

### Data Flow

```
              ┌─────────────────────────────────────────┐
              │         Analytics (Central Hub)          │
              └─────────────────────────────────────────┘
                    ↑         ↑         ↑         ↑
                    │         │         │         │
        ┌───────────┼─────────┼─────────┼─────────┼───────────┐
        │           │         │         │         │           │
   Acquisition  Activation  Retention  Revenue  Referral  Creative
```

## Execution Cadence

### Daily
- Paid Ads Manager: 캠페인 모니터링
- Analytics: 이상 징후 확인

### Weekly
- CGO: 팀 스탠드업
- All Divisions: 주간 성과 공유
- Analytics: Weekly Growth Report

### Monthly
- CGO: 전략 리뷰
- All Divisions: 월간 목표 점검
- Strategy Writer: Execution Plan 업데이트

### Quarterly
- CGO: 전략 수립/수정
- Analytics: Quarterly Review
- Strategy Writer: Strategy Document 업데이트

## Quick Start Guide

### Step 1: Initialize CGO
```
Input: Business Plan from CBO
Action: CGO defines North Star Metric and AARRR targets
Output: Growth Strategy Document (90-day roadmap)
```

### Step 2: Launch Acquisition
```
Input: Growth Strategy from CGO
Action: Channel Strategist designs channel mix
Action: Paid Ads Manager sets up campaigns
Action: Organic Growth Hacker starts SEO/content
Output: First users acquired
```

### Step 3: Optimize Activation
```
Input: New signups from Acquisition
Action: Onboarding Designer creates flows
Action: Aha Moment Engineer optimizes time-to-value
Output: Activated users ready for retention
```

### Step 4: Build Retention
```
Input: Activated users
Action: Cohort Analyst identifies patterns
Action: Engagement Strategist creates loops
Action: Churn Preventer sets up alerts
Output: Retained, engaged user base
```

### Step 5: Maximize Revenue
```
Input: Engaged users
Action: Monetization Optimizer sets pricing
Action: Upsell Strategist creates upgrade paths
Output: Paying customers, growing MRR
```

### Step 6: Enable Referral
```
Input: Satisfied paying customers
Action: Viral Loop Designer creates referral program
Action: Advocacy Builder turns users into advocates
Output: Organic growth engine
```

## Key Metrics Dashboard

| Metric | Owner | Frequency | Target |
|--------|-------|-----------|--------|
| North Star | CGO | Daily | Defined per product |
| CAC | Acquisition | Weekly | < 1/3 LTV |
| Activation Rate | Activation | Weekly | > 40% |
| D30 Retention | Retention | Weekly | > 20% |
| MRR Growth | Revenue | Monthly | > 10% MoM |
| K-Factor | Referral | Monthly | > 0.5 |
| NRR | Revenue | Monthly | > 100% |

## File Structure (Updated)

```
agents/growth/
├── cgo.md                              # Chief Growth Officer
│
├── acquisition/
│   ├── channel-strategist.md
│   ├── paid-ads-lead.md               # Lead Agent
│   ├── paid-ads/                      # Specialists
│   │   ├── meta-specialist.md
│   │   ├── google-specialist.md
│   │   ├── tiktok-specialist.md
│   │   └── performance-analyzer.md
│   ├── organic-lead.md                # Lead Agent
│   └── organic/                       # Specialists
│       ├── seo-specialist.md
│       ├── content-marketer.md
│       ├── community-manager.md
│       └── partnership-manager.md
│
├── activation/
│   ├── onboarding-designer.md
│   └── aha-moment-engineer.md
│
├── retention/
│   ├── cohort-analyst.md
│   ├── engagement-lead.md             # Lead Agent
│   ├── engagement/                    # Specialists
│   │   ├── notification-specialist.md
│   │   ├── email-marketing-specialist.md
│   │   └── gamification-designer.md
│   └── churn-preventer.md
│
├── revenue/
│   ├── monetization-optimizer.md
│   └── upsell-strategist.md
│
├── referral/
│   ├── viral-loop-designer.md
│   └── advocacy-builder.md
│
├── creative/
│   ├── ad-creative-director.md
│   ├── copy-lead.md                   # Lead Agent
│   └── copy/                          # Specialists
│       ├── ad-copywriter.md
│       ├── email-copywriter.md
│       ├── landing-page-copywriter.md
│       └── microcopy-writer.md
│
└── analytics/
    ├── growth-metrics-analyst.md
    └── growth-strategy-writer.md
```

## Agent Count Summary

| Category | Lead Agents | Specialists | Total |
|----------|-------------|-------------|-------|
| Acquisition | 2 (Paid, Organic) | 8 | 11 |
| Activation | - | - | 2 |
| Retention | 1 (Engagement) | 3 | 5 |
| Revenue | - | - | 2 |
| Referral | - | - | 2 |
| Creative | 1 (Copy) | 4 | 6 |
| Analytics | - | - | 2 |
| **Total** | **4** | **15** | **30+CGO** |

## Integration with Other Teams

### From CBO (Business Team)
- Business Plan
- Target Market Definition
- Competitive Analysis
- Budget Approval

### To CTO (Development Team)
- Feature requests for growth experiments
- Tracking/analytics requirements
- Landing page needs
- A/B test implementation

### From/To CEO
- Strategic alignment
- Resource requests
- Major decisions
- Performance reviews
