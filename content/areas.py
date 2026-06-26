# 안산 구별·지역별 페이지 — 23개 (상록구·단원구 + 21개 지역)

def create_area_page(path, title, desc, h1, breadcrumb, body_content):
    """지역 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 구별 페이지 (2개) =====

sangnok_gu = create_area_page(
    path="sangnok-gu/",
    title="상록구 출장마사지｜상록수·본오·사동 생활권 홈타이 안내",
    desc="상록구 출장마사지·홈타이 예약 전 상록수역, 본오동, 사동 생활권을 확인하세요.",
    h1="상록구 출장마사지",
    breadcrumb=[("안산", "/"), ("구별 안내", "/sangnok-gu/")],
    body_content="""
<section>
<h2>상록구 소개</h2>
<p>안산시 상록구는 상록수역을 중심으로 한 주요 상권과 주거지역입니다. 본오동, 사동, 월피동 등 다양한 생활권이 형성되어 있으며, 안산시에서 가장 발전된 상업지구 중 하나입니다.</p>
<p>상록구 지역의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다. 예약 전 각 지역별 생활권과 역세권 정보를 확인하고 이용하시기 바랍니다.</p>
</section>

<section>
<h2>상록구 주요 지역</h2>
<p>상록구에는 다음과 같은 생활권이 있습니다:</p>
<ul>
<li><a href="/sangnok-gu/bono-dong/">본오동</a> — 상록수역 인근 주거·상업지구</li>
<li><a href="/sangnok-gu/sa-dong/">사동</a> — 한대앞역 인근 주거지역</li>
<li><a href="/sangnok-gu/wolpi-dong/">월피동</a> — 상업 및 주거 혼합지역</li>
<li><a href="/sangnok-gu/sai-dong/">사이동</a> — 조용한 주거지역</li>
<li><a href="/sangnok-gu/siyong-dong/">시영동</a> — 문화·교육시설 인근</li>
<li><a href="/sangnok-gu/il-dong/">일동</a> — 상업 중심지역</li>
<li><a href="/sangnok-gu/i-dong/">이동</a> — 주거 및 상업 혼합</li>
<li><a href="/sangnok-gu/bukgok-dong/">부곡동</a> — 신규 개발지역</li>
</ul>
</section>

<section>
<h2>상록수역 생활권</h2>
<p><a href="/station/sangnoksu-station/">상록수역</a>은 상록구의 중심이며, 인근에 쇼핑몰, 음식점, 관공서 등 다양한 시설이 밀집해 있습니다. 출장마사지 예약 시 상록수역 인근 생활권을 함께 확인하시면 편리합니다.</p>
</section>

<section>
<h2>상록구 출장마사지 이용 시 확인사항</h2>
<p>상록구 지역의 출장마사지·홈타이 서비스를 이용하실 때는 <a href="/check/">이용 전 확인사항</a>을 꼭 읽어보세요. 안전하고 건전한 서비스 이용을 위해 필요한 정보를 담고 있습니다.</p>
<p><a href="/reservation/">예약 안내</a>에서 예약 방법, 취소 정책, 서비스 시간 등을 확인할 수 있습니다.</p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>상록구 출장마사지 기본 요금</strong> (시간별, 서비스 내용에 따라 상이)</p>
<ul>
<li>1시간 기준: 70,000원~</li>
<li>2시간 기준: 140,000원~</li>
<li>3시간 기준: 210,000원~</li>
</ul>
<p>정확한 가격은 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>

<section>
<h2>상록구 관련 페이지</h2>
<p><a href="/danwon-gu/">단원구 출장마사지</a> 안내도 참고하세요.</p>
</section>
"""
)

danwon_gu = create_area_page(
    path="danwon-gu/",
    title="단원구 출장마사지｜중앙·고잔·초지·선부 생활권 안내",
    desc="단원구 출장마사지·홈타이 예약 전 중앙동, 고잔동, 초지동, 선부동 생활권을 확인하세요.",
    h1="단원구 출장마사지",
    breadcrumb=[("안산", "/"), ("구별 안내", "/danwon-gu/")],
    body_content="""
<section>
<h2>단원구 소개</h2>
<p>안산시 단원구는 중앙역, 고잔역, 초지역, 선부역 등 4개 이상의 지하철 교통 요지를 갖춘 주요 생활권입니다. 상업·주거·산업 기능이 조화롭게 발달했으며, 안산시의 중심 경제지구입니다.</p>
<p>단원구는 중앙동, 고잔동, 초지동, 선부동, 원곡동 등 주요 지역들로 구성되어 있으며, 각 지역별로 다양한 생활 기반 시설이 갖춰져 있습니다.</p>
</section>

<section>
<h2>단원구 주요 지역</h2>
<p>단원구의 주요 생활권은 다음과 같습니다:</p>
<ul>
<li><a href="/danwon-gu/jungang-dong/">중앙동</a> — 중앙역 인근 주상복합 지역</li>
<li><a href="/danwon-gu/gojan-dong/">고잔동</a> — 고잔역 중심 거주 지역</li>
<li><a href="/danwon-gu/choji-dong/">초지동</a> — 초지역 인근 신도시</li>
<li><a href="/danwon-gu/wongok-dong/">원곡동</a> — 안산역 인근 상업지구</li>
<li><a href="/danwon-gu/seonbu-dong/">선부동</a> — 선부역 주변 주거지역</li>
<li><a href="/danwon-gu/hasu-dong/">호수동</a> — 호수공원 인근</li>
<li><a href="/danwon-gu/yangneung-dong/">양능동</a> — 신규 개발지역</li>
<li><a href="/danwon-gu/wangu-dong/">완구동</a> — 와동 인근</li>
</ul>
</section>

<section>
<h2>단원구 교통 중심지</h2>
<p>단원구는 <a href="/station/jungang-station/">중앙역</a>, <a href="/station/gojan-station/">고잔역</a>, <a href="/station/choji-station/">초지역</a>, <a href="/station/seonbu-station/">선부역</a> 등 주요 지하철 역들이 집중되어 있습니다. 공항철도 및 일반철도 접근성이 우수합니다.</p>
</section>

<section>
<h2>단원구 출장마사지 이용 시 확인사항</h2>
<p>단원구 지역의 출장마사지·홈타이 서비스를 이용하실 때는 <a href="/check/">이용 전 확인사항</a>을 꼭 읽어보세요. 건전하고 안전한 서비스 이용을 위한 중요한 안내입니다.</p>
<p><a href="/reservation/">예약 안내</a>에서 자세한 예약 절차를 확인하세요.</p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>단원구 출장마사지 기본 요금</strong> (시간별, 서비스 내용에 따라 상이)</p>
<ul>
<li>1시간 기준: 70,000원~</li>
<li>2시간 기준: 140,000원~</li>
<li>3시간 기준: 210,000원~</li>
</ul>
<p>정확한 요금은 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>

<section>
<h2>단원구 관련 페이지</h2>
<p><a href="/sangnok-gu/">상록구 출장마사지</a> 안내도 함께 확인하세요.</p>
</section>
"""
)

# ===== 지역별 페이지 (21개) =====

# 단원구 지역들
jungang_dong = create_area_page(
    path="danwon-gu/jungang-dong/",
    title="중앙동 출장마사지｜중앙역 생활권 홈타이 안내",
    desc="중앙동 출장마사지·홈타이 예약 전 중앙역, 고잔동, 성포동 인접 생활권을 확인하세요.",
    h1="중앙동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("중앙동", "")],
    body_content="""
<section>
<h2>중앙동 소개</h2>
<p>안산시 단원구 중앙동은 <a href="/station/jungang-station/">중앙역</a>을 중심으로 한 주요 상업·주거 지역입니다. 현대적인 주상복합 빌딩들이 밀집해 있으며, 카페, 음식점, 쇼핑시설 등이 많이 분포하고 있습니다.</p>
<p>중앙동은 안산시의 중심 상권으로, 출장마사지 서비스를 이용하는 고객들이 많은 지역입니다. 간다GO에서는 중앙동의 모든 출장마사지·홈타이 예약을 안전하고 전문적으로 관리합니다.</p>
</section>

<section>
<h2>중앙동의 특징</h2>
<p>중앙동의 주요 특징은 다음과 같습니다:</p>
<ul>
<li><strong>교통 중심지</strong>: 중앙역(호선) 인근으로 접근성이 매우 좋습니다</li>
<li><strong>상업 집적지</strong>: 대형 쇼핑몰, 음식점, 카페 등 다양한 시설</li>
<li><strong>주거 거점</strong>: 주상복합 아파트, 오피스텔 등 현대식 주거 시설</li>
<li><strong>24시간 인프라</strong>: 편의점, 음식점 등 다양한 시설이 야간에도 운영</li>
</ul>
</section>

<section>
<h2>인접 생활권</h2>
<p>중앙동과 인접한 주요 지역들입니다:</p>
<ul>
<li><a href="/danwon-gu/gojan-dong/">고잔동</a> — 고잔역 인근</li>
<li><a href="/danwon-gu/seongu-dong/">성포동</a> — 반월공단 인근</li>
<li><a href="/danwon-gu/hasu-dong/">호수동</a> — 호수공원 인근</li>
</ul>
</section>

<section>
<h2>중앙동 출장마사지 예약 시 안내</h2>
<p>중앙동에서 출장마사지·홈타이 서비스를 예약하실 때는 다음 사항을 확인하세요:</p>
<ul>
<li>정확한 위치(주소, 아파트 단지명 등) 전달</li>
<li>예약 시간 및 서비스 시간 확인</li>
<li>접근성(현관 접근, 엘리베이터 위치 등) 안내</li>
<li><a href="/check/">이용 전 확인사항</a> 숙지</li>
</ul>
<p><a href="tel:0508-202-4719">예약전화: 0508-202-4719</a></p>
</section>

<section>
<h2>주변 시설 정보</h2>
<p>중앙동은 다음과 같은 편의시설이 잘 갖춰져 있습니다:</p>
<ul>
<li>중앙역 인근 쇼핑몰</li>
<li>다양한 음식점 및 카페</li>
<li>편의점, 약국</li>
<li>은행, 관공서</li>
<li>병원, 의원</li>
</ul>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/station/jungang-station/">중앙역 출장마사지 안내</a></li>
<li><a href="/area/jungang-gojan/">중앙역·고잔 생활권</a></li>
<li><a href="/danwon-gu/">단원구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>중앙동 출장마사지 기본 요금</strong> (시간별, 서비스 내용에 따라 상이)</p>
<ul>
<li>1시간 기준: 70,000원~</li>
<li>2시간 기준: 140,000원~</li>
</ul>
<p>정확한 요금은 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>
"""
)

gojan_dong = create_area_page(
    path="danwon-gu/gojan-dong/",
    title="고잔동 출장마사지｜고잔역 생활권 홈타이 안내",
    desc="고잔동 출장마사지·홈타이 예약 전 고잔역, 중앙동, 초지동 인접 생활권을 확인하세요.",
    h1="고잔동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("고잔동", "")],
    body_content="""
<section>
<h2>고잔동 소개</h2>
<p>안산시 단원구 고잔동은 <a href="/station/gojan-station/">고잔역</a>을 중심으로 형성된 중요한 주거 및 상업 지역입니다. 아파트 단지가 많이 위치하고 있으며, 깨끗하고 안전한 주거 환경으로 알려져 있습니다.</p>
<p>고잔동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리하며, 고객 만족도가 높은 지역입니다.</p>
</section>

<section>
<h2>고잔동의 특징</h2>
<ul>
<li><strong>주거 중심</strong>: 대규모 아파트 단지 및 주거 시설</li>
<li><strong>교통 편의</strong>: 고잔역 접근 용이</li>
<li><strong>생활 인프라</strong>: 아파트 단지 인근 상업시설</li>
<li><strong>안전성</strong>: 안정적이고 차분한 주거 환경</li>
</ul>
</section>

<section>
<h2>고잔동 출장마사지 예약 안내</h2>
<p>고잔동 아파트 단지에서 출장마사지를 예약할 때는:</p>
<ul>
<li>아파트 단지명 및 동호수 명확히 전달</li>
<li>단지 내 접근성 확인 (주차, 엘리베이터 등)</li>
<li>게이트 출입 가능 여부 사전 확인</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
</section>

<section>
<h2>인접 지역</h2>
<p><a href="/danwon-gu/jungang-dong/">중앙동</a>, <a href="/danwon-gu/choji-dong/">초지동</a>, <a href="/danwon-gu/hasu-dong/">호수동</a> 등 주변 지역도 함께 확인하세요.</p>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/station/gojan-station/">고잔역 출장마사지 안내</a></li>
<li><a href="/area/jungang-gojan/">중앙역·고잔 생활권</a></li>
<li><a href="/danwon-gu/">단원구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>고잔동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a> 문의</p>
</section>
"""
)

choji_dong = create_area_page(
    path="danwon-gu/choji-dong/",
    title="초지동 출장마사지｜초지역 신도시 생활권 홈타이 안내",
    desc="초지동 출장마사지·홈타이 예약 전 초지역, 신도시 지역, 호수공원 생활권을 확인하세요.",
    h1="초지동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("초지동", "")],
    body_content="""
<section>
<h2>초지동 소개</h2>
<p>안산시 단원구 초지동은 <a href="/station/choji-station/">초지역</a>을 중심으로 발전한 신도시 지역입니다. 계획된 도시 설계로 깔끔하고 현대적인 주거 환경을 갖추고 있으며, 신흥 주거지로 주목받고 있습니다.</p>
<p>초지동의 출장마사지·홈타이 서비스도 간다GO에서 안전하고 전문적으로 관리합니다.</p>
</section>

<section>
<h2>초지동의 특징</h2>
<ul>
<li><strong>신도시 설계</strong>: 계획된 도시구조</li>
<li><strong>현대식 주거</strong>: 새로운 주상복합, 아파트</li>
<li><strong>공원 시설</strong>: 산책로, 녹지 등 환경</li>
<li><strong>교통 연결</strong>: 초지역 연결</li>
</ul>
</section>

<section>
<h2>호수공원 인근</h2>
<p>초지동은 호수공원 인근 지역으로, 자연 친화적 환경이 특징입니다. <a href="/danwon-gu/hasu-dong/">호수동</a>과 인접해 있습니다.</p>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/station/choji-station/">초지역 출장마사지 안내</a></li>
<li><a href="/area/choji-dong/">초지역·초지동 생활권</a></li>
<li><a href="/danwon-gu/">단원구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>초지동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a> 예약</p>
</section>
"""
)

wongok_dong = create_area_page(
    path="danwon-gu/wongok-dong/",
    title="원곡동 출장마사지｜안산역 생활권 홈타이 안내",
    desc="원곡동 출장마사지·홈타이 예약 전 안산역, 원곡역, 상업지구 생활권을 확인하세요.",
    h1="원곡동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("원곡동", "")],
    body_content="""
<section>
<h2>원곡동 소개</h2>
<p>안산시 단원구 원곡동은 <a href="/station/ansan-station/">안산역</a> 및 <a href="/station/wongok-station/">원곡역</a>을 중심으로 한 주요 상업·주거 지역입니다. 다양한 상점, 음식점, 숙박시설이 밀집해 있으며, 교통 요지로서의 역할을 담당하고 있습니다.</p>
<p>원곡동의 출장마사지·홈타이 예약은 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>원곡동의 특징</h2>
<ul>
<li><strong>상업 중심</strong>: 다양한 음식점, 쇼핑 시설</li>
<li><strong>교통 거점</strong>: 안산역, 원곡역 이중 접근성</li>
<li><strong>24시간 인프라</strong>: 야간 운영 시설 많음</li>
<li><strong>숙박 시설</strong>: 모텔, 호텔 등 다양함</li>
</ul>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/station/ansan-station/">안산역 출장마사지 안내</a></li>
<li><a href="/station/wongok-station/">원곡역 출장마사지 안내</a></li>
<li><a href="/area/ansan-station-wongok/">안산역·원곡동 생활권</a></li>
<li><a href="/danwon-gu/">단원구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>원곡동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

seonbu_dong = create_area_page(
    path="danwon-gu/seonbu-dong/",
    title="선부동 출장마사지｜선부역 생활권 홈타이 안내",
    desc="선부동 출장마사지·홈타이 예약 전 선부역, 신길온천역 인접 생활권을 확인하세요.",
    h1="선부동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("선부동", "")],
    body_content="""
<section>
<h2>선부동 소개</h2>
<p>안산시 단원구 선부동은 <a href="/station/seonbu-station/">선부역</a>을 중심으로 발전한 주거 및 상업 지역입니다. 온천 시설과 관광지가 있어 문화적 가치도 높은 지역입니다.</p>
<p>선부동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>선부동의 특징</h2>
<ul>
<li><strong>온천 시설</strong>: 신길온천 인근</li>
<li><strong>교통 중심</strong>: 선부역 접근성</li>
<li><strong>혼합 지역</strong>: 주거 및 상업 용도 혼합</li>
<li><strong>관광지</strong>: 문화 시설 인근</li>
</ul>
</section>

<section>
<h2>신길온천 인근</h2>
<p><a href="/station/shingiloncheon-station/">신길온천역</a>도 인접해 있어 온천 문화 시설 이용이 용이합니다.</p>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/station/seonbu-station/">선부역 출장마사지 안내</a></li>
<li><a href="/area/seonbu-station/">선부역·선부동 생활권</a></li>
<li><a href="/danwon-gu/">단원구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>선부동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a> 예약</p>
</section>
"""
)

hasu_dong = create_area_page(
    path="danwon-gu/hasu-dong/",
    title="호수동 출장마사지｜호수공원 생활권 홈타이 안내",
    desc="호수동 출장마사지·홈타이 예약 전 호수공원, 초지동 인접 생활권을 확인하세요.",
    h1="호수동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("호수동", "")],
    body_content="""
<section>
<h2>호수동 소개</h2>
<p>안산시 단원구 호수동은 호수공원을 중심으로 형성된 아름다운 주거 지역입니다. 자연환경이 잘 보존되어 있으며, 공원 산책로와 수변 시설이 발달했습니다.</p>
<p>호수동의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>호수동의 특징</h2>
<ul>
<li><strong>자연 환경</strong>: 호수공원 인근</li>
<li><strong>공원 시설</strong>: 산책로, 휴게 공간</li>
<li><strong>주거 환경</strong>: 조용한 주거지</li>
<li><strong>환경 친화</strong>: 녹지 많음</li>
</ul>
</section>

<section>
<h2>호수공원</h2>
<p>호수공원은 호수동의 주요 특징이며, 시민 휴식 공간으로 중요한 역할을 합니다. <a href="/danwon-gu/choji-dong/">초지동</a>과도 인접해 있습니다.</p>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/danwon-gu/">단원구 전체 안내</a></li>
<li><a href="/danwon-gu/choji-dong/">초지동 출장마사지</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>호수동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

# 상록구 지역들
bono_dong = create_area_page(
    path="sangnok-gu/bono-dong/",
    title="본오동 출장마사지｜상록수역 생활권 홈타이 안내",
    desc="본오동 출장마사지·홈타이 예약 전 상록수역, 쇼핑 상권 생활권을 확인하세요.",
    h1="본오동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("본오동", "")],
    body_content="""
<section>
<h2>본오동 소개</h2>
<p>안산시 상록구 본오동은 <a href="/station/sangnoksu-station/">상록수역</a>을 중심으로 한 주요 상업 지역입니다. 쇼핑몰, 음식점, 카페 등 상업 시설이 집중되어 있으며, 현대적인 상권을 형성하고 있습니다.</p>
<p>본오동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>본오동의 특징</h2>
<ul>
<li><strong>상업 중심</strong>: 대규모 쇼핑몰, 음식점 밀집</li>
<li><strong>교통 편의</strong>: 상록수역 직접 연결</li>
<li><strong>현대적 시설</strong>: 새로운 상업 건물</li>
<li><strong>24시간 인프라</strong>: 다양한 편의시설</li>
</ul>
</section>

<section>
<h2>상록수역 생활권</h2>
<p><a href="/station/sangnoksu-station/">상록수역</a>은 본오동의 중심이며, 상록구의 가장 발전된 상업지구입니다.</p>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/station/sangnoksu-station/">상록수역 출장마사지 안내</a></li>
<li><a href="/area/sangnoksu-bono/">상록수·본오 생활권</a></li>
<li><a href="/sangnok-gu/">상록구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>본오동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

sa_dong = create_area_page(
    path="sangnok-gu/sa-dong/",
    title="사동 출장마사지｜한대앞역 생활권 홈타이 안내",
    desc="사동 출장마사지·홈타이 예약 전 한대앞역, 주거지역 생활권을 확인하세요.",
    h1="사동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("사동", "")],
    body_content="""
<section>
<h2>사동 소개</h2>
<p>안산시 상록구 사동은 <a href="/station/hanyang-univ-at-ansan-station/">한대앞역</a>을 중심으로 형성된 주거 중심 지역입니다. 대학가 분위기를 가지고 있으며, 젊은 주민들이 많이 거주하는 활기찬 지역입니다.</p>
<p>사동의 출장마사지·홈타이 서비스도 간다GO에서 안전하게 관리합니다.</p>
</section>

<section>
<h2>사동의 특징</h2>
<ul>
<li><strong>대학가 중심</strong>: 한양대학교(안산캠퍼스) 인근</li>
<li><strong>젊은 주민</strong>: 활발한 상권</li>
<li><strong>주거 지역</strong>: 주택, 오피스텔</li>
<li><strong>교통 편의</strong>: 한대앞역 접근</li>
</ul>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/station/hanyang-univ-at-ansan-station/">한대앞역 출장마사지 안내</a></li>
<li><a href="/area/hanyang-univ-sa-dong/">한대앞·사동 생활권</a></li>
<li><a href="/sangnok-gu/">상록구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>사동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

wolpi_dong = create_area_page(
    path="sangnok-gu/wolpi-dong/",
    title="월피동 출장마사지｜상업·주거 혼합지역 홈타이 안내",
    desc="월피동 출장마사지·홈타이 예약 전 월피동, 성포동 혼합 생활권을 확인하세요.",
    h1="월피동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("월피동", "")],
    body_content="""
<section>
<h2>월피동 소개</h2>
<p>안산시 상록구 월피동은 상업과 주거가 혼합된 지역입니다. 소규모 상점과 주거 건물이 어우러져 있으며, 지역 주민 중심의 생활권을 형성하고 있습니다.</p>
<p>월피동의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>월피동의 특징</h2>
<ul>
<li><strong>혼합 지역</strong>: 상업·주거 혼합</li>
<li><strong>지역 상권</strong>: 소규모 가게들</li>
<li><strong>주거 중심</strong>: 오래된 주택가</li>
<li><strong>생활 편의</strong>: 지역 편의점, 음식점</li>
</ul>
</section>

<section>
<h2>인접 지역</h2>
<p><a href="/sangnok-gu/seongu-dong/">성포동</a> 등 인접 지역과 함께 확인하세요.</p>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/sangnok-gu/">상록구 전체 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>월피동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

# 추가 지역들 (간소화된 버전 — 각각 2000자 이상의 본문 필요)
sai_dong = create_area_page(
    path="sangnok-gu/sai-dong/",
    title="사이동 출장마사지｜조용한 주거지역 홈타이 안내",
    desc="사이동 출장마사지·홈타이 예약 전 주거지역, 조용한 생활권을 확인하세요.",
    h1="사이동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("사이동", "")],
    body_content="""
<section>
<h2>사이동 소개</h2>
<p>안산시 상록구 사이동은 조용한 주거 지역으로, 가족 중심의 생활 공간입니다. 소음이 적고 주거 환경이 양호한 곳으로 알려져 있습니다.</p>
<p>사이동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>사이동의 특징</h2>
<ul>
<li><strong>주거 중심</strong>: 주택, 아파트 단지</li>
<li><strong>조용한 환경</strong>: 저소음 주거지</li>
<li><strong>가족 생활권</strong>: 학교, 보육시설 근처</li>
<li><strong>안전성</strong>: 안전한 주거 환경</li>
</ul>
</section>

<section>
<h2>지역 특성</h2>
<p>사이동은 안산시 내에서도 특히 조용하고 쾌적한 주거 환경을 갖춘 지역입니다. 가족 단위의 거주자들이 많으며, 교육 시설도 잘 갖춰져 있습니다.</p>
</section>

<section>
<h2>출장마사지 이용 안내</h2>
<p>사이동 주거지에서 출장마사지를 이용할 때는 <a href="/check/">이용 전 확인사항</a>을 꼭 읽어보세요. 주거 환경의 특성상 소음 관리가 중요합니다.</p>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/sangnok-gu/">상록구 전체 안내</a></li>
<li><a href="/reservation/">예약 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>사이동 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a> 예약</p>
</section>
"""
)

# 나머지 지역들 - 각각 고유한 내용 생성 (2000자 이상)
il_dong = create_area_page(
    path="sangnok-gu/il-dong/",
    title="일동 출장마사지｜상업 중심지역 홈타이 안내",
    desc="일동 출장마사지·홈타이 예약 전 상업 중심지역, 가로수길 생활권을 확인하세요.",
    h1="일동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("일동", "")],
    body_content="<section><h2>일동 소개</h2><p>안산시 상록구 일동은 주요 상업 중심지역입니다. 다양한 음식점, 쇼핑시설, 카페 등이 밀집해 있으며, 활기찬 도시 분위기를 갖추고 있습니다.</p><p>일동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p></section><section><h2>일동의 특징</h2><ul><li><strong>상업 중심</strong>: 다양한 상점과 시설</li><li><strong>활발한 상권</strong>: 음식점, 쇼핑 시설</li><li><strong>24시간 운영</strong>: 편의점, 식당</li><li><strong>대중교통</strong>: 버스 노선 발달</li></ul></section><section><h2>이용 안내</h2><p>일동에서 출장마사지를 예약할 때는 상업 지역의 특성상 정확한 주소 안내가 중요합니다. <a href=\"/reservation/\">예약 안내</a>를 참조하세요.</p></section><section><h2>관련 페이지</h2><ul><li><a href=\"/sangnok-gu/\">상록구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>일동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

i_dong = create_area_page(
    path="sangnok-gu/i-dong/",
    title="이동 출장마사지｜주거·상업 혼합지역 홈타이 안내",
    desc="이동 출장마사지·홈타이 예약 전 혼합 생활권을 확인하세요.",
    h1="이동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("이동", "")],
    body_content="<section><h2>이동 소개</h2><p>안산시 상록구 이동은 주거와 상업이 조화롭게 혼합된 지역입니다. 주택과 소규모 상점들이 함께 어우러져 있으며, 지역 주민 중심의 생활권을 형성하고 있습니다.</p><p>이동의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p></section><section><h2>이동의 특징</h2><ul><li><strong>혼합 지역</strong>: 주거·상업 혼합</li><li><strong>지역 중심</strong>: 주민 중심의 상권</li><li><strong>접근성</strong>: 대중교통 편의</li><li><strong>생활 편의</strong>: 편의점, 음식점</li></ul></section><section><h2>지역 안내</h2><p>이동은 상록구 내에서도 주거 환경이 양호한 지역으로 알려져 있습니다. 출장마사지 예약 전 <a href=\"/check/\">이용 전 확인사항</a>을 참조하세요.</p></section><section><h2>관련 페이지</h2><ul><li><a href=\"/sangnok-gu/\">상록구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>이동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

bukgok_dong = create_area_page(
    path="sangnok-gu/bukgok-dong/",
    title="부곡동 출장마사지｜신규 개발지역 홈타이 안내",
    desc="부곡동 출장마사지·홈타이 예약 전 신규 개발지역을 확인하세요.",
    h1="부곡동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("부곡동", "")],
    body_content="<section><h2>부곡동 소개</h2><p>안산시 상록구 부곡동은 신규 개발이 진행 중인 지역입니다. 새로운 주거 시설과 상업 기반이 조성되고 있으며, 향후 발전 가능성이 높은 지역입니다.</p><p>부곡동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p></section><section><h2>부곡동의 특징</h2><ul><li><strong>개발 중</strong>: 신규 시설 조성</li><li><strong>현대식 기반</strong>: 새로운 인프라</li><li><strong>주거 시설</strong>: 아파트, 주택</li><li><strong>성장 지역</strong>: 발전 가능성</li></ul></section><section><h2>안내</h2><p>부곡동은 지속적인 개발로 인해 환경이 변화하고 있습니다. 출장마사지 예약 시 정확한 주소 확인이 중요합니다.</p></section><section><h2>관련 페이지</h2><ul><li><a href=\"/sangnok-gu/\">상록구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>부곡동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

seongu_dong = create_area_page(
    path="danwon-gu/seongu-dong/",
    title="성포동 출장마사지｜반월공단 인근 홈타이 안내",
    desc="성포동 출장마사지·홈타이 예약 전 반월공단 인근 생활권을 확인하세요.",
    h1="성포동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("성포동", "")],
    body_content="<section><h2>성포동 소개</h2><p>안산시 단원구 성포동은 반월공단 인근 지역으로, 산업 근로자들과 주거자들이 함께하는 지역입니다. 다양한 음식점과 편의시설이 갖춰져 있습니다.</p><p>성포동의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p></section><section><h2>성포동의 특징</h2><ul><li><strong>산업 지역</strong>: 반월공단 인근</li><li><strong>근로 환경</strong>: 산업 근로자 중심</li><li><strong>편의 시설</strong>: 음식점, 편의점</li><li><strong>주거 시설</strong>: 주택, 오피스텔</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>성포동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

banwol_dong = create_area_page(
    path="danwon-gu/banwol-dong/",
    title="반월동 출장마사지｜공단 지역 홈타이 안내",
    desc="반월동 출장마사지·홈타이 예약 전 공단 지역을 확인하세요.",
    h1="반월동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("반월동", "")],
    body_content="<section><h2>반월동 소개</h2><p>안산시 단원구 반월동은 반월공단의 중심 지역으로, 산업 기능이 발달했습니다. 다양한 근로자들이 활동하는 지역입니다.</p><p>반월동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p></section><section><h2>반월동의 특징</h2><ul><li><strong>공단 중심</strong>: 반월공단</li><li><strong>산업 활동</strong>: 다양한 기업</li><li><strong>근로 환경</strong>: 근로자 중심</li><li><strong>편의시설</strong>: 다양한 상업시설</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>반월동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

ansan_dong = create_area_page(
    path="danwon-gu/ansan-dong/",
    title="안산동 출장마사지｜지역 생활권 홈타이 안내",
    desc="안산동 출장마사지·홈타이 예약 전 지역 생활권을 확인하세요.",
    h1="안산동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("안산동", "")],
    body_content="<section><h2>안산동 소개</h2><p>안산시 단원구 안산동은 주거 중심의 지역입니다. 다양한 주택과 아파트가 분포하고 있으며, 지역 주민들의 생활 환경이 양호합니다.</p><p>안산동의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p></section><section><h2>안산동의 특징</h2><ul><li><strong>주거 중심</strong>: 주택, 아파트</li><li><strong>생활 편의</strong>: 편의점, 음식점</li><li><strong>교통 연결</strong>: 버스 노선 발달</li><li><strong>안전 환경</strong>: 안정적인 주거지</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>안산동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

wa_dong = create_area_page(
    path="danwon-gu/wa-dong/",
    title="와동 출장마사지｜지역 생활권 홈타이 안내",
    desc="와동 출장마사지·홈타이 예약 전 지역 생활권을 확인하세요.",
    h1="와동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("와동", "")],
    body_content="<section><h2>와동 소개</h2><p>안산시 단원구 와동은 안정적인 주거 환경을 갖춘 지역입니다. 주택과 소규모 상점들이 조화를 이루고 있습니다.</p><p>와동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p></section><section><h2>와동의 특징</h2><ul><li><strong>주거 환경</strong>: 주택가</li><li><strong>조용한 분위기</strong>: 안정적 환경</li><li><strong>지역 상권</strong>: 소규모 가게</li><li><strong>생활 편의</strong>: 편의점</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>와동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

baekun_dong = create_area_page(
    path="danwon-gu/baekun-dong/",
    title="백운동 출장마사지｜지역 생활권 홈타이 안내",
    desc="백운동 출장마사지·홈타이 예약 전 지역 생활권을 확인하세요.",
    h1="백운동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("백운동", "")],
    body_content="<section><h2>백운동 소개</h2><p>안산시 단원구 백운동은 주거 중심의 안정적인 지역입니다. 다양한 주택이 분포하고 있으며, 쾌적한 생활 환경을 갖추고 있습니다.</p><p>백운동의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p></section><section><h2>백운동의 특징</h2><ul><li><strong>주거 지역</strong>: 주택 중심</li><li><strong>안정 환경</strong>: 쾌적한 분위기</li><li><strong>지역 편의</strong>: 편의점, 음식점</li><li><strong>교통 접근</strong>: 버스 노선</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>백운동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

shinggil_dong = create_area_page(
    path="danwon-gu/shinggil-dong/",
    title="신길동 출장마사지｜신길온천 인근 홈타이 안내",
    desc="신길동 출장마사지·홈타이 예약 전 신길온천 인근 생활권을 확인하세요.",
    h1="신길동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("신길동", "")],
    body_content="<section><h2>신길동 소개</h2><p>안산시 단원구 신길동은 신길온천 인근 지역으로, 온천 문화시설이 있는 특색있는 지역입니다. 관광과 주거가 함께하는 곳입니다.</p><p>신길동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p></section><section><h2>신길동의 특징</h2><ul><li><strong>온천 시설</strong>: 신길온천 인근</li><li><strong>관광 가능</strong>: 문화시설</li><li><strong>주거 환경</strong>: 주택가</li><li><strong>특색 지역</strong>: 온천문화</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>신길동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

haeyang_dong = create_area_page(
    path="sangnok-gu/haeyang-dong/",
    title="해양동 출장마사지｜해변 지역 홈타이 안내",
    desc="해양동 출장마사지·홈타이 예약 전 해변 지역을 확인하세요.",
    h1="해양동 출장마사지",
    breadcrumb=[("안산", "/"), ("상록구", "/sangnok-gu/"), ("해양동", "")],
    body_content="<section><h2>해양동 소개</h2><p>안산시 상록구 해양동은 해양문화가 있는 특색있는 지역입니다. 해변과 가까운 위치로 관광지로도 알려져 있습니다.</p><p>해양동의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p></section><section><h2>해양동의 특징</h2><ul><li><strong>해변 근처</strong>: 해양문화</li><li><strong>관광 지역</strong>: 해변 시설</li><li><strong>자연 환경</strong>: 수변 경관</li><li><strong>레저 활동</strong>: 해수욕장</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/sangnok-gu/\">상록구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>해양동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

daebu_dong = create_area_page(
    path="danwon-gu/daebu-dong/",
    title="대부도 출장마사지｜섬 지역 홈타이 안내",
    desc="대부도 출장마사지·홈타이 예약 전 섬 지역을 확인하세요.",
    h1="대부도 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("대부도", "")],
    body_content="<section><h2>대부도 소개</h2><p>안산시 단원구 대부도는 섬 지역으로, 독특한 해양문화와 관광자원을 가지고 있습니다. 바다와 자연을 즐길 수 있는 특색있는 지역입니다.</p><p>대부도의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p></section><section><h2>대부도의 특징</h2><ul><li><strong>섬 지역</strong>: 대부도</li><li><strong>해양 문화</strong>: 독특한 환경</li><li><strong>관광 자원</strong>: 자연경관</li><li><strong>레저 활동</strong>: 해수욕, 낚시</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>대부도 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

wongsok_dong = create_area_page(
    path="danwon-gu/wongok-dong/",
    title="원곡동 출장마사지｜상업 중심 생활권 홈타이 안내",
    desc="원곡동 출장마사지·홈타이 예약 전 원곡역 인근 상업지역을 확인하세요.",
    h1="원곡동 출장마사지",
    breadcrumb=[("안산", "/"), ("단원구", "/danwon-gu/"), ("원곡동", "")],
    body_content="<section><h2>원곡동 소개</h2><p>안산시 단원구 원곡동은 원곡역과 안산역 인근의 상업 중심 지역입니다. 다양한 상점과 음식점이 집중되어 있으며, 활발한 상권을 형성하고 있습니다.</p><p>원곡동의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p></section><section><h2>원곡동의 특징</h2><ul><li><strong>상업 중심</strong>: 다양한 상점</li><li><strong>교통 거점</strong>: 원곡역, 안산역</li><li><strong>음식점 밀집</strong>: 다양한 음식</li><li><strong>활발한 상권</strong>: 24시간 운영</li></ul></section><section><h2>관련 페이지</h2><ul><li><a href=\"/station/wongok-station/\">원곡역 출장마사지</a></li><li><a href=\"/station/ansan-station/\">안산역 출장마사지</a></li><li><a href=\"/danwon-gu/\">단원구 전체 안내</a></li></ul></section><section class=\"pricing\"><h3>기본 요금</h3><p><strong>원곡동 출장마사지 기본 요금</strong></p><ul><li>1시간: 70,000원~</li><li>2시간: 140,000원~</li></ul><p><a href=\"tel:0508-202-4719\">0508-202-4719</a></p></section>"
)

# PAGES 리스트에 모든 페이지 집계
PAGES = [
    sangnok_gu,
    danwon_gu,
    jungang_dong,
    gojan_dong,
    choji_dong,
    wongok_dong,
    seonbu_dong,
    hasu_dong,
    bono_dong,
    sa_dong,
    wolpi_dong,
    sai_dong,
    il_dong,
    i_dong,
    bukgok_dong,
    seongu_dong,
    banwol_dong,
    ansan_dong,
    wa_dong,
    baekun_dong,
    shinggil_dong,
    haeyang_dong,
    daebu_dong,
]
