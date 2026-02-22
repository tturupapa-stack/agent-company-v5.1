# Cost & Time Estimates

## Tier별 Phase별 소요 시간

### Tier 1: Quick Experiment
| Phase | 소요 시간 | 에이전트 | 비고 |
|-------|----------|---------|------|
| 전체 | **8시간** | Quick Builder 1개 | 단일 프롬프트 |
| 아이디어 → 코드 | 6시간 | - | 핸드오프 없음 |
| 기본 아이콘 | 1시간 | Image Generator | MCP 1개 |
| 배포 | 1시간 | - | Vercel/Railway |

### Tier 2: Side Project
| Phase | 소요 시간 | Active Agents | 비고 |
|-------|----------|--------------|------|
| Phase 1: CBO | 4시간 | 5개 | Pain Point, Competitor, BM, Business Planner, GTM |
| Phase 2: CTO | 40시간 | 5개 | PRD~Code Review |
| Phase 2.5: CDO | 8시간 | 3개 | UI, Image Gen, Screenshot |
| Phase 3: CGO | 16시간 | 2개 | Acquisition, Copy |
| **Total** | **~70시간 (2주)** | **15개** | |

### Tier 3: Startup MVP
| Phase | 소요 시간 | Active Agents | 비고 |
|-------|----------|--------------|------|
| Phase 1: CBO | 16시간 | 5개 | 전체 CBO |
| Phase 2: CTO | 160시간 | 7개 | 전체 CTO |
| Phase 2.5: CDO | 40시간 | 6개 | 전체 CDO |
| Phase 2.9: Validation | 16시간 | - | 유저 테스트 |
| Phase 3: CGO | 80시간 | 8개 | 전체 CGO |
| **Total** | **~300시간 (2개월)** | **26개** | |

## MCP/API 비용 추정 (월간)

| MCP/Service | 무료 티어 | 유료 시작 | 비고 |
|-------------|----------|----------|------|
| Replicate (Image Gen) | 없음 | ~$0.003/이미지 | Flux Schnell 기준 |
| Figma | Starter 무료 | $15/월 | API 접근은 Professional+ |
| Google Stitch | 350회/월 | 해당 없음 | Labs 무료 |
| App Store Connect | 무료 | $99/년 (개발자 등록) | Apple 필수 |
| Analytics (Mixpanel) | 20M events/월 | $28/월 | 대부분 무료 충분 |
| Vercel (호스팅) | Hobby 무료 | $20/월 | 트래픽 따라 |

### Tier별 월 예상 비용
- **Tier 1**: $0~5 (Replicate 이미지 몇 장)
- **Tier 2**: $20~50 (Figma + Replicate + 호스팅)
- **Tier 3**: $100~200 (위 + 광고 예산 별도)
- **Tier 4**: $300+ (풀 스택 + 광고 $500+/월)

## "이것 대신 이걸 쓰라" 가이드
| 상황 | Agent Company 대신 | 이유 |
|------|-------------------|------|
| 정적 랜딩페이지 1개 | v0.dev 또는 Bolt | 3분이면 끝남 |
| 간단한 CRUD 앱 | Cursor + Supabase | 에이전트 오버헤드 불필요 |
| 디자인만 필요 | Figma + Stitch 직접 | CDO 파이프라인 불필요 |
| 마케팅 카피만 | Claude 직접 | CGO 구조 불필요 |
