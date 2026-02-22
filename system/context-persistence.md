# Context Persistence System

## 문제
Claude Code 세션이 끝나면 컨텍스트가 사라진다. 에이전트 간 핸드오프 시 이전 단계의 산출물과 결정 사항이 전달되어야 한다.

## 구현: `.agent-state/` 폴더

### 초기화
프로젝트 시작 시 CEO가 실행:
```bash
mkdir -p .agent-state
cat > .agent-state/project.json << 'EOF'
{
  "project": "",
  "tier": 0,
  "current_phase": "init",
  "current_agent": "CEO",
  "completed_phases": [],
  "handoffs": {},
  "blockers": [],
  "decisions_log": [],
  "metrics": {},
  "iteration_count": {
    "product_brief_revision": 0,
    "prd_scope_revision": 0,
    "code_review_revision": 0,
    "cdo_cto_design_review": 0,
    "user_validation_retry": 0,
    "cbo_rollback": 0
  },
  "created_at": "",
  "updated_at": ""
}
EOF
```

### Phase별 산출물 저장
```bash
.agent-state/
├── project.json                 # 프로젝트 상태 (CEO 관리)
├── outputs/
│   ├── pain-points.md          # CBO Phase 1 산출물
│   ├── competitor-analysis.md  # CBO Phase 2 산출물
│   ├── business-model.md       # CBO Phase 3 산출물
│   ├── product-brief.md        # CBO → CTO 핸드오프
│   ├── prd.md                  # CTO Phase 1 산출물
│   ├── architecture.md         # CTO Phase 2 산출물
│   ├── design-audit.md         # CDO Phase 1 산출물
│   ├── design-delivery.md      # CDO → CTO 핸드오프
│   ├── store-assets-package.md  # CDO → CGO 핸드오프
│   ├── launch-brief.md         # CTO → CGO 핸드오프
│   └── growth-insights.md      # CGO → CEO 피드백
└── logs/
    └── decisions.md            # 모든 기술/사업 결정 기록
```

### 에이전트별 컨텍스트 주입 규칙
```yaml
context_injection:
  PRD_Architect:
    must_read: [".agent-state/outputs/product-brief.md"]
    optional: [".agent-state/outputs/competitor-analysis.md"]
    
  Frontend_Engineer:
    must_read: [".agent-state/outputs/prd.md", ".agent-state/outputs/architecture.md"]
    optional: [".agent-state/outputs/design-delivery.md"]
    
  UI_Designer:
    must_read: [".agent-state/outputs/prd.md", ".agent-state/outputs/design-upgrade-brief.md"]
    optional: [".agent-state/outputs/product-brief.md"]
    
  Acquisition_Strategist:
    must_read: [".agent-state/outputs/launch-brief.md"]
    optional: [".agent-state/outputs/store-assets-package.md", ".agent-state/outputs/product-brief.md"]
```

### 세션 복원
새 Claude 세션 시작 시:
```
이전 세션에서 작업하던 프로젝트를 이어갈게.
.agent-state/project.json과 .agent-state/outputs/ 폴더를 읽어서 현재 상태를 파악해줘.
```

### 상태 업데이트 타이밍
- Phase 시작 시: `current_phase`, `current_agent` 업데이트
- 산출물 생성 시: `outputs/` 폴더에 저장
- 핸드오프 시: `handoffs` 상태 + 품질 점수 기록
- 결정 시: `decisions_log`에 추가 (날짜, 결정, 이유)
- 메트릭 수집 시: `metrics` 업데이트
