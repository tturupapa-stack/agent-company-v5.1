# Supervisor — Development Orchestration

## 용도
PRD 기반으로 Frontend/Backend 병렬 개발을 관리.

## 트리거 조건
- PRD + Architecture 완성 후
- Tier 2+

## 필요한 입력
- `.agent-state/outputs/prd.md`
- `.agent-state/outputs/architecture.md`

## 단계별 프롬프트 체인

### Step 1: Task Breakdown
```
Read PRD and Architecture. Break into development tasks:
- Backend tasks (API endpoints, DB setup, auth)
- Frontend tasks (screens, components, API integration)
- Mark dependencies (what must be done first)
- Estimate hours per task
```

### Step 2: Backend Development
```
Implement backend tasks in dependency order:
1. DB schema + migration
2. Auth setup
3. API endpoints (P0 first)
4. Input validation + error handling
5. Run tests
```

### Step 3: Frontend Development (병렬 가능)
```
Implement frontend tasks:
1. Project setup + routing
2. Shared components (Header, Layout, Loading, Error)
3. Screens in priority order
4. API integration (mock → real)
5. Run build check
```

### Step 4: Integration
```
Connect frontend to backend:
1. Replace mock data with real API calls
2. Test all user flows end-to-end
3. Fix integration issues
```

### Step 5: Code Review
```
Review all code using Code Reviewer checklist:
- Security, Performance, Error Handling, Tests, Consistency
- Fix critical issues
- Document warnings for future
```

### Step 6: Status Report
```
Save to .agent-state/project.json:
- completed tasks
- remaining issues
- deployment readiness
```

## 출력
작동하는 앱 + `.agent-state/project.json` 업데이트
