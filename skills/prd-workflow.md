# PRD Workflow

## 용도
아이디어 또는 Product Brief를 구조화된 PRD로 변환.

## 트리거 조건
- Product Brief가 Gate 1을 통과했을 때
- Tier 2+ 프로젝트

## 필요한 입력
- `.agent-state/outputs/product-brief.md`

## 단계별 프롬프트 체인

### Step 1: User Story Extraction
```
Read the Product Brief at .agent-state/outputs/product-brief.md.
For each MVP feature, write User Stories:
- Format: As a [user], I want [action], so that [benefit]
- Each story must have 2+ acceptance criteria
- Mark priority: P0 (MVP) / P1 (v1.1) / P2 (v2.0)
```

### Step 2: Screen & Flow Design
```
Based on the User Stories, define screens:
- Screen name, purpose, key elements
- User flow between screens (→ arrows)
- States for each screen: empty, loading, loaded, error
```

### Step 3: API & DB Design
```
Based on screens and user stories:
- Define RESTful API endpoints (method, path, request, response)
- Design DB schema (tables, fields, types, indexes)
- Keep within Scope Guard limits for tier [X]
```

### Step 4: Scope Guard Review
```
Review the PRD against tier [X] limits:
- Features: [X]/[limit]
- APIs: [X]/[limit]
- Screens: [X]/[limit]
Flag any violations and suggest deferrals.
```

## 출력
`.agent-state/outputs/prd.md`
