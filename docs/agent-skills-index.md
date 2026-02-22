# Agent Skills Index v5.1
## 전체 에이전트 스킬 파일 참조

이 문서는 모든 에이전트의 스킬 파일 위치와 핵심 역할을 인덱싱합니다.
각 에이전트 파일에는 상세한 프롬프트 템플릿, Input/Output 정의, 실행 가이드가 포함되어 있습니다.

> **5개 에이전트 파일, 27개 에이전트, 10개 스킬**

---

## File Structure Overview

```
agents/
├── ceo.md                              # CEO: Exception Handler (1 agent)
├── business/
│   └── business-agents.md              # CBO: 5 agents
├── development/
│   └── development-agents.md           # CTO: 7 agents
├── design/
│   └── design-agents.md                # CDO: 6 agents
└── growth/
    └── growth-agents.md                # CGO: 8 agents
```

---

## CEO (1 agent)

| Agent | File | 핵심 역할 |
|-------|------|----------|
| **CEO** | `agents/ceo.md` | 에스컬레이션, Go/No-Go, 롤백, 프로젝트 초기화 |

---

## CBO Division — Business (5 agents, 1 file)

| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Pain Point Hunter | `agents/business/business-agents.md` | 유저 페인 포인트 발굴 | Reddit/Forum 크롤링, 테마 분류, 기회 점수화 | 1+ |
| Competitor Analyst | `agents/business/business-agents.md` | 경쟁사 분석, 갭 식별 | Feature Matrix, 포지셔닝 맵, SWOT | 2+ |
| BM Designer | `agents/business/business-agents.md` | 수익 모델, 가격 설계 | Business Model Canvas, Unit Economics | 2+ |
| Business Planner | `agents/business/business-agents.md` | 사업 계획서 작성 | 투자자 관점, Executive Summary | 2+ |
| GTM Strategist | `agents/business/business-agents.md` | 시장 진입 전략, Product Brief | 채널 전략, 런칭 플랜, 핸드오프 문서 | 2+ |

---

## CTO Division — Development (7 agents, 1 file)

| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| PRD Architect | `agents/development/development-agents.md` | PRD 작성, User Story | User Story 형식, Acceptance Criteria | 1+ |
| Scope Guard | `agents/development/development-agents.md` | MVP 범위 검증 | 범위 체크리스트, 타임라인 검증 | 2+ |
| Architect | `agents/development/development-agents.md` | 기술 아키텍처, API/DB 설계 | 시스템 설계, API 스펙, DB 스키마 | 2+ |
| Frontend Engineer | `agents/development/development-agents.md` | UI 구현 | React/Next.js, Anti-Generic-AI 규칙 | 1+ |
| Backend Engineer | `agents/development/development-agents.md` | API 개발, DB 작업 | REST API, 인증, 외부 연동 | 1+ |
| Code Reviewer | `agents/development/development-agents.md` | 코드 품질 관리 | 리뷰 체크리스트, 보안, 성능 | 2+ |
| DevOps | `agents/development/development-agents.md` | CI/CD, 배포, 모니터링 | GitHub Actions, Vercel/AWS, Sentry | 2+ |

---

## CDO Division — Design (6 agents, 1 file)

| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| UI Designer | `agents/design/design-agents.md` | 디자인 감사, UI 시스템 | Figma MCP, 디자인 토큰, Anti-Generic-AI | 2+ |
| Visual Director | `agents/design/design-agents.md` | 브랜딩, 비주얼 가이드 | 색상 팔레트, 타이포그래피, 이미지 스타일 | 3+ (skippable) |
| Image Generator | `agents/design/design-agents.md` | AI 이미지/아이콘 생성 | Replicate MCP, 프롬프트 설계 | 2+ |
| Screenshot Designer | `agents/design/design-agents.md` | 스토어 스크린샷 | 앱스토어 가이드라인, 스크린샷 구성 | 2+ (skippable) |
| ASO Optimizer | `agents/design/design-agents.md` | 앱스토어 최적화 | 키워드, 메타데이터, A/B 테스트 | 2+ (skippable) |
| Design-to-Code Bridge | `agents/design/design-agents.md` | 디자인 토큰 → 코드 변환 | CSS 변수, Tailwind 매핑 | 2+ (skippable) |

---

## CGO Division — Growth (8 agents, 1 file)

| Agent | File | 핵심 역할 | 핵심 스킬 | Tier |
|-------|------|----------|----------|------|
| Acquisition Strategist | `agents/growth/growth-agents.md` | 성장 채널 선정, CAC 예측 | ICE 스코어링, 채널 매트릭스 | 2+ |
| Copy Strategist | `agents/growth/growth-agents.md` | 마케팅 카피, 메시지 전략 | AIDA, PAS, 채널별 카피 | 2+ |
| Ads Operator | `agents/growth/growth-agents.md` | 광고 캠페인 집행 | Meta/Google/TikTok, 예산 관리 | 3+ (skippable) |
| Content Creator | `agents/growth/growth-agents.md` | 콘텐츠 마케팅 | 블로그, SNS, SEO 콘텐츠 | 2+ |
| Onboarding Designer | `agents/growth/growth-agents.md` | 온보딩 플로우 설계 | 온보딩 패턴, 드롭오프 분석 | 2+ |
| Retention Manager | `agents/growth/growth-agents.md` | 리텐션 전략 | 코호트 분석, 이탈 방지, 참여 루프 | 3+ (skippable) |
| Revenue Optimizer | `agents/growth/growth-agents.md` | 수익 최적화, 가격 전략 | ARPU, 업셀, 가격 심리학 | 3+ (skippable) |
| Growth Analyst | `agents/growth/growth-agents.md` | AARRR 메트릭, Growth Insights | KPI 대시보드, 실험 분석, 전략 리포트 | 2+ |

---

## Tier별 Active Agents 요약

### Tier 1: Quick Experiment
```
quick_builder (단일 스킬, 8시간)
```

### Tier 2: Side Project (15 agents)
```
CEO
├── CBO (5): Pain Point Hunter, Competitor Analyst, BM Designer,
│            Business Planner, GTM Strategist
├── CTO (5): PRD Architect, Scope Guard, Frontend Engineer,
│            Backend Engineer, Code Reviewer
├── CDO (3): UI Designer, Image Generator, Screenshot Designer
└── CGO (2): Acquisition Strategist, Copy Strategist
```

### Tier 3: Startup MVP (27 agents)
```
전체 에이전트 활성화
CEO + CBO (5) + CTO (7) + CDO (6) + CGO (8)
```

### Tier 4: Full Product (27 agents + 스프린트)
```
Tier 3 전체 + 2주 스프린트 사이클
매 스프린트마다 CGO → CTO 피드백 루프
분기별 CBO 전략 리뷰
```

---

## 워크플로우 스킬 (10개)

```
skills/
├── business-workflow/SKILL.md       # CBO: 사업 검증
├── prd-workflow-v2/SKILL.md         # CTO: PRD 생성 + 채점
├── project-launcher/SKILL.md        # CTO: PRD → 개발 연결
├── supervisor-report-v2/SKILL.md    # CTO: 개발 오케스트레이션
├── design-system-workflow/SKILL.md  # CDO: 디자인 시스템 구축
├── ux-improvement/SKILL.md          # CDO: UI/UX 개선
├── growth-workflow/SKILL.md         # CGO: 그로스 전략
├── feature-extension/SKILL.md       # 유지보수: 기능 추가
├── refactoring-workflow/SKILL.md    # 유지보수: 리팩토링
└── context-manager/SKILL.md         # 시스템: 컨텍스트 관리
```

---

## Parallel Groups

| Group | Members | Join 조건 | Timeout |
|-------|---------|----------|---------|
| **parallel_dev** | Frontend + Backend Engineer | 둘 다 완료 | 48h |
| **parallel_design** | Visual Director + Image Generator | 둘 다 완료 | 24h |
| **parallel_growth** | Ads Operator + Content Creator | Content만 (Ads는 비동기) | — |

---

## Skippable Agents (7개)

Tier 또는 상황에 따라 건너뛸 수 있는 에이전트:

| Agent | Division | 스킵 조건 |
|-------|----------|----------|
| Visual Director | CDO | Tier 2 이하 또는 브랜딩 불필요 |
| Screenshot Designer | CDO | 스토어 등록 불필요 시 |
| ASO Optimizer | CDO | 앱스토어 최적화 불필요 시 |
| Design-to-Code Bridge | CDO | 디자인 토큰 직접 적용 시 |
| Retention Manager | CGO | 초기 단계, 리텐션 미측정 시 |
| Revenue Optimizer | CGO | 무료 서비스 또는 초기 단계 |
| Ads Operator | CGO | 광고 예산 없음 시 |

---

## 스킬 파일 공통 구조

각 에이전트 정의에 포함된 내용:

```markdown
# [Agent Name]

## Role
[역할 설명]

## Input
[must_read / optional 파일 목록]

## Output
[산출물 파일 목록]

## Prompt Template
[실행용 프롬프트]

## Quality Criteria
[품질 기준]

## Handoff Protocol
[핸드오프 규칙]
```

### Division별 특징

| Division | 특징 |
|----------|------|
| **CBO** | 시장 분석 프레임워크, 비즈니스 모델 캔버스, 재무 모델 |
| **CTO** | 기술 스펙 템플릿, 코드 리뷰 체크리스트, Anti-Generic-AI 규칙 |
| **CDO** | MCP 연동, 디자인 토큰, 브랜딩 가이드, 에셋 생성 |
| **CGO** | 채널 전략, 카피 공식, AARRR 메트릭 벤치마크 |

---

## 사용 방법

### 1. Tier 판단
`workflows/tier-playbooks.md` 참조하여 프로젝트 Tier 결정

### 2. Active Agents 확인
이 문서에서 해당 Tier의 Active Agents 목록 확인

### 3. 에이전트 파일 참조
필요한 에이전트의 파일을 열어 프롬프트 템플릿 사용

### 4. 워크플로우 실행
스킬 또는 OpenClaw 상태 머신으로 실행

---

## 관련 문서

| 문서 | 위치 | 용도 |
|------|------|------|
| README | `README.md` | 시스템 개요 (Source of Truth) |
| Agent Index | `docs/AGENT-INDEX.md` | 에이전트 통합 인덱스 |
| Tier Playbooks | `workflows/tier-playbooks.md` | Tier별 실행 가이드 |
| Team Playbook | `teams/team-playbook.md` | 5개 팀 템플릿 |
| Handoff Templates | `templates/` | 핸드오프 문서 템플릿 (6개) |
