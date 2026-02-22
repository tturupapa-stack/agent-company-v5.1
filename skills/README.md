# Skills — Claude Code 직접 사용 단축키

> ⚠️ Skills ≠ Agent Transitions
> 
> - `system/agent-transitions.yaml` → OpenClaw 자동 오케스트레이션 (파이프라인 모드)
> - `skills/*.md` → 사람이 Claude Code에서 직접 실행 (단축키 모드)
> 
> **사용 시나리오:** "전체 파이프라인 안 돌리고, 특정 작업만 빨리 하고 싶을 때"

## 언제 Skills를 쓰는가

| 상황 | 사용 도구 |
|------|----------|
| 아이디어 → 완성품 전체 자동화 | `agent-transitions.yaml` (OpenClaw) |
| 아이디어 → 빠른 프로토타입 (Tier 1) | `skills/quick-builder.md` |
| 기존 앱에 기능 추가 | `skills/feature-extension.md` |
| 기존 코드 리팩토링 | `skills/refactoring.md` |
| PRD만 빨리 작성 | `skills/prd-workflow.md` |
| 개발 중 감독/진행 | `skills/supervisor.md` |

## Skills vs Transitions 매핑

| Skill | 대응하는 Transition 에이전트 | 차이 |
|-------|--------------------------|------|
| quick-builder.md | entry.tier_1 | 동일 — Tier 1 전용 |
| prd-workflow.md | prd_architect + scope_guard | Skill은 독립 실행, Transition은 Gate 1 통과 후 실행 |
| supervisor.md | parallel_dev + code_reviewer | Skill은 사람이 감독, Transition은 자동 합류 |
| feature-extension.md | (해당 없음) | 기존 코드베이스에 기능 추가 전용 |
| refactoring.md | (해당 없음) | 코드 품질 개선 전용 |

## 사용법
```bash
# Claude Code에서 직접 실행
claude "Read /path/to/skills/quick-builder.md and follow the instructions"
```
