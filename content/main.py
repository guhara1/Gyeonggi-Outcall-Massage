import json
from .site import BRAND, BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")

# 메타 설명 (80자 이내)
DESC = "안산 출장마사지·홈타이 예약 전 중앙동, 고잔동, 초지동, 상록수, 선부동 생활권을 확인하세요."

# 자주 묻는 질문 (FAQ 스키마)
_FAQ = [
    ("안산 출장마사지는 어떤 서비스인가요?",
     "방문형 마사지 서비스로, 고객의 자택, 숙소, 오피스텔 등으로 전문가가 방문하여 관리하는 서비스입니다. 상록구와 단원구 전지역으로 방문 가능합니다."),

    ("상록구와 단원구의 생활권 차이가 뭔가요?",
     "상록구는 상록수역, 한대앞역, 본오동, 사동 중심의 북동부 생활권이고, 단원구는 중앙역, 고잔역, 초지역, 안산역 중심의 남서부·중심권 생활권입니다."),

    ("예약 전 꼭 확인해야 할 사항은?",
     "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식을 먼저 확인하고 예약하는 방식이 좋습니다."),

    ("중앙동과 고잔동은 어떻게 다른가요?",
     "중앙동은 중앙역 중심 상권과 행정 중심지를 중심으로, 고잔동은 호수공원·고잔신도시 주거지를 중심으로 운영됩니다."),

    ("추가 이동비는 어떻게 계산되나요?",
     "지역별로 기본 이동권이 정해져 있으며, 그 외 먼 거리는 추가 이동비가 발생할 수 있습니다. 예약 시 정확히 확인하세요."),
]

# FAQ 스키마 생성
_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "@id": f"#faq-{i+1}",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        }
        for i, (q, a) in enumerate(_FAQ)
    ]
}

_faq_schema_str = json.dumps(_faq_schema, ensure_ascii=False, indent=2)

# Organization 스키마
_org_schema = {
    "@context": "https://schema.org",
    "@type": "HealthAndBeautyBusiness",
    "name": BRAND,
    "telephone": PHONE,
    "url": _BASE + "/",
    "image": _BASE + "/assets/og-image.png",
    "description": "안산시 출장마사지·홈타이 안내 사이트",
    "areaServed": {
        "@type": "AdministrativeArea",
        "name": "경기도 안산시"
    },
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "00:00",
        "closes": "23:59"
    }
}

_org_schema_str = json.dumps(_org_schema, ensure_ascii=False, indent=2)

# BreadcrumbList 스키마 (메인 페이지는 홈만)
_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "홈",
            "item": _BASE + "/"
        }
    ]
}

_breadcrumb_schema_str = json.dumps(_breadcrumb_schema, ensure_ascii=False, indent=2)

_EXTRA_HEAD = f"""<script type="application/ld+json">
{_org_schema_str}
</script>
<script type="application/ld+json">
{_breadcrumb_schema_str}
</script>
<script type="application/ld+json">
{_faq_schema_str}
</script>"""

_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">안산시 전지역 방문 관리</div>
    <h1 class="hero-title">안산 출장마사지<br><span class="hero-accent">안산 홈타이</span><br>지역별 예약 안내</h1>
    <p class="hero-lead">중앙동, 고잔동, 초지동, 상록수, 선부동, 원곡동 등 안산 주요 생활권별 방문 가능 지역과 예약 전 확인사항을 안내합니다.</p>
    <div class="hero-cta">
      <a href="#coverage" class="btn btn-primary">지역별 안내 보기</a>
      <a href="#stations" class="btn btn-secondary">가까운 역 찾기</a>
      <a href="/reservation/" class="btn btn-secondary">예약 안내 보기</a>
      <a href="/check/" class="btn btn-secondary">이용 전 확인사항</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat">
      <div class="stat-number">2</div>
      <div class="stat-label">구별 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">21</div>
      <div class="stat-label">지역 페이지</div>
    </div>
    <div class="stat">
      <div class="stat-number">13</div>
      <div class="stat-label">역세권 안내</div>
    </div>
    <div class="stat">
      <div class="stat-number">24H</div>
      <div class="stat-label">상담 가능</div>
    </div>
  </div>
</div>"""

PAGE = {
    "path": "",
    "title": "안산 출장마사지｜중앙·고잔·초지·상록수 홈타이 지역 안내",
    "desc": DESC,
    "h1": "안산 출장마사지·홈타이 지역별 예약 안내",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": """
<section id="criteria">
  <h2>안산에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
  <p>안산시는 경기도 남부에 위치한 도시로, 상록구와 단원구 두 개 구로 나뉘며 각 구의 생활권이 뚜렷하게 구분됩니다. 출장마사지를 예약하기 전에 자신의 위치가 어느 구의 어느 생활권에 해당하는지 정확히 파악하는 것이 예약 과정에서 가장 중요한 첫 번째 단계입니다.</p>
  <p>상록구는 경기철도의 상록수역, 한대앞역, 사리역 인근과 본오동, 사동, 월피동, 성포동, 부곡동, 반월동 중심으로 구성되어 있습니다. 이곳은 주로 안산시의 북동부와 상록권 생활권으로 알려져 있으며, 한양대학교 에리카 캠퍼스가 위치한 학문과 문화의 거리이기도 합니다. 상록구 지역으로 예약 시에는 상록수역 근처의 교통 접근성과 본오동·사동 일대의 주거 밀집도를 고려하여 방문 주소와 시간을 결정하는 것이 좋습니다.</p>
  <p>단원구는 중앙역, 고잔역, 초지역, 안산역, 선부역, 원곡역, 원시역 인근과 고잔동, 중앙동, 호수동, 초지동, 원곡동, 선부동, 와동, 신길동, 대부동 중심으로 구성되어 있습니다. 이곳은 주로 안산시의 남서부와 중심권 생활권으로 알려져 있으며, 중앙역을 중심으로 한 상권과 고잔신도시·호수공원의 주거 지역, 그리고 다문화거리로 유명한 원곡동이 포함되어 있습니다. 단원구 지역으로 예약 시에는 중앙역의 접근성, 호수동 일대의 교통 편의성, 그리고 대부도 여행객들의 경우 차량 이동 기준을 미리 확인하는 것이 중요합니다.</p>
  <p>또한 안산시 전역으로 방문이 가능하며, 자택·숙소·오피스텔 등 다양한 방문 장소에 대응합니다. 예약 전에 자신의 주소가 어느 동에 해당하고, 가장 가까운 지하철역이 무엇인지, 그리고 기본 이동권 범위 내에 있는지를 사전에 확인하면 예약 과정이 훨씬 원활해집니다.</p>
</section>

<section id="coverage">
  <h2>상록구·단원구 생활권 차이</h2>
  <div class="card-grid">
    <a href="/sangnok-gu/" class="card">
      <h3>상록구</h3>
      <p>상록수역, 한대앞역, 본오동, 사동, 월피동 중심 생활권</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/danwon-gu/" class="card">
      <h3>단원구</h3>
      <p>중앙역, 고잔역, 초지역, 안산역, 선부동, 원곡동 중심 생활권</p>
      <span class="card-arrow">→</span>
    </a>
  </div>
</section>

<section id="areas">
  <h2>안산 대표 지역별 방문 가능 지역 안내</h2>
  <div class="card-grid">
    <a href="/danwon-gu/jungang-dong/" class="card">
      <h3>중앙동</h3>
      <p>중앙역, 고잔동, 안산 중심상권 인접 생활권</p>
    </a>
    <a href="/danwon-gu/gojan-dong/" class="card">
      <h3>고잔동</h3>
      <p>고잔역, 중앙역, 호수동 인접 생활권</p>
    </a>
    <a href="/danwon-gu/choji-dong/" class="card">
      <h3>초지동</h3>
      <p>초지역, 단원구청, 고잔신도시 인접 생활권</p>
    </a>
    <a href="/danwon-gu/wongok-dong/" class="card">
      <h3>원곡동</h3>
      <p>안산역, 원곡역, 다문화거리 인접 생활권</p>
    </a>
    <a href="/danwon-gu/seonbu-dong/" class="card">
      <h3>선부동</h3>
      <p>선부역, 달미역, 와동 인접 생활권</p>
    </a>
    <a href="/sangnok-gu/bono-dong/" class="card">
      <h3>본오동</h3>
      <p>상록수역, 사동, 이동 인접 생활권</p>
    </a>
    <a href="/sangnok-gu/sa-dong/" class="card">
      <h3>사동</h3>
      <p>한대앞역, 해양동, 사이동 인접 생활권</p>
    </a>
    <a href="/sangnok-gu/wolpi-dong/" class="card">
      <h3>월피동</h3>
      <p>성포동, 부곡동, 안산시청 인접 생활권</p>
    </a>
  </div>
</section>

<section id="stations">
  <h2>안산 주요 지하철역별 홈타이 안내</h2>
  <p>안산시의 주요 지하철역별로 인접한 지역과 예약 기준을 안내합니다. 각 역을 클릭하여 상세 정보를 확인하세요.</p>
  <div class="card-grid">
    <a href="/station/sangnoksu-station/" class="card">
      <h3>상록수역</h3>
      <p>본오동, 이동 생활권</p>
    </a>
    <a href="/station/hanyang-univ-at-ansan-station/" class="card">
      <h3>한대앞역</h3>
      <p>사동, 이동 인접 생활권</p>
    </a>
    <a href="/station/jungang-station/" class="card">
      <h3>중앙역</h3>
      <p>중앙동, 고잔동 생활권</p>
    </a>
    <a href="/station/gojan-station/" class="card">
      <h3>고잔역</h3>
      <p>고잔동, 호수동 인접권</p>
    </a>
    <a href="/station/choji-station/" class="card">
      <h3>초지역</h3>
      <p>초지동, 단원구청 생활권</p>
    </a>
    <a href="/station/ansan-station/" class="card">
      <h3>안산역</h3>
      <p>원곡동, 백운동 생활권</p>
    </a>
    <a href="/station/seonbu-station/" class="card">
      <h3>선부역</h3>
      <p>선부동, 와동 생활권</p>
    </a>
    <a href="/station/wongok-station/" class="card">
      <h3>원곡역</h3>
      <p>원곡동, 안산역 인접권</p>
    </a>
    <a href="/station/wonsi-station/" class="card">
      <h3>원시역</h3>
      <p>원시, 시화공단 인접권</p>
    </a>
  </div>
</section>

<section id="lifestyle">
  <h2>안산 생활권별 예약 기준</h2>
  <p>지역과 역을 연결한 생활권 기준으로 예약하면 더 정확한 방문 주소와 이동 시간을 확인할 수 있습니다.</p>
  <div class="card-grid">
    <a href="/area/jungang-gojan/" class="card">
      <h3>중앙역·고잔 생활권</h3>
      <p>중앙동 상권과 고잔신도시 출장마사지·홈타이 예약 기준</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/area/choji-dong/" class="card">
      <h3>초지역·초지동 생활권</h3>
      <p>단원구청·고잔신도시 인근 홈타이 방문 가능 지역</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/area/ansan-station-wongok/" class="card">
      <h3>안산역·원곡동 생활권</h3>
      <p>다문화거리·백운동 일대 출장마사지 이동 기준</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/area/sangnoksu-bono/" class="card">
      <h3>상록수·본오 생활권</h3>
      <p>상록수역·본오동·사동 주거권 홈타이 예약 안내</p>
      <span class="card-arrow">→</span>
    </a>
    <a href="/area/seonbu-station/" class="card">
      <h3>선부역·선부동 생활권</h3>
      <p>선부동·와동·달미역 인근 출장마사지 방문 안내</p>
      <span class="card-arrow">→</span>
    </a>
  </div>
</section>

<section id="check">
  <h2>안산 홈타이 예약 전 확인사항</h2>
  <p>예약을 진행하기 전에 다음 항목들을 먼저 확인하면 예약 과정이 훨씬 수월합니다.</p>
  <ul>
    <li><strong>방문 가능 주소 확인</strong> - 자택, 숙소, 오피스텔 등 정확한 방문 주소와 건물 유형 확인</li>
    <li><strong>예약 가능 시간 확인</strong> - 희망 예약 시간이 가능한지 미리 확인</li>
    <li><strong>추가 이동비 여부 확인</strong> - 기본 이동권 외 추가 이동비 발생 여부</li>
    <li><strong>건물 출입 방식 확인</strong> - 공동현관, 자동문, 경비 확인 등</li>
    <li><strong>자택·숙소·오피스텔 이용 기준 확인</strong> - 서비스 제공 장소 기준</li>
    <li><strong>결제 방식 확인</strong> - 현금, 계좌이체, 카드 등 가능한 결제 수단</li>
    <li><strong>예약 변경·취소 기준 확인</strong> - 변경·취소 수수료 및 절차</li>
    <li><strong>개인정보 처리 기준 확인</strong> - 개인정보 수집·이용·보관 방식</li>
    <li><strong>불법·선정적 서비스 불가 안내</strong> - 건전한 관리 서비스만 제공</li>
  </ul>
</section>

<section id="faq">
  <h2>안산 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    <dt id="faq-1">안산 출장마사지는 어떤 서비스인가요?</dt>
    <dd>방문형 마사지 서비스로, 고객의 자택, 숙소, 오피스텔 등으로 전문가가 방문하여 관리하는 서비스입니다. 상록구와 단원구 전지역으로 방문 가능합니다.</dd>

    <dt id="faq-2">상록구와 단원구의 생활권 차이가 뭔가요?</dt>
    <dd>상록구는 상록수역, 한대앞역, 본오동, 사동 중심의 북동부 생활권이고, 단원구는 중앙역, 고잔역, 초지역, 안산역 중심의 남서부·중심권 생활권입니다.</dd>

    <dt id="faq-3">예약 전 꼭 확인해야 할 사항은?</dt>
    <dd>방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식을 먼저 확인하고 예약하는 방식이 좋습니다.</dd>

    <dt id="faq-4">중앙동과 고잔동은 어떻게 다른가요?</dt>
    <dd>중앙동은 중앙역 중심 상권과 행정 중심지를 중심으로, 고잔동은 호수공원·고잔신도시 주거지를 중심으로 운영됩니다.</dd>

    <dt id="faq-5">추가 이동비는 어떻게 계산되나요?</dt>
    <dd>지역별로 기본 이동권이 정해져 있으며, 그 외 먼 거리는 추가 이동비가 발생할 수 있습니다. 예약 시 정확히 확인하세요.</dd>
  </dl>
</section>
"""
}
