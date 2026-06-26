# 경기 출장마사지 사이트 (간다GO)

경기도 전지역 방문 관리 서비스(출장마사지·홈타이) 안내 정적 사이트입니다.
경기남부·북부·서부·동부·외곽 **권역형 구조**로, 시군·생활권·역세권을 분리해 안내합니다.

**상호**: 간다GO
**예약전화**: 0508-202-4719

## 구조

- **정적 HTML 사이트** — GitHub Pages·Netlify·Cloudflare Pages 등 어디서나 그대로 서빙
- **build.py** + **content/** — 페이지를 Python 데이터로 정의하고 정적 HTML 생성
- 생성물은 저장소 루트에 직접 출력됩니다 (`/gyeonggi/...`)

```
build.py                     # 빌드 스크립트 (템플릿·스키마·sitemap·robots)
content/
  site.py                    # 상호·전화·도메인·상단 메뉴(NAV)
  gyeonggi_data.py           # 권역 5개 + 시군 31개 구조화 데이터
  pages_gyeonggi.py          # 루트 리다이렉트·경기 메인·권역·시군 페이지 생성기
  info_gyeonggi.py           # 예약·확인사항·개인정보·고객센터
assets/
  style.css                  # 프리미엄 옵시디언+샴페인골드+오렌지 / Pretendard
  nav.js                     # 모바일 네비게이션
```

## URL 구조

| 페이지 | URL | 수 |
|---|---|---|
| 루트 | `/` → `/gyeonggi/` 리다이렉트 | 1 |
| 경기 메인 | `/gyeonggi/` | 1 |
| 권역 | `/gyeonggi/zone/{south,north,west,east,outer-area}/` | 5 |
| 시군 | `/gyeonggi/{slug}/` (예: `/gyeonggi/suwon/`) | 31 |
| 일반구 | `/gyeonggi/{city}/{gu}/` (예: `/gyeonggi/suwon/paldal-gu/`) | 20 |
| 생활권 | `/gyeonggi/life/{slug}/` (예: `/gyeonggi/life/bundang-pangyo/`) | 25 |
| 역세권 | `/gyeonggi/station/{slug}/` (예: `/gyeonggi/station/suwon-station/`) | 55 |
| 읍면동 | `/gyeonggi/{city}/({gu}/){dong}/` | 76 |
| 정보 | `/gyeonggi/{reservation,check,privacy,support}/` | 4 |

전체 218페이지. 색인(index) 137페이지, 나머지는 `noindex,follow`(아래 참고).

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 색인(index/noindex) 리포트가 출력됩니다.

## SEO 운영 원칙

- 본문 **1,300자 미만 페이지는 자동 `noindex`** (얇은 페이지 보호 = 도어웨이 회피)
- 현재 색인: 메인1 + 권역5 + 시군31 + 일반구20 + 생활권25 + 역세권55 = **137페이지**
- **읍면동 76개는 의도적으로 `noindex,follow`로 단계 보류**: 동 계층은 페이지 수가 많고
  서로 유사해질 위험(도어웨이)이 가장 크므로, 동별 고유 정보가 충분히 쌓일 때까지
  색인을 보류한다. 노출은 안 되지만 크롤링·내부링크 전달은 유지된다.
- 시군 본문은 도시별 고유 데이터(구·동·역·생활권·인접 시군)와 고유 문단으로 작성 — 지역명만 바꾼 복붙 없음
- 메뉴명·URL에 `출장마사지` 키워드를 반복하지 않음
- 환승역은 노선별로 쪼개지 않고 역명 기준 한 페이지
- 외곽 지역은 차량 이동 기준·추가 이동비 안내를 반드시 포함
- 모든 페이지에 JSON-LD 스키마: Organization / WebPage / BreadcrumbList, 메인·시군에는 FAQPage 추가
- 푸터: 오렌지 **웹사이트 제작문의·제휴문의** 버튼(텔레그램), 권위 기관 아웃바운드 링크(경기도청·개인정보보호위원회)

## 디자인

- 프리미엄 옵시디언 다크 + 샴페인골드 액센트, 오렌지(#FF6B35)는 CTA·버튼 전용
- 컴포넌트 오버레이: 버튼 시인(광택), 카드 골드 헤어라인, 글래스 패널
- Pretendard 폰트, 반응형, WAI-ARIA 시맨틱 마크업

## 배포 전 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행
3. Google Search Console에 `sitemap.xml` 제출

## 데이터·생성기 파일

| 계층 | 데이터 | 생성기 |
|---|---|---|
| 권역·시군 | `gyeonggi_data.py` | `pages_gyeonggi.py: zone_page/city_page` |
| 일반구 | `gyeonggi_gu_data.py` | `gu_page` |
| 생활권 | `gyeonggi_life_data.py` | `life_page` |
| 역세권 | `gyeonggi_station_data.py` | `station_page` |
| 읍면동 | `gyeonggi_dong_data.py` | `dong_page` |
| 정보 | `info_gyeonggi.py` | — |

## 2차 확장 (단계적 색인)

- **읍면동 색인 승격**: 동별 고유 정보(랜드마크·도로·단지 특성)를 보강해 본문을 충분히
  차별화한 뒤 `noindex`를 해제한다. GSC 노출·문의 데이터를 기준으로 동 단위로 승격.
- 이용 목적별 안내 (자택·숙소·오피스텔·업무지구·외곽·추가 이동비)
- 잔여 읍면동·역세권을 검색 수요에 맞춰 추가 (번호 동은 대표동으로 묶음)
