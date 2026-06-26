# -*- coding: utf-8 -*-
"""경기 출장마사지 — 페이지 생성기.

gyeonggi_data 의 구조화 데이터를 받아 페이지 dict 를 생성한다.
  - 루트 리다이렉트 (/)  → /gyeonggi/
  - 경기 메인 (/gyeonggi/)
  - 권역 페이지 (/gyeonggi/zone/<key>/)  5개
  - 시군 페이지 (/gyeonggi/<slug>/)       31개
스키마(Organization/WebPage/BreadcrumbList)는 build.py 가 자동 주입하고,
시군 페이지에는 FAQPage 스키마를 extra_head 로 추가한다.
"""
import json

from .site import BASE_URL, BRAND, PHONE
from .gyeonggi_data import ZONES, CITIES, ZONE_BY_KEY, CITY_BY_SLUG
from .gyeonggi_gu_data import GU, GU_BY_CITY
from .gyeonggi_life_data import LIFE
from .gyeonggi_station_data import STATIONS
from .gyeonggi_dong_data import DONGS

# (city, gu_slug) → 구 한글명
_GU_NAME = {(g["city"], g["slug"]): g["gu"] for g in GU}
# (city, 동 한글명) → 동 슬러그 (구·시 페이지에서 동 상세로 링크)
_DONG_SLUG_BY_KEY = {(d["city"], d["name"]): d["slug"] for d in DONGS}
# (city, 동 한글명) → (구 슬러그 또는 None, 동 슬러그) — 인접 동 정확 링크용
_DONG_REF_BY_KEY = {(d["city"], d["name"]): (d["gu"], d["slug"]) for d in DONGS}


def _dong_url(city, name):
    """같은 시의 동 이름 → 실제 URL(구 유무 반영). 없으면 None."""
    ref = _DONG_REF_BY_KEY.get((city, name))
    if not ref:
        return None
    gu, slug = ref
    return f"/gyeonggi/{city}/{gu}/{slug}/" if gu else f"/gyeonggi/{city}/{slug}/"


def _dongs_of_gu(city, gu):
    return [d for d in DONGS if d["city"] == city and d["gu"] == gu]


def _dongs_of_city_nogu(city):
    return [d for d in DONGS if d["city"] == city and d["gu"] is None]

# 생활권 이름 → 슬러그 (시군 페이지에서 생활권 허브로 링크)
_LIFE_SLUG_BY_NAME = {l["name"]: l["slug"] for l in LIFE}
# 역 이름 → 슬러그 (시군·생활권 페이지에서 역세권 허브로 링크)
_STATION_SLUG_BY_NAME = {s["name"]: s["slug"] for s in STATIONS}


def _station_links(names):
    """역 이름 목록 → 역 페이지 링크(있으면) 또는 텍스트, ' · ' 연결."""
    out = []
    for n in names:
        slug = _STATION_SLUG_BY_NAME.get(n)
        out.append(f'<a href="/gyeonggi/station/{slug}/">{n}</a>' if slug else n)
    return " · ".join(out)


# 이용 목적별(롱테일 주제) 내부링크 — 방문 장소 안내 6개
_PURPOSE = [
    ("자택", "home"), ("호텔·숙소", "lodging"), ("오피스텔", "officetel"),
    ("업무지구", "business"), ("외곽 지역", "outer"), ("추가 이동비", "travel-fee"),
]


def _purpose_links():
    return _li_links([(f"{n} 이용 안내", f"/gyeonggi/purpose/{s}/") for n, s in _PURPOSE])


# E-E-A-T 신호: 작성·검수 바이라인 + 연락처(YMYL 신뢰 신호).
_BYLINE = (
    '<section id="byline" class="byline">'
    '<h2>작성·검수 안내</h2>'
    f'<p>이 안내는 <strong>{BRAND}</strong> 운영팀이 직접 방문 가능 지역과 이동 기준을 '
    '정리하고 검수해 작성했습니다. 지역 구분·역세권·이동권 정보는 실제 예약 상담 데이터를 '
    '바탕으로 주기적으로 갱신합니다.</p>'
    f'<p><strong>운영</strong> {BRAND} 편집팀 · <strong>예약·문의</strong> '
    f'<a href="tel:{PHONE}">{PHONE}</a> (연중무휴 24시간) · '
    '<strong>회사 안내</strong> <a href="/gyeonggi/support/">고객센터</a> · '
    '<strong>개인정보</strong> <a href="/gyeonggi/privacy/">처리방침</a></p>'
    '</section>'
)

_BASE = BASE_URL.rstrip("/")


def _faq_schema(pairs):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2)
            + "\n</script>")


def _li_links(items):
    """[(label, href)] → <li><a>…</a></li> 묶음."""
    return "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in items)


def _cards(items):
    """[(title, desc, href)] → 카드 그리드."""
    cells = "".join(
        f'<a href="{href}" class="card"><h3>{t}</h3><p>{d}</p>'
        f'<span class="card-arrow">→</span></a>'
        for t, d, href in items
    )
    return f'<div class="card-grid">{cells}</div>'


# 생활권 상세 문장 템플릿 — 인덱스로 순환시켜 같은 도시 안에서도 표현을 달리한다.
_LIFE_TPL = [
    "{lf} 생활권은 {anchor} 인근을 기준으로 이동권이 형성됩니다. 방문 주소가 이 생활권에 해당한다면 자택·숙소·오피스텔 유형과 건물 출입 방식을 함께 알려주시면 예약이 빠릅니다.",
    "{lf} 일대는 {anchor} 쪽 생활권으로, 같은 시 안에서도 다른 권역과 이동 기준이 구분됩니다. 예약 가능 시간과 정확한 동·단지명을 확인해 두면 방문 일정을 정확히 잡을 수 있습니다.",
    "{lf} 생활권은 {anchor}을(를) 중심으로 한 주거·상권 이동권입니다. 경계 지역이라면 인접 생활권 기준이 적용될 수 있으니 예약 시 도로명 주소를 알려주세요.",
    "{lf} 권역은 {anchor} 방향 이동이 많은 생활권으로, 기본 이동권 범위와 추가 이동비 여부를 미리 확인하면 안내가 수월합니다.",
    "{lf} 생활권은 {anchor} 인근 방문 수요가 꾸준한 지역입니다. 야간·새벽 방문도 사전 확인을 통해 조율할 수 있습니다.",
]


def _life_detail(c):
    """도시의 생활권을 역·동 데이터와 엮어 고유한 상세 안내를 만든다."""
    if not c["life"]:
        return ""
    anchors = c["stations"] or c["dong"] or [c["name"]]
    rows = []
    for i, lf in enumerate(c["life"]):
        anchor = anchors[i % len(anchors)]
        rows.append(f"<dt>{lf}</dt><dd>{_LIFE_TPL[i % len(_LIFE_TPL)].format(lf=lf, anchor=anchor)}</dd>")
    return (
        f'<section id="life-detail"><h2>{c["name"]} 생활권 상세 안내</h2>'
        f'<p>{c["name"]}의 대표 생활권별 이동 기준과 예약 시 확인할 점을 정리했습니다. '
        f'같은 {c["name"]}이라도 생활권에 따라 방문 주소 기준이 달라집니다.</p>'
        f'<dl class="faq-list">{"".join(rows)}</dl></section>'
    )


# ── 공통 안내 블록 (모든 시군·권역 하단) ───────────────────
_CHECK_BLOCK = """
<section id="check">
  <h2>예약 전 확인사항</h2>
  <p>방문형 관리 서비스는 지역과 생활권에 따라 이동 기준이 다릅니다. 예약 전 아래 항목을 먼저 확인하면 예약 과정이 한결 수월합니다.</p>
  <ul>
    <li><strong>방문 가능 주소</strong> — 자택·숙소·오피스텔 등 정확한 주소와 건물 유형</li>
    <li><strong>예약 가능 시간</strong> — 희망 시간대의 예약 가능 여부</li>
    <li><strong>차량 이동 가능 여부</strong> — 외곽·도서 지역은 차량 이동 가능 여부를 먼저 확인</li>
    <li><strong>추가 이동비</strong> — 기본 이동권 외 추가 이동비 발생 여부</li>
    <li><strong>숙소 이용 가능 여부</strong> — 호텔·펜션 등 숙소 방문 가능 여부</li>
    <li><strong>예약 변경 기준</strong> — 변경·취소 절차와 기준</li>
    <li><strong>개인정보 처리 기준</strong> — 개인정보 수집·이용·보관 방식</li>
    <li><strong>불법·선정적 서비스 불가 안내</strong> — 건전한 방문 관리 서비스만 제공</li>
  </ul>
  <p>자세한 내용은 <a href="/gyeonggi/reservation/">예약 안내</a>와 <a href="/gyeonggi/check/">이용 전 확인사항</a>에서 확인하세요.</p>
</section>"""


# ───────────────────────────────────────────────────────────
def root_redirect_page():
    return {
        "path": "",
        "title": "경기 출장마사지｜수원·분당·용인·부천·일산 홈타이 안내",
        "desc": "경기 출장마사지·홈타이 안내. 경기 주요 생활권 페이지로 이동합니다.",
        "h1": "경기 출장마사지",
        "breadcrumb": [],
        "noindex": True,
        "extra_head": '<meta http-equiv="refresh" content="0;url=/gyeonggi/">',
        "body": ('<p>경기 출장마사지·홈타이 안내 페이지로 이동합니다. 자동으로 이동하지 않으면 '
                 '<a href="/gyeonggi/">여기를 클릭</a>하세요.</p>'),
    }


# ── 경기 메인 ───────────────────────────────────────────────
def main_page():
    zone_cards = _cards([
        (z["name"], z["focus"].split(". ")[0] + ".", f'/gyeonggi/zone/{z["key"]}/')
        for z in ZONES
    ])

    # 시군 카드 — 31개 전부 내부링크
    city_cells = "".join(
        f'<a href="/gyeonggi/{c["slug"]}/" class="card"><h3>{c["name"]}</h3>'
        f'<p>{" · ".join(c["life"][:2]) if c["life"] else "차량 이동 기준 안내"}</p></a>'
        for c in CITIES
    )
    city_grid = f'<div class="card-grid">{city_cells}</div>'

    # 핵심 생활권 카드 — 25개 생활권 허브로 직접 연결
    life_grid = _cards([
        (l["name"], f"{l['city_name']} {l['name']} 생활권 · 출장마사지 예약 기준",
         f"/gyeonggi/life/{l['slug']}/")
        for l in LIFE
    ])

    faq = [
        ("경기 전지역을 한 번에 모두 색인해도 되나요?",
         "권장하지 않습니다. 전체 시군과 읍면동은 데이터로 보관하고, 1차는 핵심 도시와 생활권부터 색인하는 것이 좋습니다."),
        ("경기남부와 경기북부 페이지를 따로 만들어야 하나요?",
         "만드는 것이 좋습니다. 경기도는 면적이 넓어 남부와 북부의 이동 기준이 다릅니다."),
        ("일반구가 있는 도시는 어떻게 구성하나요?",
         "수원, 용인, 성남, 고양, 부천, 안산, 안양은 시 페이지 아래 일반구 안내를 두고, 그 아래 대표 동을 연결합니다."),
        ("환승역은 노선별로 나눠도 되나요?",
         "나누지 않습니다. 금정역, 기흥역, 정자역 같은 환승역도 역명 기준 한 페이지로 안내합니다."),
        ("외곽 지역도 방문이 가능한가요?",
         "가평·연천·포천·여주·양평 등 외곽은 예약 전 차량 이동 가능 여부와 추가 이동비를 먼저 확인하면 방문 가능합니다."),
    ]

    hero = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">경기 전지역 방문 관리</div>
    <h1 class="hero-title">경기 출장마사지·<span class="hero-accent">홈타이</span><br>주요 생활권 안내</h1>
    <p class="hero-lead">수원, 분당, 용인, 일산, 부천, 안산, 안양, 동탄, 평택, 김포, 의정부 등 경기 주요 생활권별 방문 가능 지역과 예약 전 확인사항을 안내합니다.</p>
    <div class="hero-cta">
      <a href="#zones" class="btn btn-primary">권역별 보기</a>
      <a href="#cities" class="btn btn-secondary">시군 찾기</a>
      <a href="#life" class="btn btn-secondary">생활권 찾기</a>
      <a href="/gyeonggi/reservation/" class="btn btn-secondary">예약 안내 보기</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-number">5</div><div class="stat-label">권역 안내</div></div>
    <div class="stat"><div class="stat-number">31</div><div class="stat-label">시군 페이지</div></div>
    <div class="stat"><div class="stat-number">25</div><div class="stat-label">핵심 생활권</div></div>
    <div class="stat"><div class="stat-number">24H</div><div class="stat-label">상담 가능</div></div>
  </div>
</div>"""

    body = f"""
<section id="intro">
  <h2>경기 출장마사지는 시군보다 생활권 기준이 중요합니다</h2>
  <p>경기도는 서울보다 면적이 넓고 도시별 이동 기준이 완전히 다릅니다. 같은 시 안에서도 이동 기준과 검색 의도가 다른데, 수원은 수원역·인계동과 광교·영통이 다르고, 성남은 분당·판교와 모란·수정구가 다릅니다. 용인은 수지·기흥·처인의 생활권이 완전히 다르고, 화성은 동탄과 향남·남양이 전혀 다른 이동권입니다.</p>
  <p>그래서 간다GO 경기 안내는 31개 시군을 단순 나열하지 않고, 먼저 <strong>경기남부·경기북부·경기서부·경기동부·경기외곽</strong> 다섯 개 권역으로 나눈 뒤 시군과 생활권을 분리해 안내합니다. 도심형 역세권 생활권과 신도시 생활권, 그리고 외곽 차량 이동권을 구분해 예약 전 정확한 정보를 확인할 수 있도록 구성했습니다.</p>
</section>

<section id="zones">
  <h2>경기 권역별 방문 가능 지역 안내</h2>
  <p>경기도를 다섯 개 권역으로 나누어 포함 시군과 대표 생활권, 이동 기준을 안내합니다.</p>
  {zone_cards}
</section>

<section id="cities">
  <h2>경기 31개 시군별 안내</h2>
  <p>경기 31개 시군 페이지로 바로 이동할 수 있습니다. 각 시군은 일반구·대표 동·대표 역·생활권·인접 시군 안내를 함께 제공합니다.</p>
  {city_grid}
</section>

<section id="life">
  <h2>경기 주요 생활권별 예약 기준</h2>
  <p>지역과 역을 연결한 생활권 기준으로 보면 더 정확한 방문 주소와 이동 시간을 확인할 수 있습니다. 생활권 안내는 시군 페이지와 함께 확인하세요.</p>
  {life_grid}
</section>

<section id="purpose">
  <h2>이용 목적별 안내</h2>
  <p>방문 장소와 목적에 따라 확인할 점이 다릅니다. 자택·숙소·오피스텔·업무지구·외곽 방문과 추가 이동비 기준을 안내합니다.</p>
  {_cards([
    ("자택 이용 안내", "자택 방문 시 주소·출입·준비 사항", "/gyeonggi/purpose/home/"),
    ("호텔·숙소 이용 안내", "호텔·펜션 방문 시 건물명·객실 안내", "/gyeonggi/purpose/lodging/"),
    ("오피스텔 이용 안내", "오피스텔 공동현관·호수 출입 안내", "/gyeonggi/purpose/officetel/"),
    ("업무지구 예약 안내", "판교·광교·동탄 업무지구 출입 안내", "/gyeonggi/purpose/business/"),
    ("외곽 지역 이용 안내", "가평·연천·포천 등 차량 이동 기준", "/gyeonggi/purpose/outer/"),
    ("추가 이동비 안내", "기본 이동권과 추가 이동비 기준", "/gyeonggi/purpose/travel-fee/"),
  ])}
</section>

<section id="outer">
  <h2>경기 외곽 지역 예약 전 확인사항</h2>
  <p>경기도는 외곽 지역이 많아 도심형 예약 기준과 외곽형 예약 기준을 분리해야 합니다. 양평, 가평, 연천, 포천, 안성, 여주, 이천 일부 지역은 예약 전 차량 이동 가능 여부와 추가 이동비 여부를 먼저 확인해야 합니다.</p>
  <ul>
    <li><strong>방문 가능 주소</strong> 및 <strong>예약 가능 시간</strong> 확인</li>
    <li><strong>차량 이동 가능 여부</strong>와 <strong>추가 이동비</strong> 확인</li>
    <li><strong>숙소 이용 가능 여부</strong>와 <strong>예약 변경 기준</strong> 확인</li>
    <li><strong>개인정보 처리 기준</strong>과 <strong>불법·선정적 서비스 불가</strong> 안내</li>
  </ul>
</section>
{_BYLINE}
<section id="faq">
  <h2>경기 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    {''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)}
  </dl>
</section>
"""

    return {
        "path": "gyeonggi/",
        "title": "경기 출장마사지｜수원·분당·용인·부천·일산 홈타이 안내",
        "desc": "경기 출장마사지·홈타이 예약 전 수원, 분당, 용인, 부천, 일산, 동탄 생활권을 확인하세요.",
        "h1": "경기 출장마사지·홈타이 · 주요 생활권 안내",
        "hero": hero,
        "breadcrumb": [],
        "extra_head": _faq_schema(faq),
        "body": body,
    }


# ── 권역 페이지 ─────────────────────────────────────────────
def zone_page(zone):
    cities = [CITY_BY_SLUG[s] for s in zone["cities"] if s in CITY_BY_SLUG]
    city_cards = _cards([
        (c["name"], (" · ".join(c["life"][:2]) if c["life"]
                     else "차량 이동 기준 안내") + " 생활권",
         f'/gyeonggi/{c["slug"]}/')
        for c in cities
    ])
    # 권역 대표 생활권·역 모으기
    life = []
    stations = []
    for c in cities:
        life += c["life"][:2]
        stations += c["stations"][:2]
    life = list(dict.fromkeys(life))[:12]
    stations = list(dict.fromkeys(stations))[:14]

    body = f"""
<section id="overview">
  <h2>{zone['name']} 권역 안내</h2>
  <p>{zone['focus']}</p>
</section>

<section id="cities">
  <h2>{zone['name']} 포함 시군</h2>
  <p>{zone['name']} 권역에 포함되는 시군별 안내 페이지입니다. 각 시군의 대표 생활권과 이동 기준을 확인하세요.</p>
  {city_cards}
</section>

<section id="city-summary">
  <h2>{zone['name']} 시군별 한눈 요약</h2>
  <dl class="faq-list">
    {''.join(f'<dt><a href="/gyeonggi/{c["slug"]}/">{c["name"]}</a></dt><dd>{c["focus"].split(". ")[0]}.</dd>' for c in cities)}
  </dl>
</section>

<section id="life">
  <h2>{zone['name']} 대표 생활권</h2>
  <p>{zone['name']} 권역에서 검색·예약이 많은 대표 생활권입니다.</p>
  <p>{' · '.join(life)}</p>
</section>

<section id="stations">
  <h2>{zone['name']} 대표 역세권</h2>
  <p>역세권은 역명 기준 한 페이지로 안내하며, 환승역도 노선별로 나누지 않습니다.</p>
  <p>{' · '.join(stations)}</p>
</section>

<section id="zone-guide">
  <h2>{zone['name']} 이동·예약 기준</h2>
  <p>{zone['name']}은(는) 도심 역세권 생활권과 신도시·외곽 생활권의 예약 기준이 서로 다릅니다. 도심·신도시 생활권은 가까운 역과 기본 이동권을 기준으로 방문 주소를 정하면 되고, 외곽 방향은 예약 전 <strong>차량 이동 가능 여부</strong>, <strong>예약 가능 시간</strong>, <strong>추가 이동비</strong>, <strong>숙소 이용 가능 여부</strong>를 먼저 확인하는 것이 좋습니다.</p>
  <p>방문 주소가 시군 경계에 있다면 인접 권역·시군 기준이 적용될 수 있으니, 예약 시 도로명 주소와 건물 유형을 함께 알려주시면 가장 빠르게 안내해 드릴 수 있습니다. 권역 전체 안내는 <a href="/gyeonggi/">경기 메인</a>에서, 예약 방법은 <a href="/gyeonggi/reservation/">예약 안내</a>에서 확인하세요.</p>
</section>
{_CHECK_BLOCK}
{_BYLINE}
"""
    return {
        "path": f"gyeonggi/zone/{zone['key']}/",
        "title": zone["title"],
        "desc": zone["desc"],
        "h1": f"{zone['name']} 출장마사지·홈타이 권역별 생활권 안내",
        "breadcrumb": [("경기", "/gyeonggi/"), ("권역별 안내", ""), (zone["name"], "")],
        "body": body,
    }


# ── 시군 페이지 ─────────────────────────────────────────────
def city_page(c):
    zone = ZONE_BY_KEY[c["zone"]]

    # 구조: 일반구가 있으면 구 → 동, 없으면 동
    if c["gu"]:
        gu_items = GU_BY_CITY.get(c["slug"], [])
        gu_links = " · ".join(
            f'<a href="/gyeonggi/{c["slug"]}/{g["slug"]}/">{g["gu"]}</a>' for g in gu_items
        ) or ", ".join(c["gu"])
        struct = (
            f'<p><strong>{c["name"]}</strong>은(는) {", ".join(c["gu"])} 일반구로 나뉩니다. '
            f'시 → 구 → 동 구조로 생활권을 확인하면 방문 주소를 더 정확히 정할 수 있습니다. '
            f'각 구별 안내는 다음에서 확인하세요: {gu_links}.</p>'
            f'<p>대표 동: {", ".join(c["dong"])}</p>'
        )
    else:
        all_dongs = _dongs_of_city_nogu(c["slug"])
        if all_dongs:
            dong_links = " · ".join(
                f'<a href="/gyeonggi/{c["slug"]}/{d["slug"]}/">{d["name"]}</a>'
                for d in all_dongs
            )
            struct = (
                f'<p><strong>{c["name"]}</strong>은(는) 시군 → 읍면동 구조로 안내합니다. '
                f'아래 {len(all_dongs)}개 읍·면·동을 클릭하면 동별 방문 안내로 이동합니다. '
                f'(1·2·3동 등 번호 동은 대표 동 하나로 묶었습니다.)</p>'
                f'<p class="dong-list">{dong_links}</p>'
            )
        else:
            struct = (f'<p><strong>{c["name"]}</strong>은(는) 시군 → 읍면동 구조로 안내합니다. '
                      f'도심권과 외곽 생활권 기준으로 방문 안내를 확인하세요.</p>')

    stations_html = (
        f'<p>{_station_links(c["stations"])}</p>'
        if c["stations"]
        else '<p>이 지역은 도시철도 역세권이 제한적이라 역 기준보다 <strong>차량 이동 기준</strong>과 방문 가능 주소를 먼저 확인하는 것이 좋습니다.</p>'
    )

    life_html = (
        _cards([
            (lf, f"{c['name']} {lf} 생활권 · 출장마사지·홈타이 예약 기준",
             f"/gyeonggi/life/{_LIFE_SLUG_BY_NAME[lf]}/" if lf in _LIFE_SLUG_BY_NAME
             else f"/gyeonggi/{c['slug']}/#check")
            for lf in c["life"]
        ])
        if c["life"] else "<p>생활권은 도심권과 외곽권으로 나누어 예약 기준을 확인합니다.</p>"
    )

    nearby_html = _li_links([(name, f"/gyeonggi/{slug}/") for name, slug in c["nearby"]])

    outer_html = ""
    if c["outer"]:
        outer_html = f"""
<section id="outer">
  <h2>{c['name']} 외곽 지역 이용 안내</h2>
  <p>{c['name']}은(는) 도심권과 외곽 차량 이동권이 함께 있어 예약 기준을 분리해야 합니다. 외곽 방향은 예약 전 <strong>차량 이동 가능 여부</strong>, <strong>예약 가능 시간</strong>, <strong>추가 이동비</strong>, <strong>숙소 이용 가능 여부</strong>를 먼저 확인하면 방문 일정을 정확히 잡을 수 있습니다.</p>
</section>"""

    faq = [
        (f"{c['name']} 어느 생활권까지 방문이 가능한가요?",
         f"{c['name']} 전역으로 방문 가능합니다. 다만 {(' · '.join(c['life'][:3])) if c['life'] else '도심·외곽'} 등 생활권에 따라 이동 기준이 다르므로 예약 전 정확한 방문 주소를 알려주시는 것이 좋습니다."),
        (f"{c['name']}에서 예약 전 확인할 사항은 무엇인가요?",
         "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 개인정보 처리 기준을 먼저 확인하면 예약이 수월합니다."),
        (f"{c['name']} 출장마사지·홈타이는 어떤 서비스인가요?",
         "고객의 자택·숙소·오피스텔 등으로 전문가가 방문하는 방문형 관리 서비스입니다. 건전한 위생·안전 기준 안에서만 제공되며 불법·선정적 요청에는 응하지 않습니다."),
    ]

    body = f"""
<section id="overview">
  <h2>{c['name']}에서 출장마사지를 찾을 때 확인할 기준</h2>
  <p>{c['focus']}</p>
  <p>{c['name']}은(는) <a href="/gyeonggi/zone/{zone['key']}/">{zone['name']}</a> 권역에 속합니다. 예약 전 자신의 위치가 어느 생활권에 해당하는지, 가장 가까운 역과 기본 이동권 범위 안에 있는지를 먼저 확인하면 예약 과정이 한결 원활합니다.</p>
</section>

<section id="structure">
  <h2>{c['name']} 구·동 구조</h2>
  {struct}
</section>

<section id="stations">
  <h2>{c['name']} 대표 역세권</h2>
  {stations_html}
</section>

<section id="life">
  <h2>{c['name']} 생활권별 예약 기준</h2>
  {life_html}
</section>
{_life_detail(c)}
{outer_html}
<section id="places">
  <h2>{c['name']} 방문 장소별 안내</h2>
  <p>{c['name']}에서는 자택·숙소·오피스텔·업무 공간 등 방문 장소에 따라 확인할 점이 다릅니다. 목적별 안내에서 출입 기준과 준비 사항을 확인하세요.</p>
  <ul>{_purpose_links()}</ul>
</section>

<section id="nearby">
  <h2>{c['name']} 인접 시군 안내</h2>
  <p>{c['name']}과(와) 이동권이 이어지는 인접 시군입니다. 방문 주소가 경계 지역이라면 인접 시군 안내도 함께 확인하세요.</p>
  <ul>{nearby_html}</ul>
</section>
{_CHECK_BLOCK}
{_BYLINE}
<section id="faq">
  <h2>{c['name']} 출장마사지·홈타이 자주 묻는 질문</h2>
  <dl class="faq-list">
    {''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)}
  </dl>
</section>
"""
    return {
        "path": f"gyeonggi/{c['slug']}/",
        "title": c["title"],
        "desc": c["desc"],
        "h1": f"{c['name']} 출장마사지·홈타이 생활권별 예약 안내",
        "breadcrumb": [("경기", "/gyeonggi/"),
                        (zone["name"], f"/gyeonggi/zone/{zone['key']}/"),
                        (c["name"], "")],
        "extra_head": _faq_schema(faq),
        "body": body,
    }


# ── 일반구 페이지 ───────────────────────────────────────────
def gu_page(g):
    city = CITY_BY_SLUG[g["city"]]
    zone = ZONE_BY_KEY[city["zone"]]
    base = f'/gyeonggi/{g["city"]}/{g["slug"]}/'

    # 동별 안내 — (동, 한 줄 특징) 데이터로 구별 고유 본문 구성.
    # 해당 동의 상세 페이지가 있으면 동 이름에 링크를 건다.
    def _dlabel(name):
        slug = _DONG_SLUG_BY_KEY.get((g["city"], name))
        return (f'<a href="/gyeonggi/{g["city"]}/{g["slug"]}/{slug}/">{name}</a>'
                if slug else name)
    dong_rows = "".join(
        f"<dt>{_dlabel(d)}</dt><dd>{note} 일대 생활권입니다. 방문 시 정확한 단지·건물명과 출입 방식을 함께 알려주시면 빠르게 안내해 드립니다.</dd>"
        for d, note in g["dong"]
    )

    # 구 소속 전체 행정동 목록(클릭 동선 완결)
    gu_all = _dongs_of_gu(g["city"], g["slug"])
    gu_all_links = " · ".join(
        f'<a href="/gyeonggi/{g["city"]}/{g["slug"]}/{d["slug"]}/">{d["name"]}</a>'
        for d in gu_all
    )

    # 같은 시의 다른 구 (형제 구) 내부링크
    siblings = [x for x in GU_BY_CITY.get(g["city"], []) if x["slug"] != g["slug"]]
    sib_links = _li_links([(x["gu"], f'/gyeonggi/{g["city"]}/{x["slug"]}/') for x in siblings])

    life_html = _cards([
        (lf, f"{g['gu']} {lf} 생활권 · 예약 기준", base + "#check") for lf in g["life"]
    ]) if g["life"] else ""

    faq = [
        (f"{g['city_name']} {g['gu']}는 어디까지 방문이 가능한가요?",
         f"{g['gu']} 전역으로 방문 가능합니다. {' · '.join(d for d, _ in g['dong'][:4])} 등 동별로 가까운 역과 이동권이 다르므로 예약 시 정확한 주소를 알려주세요."),
        (f"{g['gu']}에서 가까운 역은 어디인가요?",
         f"{' · '.join(g['stations']) if g['stations'] else '도시철도 역이 제한적이라 차량 이동 기준으로 안내합니다.'} 환승역도 역명 기준 한 곳으로 안내합니다."),
        (f"{g['gu']} 예약 전 확인할 사항은 무엇인가요?",
         "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식을 먼저 확인하면 예약이 수월합니다."),
    ]

    body = f"""
<section id="overview">
  <h2>{g['city_name']} {g['gu']} 생활권 안내</h2>
  <p>{g['focus']}</p>
  <p>{g['gu']}는 <a href="/gyeonggi/{g['city']}/">{g['city_name']}</a>의 일반구로, 시 전체 안내와 동 단위 사이의 중간 안내 역할을 합니다. {g['city_name']}은(는) <a href="/gyeonggi/zone/{zone['key']}/">{zone['name']}</a> 권역에 속합니다.</p>
</section>

<section id="dong">
  <h2>{g['gu']} 대표 동 안내</h2>
  <p>{g['gu']} 안에서도 동에 따라 가까운 역과 생활권이 다릅니다. 방문 주소가 어느 동인지 확인하면 이동 기준을 정확히 안내해 드릴 수 있습니다.</p>
  <dl class="faq-list">{dong_rows}</dl>
</section>

<section id="dong-all">
  <h2>{g['gu']} 행정동 전체 안내</h2>
  <p>{g['gu']} 소속 행정동입니다. 아래에서 동을 클릭하면 동별 출장마사지·홈타이 방문 안내로 이동합니다. (1·2·3동 등 번호 동은 대표 동 하나로 묶었습니다.)</p>
  <p class="dong-list">{gu_all_links}</p>
</section>

<section id="stations">
  <h2>{g['gu']} 가까운 역</h2>
  <p>{' · '.join(g['stations']) if g['stations'] else '이 구는 도시철도 역세권이 제한적이라 차량 이동 기준과 방문 가능 주소를 먼저 확인하는 것이 좋습니다.'}</p>
</section>

<section id="life">
  <h2>{g['gu']} 관련 생활권</h2>
  {life_html or '<p>도심권과 주거권으로 나누어 예약 기준을 확인합니다.</p>'}
</section>

<section id="parent">
  <h2>상위 시·인접 구 안내</h2>
  <p>{g['gu']}의 상위 시 전체 안내는 <a href="/gyeonggi/{g['city']}/">{g['city_name']} 출장마사지 안내</a>에서 확인할 수 있습니다. 같은 {g['city_name']} 내 다른 구는 아래에서 확인하세요.</p>
  <ul>{sib_links or f'<li><a href="/gyeonggi/{g["city"]}/">{g["city_name"]} 전체 안내</a></li>'}</ul>
</section>
{_CHECK_BLOCK}
{_BYLINE}
<section id="faq">
  <h2>{g['city_name']} {g['gu']} 자주 묻는 질문</h2>
  <dl class="faq-list">{''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)}</dl>
</section>
"""
    return {
        "path": f"gyeonggi/{g['city']}/{g['slug']}/",
        "title": f"{g['city_name']} {g['gu']} 출장마사지·홈타이 생활권 안내",
        "desc": f"{g['city_name']} {g['gu']} 출장마사지·홈타이 — {' · '.join([d for d, _ in g['dong'][:3]])} 생활권 안내.",
        "h1": f"{g['city_name']} {g['gu']} 출장마사지·홈타이 생활권 안내",
        "breadcrumb": [("경기", "/gyeonggi/"),
                        (g["city_name"], f"/gyeonggi/{g['city']}/"),
                        (g["gu"], "")],
        "extra_head": _faq_schema(faq),
        "body": body,
    }


# ── 생활권(life-area) 페이지 ────────────────────────────────
def life_page(l):
    city = CITY_BY_SLUG[l["city"]]
    zone = ZONE_BY_KEY[city["zone"]]

    _dtpl = [
        "{d}은(는) {st} 인근 이동권에 속합니다. 자택·숙소·오피스텔 등 방문 장소 유형과 건물 출입 방식을 함께 알려주시면 예약이 빠릅니다.",
        "{d} 일대는 {st} 방향 생활권으로, 단지·건물명과 동호수를 확인해 두면 방문 일정을 정확히 잡을 수 있습니다.",
        "{d}은(는) {st}을(를) 끼고 있어 방문 수요가 꾸준합니다. 야간·새벽 방문도 사전 확인을 통해 조율할 수 있습니다.",
        "{d} 쪽은 {st} 기준으로 이동권이 형성됩니다. 경계 지역이라면 인접 생활권 기준이 적용될 수 있으니 도로명 주소를 알려주세요.",
    ]
    _st = l["stations"][0] if l["stations"] else l["city_name"]
    dong_html = "".join(
        f"<dt>{d}</dt><dd>{_dtpl[i % len(_dtpl)].format(d=d, st=l['stations'][i % len(l['stations'])] if l['stations'] else _st)}</dd>"
        for i, d in enumerate(l["dong"])
    )

    # 같은 시의 다른 생활권 (인접 생활권 내부링크)
    siblings = [x for x in LIFE if x["city"] == l["city"] and x["slug"] != l["slug"]]
    sib_links = _li_links([(x["name"], f"/gyeonggi/life/{x['slug']}/") for x in siblings])

    faq = [
        (f"{l['name']} 생활권은 어디까지 포함되나요?",
         f"{l['city_name']}의 {' · '.join(l['dong'])} 일대를 중심으로 한 생활권입니다. 가까운 역은 {' · '.join(l['stations'])}이며, 경계 지역은 인접 생활권 기준이 적용될 수 있습니다."),
        (f"{l['name']}에서 예약 전 확인할 사항은?",
         "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식을 먼저 확인하면 예약이 수월합니다."),
    ]

    body = f"""
<section id="overview">
  <h2>{l['name']} 생활권 안내</h2>
  <p>{l['focus']}</p>
  <p>{l['name']}은(는) <a href="/gyeonggi/{l['city']}/">{l['city_name']}</a>에 속한 생활권으로, 시군 안내와 역세권·동 안내를 잇는 허브 역할을 합니다. {l['city_name']}은(는) <a href="/gyeonggi/zone/{zone['key']}/">{zone['name']}</a> 권역입니다.</p>
</section>

<section id="stations">
  <h2>{l['name']} 가까운 역</h2>
  <p>{_station_links(l['stations'])}. 환승역도 노선별로 나누지 않고 역명 기준 한 곳으로 안내합니다.</p>
</section>

<section id="dong">
  <h2>{l['name']} 구성 동 안내</h2>
  <p>{l['name']} 생활권을 이루는 대표 동입니다. 방문 주소가 어느 동인지 확인하면 이동 기준을 정확히 안내해 드릴 수 있습니다.</p>
  <dl class="faq-list">{dong_html}</dl>
</section>

<section id="guide">
  <h2>{l['name']} 이용·예약 기준</h2>
  <p>{l['name']} 생활권은 같은 {l['city_name']} 안에서도 다른 권역과 이동 기준이 구분됩니다. 방문 주소가 이 생활권에 해당한다면 기본 이동권 범위 안에서 안내되며, 추가 이동비가 발생하는지는 정확한 주소를 확인한 뒤 안내해 드립니다. 자택·숙소·오피스텔 등 방문 장소 유형과 예약 가능 시간을 함께 알려주시면 방문 일정을 빠르게 확정할 수 있습니다. 예약 방법은 <a href="/gyeonggi/reservation/">예약 안내</a>, 확인사항은 <a href="/gyeonggi/check/">이용 전 확인사항</a>에서 볼 수 있습니다.</p>
</section>

<section id="related">
  <h2>관련 시군·생활권 안내</h2>
  <p>{l['name']}의 상위 시 전체 안내는 <a href="/gyeonggi/{l['city']}/">{l['city_name']} 출장마사지 안내</a>에서 확인하세요. {l['city_name']} 내 다른 생활권은 아래에서 확인할 수 있습니다.</p>
  <ul>{sib_links or f'<li><a href="/gyeonggi/{l["city"]}/">{l["city_name"]} 전체 안내</a></li>'}</ul>
</section>
{_CHECK_BLOCK}
{_BYLINE}
<section id="faq">
  <h2>{l['name']} 자주 묻는 질문</h2>
  <dl class="faq-list">{''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)}</dl>
</section>
"""
    return {
        "path": f"gyeonggi/life/{l['slug']}/",
        "title": f"{l['name']} 출장마사지·홈타이 생활권 안내",
        "desc": f"{l['name']} 출장마사지·홈타이 — {l['city_name']} {' · '.join(l['dong'][:2])} 생활권 예약 안내.",
        "h1": f"{l['name']} 출장마사지·홈타이 생활권 예약 안내",
        "breadcrumb": [("경기", "/gyeonggi/"),
                        (l["city_name"], f"/gyeonggi/{l['city']}/"),
                        (l["name"], "")],
        "extra_head": _faq_schema(faq),
        "body": body,
    }


# ── 역세권(station) 페이지 ──────────────────────────────────
_SDTPL = [
    "{a}은(는) {name} 이용권에 속하는 지역입니다. 자택·숙소·오피스텔 등 방문 장소 유형을 알려주시면 빠르게 안내해 드립니다.",
    "{a} 일대는 {name}을(를) 끼고 있어, 단지·건물명과 출입 방식을 확인하면 방문 일정을 정확히 잡을 수 있습니다.",
    "{a} 쪽은 {name} 기준으로 이동권이 형성됩니다. 경계 지역이라면 인접 역·생활권 기준이 적용될 수 있으니 도로명 주소를 알려주세요.",
]


def station_page(s):
    city = CITY_BY_SLUG[s["city"]]
    zone = ZONE_BY_KEY[city["zone"]]

    area_html = "".join(
        f"<dt>{a}</dt><dd>{_SDTPL[i % len(_SDTPL)].format(a=a, name=s['name'])} "
        f"{_SDTPL[(i + 1) % len(_SDTPL)].format(a=a, name=s['name'])}</dd>"
        for i, a in enumerate(s["areas"])
    )

    # 노선·환승 안내 (역마다 노선 구성이 달라 고유)
    if len(s["lines"]) > 1:
        line_note = (
            f"{s['name']}은 {' · '.join(s['lines'])}이(가) 만나는 환승역입니다. "
            f"환승 거점이라 유동 인구가 많지만, 노선별·출구별로 페이지를 나누지 않고 "
            f"{s['name']} 한 곳을 기준으로 인근 생활권을 안내합니다. 환승 동선과 가까운 출구 정보를 "
            f"함께 알려주시면 방문 위치를 더 빠르게 확인할 수 있습니다."
        )
    else:
        line_note = (
            f"{s['name']}은 {s['lines'][0]}이(가) 지나는 역입니다. 단일 노선 역세권으로 "
            f"역 주변 생활권이 비교적 명확하므로, 방문 주소가 역과 도보권인지 차량 이동권인지 "
            f"확인하면 기본 이동권 범위를 정확히 안내해 드릴 수 있습니다."
        )

    # 같은 시의 생활권·다른 역 내부링크
    city_life = [l for l in LIFE if l["city"] == s["city"]]
    life_links = _li_links([(l["name"], f"/gyeonggi/life/{l['slug']}/") for l in city_life])
    sib_st = [x for x in STATIONS if x["city"] == s["city"] and x["slug"] != s["slug"]]
    sib_links = _li_links([(x["name"], f"/gyeonggi/station/{x['slug']}/") for x in sib_st])

    faq = [
        (f"{s['name']}은 무슨 노선인가요?",
         f"{s['name']}은 {' · '.join(s['lines'])} 노선이 지나는 역입니다. 환승역이라도 노선별로 나누지 않고 역명 기준 한 페이지로 안내합니다."),
        (f"{s['name']} 인근 어디까지 방문이 가능한가요?",
         f"{' · '.join(s['areas'])} 등 {s['name']} 인근 생활권으로 방문 가능합니다. 정확한 방문 주소와 건물 출입 방식을 알려주시면 예약이 수월합니다."),
    ]

    body = f"""
<section id="overview">
  <h2>{s['name']} 역세권 안내</h2>
  <p>{s['focus']}</p>
  <p>{s['name']}은 <a href="/gyeonggi/{s['city']}/">{s['city_name']}</a>에 위치한 역으로, {' · '.join(s['lines'])} 노선이 지납니다. {s['city_name']}은(는) <a href="/gyeonggi/zone/{zone['key']}/">{zone['name']}</a> 권역이며, 환승역도 출구별·노선별로 나누지 않고 역명 기준 한 곳으로 안내합니다.</p>
</section>

<section id="lines">
  <h2>{s['name']} 노선·환승 안내</h2>
  <p>{line_note}</p>
</section>

<section id="nearby">
  <h2>{s['name']} 인접 동·생활권</h2>
  <p>{s['name']} 인근에서도 동에 따라 이동권이 조금씩 다릅니다. 방문 주소가 어느 동인지 확인하면 안내가 정확합니다.</p>
  <dl class="faq-list">{area_html}</dl>
</section>

<section id="guide">
  <h2>{s['name']} 이용·예약 기준</h2>
  <p>{s['name']} 인근은 {s['city_name']} 안에서도 다른 권역과 이동 기준이 구분됩니다. 역과 도보권이면 기본 이동권 범위에서 안내되고, 차량 이동이 필요한 거리라면 추가 이동비 발생 여부를 정확한 주소 확인 후 안내해 드립니다. 자택·숙소·오피스텔 등 방문 장소 유형과 예약 가능 시간을 함께 알려주시면 방문 일정을 빠르게 확정할 수 있습니다. 예약 방법은 <a href="/gyeonggi/reservation/">예약 안내</a>, 확인사항은 <a href="/gyeonggi/check/">이용 전 확인사항</a>에서 확인하세요.</p>
</section>

<section id="related">
  <h2>{s['city_name']} 연결 생활권·역</h2>
  <p>{s['name']}과(와) 이어지는 {s['city_name']} 생활권 및 인근 역 안내입니다.</p>
  <ul>{life_links}{sib_links}</ul>
</section>
{_CHECK_BLOCK}
{_BYLINE}
<section id="faq">
  <h2>{s['name']} 자주 묻는 질문</h2>
  <dl class="faq-list">{''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)}</dl>
</section>
"""
    return {
        "path": f"gyeonggi/station/{s['slug']}/",
        "title": f"{s['name']} 출장마사지·홈타이 역세권 안내",
        "desc": f"{s['name']} 출장마사지·홈타이 — {s['city_name']} {' · '.join(s['areas'][:2])} 인근 생활권 안내.",
        "h1": f"{s['name']} 출장마사지·홈타이 역세권 예약 안내",
        "breadcrumb": [("경기", "/gyeonggi/"),
                        (s["city_name"], f"/gyeonggi/{s['city']}/"),
                        (s["name"], "")],
        "extra_head": _faq_schema(faq),
        "body": body,
    }


# ── 읍면동(dong) 페이지 ─────────────────────────────────────
def dong_page(d):
    city = CITY_BY_SLUG[d["city"]]
    zone = ZONE_BY_KEY[city["zone"]]
    gu_name = _GU_NAME.get((d["city"], d["gu"])) if d["gu"] else None

    # URL·브레드크럼 (구 유무에 따라)
    if d["gu"]:
        path = f"gyeonggi/{d['city']}/{d['gu']}/{d['slug']}/"
        parent_url = f"/gyeonggi/{d['city']}/{d['gu']}/"
        parent_label = f"{d['city_name']} {gu_name}"
        crumb = [("경기", "/gyeonggi/"), (d["city_name"], f"/gyeonggi/{d['city']}/"),
                 (gu_name, parent_url), (d["name"], "")]
    else:
        path = f"gyeonggi/{d['city']}/{d['slug']}/"
        parent_url = f"/gyeonggi/{d['city']}/"
        parent_label = f"{d['city_name']}"
        crumb = [("경기", "/gyeonggi/"), (d["city_name"], parent_url), (d["name"], "")]

    adj = " · ".join(d["adjacent"]) if d["adjacent"] else "인접 생활권"
    st_html = (_station_links(d["stations"]) if d["stations"]
               else "도시철도 역세권이 제한적이라 차량 이동 기준으로 안내합니다")

    # 같은 시 역·생활권 내부링크
    city_life = [l for l in LIFE if l["city"] == d["city"]]
    life_links = _li_links([(l["name"], f"/gyeonggi/life/{l['slug']}/") for l in city_life])
    near_st = [s for s in STATIONS if s["city"] == d["city"] and s["name"] in d["stations"]]
    st_links = _li_links([(s["name"], f"/gyeonggi/station/{s['slug']}/") for s in near_st])

    # 인접 동을 같은 시 동 페이지로 링크(있으면) — 시→구→동 내부 순환
    adj_links = []
    for a in d["adjacent"]:
        url = _dong_url(d["city"], a)
        adj_links.append(f'<a href="{url}">{a}</a>' if url else a)
    adj_linked = " · ".join(adj_links) if adj_links else "인접 생활권"

    zone_outer = CITY_BY_SLUG[d["city"]]["outer"]
    move_note = (
        f"{d['name']}은(는) 도심권과 외곽 차량 이동권이 함께 있는 {d['city_name']}에 속해, "
        "방문 주소에 따라 기본 이동권과 추가 이동비 적용이 달라질 수 있습니다."
        if zone_outer else
        f"{d['name']}은(는) 비교적 이동 동선이 명확한 생활권으로, 도보권이면 기본 이동권 안에서 안내됩니다."
    )

    faq = [
        (f"{d['name']}도 출장마사지·홈타이 방문이 가능한가요?",
         f"{d['city_name']} {d['name']} 전역으로 방문 가능합니다. {adj} 등 인접 지역과 이동권이 이어지며, 정확한 단지·건물명과 출입 방식을 알려주시면 예약이 수월합니다."),
        (f"{d['name']}에서 가까운 역은 어디인가요?",
         f"{' · '.join(d['stations']) if d['stations'] else '가까운 도시철도 역이 제한적이라 차량 이동 기준으로 안내합니다.'} 환승역도 역명 기준 한 곳으로 안내합니다."),
        (f"{d['name']}은 어떤 장소로 방문하나요?",
         "자택·숙소·오피스텔·업무 공간 등으로 방문 가능합니다. 방문 장소 유형에 따라 출입 절차가 다르므로 예약 시 함께 알려주세요."),
        (f"{d['name']} 예약 시 추가 비용이 있나요?",
         "기본 이동권 안이면 추가 이동비가 없습니다. 외곽·원거리는 거리 기준으로 발생할 수 있으며, 정확한 금액은 주소 확인 후 사전에 안내합니다."),
    ]

    body = f"""
<section id="overview">
  <h2>{d['city_name']} {d['name']} 출장마사지·홈타이 안내</h2>
  <p>{d['note']}</p>
  <p>{d['name']}은(는) <a href="{parent_url}">{parent_label}</a>에 속하는 행정동으로, {d['city_name']}은(는) <a href="/gyeonggi/zone/{zone['key']}/">{zone['name']}</a> 권역에 위치합니다. 경기도는 같은 시·구 안에서도 동에 따라 가까운 역과 이동 기준이 다르기 때문에, 방문 주소가 정확히 {d['name']}에 해당하는지 먼저 확인하면 이동권 안내가 한결 정확합니다. {move_note}</p>
</section>

<section id="area">
  <h2>{d['name']} 위치와 생활권</h2>
  <p>{d['name']}은(는) {parent_label} 생활권의 한 축을 이루며, 인접한 {adj_linked} 일대와 이동권이 자연스럽게 이어집니다. 같은 동 안에서도 대단지 아파트, 빌라·다세대, 오피스텔, 단독주택 등 주거 형태가 섞여 있어 방문 위치에 따라 출입 방식이 달라집니다. 예약 시 단지명과 동·호수, 또는 건물명과 공동현관 출입 방법을 함께 알려주시면 방문 동선을 정확히 잡을 수 있습니다.</p>
  <p>{d['name']}이(가) 시·구 경계에 가까운 경우에는 인접 동이나 인접 생활권 기준이 적용될 수 있습니다. 정확한 도로명 주소를 알려주시면 어느 이동권으로 안내하는지 빠르게 확인해 드립니다.</p>
</section>

<section id="transport">
  <h2>{d['name']} 교통·이동 안내</h2>
  <p>가까운 역: {st_html}. 환승역도 노선별·출구별로 나누지 않고 역명 기준 한 곳으로 안내합니다. 역과 도보권인 주소는 기본 이동권 범위에서 안내되고, 역과 떨어진 주소는 차량 이동 기준으로 안내합니다.</p>
  <p>인접 동·생활권: {adj_linked}. 방문 주소가 이 가운데 어디와 더 가까운지에 따라 이동 동선이 달라질 수 있습니다.</p>
</section>

<section id="places">
  <h2>{d['name']} 방문 장소별 안내</h2>
  <p>{d['name']}에서는 방문 장소 유형에 따라 확인할 점이 다릅니다. 아래 목적별 안내에서 주거·숙소·업무 공간별 출입 기준과 준비 사항을 확인하세요.</p>
  <ul>{_purpose_links()}</ul>
</section>

<section id="guide">
  <h2>{d['name']} 이용·예약 기준</h2>
  <p>{d['name']} 방문은 기본 이동권 범위 안에서 안내되며, 차량 이동이 필요한 거리라면 추가 이동비 발생 여부를 정확한 주소 확인 후 안내해 드립니다. 자택·숙소·오피스텔 등 방문 장소 유형과 예약 가능 시간, 건물 출입 방식을 함께 알려주시면 방문 일정을 빠르게 확정할 수 있습니다. 예약 방법은 <a href="/gyeonggi/reservation/">예약 안내</a>, 확인사항은 <a href="/gyeonggi/check/">이용 전 확인사항</a>에서 확인하세요.</p>
</section>

<section id="related">
  <h2>{d['city_name']} 연결 생활권·역 안내</h2>
  <p>{d['name']}과(와) 이어지는 {d['city_name']}의 생활권·역세권 안내입니다. 상위 안내는 <a href="{parent_url}">{parent_label} 안내</a>에서, 시 전체 안내는 <a href="/gyeonggi/{d['city']}/">{d['city_name']} 출장마사지·홈타이 안내</a>에서 확인하세요.</p>
  <ul>{st_links}{life_links}</ul>
</section>
{_CHECK_BLOCK}
{_BYLINE}
<section id="faq">
  <h2>{d['city_name']} {d['name']} 자주 묻는 질문</h2>
  <dl class="faq-list">{''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)}</dl>
</section>
"""
    return {
        "path": path,
        "title": f"{d['city_name']} {d['name']} 출장마사지·홈타이 안내",
        "desc": f"{d['city_name']} {d['name']} 출장마사지·홈타이 — {adj} 인근 생활권 예약 안내."[:79],
        "h1": f"{d['city_name']} {d['name']} 출장마사지·홈타이 생활권 안내",
        "breadcrumb": crumb,
        "extra_head": _faq_schema(faq),
        "body": body,
    }


def all_pages():
    pages = [root_redirect_page(), main_page()]
    pages += [zone_page(z) for z in ZONES]
    pages += [city_page(c) for c in CITIES]
    pages += [gu_page(g) for g in GU]
    pages += [life_page(l) for l in LIFE]
    pages += [station_page(s) for s in STATIONS]
    pages += [dong_page(d) for d in DONGS]
    return pages
