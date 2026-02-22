# Agent Company v5.1

> **OpenClaw 자동화 호환** — 상태 머신 기반 32 에이전트 오케스트레이션 시스템
>
> v5.1 최종 업데이트: P0/P1 피드백 반영
> - CEO: 라우팅 제거 → 예외처리/의사결정 전용 재정의
> - 모든 에이전트: `on_max_retry_exceeded` 기본값 (escalate_to_ceo)
> - 롤백: 산출물 archive → clear 규칙 (3단계: CBO/CTO/CDO)
> - Skills: transitions와 역할 분리 (Claude Code 단축키로 재포지셔닝)
> - Quality Gates: LLM 시맨틱 검증 옵션 (hybrid: pattern + Claude Haiku)

## v5 → v5.1 핵심 변경

| 항목 | v5 | v5.1 |
|------|----|----|
| 에이전트 전환 | 자연어 ("완성되면 다음으로") | **YAML 상태 머신 (trigger→execute→next)** |
| Input/Output | 에이전트 파일에 흩어짐 | **agent-io-map.yaml에 통합** |
| 프롬프트 조립 | [paste X] 수동 | **prompt-assembly.yaml (변수→출처 매핑)** |
| 상태 업데이트 | 암묵적 | **state-mutations.yaml (필드별 명시)** |
| 사람 개입 | 구분 없음 | **human-checkpoints.yaml (6개 체크포인트)** |
| 병렬 실행 | "병렬 가능"만 언급 | **parallel-groups.yaml (시작/합류/에러)** |
| CDO 포맷 | v4 복붙 (불일치) | **CBO/CTO/CGO와 동일 포맷** |
| 빈 템플릿 | 4개 미완성 | **6개 전체 완성** |

## Architecture

```
v5/
├── agents/                          # 에이전트 정의 (프롬프트 + I/O + 판단 기준)
│   ├── ceo.md                       #   CEO 오케스트레이터
│   ├── business/business-agents.md  #   CBO: 5 agents
│   ├── development/development-agents.md  # CTO: 7 agents
│   ├── design/design-agents.md      #   CDO: 6 agents (v5.1 재작성)
│   └── growth/growth-agents.md      #   CGO: 8 agents
│
├── system/                          # OpenClaw 실행 엔진 (★ v5.1 핵심)
│   ├── agent-transitions.yaml       #   전체 상태 머신 (trigger→next)
│   ├── agent-io-map.yaml           #   모든 에이전트의 입출력 파일 경로
│   ├── prompt-assembly.yaml        #   프롬프트 변수 → 값 출처 매핑
│   ├── state-mutations.yaml        #   project.json 변경 규칙
│   ├── human-checkpoints.yaml      #   사람 개입 지점 + 재개 조건
│   ├── parallel-groups.yaml        #   병렬 실행 시작/합류 조건
│   ├── quality-gates.md            #   핸드오프 품질 체크리스트 (사람용)
│   ├── quality-gates-auto.yaml    #   자동 검증 규칙 (OpenClaw용)
│   ├── context-persistence.md      #   .agent-state/ 관리 방법
│   ├── feedback-loops.md           #   피드백 루프 + 롤백 조건
│   └── cost-time-estimates.md      #   비용/시간 추정표
│
├── workflows/                       # 워크플로우 가이드
│   ├── integrated-workflow.md       #   전체 라이프사이클
│   ├── tier-playbooks.md           #   Tier별 실행 플레이북
│   └── user-validation-gate.md     #   유저 검증 프로토콜
│
├── templates/                       # 핸드오프 문서 템플릿 (6개 전체 완성)
│   ├── product-brief.md            #   CBO → CTO
│   ├── design-upgrade-brief.md     #   CTO → CDO
│   ├── design-delivery.md          #   CDO → CTO
│   ├── store-assets-package.md     #   CDO → CGO
│   ├── launch-brief.md             #   CTO → CGO
│   └── growth-insights.md          #   CGO → CBO/CEO
│
├── skills/                          # Claude Code 워크플로우
│   ├── quick-builder.md            #   Tier 1 단일 프롬프트
│   ├── prd-workflow.md             #   PRD 생성 체인
│   ├── supervisor.md               #   개발 오케스트레이션
│   ├── feature-extension.md        #   기능 추가
│   └── refactoring.md              #   리팩토링
│
└── mcp/
    └── mcp-setup.md                #   MCP 의존성 + fallback + health check
```

## OpenClaw 실행 흐름

```
1. OpenClaw reads: system/agent-transitions.yaml (전체 상태 머신)
2. For each agent:
   a. Check trigger condition
   b. Read input files (from agent-io-map.yaml)
   c. Assemble prompt (from prompt-assembly.yaml)
   d. Execute (ai_autonomous / human_required / etc.)
   e. Validate output (completion_check in transitions)
   f. Update state (from state-mutations.yaml)
   g. Route to next agent (on_complete / on_fail)
3. At human checkpoints: pause, show prompt, wait for input
4. At parallel groups: fork, track, join per parallel-groups.yaml
```

## Data Flow

```
.agent-state/
├── project.json              # 프로젝트 상태 (CEO 관리)
├── outputs/                  # 29개 산출물 파일
│   ├── pain-points.md        ─→ competitor-analysis.md
│   ├── competitor-analysis.md ─→ business-model.md
│   ├── business-model.md     ─→ business-plan.md
│   ├── business-plan.md      ─→ product-brief.md
│   ├── product-brief.md      ─→ [Gate 1] ─→ prd.md
│   ├── prd.md                ─→ scope-review.md ─→ architecture.md
│   ├── architecture.md       ─→ frontend-complete.md + backend-complete.md
│   ├── code-review.md        ─→ deployment-config.md
│   ├── design-upgrade-brief.md ─→ design-audit.md ─→ brand-identity.md
│   ├── generated-assets.md   ─→ store-screenshots.md ─→ aso-recommendations.md
│   ├── design-delivery.md    ─→ [Gate 4] ─→ CTO 적용
│   ├── store-assets-package.md ─→ CGO
│   ├── launch-brief.md       ─→ acquisition-strategy.md
│   ├── copy-package.md       ─→ campaign-setup.md + content-plan.md
│   ├── onboarding-design.md  ─→ retention-strategy.md ─→ revenue-optimization.md
│   └── growth-insights.md    ─→ [Gate 6] ─→ CEO Decision
└── logs/
    └── decisions.md           # 모든 기술/사업 결정 기록
```

## Human Checkpoints (6개)

| # | Checkpoint | Type | When |
|---|-----------|------|------|
| 1 | Gate 3: Design Brief | approval | CTO→CDO 전환 시 |
| 2 | Gate 4: Design Delivery | approval | CDO→CTO 전환 시 |
| 3 | User Validation | human_required | 디자인 후 그로스 전 |
| 4 | Ads Operator | human_execute | 광고 캠페인 실제 집행 |
| 5 | Growth Analyst | human_data | 메트릭 데이터 입력 |
| 6 | CEO Decision | approval | Go/No-Go 최종 결정 |

## Agent Teams (v5.1+)

> `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 활성화 시 사용 가능

32개 에이전트를 Claude Code Agent Teams의 병렬 실행 구조에 최적화한 5개 팀 템플릿.
상세 가이드: `teams/team-playbook.md`

| 팀 | 용도 | 팀원 수 |
|----|------|---------|
| **Business Discovery** | 시장 검증 + Product Brief | 3명 |
| **Development** | PRD → 구현 → 배포 | 3명 |
| **Design** | 디자인 시스템 + 에셋 | 3명 |
| **Growth** | 마케팅 + 리텐션 + 분석 | 4명 |
| **Full Pipeline** | 아이디어 → 런칭 E2E | 4명 |

## Quick Start
1. `workflows/tier-playbooks.md`로 Tier 판단
2. Tier 1: `skills/quick-builder.md` 단일 실행
3. Tier 2: 개별 팀 (Business → Development → Growth)
4. Tier 3+: Full Pipeline Team (`teams/team-playbook.md`)
5. 자동 오케스트레이션: `system/agent-transitions.yaml`
