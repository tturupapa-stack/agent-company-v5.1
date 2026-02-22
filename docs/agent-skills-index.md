# Agent Skills Index
## 전체 에이전트 스킬 파일 참조

이 문서는 모든 에이전트의 스킬 파일 위치와 핵심 역할을 인덱싱합니다.
각 에이전트 파일에는 상세한 프롬프트 템플릿, Input/Output 정의, 실행 가이드가 포함되어 있습니다.

> **총 45개 스킬 파일, 55개 에이전트**

---

## 📁 File Structure Overview

```
agents/
├── ceo/
│   └── ceo.md                          # 전체 오케스트레이터
├── business/                           # CBO Division (12 agents, 4 files)
│   ├── cbo.md
│   ├── research/research-agents.md     # 4 agents
│   ├── strategy/strategy-agents.md     # 4 agents
│   └── documentation/documentation-agents.md  # 2 agents
├── development/                        # CTO Division (10 agents, 4 files)
│   ├── cto.md
│   ├── product/product-agents.md       # 2 agents
│   ├── engineering/engineering-agents.md  # 4 agents
│   └── operations/operations-agents.md # 3 agents
└── growth/                             # CGO Division (31 agents, 36 files)
    ├── cgo.md
    ├── acquisition/                    # 11 agents, 11 files
    ├── activation/                     # 2 agents, 2 files
    ├── retention/                      # 5 agents, 6 files
    ├── revenue/                        # 2 agents, 2 files
    ├── referral/                       # 2 agents, 2 files
    ├── creative/                       # 6 agents, 7 files
    └── analytics/                      # 2 agents, 2 files
```

---

## 🏢 CEO (1 agent)

| Agent | File | 핵심 역할 |
|-------|------|----------|
| **CEO** | `/agents/ceo/ceo.md` | 전체 프로젝트 오케스트레이션, Tier 판단, 부서간 조율 |

---

## 💼 CBO Division - Business (12 agents, 4 files)

### Division Lead
| Agent | File | 핵심 역할 |
|-------|------|----------|
| **CBO** | `/agents/business/cbo.md` | 사업팀 총괄, 핸드오프 관리 |

### Research Division (4 agents)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Trend Scout | `/agents/business/research/research-agents.md` | 기술/소비자 트렌드 탐색 | 트렌드 리포트, 기회 영역 도출 | 3+ |
| Market Analyzer | `/agents/business/research/research-agents.md` | TAM/SAM/SOM 시장 분석 | 시장 규모 추정, 지역별 분석, 세분화 | 3+ |
| Competitor Analyst | `/agents/business/research/research-agents.md` | 경쟁사 분석, 갭 식별 | Feature Matrix, 포지셔닝 맵, SWOT | 2+ |
| Pain Point Hunter | `/agents/business/research/research-agents.md` | Reddit/Forum 유저 불만 수집 | 소스 크롤링, 테마 분류, 기회 점수화 | 1+ |

### Strategy Division (4 agents)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Opportunity Scorer | `/agents/business/strategy/strategy-agents.md` | 기회 평가 및 우선순위 | 다차원 스코어링 (시장/경쟁/실현성) | 3+ |
| BM Designer | `/agents/business/strategy/strategy-agents.md` | 비즈니스 모델 설계 | Business Model Canvas, 가격 전략 | 2+ |
| Financial Modeler | `/agents/business/strategy/strategy-agents.md` | 재무 예측, Unit Economics | 3년 예측, CAC/LTV, 손익분기점 | 3+ |
| GTM Strategist | `/agents/business/strategy/strategy-agents.md` | 시장 진입 전략, Product Brief 작성 | 채널 전략, 런칭 플랜, 핸드오프 문서 | 3+ |

### Documentation Division (2 agents)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Research Report Writer | `/agents/business/documentation/documentation-agents.md` | 시장 리서치 보고서 작성 | Executive Summary, 인사이트 종합 | 3+ |
| Business Plan Writer | `/agents/business/documentation/documentation-agents.md` | 사업 계획서 작성 | 10섹션 구조, 투자자 관점 | 2+ |

---

## 💻 CTO Division - Development (10 agents, 4 files)

### Division Lead
| Agent | File | 핵심 역할 |
|-------|------|----------|
| **CTO** | `/agents/development/cto.md` | 개발팀 총괄, Launch Brief 관리 |

### Product Division (2 agents)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| PRD Architect | `/agents/development/product/product-agents.md` | PRD 작성, User Story 정의 | User Story 형식, Acceptance Criteria, 기능 명세 | 1+ |
| Scope Guard | `/agents/development/product/product-agents.md` | MVP 범위 검증, 피처 크립 방지 | 범위 체크리스트, 타임라인 검증, 에스컬레이션 | 2+ |

### Engineering Division (4 agents)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Architect | `/agents/development/engineering/engineering-agents.md` | 기술 아키텍처, API/DB 설계 | 시스템 설계, API 스펙, DB 스키마 | 2+ |
| Frontend Engineer | `/agents/development/engineering/engineering-agents.md` | UI 구현, React/Next.js | 컴포넌트 설계, 상태 관리, 반응형 | 1+ |
| Backend Engineer | `/agents/development/engineering/engineering-agents.md` | API 개발, DB 작업 | REST API, 인증, 외부 연동 | 1+ |
| Code Reviewer | `/agents/development/engineering/engineering-agents.md` | 코드 품질 관리 | 리뷰 체크리스트, 보안, 성능 | 2+ |

### Operations Division (3 agents)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Test Writer | `/agents/development/operations/operations-agents.md` | Unit/E2E 테스트 작성 | Jest, Playwright, 커버리지 관리 | 3+ |
| Doc Writer | `/agents/development/operations/operations-agents.md` | API 문서, Launch Brief 작성 | OpenAPI, README, 핸드오프 문서 | 2+ |
| DevOps Engineer | `/agents/development/operations/operations-agents.md` | CI/CD, 배포, 모니터링 | GitHub Actions, Vercel/AWS, Sentry | 3+ |

---

## 📈 CGO Division - Growth (31 agents, 36 files)

### Division Lead
| Agent | File | 핵심 역할 |
|-------|------|----------|
| **CGO** | `/agents/growth/cgo.md` | 그로스팀 총괄, AARRR 전략 |

### Acquisition Division (11 agents, 11 files)

#### Direct Reports
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Channel Strategist | `/agents/growth/acquisition/channel-strategist.md` | 채널 믹스 전략, CAC 예측 | ICE 스코어링, 채널 매트릭스, CAC 예측 모델 | 1+ |

#### Paid Ads Team (Lead + 4 Specialists)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| **Paid Ads Lead** | `/agents/growth/acquisition/paid-ads-lead.md` | 유료 광고 전략, 예산 배분 | 크로스 플랫폼 전략, 예산 배분 모델, 서브에이전트 호출 | 2+ |
| ↳ Meta Specialist | `/agents/growth/acquisition/paid-ads/meta-specialist.md` | Facebook/Instagram 광고 | Advantage+, Pixel/CAPI, Lookalike, 캠페인 구조 | 3+ |
| ↳ Google Specialist | `/agents/growth/acquisition/paid-ads/google-specialist.md` | Search/Display/YouTube 광고 | RSA, Performance Max, 키워드 전략, 입찰 전략 | 3+ |
| ↳ TikTok Specialist | `/agents/growth/acquisition/paid-ads/tiktok-specialist.md` | TikTok 광고, Spark Ads | 훅 전략, 네이티브 포맷, Spark Ads 설정 | 3+ |
| ↳ Performance Analyzer | `/agents/growth/acquisition/paid-ads/performance-analyzer.md` | 크로스 플랫폼 성과 분석 | 통합 메트릭, 예산 재배분, 주간/월간 리포트 | 3+ |

#### Organic Team (Lead + 4 Specialists)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| **Organic Lead** | `/agents/growth/acquisition/organic-lead.md` | 오가닉 채널 전략 | 채널 시너지, 런칭 조율, 서브에이전트 호출 | 2+ |
| ↳ SEO Specialist | `/agents/growth/acquisition/organic/seo-specialist.md` | 검색 엔진 최적화 | Technical SEO, 키워드 리서치, 링크 빌딩 | 3+ |
| ↳ Content Marketer | `/agents/growth/acquisition/organic/content-marketer.md` | 콘텐츠 전략, 캘린더 | Content Pillars, TOFU/MOFU/BOFU, 배포 전략 | 3+ |
| ↳ Community Manager | `/agents/growth/acquisition/organic/community-manager.md` | Reddit, Product Hunt | 커뮤니티 규칙, PH 런칭 체크리스트 | 3+ |
| ↳ Partnership Manager | `/agents/growth/acquisition/organic/partnership-manager.md` | 인플루언서, 제휴 | 파트너십 구조, 어필리에이트 프로그램 | 4 |

#### Solo Mode Agent (Tier 2 전용)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Paid Ads Manager | `/agents/growth/acquisition/paid-ads-manager.md` | 유료 광고 (단일 에이전트) | 멀티 플랫폼 기초, A/B 테스트 | 2 only |
| Organic Growth Hacker | `/agents/growth/acquisition/organic-growth-hacker.md` | 오가닉 성장 (단일 에이전트) | SEO 기초, 콘텐츠, 커뮤니티 | 2 only |

### Activation Division (2 agents, 2 files)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Onboarding Designer | `/agents/growth/activation/onboarding-designer.md` | 온보딩 플로우 설계 | 온보딩 패턴, 드롭오프 분석, 진행률 지표 | 2+ |
| Aha Moment Engineer | `/agents/growth/activation/aha-moment-engineer.md` | Aha Moment 정의, 최적화 | Aha Moment 프레임워크, Time-to-Value, 상관관계 분석 | 3+ |

### Retention Division (5 agents, 6 files)

| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Cohort Analyst | `/agents/growth/retention/cohort-analyst.md` | 코호트 분석, 리텐션 커브 | 코호트 테이블, 리텐션 커브, 행동 패턴 상관관계 | 3+ |
| Churn Preventer | `/agents/growth/retention/churn-preventer.md` | 이탈 예측, 개입 플레이북 | Churn 시그널, 리스크 스코어링, 개입 자동화 | 4 |
| Engagement Strategist | `/agents/growth/retention/engagement-strategist.md` | 참여 루프 설계 (Solo) | Habit Loop, 참여 메트릭, 게이미피케이션 기초 | 2 only |

#### Engagement Team (Lead + 3 Specialists)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| **Engagement Lead** | `/agents/growth/retention/engagement-lead.md` | 참여 전략, 채널 조율 | 크로스 채널 조율, 빈도 최적화, 서브에이전트 호출 | 3+ |
| ↳ Notification Specialist | `/agents/growth/retention/engagement/notification-specialist.md` | 푸시/인앱 알림 | 푸시 타이밍, 인앱 메시지 타입, 빈도 캡 | 4 |
| ↳ Email Marketing Specialist | `/agents/growth/retention/engagement/email-marketing-specialist.md` | 이메일 자동화 | 라이프사이클 시퀀스, 트리거 이메일, 세그멘테이션 | 4 |
| ↳ Gamification Designer | `/agents/growth/retention/engagement/gamification-designer.md` | 게이미피케이션 설계 | 진행 시스템, 성취, 스트릭, 리워드 | 4 |

### Revenue Division (2 agents, 2 files)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Monetization Optimizer | `/agents/growth/revenue/monetization-optimizer.md` | 가격 전략, ARPU 최적화 | 가격 심리학, 티어 설계, 가격 테스트 | 3+ |
| Upsell Strategist | `/agents/growth/revenue/upsell-strategist.md` | 업셀/크로스셀 캠페인 | 업그레이드 트리거, Account Expansion, NRR | 4 |

### Referral Division (2 agents, 2 files)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Viral Loop Designer | `/agents/growth/referral/viral-loop-designer.md` | 바이럴 루프, K-Factor | 바이럴 메커니즘, K-Factor 계산, 공유 트리거 | 4 |
| Advocacy Builder | `/agents/growth/referral/advocacy-builder.md` | 브랜드 옹호자, UGC | 옹호자 식별, UGC 프로그램, 리뷰 전략 | 4 |

### Creative Division (6 agents, 7 files)

| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Ad Creative Director | `/agents/growth/creative/ad-creative-director.md` | 크리에이티브 전략, 비주얼 | 크리에이티브 프레임워크, A/B 테스트 설계, 브랜드 일관성 | 4 |
| Copywriter | `/agents/growth/creative/copywriter.md` | 카피 전체 (Solo) | AIDA, PAS, 헤드라인 공식 | 2 only |

#### Copy Team (Lead + 4 Specialists)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| **Copy Lead** | `/agents/growth/creative/copy-lead.md` | 메시지 전략, 톤 가이드 | 메시지 프레임워크, Voice Guidelines, 서브에이전트 호출 | 2+ |
| ↳ Ad Copywriter | `/agents/growth/creative/copy/ad-copywriter.md` | 광고 헤드라인, 소셜 카피 | 플랫폼별 글자 수, 훅 타입, CTA 공식 | 3+ |
| ↳ Email Copywriter | `/agents/growth/creative/copy/email-copywriter.md` | 이메일 시퀀스, 뉴스레터 | Subject line 공식, 시퀀스 템플릿, A/B 테스트 | 3+ |
| ↳ Landing Page Copywriter | `/agents/growth/creative/copy/landing-page-copywriter.md` | LP 카피, 세일즈 페이지 | 페이지 구조, 헤드라인 공식, FAQ 설계 | 1+ |
| ↳ Microcopy Writer | `/agents/growth/creative/copy/microcopy-writer.md` | UI 텍스트, 푸시 알림 | 버튼, 에러메시지, Empty State, 토스트 | 4 |

### Analytics Division (2 agents, 2 files)
| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Growth Metrics Analyst | `/agents/growth/analytics/growth-metrics-analyst.md` | KPI 대시보드, 실험 분석 | AARRR 메트릭, 통계적 유의성, 대시보드 설계 | 2+ |
| Growth Strategy Writer | `/agents/growth/analytics/growth-strategy-writer.md` | 전략 문서, Growth Insights | 전략 문서 구조, 분기 리뷰, 플레이북 작성 | 3+ |

---

## 📊 Tier별 Active Agents 요약

### Tier 1: Quick Experiment (8 agents)
```
CEO (lite)
├── CBO: Pain Point Hunter
├── CTO: PRD Architect (lite), Frontend Engineer, Backend Engineer
└── CGO: Channel Strategist (lite), Landing Page Copywriter
```

**스킬 파일:**
- `/agents/business/research/research-agents.md` → Pain Point Hunter 섹션
- `/agents/development/product/product-agents.md` → PRD Architect 섹션
- `/agents/development/engineering/engineering-agents.md` → Frontend/Backend 섹션
- `/agents/growth/acquisition/channel-strategist.md`
- `/agents/growth/creative/copy/landing-page-copywriter.md`

### Tier 2: Side Project (18 agents)
```
CEO
├── CBO: Pain Point Hunter, Competitor Analyst, BM Designer, Business Plan Writer
├── CTO: PRD Architect, Scope Guard, Architect, Frontend, Backend, Code Reviewer, Doc Writer
└── CGO: Channel Strategist, Paid Ads Lead (solo), Organic Lead (solo), 
         Onboarding Designer, Copy Lead (solo), Growth Metrics Analyst
```

**추가 스킬 파일:**
- `/agents/business/research/research-agents.md` → Competitor Analyst 섹션
- `/agents/business/strategy/strategy-agents.md` → BM Designer 섹션
- `/agents/development/product/product-agents.md` → Scope Guard 섹션
- `/agents/growth/acquisition/paid-ads-lead.md`
- `/agents/growth/acquisition/organic-lead.md`
- `/agents/growth/creative/copy-lead.md`

### Tier 3: Startup MVP (35 agents)
```
전체 CBO + 전체 CTO + CGO (Referral 제외, Specialist 선택적)
```

**추가 스킬 파일:**
- 플랫폼 Specialist 2개 선택 (예: Meta + Google)
- Copy Specialist 2개 선택 (예: Ad + LP)
- Organic Specialist 2개 선택 (예: SEO + Content)

### Tier 4: Full Product (55 agents)
```
전체 에이전트 활성화
```

**모든 스킬 파일 사용**

---

## 🔍 스킬 파일 상세 내용

각 스킬 파일에 포함된 내용:

### 공통 구조
```markdown
# [Agent Name]

## Role
[역할 설명]

## Position in Hierarchy
[조직 내 위치]

## Responsibilities
[책임 목록]

## Input/Output
[입력과 출력 정의]

## Frameworks/Methods
[사용하는 프레임워크]

## Prompt Template
[실행용 프롬프트]

## Handoff Protocol
[핸드오프 규칙]
```

### 스킬 파일 특징

| Division | 특징 |
|----------|------|
| **CBO** | 시장 분석 프레임워크, 비즈니스 모델 캔버스, 재무 모델 |
| **CTO** | 기술 스펙 템플릿, 코드 리뷰 체크리스트, PRD 구조 |
| **CGO** | 플랫폼별 광고 설정, 카피 공식, 메트릭 벤치마크 |

---

## 📌 사용 방법

### 1. Tier 판단
`/docs/project-scaler.md` 참조하여 프로젝트 Tier 결정

### 2. Active Agents 확인
이 문서에서 해당 Tier의 Active Agents 목록 확인

### 3. 스킬 파일 참조
필요한 에이전트의 스킬 파일을 열어 프롬프트 템플릿 사용

### 4. 워크플로우 실행
`/docs/integrated-workflow.md`의 Phase별 순서대로 진행

---

## 📎 관련 문서

| 문서 | 위치 | 용도 |
|------|------|------|
| Project Scaler | `/docs/project-scaler.md` | Tier 판단, 에이전트 선택 |
| Integrated Workflow | `/docs/integrated-workflow.md` | 전체 워크플로우 |
| Growth Team Workflow | `/docs/growth-team-workflow.md` | CGO 상세 워크플로우 |
| Handoff Templates | `/templates/handoff/` | 핸드오프 문서 템플릿 |
| Context Schema | `/context/SCHEMA.md` | 공유 컨텍스트 구조 |
