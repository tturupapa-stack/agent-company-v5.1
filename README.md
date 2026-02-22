# Agent Company v5.1

> **compatible state machine** — 4개 Division, 27개 에이전트, 6개 Quality Gate, 3개 병렬 그룹

솔로 파운더가 아이디어 검증부터 런칭·그로스까지 전 과정을 에이전트 파이프라인으로 실행하는 시스템.

---

## Overview

```
CBO (5 agents)     CTO (7 agents)     CDO (6 agents)     CGO (8 agents)
시장 검증·BM 설계    PRD·설계·구현·배포    디자인·브랜딩·에셋    유저획득·리텐션·분석
      │                   │                   │                   │
      └──── Gate 1 ──→ ───┘──── Gate 3 ──→ ───┘──── Gate 5 ──→ ───┘──→ Gate 6 → CEO Decision
           CBO→CTO            CTO→CDO            CTO→CGO              CGO→CEO
```

| Division | Agents | 역할 |
|----------|--------|------|
| **CBO** | Pain Point Hunter, Competitor Analyst, BM Designer, Business Planner, GTM Strategist | 시장 검증 → Product Brief |
| **CTO** | PRD Architect, Scope Guard, Architect, Frontend Engineer, Backend Engineer, Code Reviewer, DevOps | PRD → 구현 → 배포 |
| **CDO** | UI Designer, Visual Director, Image Generator, Screenshot Designer, ASO Optimizer, Design-to-Code Bridge | 디자인 감사 → 브랜딩 → 에셋 → 토큰 변환 |
| **CGO** | Acquisition Strategist, Ads Operator, Content Creator, Onboarding Designer, Retention Manager, Revenue Optimizer, Copy Strategist, Growth Analyst | 유저 획득 → 리텐션 → 분석 |
| **CEO** | Exception Handler | 에스컬레이션, Go/No-Go, 롤백, 프로젝트 초기화 |

---

## Pipeline Flow

```
[CBO Phase]
pain_point_hunter → competitor_analyst → bm_designer → business_planner → gtm_strategist
    → Gate 1 (Product Brief)

[CTO Phase]
prd_architect → scope_guard → architect → quick_design_brief → parallel_dev
    ├── frontend_engineer  ──┐
    └── backend_engineer   ──┤→ code_reviewer → devops
                              → Gate 3 (Design Upgrade Brief)

[CDO Phase]
ui_designer → parallel_design
    ├── visual_director    ──┐
    └── image_generator    ──┤→ screenshot_designer → aso_optimizer → design_to_code_bridge
                              → Gate 4 (Design Delivery)

[CGO Phase]
acquisition_strategist → copy_strategist → parallel_growth
    ├── ads_operator (async) ┐
    └── content_creator    ──┤→ onboarding_designer → retention_manager → revenue_optimizer
                              → growth_analyst → Gate 6 (Growth Insights) → CEO Decision
```

---

## Parallel Groups

| Group | Members | Join 조건 | Timeout |
|-------|---------|----------|---------|
| **parallel_dev** | Frontend + Backend Engineer | 둘 다 완료 | 48h |
| **parallel_design** | Visual Director + Image Generator | 둘 다 완료 | 24h |
| **parallel_growth** | Ads Operator + Content Creator | Content만 (Ads는 비동기) | — |

---

## Quality Gates

| Gate | 핸드오프 | 필수 항목 | 실패 시 |
|------|---------|----------|--------|
| **Gate 1** | CBO → CTO | Problem 근거, Persona, MVP 3개, KPI 2개 | GTM 재작성 (max 2) |
| **Gate 2** | CTO 내부 | User Stories 3+, API, DB, 화면 + Scope Guard | PRD 재작성 |
| **Gate 3** | CTO → CDO | 프로토타입, 브랜드 키워드, 플랫폼, 범위, **MCP 상태** | 사용자 승인 |
| **Gate 4** | CDO → CTO | 디자인 토큰, **토큰 소스**, 컴포넌트, 에셋 | UI Designer 재시작 (max 3) |
| **Gate 5** | CTO → CGO | URL, 기능 설명, 트래킹, 타겟 | 자동 생성 |
| **Gate 6** | CGO → CEO | 메트릭 5개, 채널 비교, 전략 제안 | CEO Decision |

---

## MCP Integration

CDO + CTO Frontend에서 외부 디자인 도구와 연동.

| MCP Server | 용도 | 사용 에이전트 | Fallback |
|------------|------|-------------|----------|
| **figma-mcp** | Figma 디자인 읽기/쓰기, Variables/Styles | UI Designer, Visual Director, Screenshot Designer, Bridge, Frontend Engineer | 텍스트 기반 design-delivery.md |
| **stitch-mcp** | Google Stitch AI UI 생성, Figma 내보내기 | UI Designer, Visual Director, Screenshot Designer, Bridge | 텍스트 기반 디자인 명세 |
| **image-gen-server** | AI 이미지 생성 (Replicate) | Image Generator | Lucide/Heroicons 라이브러리 |
| **store-screenshot-mcp** | 스토어 스크린샷 생성 | Screenshot Designer | Figma/Canva 수동 제작 |

모든 MCP는 **optional** (image-gen-server만 Image Generator에서 required). 미연결 시 fallback 자동 적용.

---

## Tier System

| Tier | 규모 | 진입점 | 실행 방식 |
|------|------|--------|----------|
| **1** | 기능 1개, 8h | `quick_builder` | 단일 스킬 실행 |
| **2** | 기능 3개, 80h | `pain_point_hunter` | 개별 팀 순차 실행 |
| **3** | 기능 5개, 320h | `pain_point_hunter` | Full Pipeline Team |
| **4** | 기능 10개, 640h | `pain_point_hunter` | Full Pipeline + 스프린트 |

---

## Agent Teams

> `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 필요

| Team | 용도 | 팀원 | 예상 시간 |
|------|------|------|----------|
| **Business Discovery** | 시장 검증 → Product Brief | 3명 | 30-60분 |
| **Development** | PRD → 구현 → 배포 | 3명 | 2-8시간 |
| **Design** | 디자인 시스템 + 에셋 | 3명 | 1-2시간 |
| **Growth** | 마케팅 + 리텐션 + 분석 | 4명 | 1-3시간 |
| **Full Pipeline** | 아이디어 → 런칭 E2E | 4명 | 4-12시간 |

상세 가이드: [`teams/team-playbook.md`](teams/team-playbook.md)

---

## Directory Structure

```
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
    ├── AGENT-INDEX.md                   #   에이전트 인덱스
    └── agent-skills-index.md            #   스킬 인덱스
```

---

## Design Philosophy

### Anti-Generic-AI Design Rules
Frontend Engineer와 CDO 전체에 적용되는 7개 디자인 규칙:

1. 이모지를 UI 아이콘으로 사용 금지 — Lucide React, Heroicons 등 사용
2. Tailwind 기본 색상 직접 사용 금지 — 시맨틱 변수 사용
3. Inter/Roboto 무조건 사용 금지 — 앱 성격에 맞는 폰트 선택
4. 앱 목적에 맞는 톤/색상/레이아웃 설계 필수
5. 모든 요소에 동일 border-radius 금지 — 요소별 적절한 곡률 차등
6. 기본 그림자 없는 평면 디자인 금지 — 미묘한 depth와 입체감 적용
7. design-delivery.md 참조 필수 (없으면 자체 생성)

---

## Quick Start

```bash
# 1. Tier 판단
# workflows/tier-playbooks.md의 5-question quiz 참조

# 2. Tier별 실행
# Tier 1: 단일 스킬
/quick-builder

# Tier 2: 스킬 조합
/business-workflow → /prd-workflow-v2 → /supervisor-report-v2 → /growth-workflow

# Tier 3+: Full Pipeline Team
/project-launcher  # 또는 teams/team-playbook.md 참고하여 팀 생성

# 3. 자동 오케스트레이션 (OpenClaw)
# system/agent-transitions.yaml을 OpenClaw 엔진에 로드
```

---

## Runtime State

```
.agent-state/
├── project.json              # 프로젝트 상태 (CEO 관리)
├── outputs/                  # 에이전트 산출물 (31개 파일)
├── archive/v{N}/             # 롤백 시 아카이브
└── logs/
    └── decisions.md          # 기술/사업 결정 기록
```

---

## Human Checkpoints

| # | Checkpoint | Type | When |
|---|-----------|------|------|
| 1 | Gate 3: Design Brief | approval | CTO → CDO 전환 |
| 2 | Gate 4: Design Delivery | approval | CDO → CTO 전환 |
| 3 | User Validation | human_required | Tier 3+ 디자인 후 |
| 4 | Ads Operator | human_execute | 광고 캠페인 집행 |
| 5 | Growth Analyst | human_data | 메트릭 데이터 입력 |
| 6 | CEO Decision | approval | Go/No-Go 최종 결정 |

---

## Error Handling

```yaml
# 에이전트 실패
retry: max 1-2회 (에이전트별 상이)
escalate: CEO에 에스컬레이션 (max_retry 초과 시)
skip: skippable agents만 (visual_director, screenshot_designer, aso_optimizer,
      design_to_code_bridge, retention_manager, revenue_optimizer, ads_operator)

# 롤백
rollback_to_cbo: 전체 산출물 아카이브 후 CBO 재시작
rollback_to_cto: CDO/CGO 산출물 정리, PRD/아키텍처 보존
rollback_to_cdo: 디자인 산출물 재작성, 브리프 보존
max_rollback: Phase당 2회 (초과 시 CEO kill 판단)
```
