# Agent Company v5.1
## AI 에이전트 조직 시스템

> 4개 Division, 27개 AI 에이전트, 6개 Quality Gate, 3개 병렬 그룹.
> 아이디어 발굴(CBO) → 제품 개발(CTO) → 디자인(CDO) → 성장(CGO)까지 전 과정을 오케스트레이션.

---

## Quick Start

### 1. 프로젝트 규모 결정
```
workflows/tier-playbooks.md
```
5개 질문으로 Tier(1~4) 판단 → 필요한 에이전트만 활성화

### 2. 에이전트 파일 찾기
```
docs/AGENT-INDEX.md
```
전체 에이전트의 파일 위치, 역할, Tier별 매핑 인덱스

### 3. 워크플로우 실행
```
# Tier 1: 단일 스킬
/quick-builder

# Tier 2: 스킬 조합
/business-workflow → /prd-workflow-v2 → /supervisor-report-v2 → /growth-workflow

# Tier 3+: Full Pipeline Team
/project-launcher  # 또는 teams/team-playbook.md 참고하여 팀 생성
```

---

## Tier System

| Tier | 이름 | Agents | Timeline | 예시 |
|------|------|--------|----------|------|
| **1** | Quick Experiment | quick_builder | 8h | 랜딩페이지 검증, 해커톤 |
| **2** | Side Project | 15개 | ~70h (2주) | 개인 SaaS, 소규모 수익화 |
| **3** | Startup MVP | 27개 | ~300h (2개월) | 투자 유치 목표 MVP |
| **4** | Full Product | 27개 + 스프린트 | 6개월+ | 대규모 확장 |

---

## Organization Structure

```
CEO (Exception Handler)
│
├── CBO (Business) ────────── 5 agents
│   Pain Point Hunter, Competitor Analyst, BM Designer,
│   Business Planner, GTM Strategist
│
├── CTO (Development) ─────── 7 agents
│   PRD Architect, Scope Guard, Architect,
│   Frontend Engineer, Backend Engineer, Code Reviewer, DevOps
│
├── CDO (Design) ──────────── 6 agents
│   UI Designer, Visual Director, Image Generator,
│   Screenshot Designer, ASO Optimizer, Design-to-Code Bridge
│
└── CGO (Growth) ──────────── 8 agents
    Acquisition Strategist, Copy Strategist, Ads Operator,
    Content Creator, Onboarding Designer, Retention Manager,
    Revenue Optimizer, Growth Analyst
```

---

## Claude Code Skills (10개)

실제 개발 실행을 위한 워크플로우 스킬:

| Skill | 위치 | 용도 |
|-------|------|------|
| **business-workflow** | `skills/business-workflow/SKILL.md` | CBO 사업 검증 오케스트레이션 |
| **prd-workflow-v2** | `skills/prd-workflow-v2/SKILL.md` | 아이디어 → PRD → 기술 명세 |
| **project-launcher** | `skills/project-launcher/SKILL.md` | PRD → 개발 시작 연결 |
| **supervisor-report-v2** | `skills/supervisor-report-v2/SKILL.md` | 개발 오케스트레이션 |
| **design-system-workflow** | `skills/design-system-workflow/SKILL.md` | 디자인 시스템 구축 |
| **ux-improvement** | `skills/ux-improvement/SKILL.md` | UX 분석/개선 |
| **growth-workflow** | `skills/growth-workflow/SKILL.md` | 그로스 전략 오케스트레이션 |
| **feature-extension** | `skills/feature-extension/SKILL.md` | 기존 프로젝트 기능 추가 |
| **refactoring-workflow** | `skills/refactoring-workflow/SKILL.md` | 코드 구조 개선 |
| **context-manager** | `skills/context-manager/SKILL.md` | 세션간 컨텍스트 관리 |

### Skills 사용 흐름

```
[아이디어]
    ↓
business-workflow     → Pain Points + BM + Product Brief
    ↓
prd-workflow-v2       → PRD + 기술 명세 생성
    ↓
project-launcher      → 개발 계획 + 시작
    ↓
supervisor-report-v2  → 실제 개발 (FE + BE + Review)
    ↓
[디자인 필요 시] design-system-workflow / ux-improvement
    ↓
growth-workflow       → 채널 전략 + 카피 + 메트릭
    ↓
[기능 추가 시] feature-extension
[리팩토링 시] refactoring-workflow
```

---

## File Structure

```
.claude/
├── README.md                            # Source of Truth
│
├── agents/                              # 에이전트 정의 (5 files)
│   ├── ceo.md                           #   CEO: Exception Handler
│   ├── business/business-agents.md      #   CBO: 5 agents
│   ├── development/development-agents.md #  CTO: 7 agents
│   ├── design/design-agents.md          #   CDO: 6 agents
│   └── growth/growth-agents.md          #   CGO: 8 agents
│
├── system/                              # OpenClaw 실행 엔진 (11 files)
│   ├── agent-transitions.yaml           #   상태 머신
│   ├── parallel-groups.yaml             #   병렬 실행
│   ├── quality-gates.md                 #   품질 체크리스트
│   ├── quality-gates-auto.yaml          #   자동 검증 규칙
│   ├── agent-io-map.yaml               #   입출력 파일 경로
│   ├── prompt-assembly.yaml             #   프롬프트 변수 매핑
│   ├── state-mutations.yaml             #   project.json 변경 규칙
│   ├── human-checkpoints.yaml           #   사람 개입 지점
│   ├── context-persistence.md           #   .agent-state/ 관리
│   ├── feedback-loops.md                #   피드백 루프 + 롤백
│   └── cost-time-estimates.md           #   비용/시간 추정표
│
├── skills/                              # Claude Code 스킬 (10개)
│   ├── business-workflow/SKILL.md
│   ├── prd-workflow-v2/SKILL.md
│   ├── project-launcher/SKILL.md
│   ├── supervisor-report-v2/SKILL.md
│   ├── design-system-workflow/SKILL.md
│   ├── ux-improvement/SKILL.md
│   ├── growth-workflow/SKILL.md
│   ├── feature-extension/SKILL.md
│   ├── refactoring-workflow/SKILL.md
│   └── context-manager/SKILL.md
│
├── teams/
│   └── team-playbook.md                 #   5개 팀 템플릿
│
├── templates/                           # 핸드오프 템플릿 (6개)
│   ├── product-brief.md                 #   Gate 1: CBO → CTO
│   ├── design-upgrade-brief.md          #   Gate 3: CTO → CDO
│   ├── design-delivery.md               #   Gate 4: CDO → CTO
│   ├── store-assets-package.md          #   CDO → CGO
│   ├── launch-brief.md                  #   Gate 5: CTO → CGO
│   └── growth-insights.md               #   Gate 6: CGO → CEO
│
├── workflows/                           # 워크플로우 가이드
│   ├── tier-playbooks.md
│   ├── integrated-workflow.md
│   └── user-validation-gate.md
│
└── docs/                                # 참조 문서
    ├── README-agent-company.md          #   이 문서
    ├── AGENT-INDEX.md                   #   에이전트 인덱스
    └── agent-skills-index.md            #   스킬 인덱스
```

---

## Workflow Pipeline

```
[Phase 1: CBO — Business]
pain_point_hunter → competitor_analyst → bm_designer → business_planner → gtm_strategist
     └──────────────────────────────────────────────────→ Product Brief
                                                          ↓ Gate 1

[Phase 2: CTO — Development]
prd_architect → scope_guard → architect → parallel_dev (FE + BE) → code_reviewer → devops
     └──────────────────────────────────────────────────→ Design Upgrade Brief
                                                          ↓ Gate 3

[Phase 2.5: CDO — Design]
ui_designer → parallel_design (VD + IG) → screenshot_designer → aso_optimizer → bridge
     └──────────────────────────────────────────────────→ Design Delivery
                                                          ↓ Gate 4 → Gate 5

[Phase 3: CGO — Growth]
acquisition_strategist → copy_strategist → parallel_growth (Ads + Content)
→ onboarding_designer → retention_manager → revenue_optimizer → growth_analyst
     └──────────────────────────────────────────────────→ Growth Insights
                                                          ↓ Gate 6
                                                     CEO Decision
                                          (Continue / Iterate / Pivot / Kill)
```

---

## Handoff Documents

| 핸드오프 | 발신 | 수신 | 템플릿 |
|----------|------|------|--------|
| Product Brief | CBO | CTO | `templates/product-brief.md` |
| Design Upgrade Brief | CTO | CDO | `templates/design-upgrade-brief.md` |
| Design Delivery | CDO | CTO | `templates/design-delivery.md` |
| Store Assets Package | CDO | CGO | `templates/store-assets-package.md` |
| Launch Brief | CTO | CGO | `templates/launch-brief.md` |
| Growth Insights | CGO | CEO | `templates/growth-insights.md` |

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

상세 가이드: `teams/team-playbook.md`

---

## MCP Integration

| MCP Server | 용도 | 사용 에이전트 | Fallback |
|------------|------|-------------|----------|
| **figma-mcp** | Figma 디자인 읽기/쓰기 | UI Designer, Visual Director, Screenshot Designer, Bridge, Frontend | 텍스트 기반 design-delivery.md |
| **stitch-mcp** | Google Stitch AI UI 생성 | UI Designer, Visual Director, Screenshot Designer, Bridge | 텍스트 기반 디자인 명세 |
| **image-gen-server** | AI 이미지 생성 (Replicate) | Image Generator | Lucide/Heroicons |
| **store-screenshot-mcp** | 스토어 스크린샷 생성 | Screenshot Designer | Figma/Canva 수동 제작 |

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

## Related Documents

| 문서 | 설명 |
|------|------|
| [README](../README.md) | 시스템 개요 (Source of Truth) |
| [Agent Index](AGENT-INDEX.md) | 에이전트 통합 인덱스 |
| [Agent Skills Index](agent-skills-index.md) | 전체 스킬 파일 인덱스 |
| [Tier Playbooks](../workflows/tier-playbooks.md) | Tier별 실행 가이드 |
| [Team Playbook](../teams/team-playbook.md) | 5개 팀 템플릿 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 5.1 | 2026-02 | CDO Division 추가, 27 에이전트, 6 Gate, MCP, Agent Teams |
| 3.0 | 2024-02 | Project Scaler, Tier 시스템, Skills Index 추가 |
| 2.0 | 2024-02 | CGO 계층 구조화, 핸드오프 프로토콜 |
| 1.0 | 2024-02 | 초기 버전 (CBO, CTO, CGO 기본 구조) |
