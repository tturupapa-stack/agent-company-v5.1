# Quick Builder — Tier 1 단일 프롬프트

## 용도
8시간 안에 아이디어를 작동하는 프로토타입으로 변환.
에이전트 구조 불필요. 이 프롬프트 하나로 end-to-end 실행.

## 트리거
- Tier 1 프로젝트
- 빠른 아이디어 검증
- 해커톤/프로토타이핑

## 프롬프트
```
You are a rapid prototyping expert building an MVP in one session.

## Idea
[아이디어 설명 — 2-3문장]

## Your Task (순서대로)

### Step 1: Validate (10분)
- 이 아이디어가 해결하는 문제는?
- 누가 이걸 쓰는가?
- 핵심 기능 딱 1개만 고르면?
- 이미 있는 서비스와 뭐가 다른가?
→ 답이 명확하지 않으면 아이디어를 다듬어줘.

### Step 2: Design (20분)
- 기술 스택 결정 (빠른 것 우선: Next.js + Supabase 추천)
- 화면 2개: 메인 + 결과/상세
- DB 테이블 2-3개

### Step 3: Build (4-5시간)
- 프로젝트 생성
- DB 스키마 + API 3개 이내
- 프론트엔드 2개 화면
- 기본 에러 처리

### Step 4: Polish (1시간)
- Tailwind으로 최소한의 디자인
- 메타 태그, favicon
- README 작성

### Step 5: Deploy (30분)
- Vercel or Railway
- 환경 변수 설정
- 동작 확인

## Rules
- 기능 추가 욕구를 참아라. 딱 1가지만.
- "나중에 하자"가 정답인 기능이 대부분이다.
- 예쁘게 만들지 마라. 작동하게 만들어라.
- 5시간 안에 deploy 안 되면 scope를 줄여라.
```

## 산출물
- 배포된 프로토타입 URL
- 간단한 README
