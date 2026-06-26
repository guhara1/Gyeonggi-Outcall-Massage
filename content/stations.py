# 안산 역세권 페이지 — 13개 지하철역

def create_station_page(path, title, desc, h1, breadcrumb, body_content):
    """역세권 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 13개 역세권 페이지 =====

sangnoksu_station = create_station_page(
    path="station/sangnoksu-station/",
    title="상록수역 출장마사지｜상록구 중심 홈타이 안내",
    desc="상록수역 출장마사지·홈타이 예약 전 본오동, 상업지구 생활권을 확인하세요.",
    h1="상록수역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("상록수역", "")],
    body_content="""
<section>
<h2>상록수역 소개</h2>
<p><strong>상록수역</strong>은 안산시 상록구의 중심 교통 허브로, 대규모 쇼핑몰과 상업시설이 밀집해 있습니다. 역 주변에는 <a href="/sangnok-gu/bono-dong/">본오동</a>의 주요 상권이 형성되어 있으며, 하루 중 가장 많은 이용객이 집중되는 곳입니다.</p>
<p>상록수역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>상록수역 역세권 특징</h2>
<ul>
<li><strong>대규모 상업시설</strong>: 쇼핑몰, 음식점 집중</li>
<li><strong>교통 중심</strong>: 버스 노선 다양</li>
<li><strong>24시간 운영</strong>: 야간 편의시설 충분</li>
<li><strong>현대식 건물</strong>: 주상복합, 오피스</li>
<li><strong>접근성</strong>: 역 근처 다양한 시설</li>
</ul>
</section>

<section>
<h2>인접 생활권</h2>
<p>상록수역은 다음 지역과 인접해 있습니다:</p>
<ul>
<li><a href="/sangnok-gu/bono-dong/">본오동</a> — 쇼핑 중심지</li>
<li><a href="/area/sangnoksu-bono/">상록수·본오 생활권</a> — 통합 안내</li>
<li><a href="/sangnok-gu/">상록구 전체</a></li>
</ul>
</section>

<section>
<h2>상록수역 역세권 이용 안내</h2>
<p>상록수역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>정확한 빌딩명 또는 주소 전달</li>
<li>역 출구 번호 안내 (역세권 이동 시간 단축)</li>
<li>접근성 및 주차 상황 확인</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section>
<h2>주변 시설</h2>
<p>상록수역 역세권에는 다음 시설들이 있습니다:</p>
<ul>
<li>대형 쇼핑몰</li>
<li>음식점, 카페, 편의점</li>
<li>은행, 관공서</li>
<li>병원, 의원</li>
<li>숙박시설</li>
</ul>
</section>

<section class="pricing">
<h3>상록수역 기본 요금</h3>
<p><strong>상록수역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
<li>3시간: 210,000원~</li>
</ul>
<p>정확한 가격은 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>
"""
)

hanyang_station = create_station_page(
    path="station/hanyang-univ-at-ansan-station/",
    title="한대앞역 출장마사지｜대학가 생활권 홈타이 안내",
    desc="한대앞역 출장마사지·홈타이 예약 전 대학가, 사동 생활권을 확인하세요.",
    h1="한대앞역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("한대앞역", "")],
    body_content="""
<section>
<h2>한대앞역 소개</h2>
<p><strong>한대앞역</strong>은 한양대학교(안산캠퍼스) 인근의 대학 중심 역으로, <a href="/sangnok-gu/sa-dong/">사동</a>에 위치합니다. 젊은 학생과 청년들이 많이 이용하는 활기찬 역세권입니다. 음식점, 카페, 노래방 등 문화시설이 발달했습니다.</p>
<p>한대앞역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>한대앞역 역세권 특징</h2>
<ul>
<li><strong>대학 중심</strong>: 한양대학교 인근</li>
<li><strong>젊은 분위기</strong>: 학생·청년 중심</li>
<li><strong>활발한 상권</strong>: 음식점, 카페 많음</li>
<li><strong>문화시설</strong>: 노래방, 영화관 등</li>
<li><strong>야간 활동</strong>: 야간 운영 시설 많음</li>
</ul>
</section>

<section>
<h2>인접 지역</h2>
<ul>
<li><a href="/sangnok-gu/sa-dong/">사동</a> — 한대앞역 인근</li>
<li><a href="/sangnok-gu/">상록구 전체</a></li>
</ul>
</section>

<section>
<h2>한대앞역 역세권 이용 안내</h2>
<p>한대앞역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>건물명 또는 주소 정확히 전달</li>
<li>역 출구 번호 확인</li>
<li>대학 캠퍼스 인근 특성 고려</li>
<li><a href="/check/">이용 전 확인사항</a> 확인</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>한대앞역 기본 요금</h3>
<p><strong>한대앞역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

sari_station = create_station_page(
    path="station/sari-station/",
    title="사리역 출장마사지｜지역 생활권 홈타이 안내",
    desc="사리역 출장마사지·홈타이 예약 전 인근 생활권을 확인하세요.",
    h1="사리역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("사리역", "")],
    body_content="""
<section>
<h2>사리역 소개</h2>
<p><strong>사리역</strong>은 안산시의 주거 중심 역으로, 안정적인 생활 환경을 갖추고 있습니다. 역 주변에는 주택과 소규모 상점들이 분포하고 있으며, 조용한 분위기를 유지하고 있습니다.</p>
<p>사리역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>사리역 역세권 특징</h2>
<ul>
<li><strong>주거 중심</strong>: 주택가 역</li>
<li><strong>조용한 환경</strong>: 안정적 분위기</li>
<li><strong>지역 상권</strong>: 소규모 가게</li>
<li><strong>교통 편의</strong>: 버스 노선</li>
</ul>
</section>

<section>
<h2>사리역 이용 안내</h2>
<p>사리역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>정확한 주소 전달</li>
<li>역 출구 번호 안내</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>사리역 기본 요금</h3>
<p><strong>사리역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

jungang_station = create_station_page(
    path="station/jungang-station/",
    title="중앙역 출장마사지｜단원구 중심 홈타이 안내",
    desc="중앙역 출장마사지·홈타이 예약 전 중앙동, 상업지구 생활권을 확인하세요.",
    h1="중앙역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("중앙역", "")],
    body_content="""
<section>
<h2>중앙역 소개</h2>
<p><strong>중앙역</strong>은 안산시 단원구의 중심 교통 거점으로, <a href="/danwon-gu/jungang-dong/">중앙동</a>에 위치합니다. 역 주변에는 현대적인 상업시설과 주상복합이 밀집해 있으며, 안산시의 주요 상권을 형성합니다.</p>
<p>중앙역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>중앙역 역세권 특징</h2>
<ul>
<li><strong>상업 중심</strong>: 주상복합, 쇼핑시설</li>
<li><strong>교통 거점</strong>: 다양한 버스 노선</li>
<li><strong>현대식 건물</strong>: 새로운 시설</li>
<li><strong>24시간 인프라</strong>: 편의시설 충분</li>
<li><strong>접근성</strong>: 역에서 근처 시설 바로 접근</li>
</ul>
</section>

<section>
<h2>인접 생활권</h2>
<ul>
<li><a href="/danwon-gu/jungang-dong/">중앙동</a> — 역 직인접</li>
<li><a href="/area/jungang-gojan/">중앙역·고잔 생활권</a></li>
<li><a href="/danwon-gu/">단원구 전체</a></li>
</ul>
</section>

<section>
<h2>중앙역 역세권 이용 안내</h2>
<p>중앙역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>빌딩명 또는 주소 정확히 전달</li>
<li>역 출구 번호 확인</li>
<li>주상복합 건물 접근 방법 안내</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>중앙역 기본 요금</h3>
<p><strong>중앙역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

gojan_station = create_station_page(
    path="station/gojan-station/",
    title="고잔역 출장마사지｜고잔동 생활권 홈타이 안내",
    desc="고잔역 출장마사지·홈타이 예약 전 고잔동 아파트단지 생활권을 확인하세요.",
    h1="고잔역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("고잔역", "")],
    body_content="""
<section>
<h2>고잔역 소개</h2>
<p><strong>고잔역</strong>은 <a href="/danwon-gu/gojan-dong/">고잔동</a>의 중심 역으로, 대규모 아파트 단지가 밀집한 주거 중심 역세권입니다. 역 주변에는 아파트 단지 내 편의시설과 상점들이 위치하고 있습니다.</p>
<p>고잔역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>고잔역 역세권 특징</h2>
<ul>
<li><strong>아파트 단지 중심</strong>: 대규모 주거시설</li>
<li><strong>교통 편의</strong>: 역 근처 버스 정류장</li>
<li><strong>단지 내 편의</strong>: 아파트 단지 시설</li>
<li><strong>안전 환경</strong>: 안정적 주거지</li>
</ul>
</section>

<section>
<h2>고잔역 역세권 이용 안내</h2>
<p>고잔역 인근 아파트 단지에서 출장마사지를 예약할 때는:</p>
<ul>
<li>아파트 단지명 정확히 전달</li>
<li>동호수 명확히 안내</li>
<li>단지 출입 가능 여부 확인</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>고잔역 기본 요금</h3>
<p><strong>고잔역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

choji_station = create_station_page(
    path="station/choji-station/",
    title="초지역 출장마사지｜초지동 신도시 홈타이 안내",
    desc="초지역 출장마사지·홈타이 예약 전 초지동 신도시, 호수공원 생활권을 확인하세요.",
    h1="초지역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("초지역", "")],
    body_content="""
<section>
<h2>초지역 소개</h2>
<p><strong>초지역</strong>은 <a href="/danwon-gu/choji-dong/">초지동</a> 신도시의 중심 역으로, 계획된 도시 설계와 현대식 주거 시설이 특징입니다. 호수공원 인근으로 자연 환경도 우수합니다.</p>
<p>초지역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>초지역 역세권 특징</h2>
<ul>
<li><strong>신도시 중심</strong>: 계획된 설계</li>
<li><strong>현대식 시설</strong>: 새로운 아파트</li>
<li><strong>공원 시설</strong>: 호수공원 근처</li>
<li><strong>자연 환경</strong>: 녹지 많음</li>
<li><strong>교통 편의</strong>: 역 중심의 버스</li>
</ul>
</section>

<section>
<h2>초지역 역세권 이용 안내</h2>
<p>초지역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>신도시 주거단지명 정확히 전달</li>
<li>동호수 명확히 안내</li>
<li>접근성 확인</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>초지역 기본 요금</h3>
<p><strong>초지역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

ansan_station = create_station_page(
    path="station/ansan-station/",
    title="안산역 출장마사지｜원곡동 상업지구 홈타이 안내",
    desc="안산역 출장마사지·홈타이 예약 전 원곡동 상업 생활권을 확인하세요.",
    h1="안산역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("안산역", "")],
    body_content="""
<section>
<h2>안산역 소개</h2>
<p><strong>안산역</strong>은 <a href="/danwon-gu/wongok-dong/">원곡동</a>의 주요 상업지구 중심 역으로, 안산시의 주요 교통 거점 중 하나입니다. 역 주변에는 다양한 음식점, 상점, 숙박시설이 밀집해 있습니다.</p>
<p>안산역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>안산역 역세권 특징</h2>
<ul>
<li><strong>상업 중심</strong>: 음식점, 상점 많음</li>
<li><strong>교통 거점</strong>: 버스 노선 발달</li>
<li><strong>24시간 시설</strong>: 야간 운영 편의</li>
<li><strong>숙박시설</strong>: 모텔, 호텔 인근</li>
<li><strong>활발한 상권</strong>: 다양한 업종</li>
</ul>
</section>

<section>
<h2>인접 역</h2>
<ul>
<li><a href="/station/wongok-station/">원곡역</a> — 인접역</li>
<li><a href="/danwon-gu/">단원구 전체</a></li>
</ul>
</section>

<section>
<h2>안산역 역세권 이용 안내</h2>
<p>안산역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>정확한 빌딩명 또는 주소 전달</li>
<li>역 출구 번호 확인</li>
<li>상업지구 위치 특성 고려</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>안산역 기본 요금</h3>
<p><strong>안산역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

shingiloncheon_station = create_station_page(
    path="station/shingiloncheon-station/",
    title="신길온천역 출장마사지｜온천문화 생활권 홈타이 안내",
    desc="신길온천역 출장마사지·홈타이 예약 전 온천시설, 신길동 생활권을 확인하세요.",
    h1="신길온천역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("신길온천역", "")],
    body_content="""
<section>
<h2>신길온천역 소개</h2>
<p><strong>신길온천역</strong>은 신길온천 시설과 문화가 있는 특색있는 역으로, 온천 관광지로도 알려져 있습니다. <a href="/danwon-gu/seonbu-dong/">선부동</a>과도 인접해 있습니다.</p>
<p>신길온천역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>신길온천역 역세권 특징</h2>
<ul>
<li><strong>온천시설</strong>: 신길온천 인근</li>
<li><strong>관광지</strong>: 문화시설 많음</li>
<li><strong>레저활동</strong>: 온천 이용</li>
<li><strong>특색 지역</strong>: 온천문화 중심</li>
<li><strong>교통 편의</strong>: 버스 노선</li>
</ul>
</section>

<section>
<h2>신길온천역 역세권 이용 안내</h2>
<p>신길온천역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>정확한 주소 전달</li>
<li>온천시설 인근 특성 고려</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>신길온천역 기본 요금</h3>
<p><strong>신길온천역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

seonbu_station = create_station_page(
    path="station/seonbu-station/",
    title="선부역 출장마사지｜선부동 생활권 홈타이 안내",
    desc="선부역 출장마사지·홈타이 예약 전 선부동, 신길온천 인근 생활권을 확인하세요.",
    h1="선부역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("선부역", "")],
    body_content="""
<section>
<h2>선부역 소개</h2>
<p><strong>선부역</strong>은 <a href="/danwon-gu/seonbu-dong/">선부동</a>의 중심 역으로, 신길온천 시설과 가까운 특색있는 역세권입니다. 온천 문화와 주거가 함께하는 지역입니다.</p>
<p>선부역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>선부역 역세권 특징</h2>
<ul>
<li><strong>온천 근처</strong>: 신길온천 인접</li>
<li><strong>주거 환경</strong>: 주택가</li>
<li><strong>교통 편의</strong>: 버스 노선</li>
<li><strong>문화시설</strong>: 온천 관련</li>
<li><strong>관광지</strong>: 휴양 기능</li>
</ul>
</section>

<section>
<h2>선부역 역세권 이용 안내</h2>
<p>선부역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>정확한 주소 전달</li>
<li>역 출구 번호 안내</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>선부역 기본 요금</h3>
<p><strong>선부역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

wongok_station = create_station_page(
    path="station/wongok-station/",
    title="원곡역 출장마사지｜원곡동 상업지구 홈타이 안내",
    desc="원곡역 출장마사지·홈타이 예약 전 원곡동 상업 생활권을 확인하세요.",
    h1="원곡역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("원곡역", "")],
    body_content="""
<section>
<h2>원곡역 소개</h2>
<p><strong>원곡역</strong>은 <a href="/danwon-gu/wongok-dong/">원곡동</a>의 주요 역으로, 상업지구의 중심입니다. <a href="/station/ansan-station/">안산역</a>과 인접해 있으며, 활발한 상권을 형성하고 있습니다.</p>
<p>원곡역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>원곡역 역세권 특징</h2>
<ul>
<li><strong>상업 중심</strong>: 음식점, 상점 밀집</li>
<li><strong>교통 거점</strong>: 버스 노선 많음</li>
<li><strong>24시간 시설</strong>: 야간 편의</li>
<li><strong>활발한 상권</strong>: 다양한 업종</li>
<li><strong>인접역</strong>: 안산역 근처</li>
</ul>
</section>

<section>
<h2>원곡역 역세권 이용 안내</h2>
<p>원곡역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>빌딩명 또는 주소 정확히 전달</li>
<li>역 출구 번호 확인</li>
<li>상업지구 위치 특성 고려</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>원곡역 기본 요금</h3>
<p><strong>원곡역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

dalmi_station = create_station_page(
    path="station/dalmi-station/",
    title="달미역 출장마사지｜지역 생활권 홈타이 안내",
    desc="달미역 출장마사지·홈타이 예약 전 인근 생활권을 확인하세요.",
    h1="달미역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("달미역", "")],
    body_content="""
<section>
<h2>달미역 소개</h2>
<p><strong>달미역</strong>은 안산시의 주거 중심 역으로, 안정적인 생활 환경을 갖추고 있습니다. 역 주변에는 주택과 편의시설이 함께 분포하고 있습니다.</p>
<p>달미역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>달미역 역세권 특징</h2>
<ul>
<li><strong>주거 중심</strong>: 주택가</li>
<li><strong>안정 환경</strong>: 조용한 분위기</li>
<li><strong>교통 편의</strong>: 버스 노선</li>
<li><strong>생활 편의</strong>: 편의점, 음식점</li>
</ul>
</section>

<section>
<h2>달미역 이용 안내</h2>
<p>달미역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>정확한 주소 전달</li>
<li>역 출구 번호 안내</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>달미역 기본 요금</h3>
<p><strong>달미역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

wonsi_station = create_station_page(
    path="station/wonsi-station/",
    title="원시역 출장마사지｜원시 생활권 홈타이 안내",
    desc="원시역 출장마사지·홈타이 예약 전 인근 생활권을 확인하세요.",
    h1="원시역 출장마사지",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/"), ("원시역", "")],
    body_content="""
<section>
<h2>원시역 소개</h2>
<p><strong>원시역</strong>은 안산시의 끝부분 역으로, 신도시 개발이 진행되고 있는 지역입니다. 현대식 주거 시설과 상업 기반이 조성되고 있습니다.</p>
<p>원시역 역세권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>원시역 역세권 특징</h2>
<ul>
<li><strong>개발 진행중</strong>: 신도시 설계</li>
<li><strong>현대식 시설</strong>: 새로운 주거</li>
<li><strong>교통 거점</strong>: 버스 노선 발달</li>
<li><strong>성장 잠재력</strong>: 발전 가능 지역</li>
</ul>
</section>

<section>
<h2>원시역 이용 안내</h2>
<p>원시역 인근에서 출장마사지를 예약할 때는:</p>
<ul>
<li>정확한 주소 전달</li>
<li>새로운 주거단지명 명확히 전달</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>원시역 기본 요금</h3>
<p><strong>원시역 역세권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

# PAGES 리스트에 모든 역세권 페이지 집계
PAGES = [
    sangnoksu_station,
    hanyang_station,
    sari_station,
    jungang_station,
    gojan_station,
    choji_station,
    ansan_station,
    shingiloncheon_station,
    seonbu_station,
    wongok_station,
    dalmi_station,
    wonsi_station,
]
