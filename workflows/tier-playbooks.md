# Tier Playbooks — 규모별 실행 가이드

## Tier 판단 (5개 질문)
1. 이 프로젝트에 투자할 시간은? → 하루(T1) / 2주(T2) / 2개월(T3) / 6개월+(T4)
2. 핵심 기능 수는? → 1개(T1) / 2-3개(T2) / 5개(T3) / 10+(T4)
3. 유저 규모 목표는? → 100명(T1) / 1K(T2) / 10K(T3) / 100K+(T4)
4. 수익 모델이 있나? → 없음(T1) / 간단(T2) / 복합(T3) / 다중(T4)
5. 디자인 품질 기대치는? → 프로토(T1) / 기본(T2) / 전문(T3) / 브랜드(T4)

**가장 높은 Tier를 따른다.**

---

## Tier 1: Quick Experiment (8시간)

### 에이전트: 없음 — `skills/quick-builder.md` 단일 프롬프트
```
핸드오프 문서: 불필요
컨텍스트 관리: 불필요 (단일 세션)
디자인: 프로토타입 수준 (Tailwind 기본)
마케팅: 직접 공유 (Product Hunt, Reddit)
```

### 실행 흐름
1. [2h] Quick Builder로 아이디어 → 코드 (한 세션)
2. [1h] Image Generator MCP로 기본 아이콘
3. [1h] Vercel/Railway 배포
4. [4h] 직접 피드백 수집

---

## Tier 2: Side Project (2주)

### Active Agents: 14개
```
CBO: Pain Point Hunter, Competitor Analyst, BM Designer, GTM Strategist (4)
CTO: PRD Architect, Scope Guard, Frontend, Backend, Code Reviewer (5)
CDO: UI Designer, Image Generator, Screenshot Designer (3)
CGO: Acquisition Strategist, Copy Strategist (2)
```

### 실행 흐름
1. [Day 1-2] CBO: Pain Point → Competitor → BM → Product Brief
2. [Day 3] CTO: PRD → Scope Guard
3. [Day 4-8] CTO: Development (Frontend + Backend)
4. [Day 9] CDO: UI Polish + Icons
5. [Day 10] CTO: Code Review + Deploy
6. [Day 11-14] CGO: Acquisition Strategy + Landing Page Copy

### 핸드오프: 간소화 버전
Product Brief = 1페이지, 나머지 = 구두/인라인

---

## Tier 3: Startup MVP (2개월)

### Active Agents: 전체 32개

### 실행 흐름
1. [Week 1-2] CBO: 전체 파이프라인
2. [Week 3-6] CTO: 전체 개발 사이클
3. [Week 5-7] CDO: 디자인 (CTO와 병렬 + 반복)
4. [Week 7] User Validation Gate
5. [Week 8-12] CGO: 전체 그로스 사이클
6. [Week 12] CEO Go/No-Go

### 핸드오프: 전체 Gate 시스템 적용

---

## Tier 4: Full Product (6개월+)

### 모든 것을 Tier 3처럼 하되:
- 2주 스프린트 사이클
- 매 스프린트마다 CGO → CTO 피드백 루프
- 분기별 CBO 전략 리뷰
- CDO 디자인 시스템 구축 (일회성이 아닌 유지보수)
