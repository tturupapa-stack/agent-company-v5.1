---
name: design-system-workflow
description: |
  프로젝트 초기에 일관된 디자인 시스템을 구축하는 워크플로우.
  PRD 완료 후 개발 시작 전(STAGE 2.5)에 디자인 토큰과 컴포넌트 규칙을 정의한다.
  design-system-generator 에이전트를 사용한다.

  다음 상황에서 사용:
  - 디자인 시스템 구축 요청 시
  - 디자인 토큰 생성 요청 시
  - 디자인 시스템 검증 요청 시
---

# Design System Workflow

> 프로젝트 초기에 일관된 디자인 시스템을 구축하는 워크플로우

---

## 개요

| 항목 | 내용 |
|------|------|
| **목적** | 개발 전 디자인 토큰과 컴포넌트 규칙 정의 |
| **시점** | STAGE 2.5 (PRD 완료 후, 개발 시작 전) |
| **실행 횟수** | 프로젝트당 1회 |

---

## 왜 필요한가?

### 문제: Design System 없이 개발하면

```
FR-001 개발 -> bg-blue-500 사용
FR-002 개발 -> bg-indigo-600 사용
FR-003 개발 -> #3b82f6 하드코딩

결과:
- 페이지마다 스타일 제각각
- 브랜드 컬러 변경 시 100군데 수정
- "학생 프로젝트" 느낌
```

### 해결: Design System 먼저 정의하면

```
STAGE 2.5 -> Design System 생성
    |
    +-- tokens.css: --color-primary-500 정의
        |
        +-- FR-001: bg-primary-500 사용
        +-- FR-002: bg-primary-500 사용
        +-- FR-003: bg-primary-500 사용

결과:
- 모든 페이지 일관성
- 브랜드 컬러 변경 시 1군데만 수정
- "실제 서비스" 느낌
```

---

## 사용하는 에이전트

```
design-system-workflow
  |
  Phase 1: 분석
  +-- 수동 또는 PRD 기반
  |
  Phase 2: 생성
  +-- design-system-generator (Sonnet)
  |
  Phase 3: 검증
  +-- 수동 검토 또는 ux-auditor
```

---

## Phase 1: 앱 성격 분석

### 1.1 PRD에서 추출

PRD-FINAL.md에서 다음 정보 추출:

```yaml
타겟_사용자:
  - B2B / B2C
  - 연령대
  - 기술 숙련도

앱_성격:
  - 대시보드 / 소셜 / 이커머스 / 콘텐츠
  - 전문적 / 친근한 / 미니멀 / 화려한

핵심_기능:
  - 데이터 시각화 -> 차트 컴포넌트 필요
  - 소셜 피드 -> 카드 컴포넌트 필요
  - 폼 중심 -> 입력 컴포넌트 필요
```

### 1.2 사용자 입력 수집

```markdown
## 디자인 선호도 질문

1. 레퍼런스 앱/사이트가 있나요?
   - URL:
   - 좋아하는 점:

2. 브랜드 컬러가 있나요?
   - Primary:
   - Secondary:

3. 선호하는 스타일은?
   [ ] 미니멀/클린
   [ ] 화려한/볼드
   [ ] 전문적/비즈니스
   [ ] 친근한/부드러운

4. 다크모드 지원이 필요한가요?
   [ ] 예
   [ ] 아니오
   [ ] 시스템 설정 따름
```

---

## Phase 2: Design System 생성

### 2.0 디자인 철학 (필수 준수)

> **"제네릭 AI 미학을 절대 사용하지 않는다."**

#### 금지 원칙

| # | 금지 항목 | 이유 | 대안 |
|---|----------|------|------|
| 1 | 이모지를 UI 아이콘으로 사용 | 비전문적, 프로토타입 느낌 | Lucide, Heroicons, React Icons |
| 2 | Inter/Roboto 무조건 사용 | 모든 AI 앱이 동일 폰트 | 앱 성격에 맞는 폰트 선택 |
| 3 | Tailwind 기본 파란색 팔레트 | 제네릭한 "AI가 만든" 느낌 | 앱 목적에 맞는 대담한 팔레트 |
| 4 | 모든 요소에 동일 border-radius | 시각적 위계 부재 | 요소별 적절한 곡률 차등 |
| 5 | 기본 그림자/그라데이션 없음 | 평평하고 무미건조 | 미묘한 depth와 입체감 |

#### 폰트 선택 가이드

| 앱 성격 | 추천 폰트 | 이유 |
|---------|-----------|------|
| 금융/전문 | IBM Plex Sans, DM Sans | 정돈되고 신뢰감 |
| 소셜/커뮤니티 | Plus Jakarta Sans, Nunito | 친근하고 부드러움 |
| 생산성/SaaS | Space Grotesk, Outfit | 현대적이고 기능적 |
| 크리에이티브 | Clash Display, Cabinet Grotesk | 개성 있고 대담 |
| 이커머스 | Satoshi, General Sans | 깔끔하고 상품 중심 |

#### 색상 팔레트 원칙

- Primary 색상은 앱의 핵심 감정/목적과 연결
- 보조 색상은 Primary와 조화 (유사색 or 보색)
- 중립색(Gray)도 차가운/따뜻한 톤 선택 필수 (순수 Gray 지양)
- Semantic 색상 (success, error, warning, info)은 브랜드 톤과 일관성 유지

### 2.1 design-system-generator 호출

```yaml
입력:
  prd: PRD-FINAL.md
  tech_stack: React + Tailwind (예시)
  preferences: Phase 1.2에서 수집한 정보

출력:
  - .design-system/tokens.css
  - .design-system/STYLE_GUIDE.md
  - .design-system/components.md
  - .design-system/tailwind.extend.js (Tailwind 사용 시)
```

### 2.2 생성 파일 구조

```
프로젝트/
+-- .design-system/
    +-- tokens.css           # CSS 변수 (색상, 타이포, 간격)
    +-- STYLE_GUIDE.md       # 사용 규칙
    +-- components.md        # 컴포넌트 명세
    +-- tailwind.extend.js   # Tailwind 확장 설정
    +-- examples/            # 예시 코드 (선택)
        +-- Button.example.tsx
        +-- Input.example.tsx
        +-- Card.example.tsx
```

---

## Phase 3: 검증

### 3.1 체크리스트

| # | 항목 | 확인 |
|---|------|------|
| 1 | 색상 대비 WCAG AA 이상 | |
| 2 | 다크모드 변수 정의 완료 | |
| 3 | 모든 시맨틱 색상 정의 (success, error, warning, info) | |
| 4 | 타이포그래피 계층 명확 | |
| 5 | 간격 시스템 일관성 | |
| 6 | 반응형 고려 | |
| 7 | 버튼 variants 정의 (primary, secondary, ghost, destructive) | |
| 8 | 입력 필드 상태 정의 (default, focus, error, disabled) | |

### 3.2 색상 대비 검증

```bash
# 온라인 도구
https://webaim.org/resources/contrastchecker/

# 필수 확인
- 본문 텍스트: 4.5:1 이상
- 큰 텍스트 (18px+): 3:1 이상
- 버튼 텍스트: 4.5:1 이상
```

### 3.3 검증 결과

```markdown
## Design System 검증 결과

### 통과

- 색상 대비: Primary 버튼 텍스트 7.2:1
- 다크모드: 모든 변수 정의 완료
- 타이포: 6단계 계층 정의

### 수정 필요

- Warning 색상 (#f59e0b) 흰색 배경 대비 3.8:1 -> 4.5:1 미만
  - 권장: #d97706 으로 변경

### 수정 후 최종 승인: [ ]
```

---

## Phase 4: 프로젝트 설정

### 4.1 tokens.css 연결

```tsx
// src/app/layout.tsx (Next.js)
import '@/styles/tokens.css';

// src/main.tsx (Vite)
import './design-system/tokens.css';
```

### 4.2 Tailwind 설정 (사용 시)

```javascript
// tailwind.config.js
const designSystemExtend = require('./.design-system/tailwind.extend.js');

module.exports = {
  theme: {
    extend: {
      ...designSystemExtend.theme.extend,
    },
  },
};
```

### 4.3 CLAUDE.md 업데이트

```markdown
## 디자인 시스템

| 파일 | 위치 | 용도 |
|------|------|------|
| Design Tokens | `.design-system/tokens.css` | CSS 변수 |
| Style Guide | `.design-system/STYLE_GUIDE.md` | 사용 규칙 |
| Components | `.design-system/components.md` | 컴포넌트 명세 |

### 필수 규칙

- 색상: `var(--color-xxx)` 사용, `#xxx` 금지
- 간격: `var(--space-x)` 사용, 임의 값 금지
- Tailwind: `bg-primary-500` 사용, `bg-blue-500` 금지
```

---

## 산출물 요약

| 파일 | 필수 | 설명 |
|------|------|------|
| `.design-system/tokens.css` | 필수 | 모든 CSS 변수 |
| `.design-system/STYLE_GUIDE.md` | 필수 | 사용 규칙 문서 |
| `.design-system/components.md` | 필수 | 컴포넌트 명세 |
| `.design-system/tailwind.extend.js` | 선택 | Tailwind 확장 (사용 시) |
| `.design-system/examples/` | 선택 | 예시 코드 (선택) |

---

## 후속 단계

### 개발 시작 전 확인

```
- .design-system/ 폴더 생성 완료
- tokens.css 프로젝트에 연결
- STYLE_GUIDE.md 팀원 공유 (또는 CLAUDE.md에 링크)
- frontend-developer가 참조할 수 있도록 설정
```

### 개발 중 규칙

```markdown
## frontend-developer 필수 규칙

1. 색상 사용 시:
   OK: var(--color-primary-500)
   OK: bg-primary-500 (Tailwind)
   NO: #3b82f6
   NO: bg-blue-500

2. 간격 사용 시:
   OK: var(--space-4)
   OK: p-4 (Tailwind - 확장 설정 필요)
   NO: 16px
   NO: 1rem

3. 새 스타일 필요 시:
   - Design System에 먼저 추가
   - 그 후 사용
```

---

## 트리거 명령어

| 명령어 | 동작 |
|--------|------|
| "디자인 시스템 만들어줘" | Phase 1~4 전체 실행 |
| "디자인 토큰 생성해줘" | Phase 2만 실행 |
| "디자인 시스템 검증해줘" | Phase 3만 실행 |

---

## 예상 시나리오

### 시나리오 1: 새 프로젝트

```
사용자: "디자인 시스템 만들어줘"

Claude:
1. PRD 분석 (앱 성격 파악)
2. 선호도 질문 (레퍼런스, 브랜드 컬러)
3. design-system-generator 실행
4. 검증 체크리스트 확인
5. 프로젝트 설정 안내
```

### 시나리오 2: 레퍼런스 있음

```
사용자: "Linear 같은 느낌으로 디자인 시스템 만들어줘"

Claude:
1. Linear 스타일 분석 (미니멀, 다크 우선, 모노크롬)
2. 해당 스타일로 토큰 생성
3. 검증 및 설정
```

### 시나리오 3: 기존 브랜드

```
사용자: "우리 브랜드 컬러는 #FF6B35야. 이걸로 디자인 시스템 만들어줘"

Claude:
1. #FF6B35 기반 색상 팔레트 생성 (50~900)
2. 보조 색상 제안
3. 토큰 생성 및 설정
```

---

## 주의사항

### 한 번만 실행

- 프로젝트 시작 시 1회만
- 개발 중 대폭 변경 지양
- 작은 수정은 tokens.css 직접 편집

### frontend-developer 필수 연계

- 이 스킬 완료 후 개발 시작
- frontend-developer가 Design System 참조하도록 설정
- 임의값 사용 시 code-reviewer가 지적

### 너무 복잡하게 만들지 않기

- MVP에는 기본 토큰만
- 필요할 때 확장
- 사용하지 않는 토큰은 정의하지 않음
