# Design Delivery (CDO → CTO)

## Product Name:
## Date:
## CDO Phase Completed: [Audit / UI-UX / Visual / Store Assets / Full]

---

### 토큰 소스
- [ ] Figma Variables (figma-mcp로 추출)
- [ ] Stitch Export (stitch-mcp로 추출)
- [ ] 수동 정의

### 디자인 토큰
```yaml
colors:
  primary: "#"
  secondary: "#"
  accent: "#"
  background: "#"
  surface: "#"
  text_primary: "#"
  text_secondary: "#"
  error: "#"
  success: "#"
  warning: "#"

typography:
  font_family: ""
  h1: { size: "", weight: 700 }
  h2: { size: "", weight: 700 }
  h3: { size: "", weight: 600 }
  body: { size: "", weight: 400 }
  caption: { size: "", weight: 400 }
  button: { size: "", weight: 600 }

spacing:
  base: "4px"
  scale: [4, 8, 12, 16, 20, 24, 32, 40, 48, 64]

border_radius:
  small: ""
  medium: ""
  large: ""
  full: "9999px"

elevation:
  level_1: ""
  level_2: ""
  level_3: ""
```

### 컴포넌트 목록
| 컴포넌트 | 상태 | 파일/설명 |
|---------|------|----------|
| Button | default, hover, disabled, loading | |
| Input | default, focus, error, disabled | |
| Card | default, hover | |
| Modal | open, closing | |
| Navigation | active, inactive | |

### 화면별 디자인 스펙
| 화면 | Figma/스펙 링크 | 반응형 | 다크모드 |
|------|----------------|--------|---------|
| | | Y/N | Y/N |

### 에셋 파일 경로
```
/assets/
├── icons/
├── images/
└── app-icon/
    ├── ios/ (1024x1024)
    └── android/ (512x512)
```

### 구현 시 주의사항
- [ ] 기술 제약 반영 여부
- [ ] 애니메이션 스펙 (있으면)
- [ ] 접근성 요구사항

---
### Quality Gate 4 체크
- [ ] 디자인 토큰 (컬러, 타이포, 스페이싱) 정의됨
- [ ] 토큰 소스 명시 (Figma Variables / Stitch Export / 수동 정의)
- [ ] 컴포넌트별 상태 시안 (default, hover, disabled, error) 포함
- [ ] 에셋 파일 경로 명시
- [ ] Figma 파일 또는 디자인 스펙 문서 존재
- [ ] MCP 연결 시 Variables/Styles 동기화 확인
