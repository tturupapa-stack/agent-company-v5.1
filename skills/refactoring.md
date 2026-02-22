# Refactoring Workflow

## 용도
테스트 우선 접근으로 안전한 코드 리팩토링.

## 원칙
"먼저 테스트, 그 다음 리팩토링, 한 번에 하나만"

## 단계별 프롬프트 체인

### Step 1: Test Coverage Check
```
For [target file/module]:
1. What tests exist?
2. What's the coverage?
3. If coverage < 80%, write tests FIRST before any changes
```

### Step 2: Identify Issues
```
Analyze the code for:
- Duplicated logic
- Functions > 50 lines
- Deeply nested conditions
- Mixed responsibilities
- Magic numbers/strings
Rank by impact × ease of fix
```

### Step 3: Refactor (하나씩)
```
For each issue (highest priority first):
1. Make ONE change
2. Run tests — all must pass
3. Commit
4. Next issue
NEVER make multiple changes between test runs.
```

### Step 4: Verify
```
Run full test suite.
Compare behavior before/after.
Document what changed and why.
```
