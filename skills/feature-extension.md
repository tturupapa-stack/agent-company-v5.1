# Feature Extension

## 용도
기존 코드에 새 기능을 안전하게 추가.

## 트리거 조건
- v1.0 배포 후 기능 추가 시
- CGO → CTO 피드백에서 기능 요청 시

## 단계별 프롬프트 체인

### Step 1: Codebase Analysis
```
Read the existing codebase:
1. List all files and their purposes
2. Identify the architecture pattern
3. Find where the new feature would plug in
4. Check for relevant tests
```

### Step 2: Impact Assessment
```
For the new feature [description]:
1. Which files need to change?
2. Are there database changes needed?
3. Does this affect existing functionality?
4. What could break?
```

### Step 3: Implementation
```
Implement the feature:
1. DB changes first (if any)
2. Backend logic
3. Frontend UI
4. Tests for new functionality
5. Regression test for existing functionality
```

### Step 4: Review
```
Self-review against Code Reviewer checklist.
Run full test suite. Fix any failures.
```
