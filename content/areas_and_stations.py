# 안산 생활권 페이지 — 12개 (지역·역 통합 생활권)

def create_lifestyle_page(path, title, desc, h1, breadcrumb, body_content):
    """생활권 페이지 생성 헬퍼 함수"""
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }

# ===== 12개 생활권 페이지 =====

jungang_gojan = create_lifestyle_page(
    path="area/jungang-gojan/",
    title="중앙역·고잔 생활권 출장마사지｜단원 중심 홈타이 안내",
    desc="중앙역·고잔 생활권 출장마사지·홈타이 예약 전 중앙동, 고잔동 지역을 확인하세요.",
    h1="중앙역·고잔 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("중앙역·고잔", "")],
    body_content="""
<section>
<h2>중앙역·고잔 생활권 소개</h2>
<p><strong>중앙역·고잔 생활권</strong>은 안산시 단원구의 중심 상권으로, <a href="/station/jungang-station/">중앙역</a>을 중심으로 <a href="/danwon-gu/jungang-dong/">중앙동</a>과 <a href="/station/gojan-station/">고잔역</a>의 <a href="/danwon-gu/gojan-dong/">고잔동</a>을 통합한 광역 생활권입니다.</p>
<p>이 지역은 현대적인 상업 시설과 주거 단지가 함께 어우러진 안산시의 가장 발전된 도시 중심지입니다. 출장마사지·홈타이 서비스도 간다GO에서 안전하게 관리합니다.</p>
</section>

<section>
<h2>생활권 구성</h2>
<p>중앙역·고잔 생활권은 다음과 같이 구성됩니다:</p>
<ul>
<li><a href="/station/jungang-station/">중앙역</a> 역세권 — 상업 중심지</li>
<li><a href="/danwon-gu/jungang-dong/">중앙동</a> — 주상복합 주거</li>
<li><a href="/station/gojan-station/">고잔역</a> 역세권 — 아파트 단지 중심</li>
<li><a href="/danwon-gu/gojan-dong/">고잔동</a> — 주거 환경</li>
</ul>
</section>

<section>
<h2>중앙역·고잔 생활권의 특징</h2>
<ul>
<li><strong>이중 교통 거점</strong>: 중앙역과 고잔역 모두 이용 가능</li>
<li><strong>현대식 시설</strong>: 새로운 주상복합, 아파트</li>
<li><strong>상업 발달</strong>: 쇼핑, 음식점 다양</li>
<li><strong>주거 환경</strong>: 안정적이고 쾌적</li>
<li><strong>24시간 인프라</strong>: 편의시설 충분</li>
</ul>
</section>

<section>
<h2>인접 생활권</h2>
<ul>
<li><a href="/area/choji-dong/">초지역·초지동</a> — 신도시 방향</li>
<li><a href="/danwon-gu/">단원구 전체</a> — 광역 정보</li>
</ul>
</section>

<section>
<h2>출장마사지 이용 안내</h2>
<p>중앙역·고잔 생활권에서 출장마사지를 이용할 때는:</p>
<ul>
<li>중앙역 인근 상업 건물 또는 고잔동 아파트 단지 명확히 구분</li>
<li>정확한 주소 및 건물명 전달</li>
<li>접근성 및 주차 상황 안내</li>
<li><a href="/check/">이용 전 확인사항</a> 확인</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>중앙역·고잔 생활권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
<li>3시간: 210,000원~</li>
</ul>
<p>정확한 가격은 <a href="tel:0508-202-4719">0508-202-4719</a>로 문의하세요.</p>
</section>
"""
)

choji_lifestyle = create_lifestyle_page(
    path="area/choji-dong/",
    title="초지역·초지동 생활권 출장마사지｜신도시 홈타이 안내",
    desc="초지역·초지동 생활권 출장마사지·홈타이 예약 전 신도시, 호수공원 생활권을 확인하세요.",
    h1="초지역·초지동 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("초지역·초지동", "")],
    body_content="""
<section>
<h2>초지역·초지동 생활권 소개</h2>
<p><strong>초지역·초지동 생활권</strong>은 안산시의 신도시 중심으로, <a href="/station/choji-station/">초지역</a>과 <a href="/danwon-gu/choji-dong/">초지동</a>을 통합한 현대적 생활권입니다. 계획된 도시 설계와 호수공원 자연 환경이 조화된 특색있는 지역입니다.</p>
<p>초지역·초지동 생활권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>생활권 구성</h2>
<ul>
<li><a href="/station/choji-station/">초지역</a> 역세권 — 신도시 중심</li>
<li><a href="/danwon-gu/choji-dong/">초지동</a> — 현대식 주거</li>
<li><a href="/danwon-gu/hasu-dong/">호수동</a> — 호수공원 인근</li>
</ul>
</section>

<section>
<h2>초지역·초지동 생활권의 특징</h2>
<ul>
<li><strong>신도시 설계</strong>: 계획된 도시구조</li>
<li><strong>현대식 주거</strong>: 새로운 아파트, 주상복합</li>
<li><strong>자연 환경</strong>: 호수공원, 녹지</li>
<li><strong>공원 시설</strong>: 산책로, 휴게 공간</li>
<li><strong>교통 편의</strong>: 초지역 중심</li>
<li><strong>깨끗한 환경</strong>: 환경 친화적</li>
</ul>
</section>

<section>
<h2>호수공원</h2>
<p>초지역·초지동 생활권은 호수공원과 인접해 있어, 자연 속에서 휴식을 취할 수 있는 환경을 갖추고 있습니다. 공원 산책로와 수변 시설을 통해 쾌적한 생활환경을 제공합니다.</p>
</section>

<section>
<h2>출장마사지 이용 안내</h2>
<p>초지역·초지동 생활권에서 출장마사지를 이용할 때는:</p>
<ul>
<li>신도시 주거단지명 정확히 전달</li>
<li>동호수 명확히 안내</li>
<li>단지 출입 가능 여부 확인</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>초지역·초지동 생활권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

ansan_wongok = create_lifestyle_page(
    path="area/ansan-station-wongok/",
    title="안산역·원곡동 생활권 출장마사지｜상업중심 홈타이 안내",
    desc="안산역·원곡동 생활권 출장마사지·홈타이 예약 전 상업지구 생활권을 확인하세요.",
    h1="안산역·원곡동 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("안산역·원곡동", "")],
    body_content="""
<section>
<h2>안산역·원곡동 생활권 소개</h2>
<p><strong>안산역·원곡동 생활권</strong>은 안산시의 주요 상업 중심으로, <a href="/station/ansan-station/">안산역</a>과 <a href="/danwon-gu/wongok-dong/">원곡동</a>을 통합한 활발한 상권입니다. 다양한 음식점, 숙박시설, 상점이 밀집해 있습니다.</p>
<p>안산역·원곡동 생활권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>생활권 구성</h2>
<ul>
<li><a href="/station/ansan-station/">안산역</a> 역세권 — 상업 중심지</li>
<li><a href="/danwon-gu/wongok-dong/">원곡동</a> — 상업·주거 혼합</li>
<li><a href="/station/wongok-station/">원곡역</a> — 인접역</li>
</ul>
</section>

<section>
<h2>안산역·원곡동 생활권의 특징</h2>
<ul>
<li><strong>상업 중심</strong>: 음식점, 상점 밀집</li>
<li><strong>교통 거점</strong>: 버스 노선 발달</li>
<li><strong>24시간 시설</strong>: 야간 운영 편의</li>
<li><strong>숙박시설</strong>: 모텔, 호텔 인근</li>
<li><strong>활발한 상권</strong>: 다양한 업종</li>
<li><strong>이중 역세권</strong>: 안산역, 원곡역</li>
</ul>
</section>

<section>
<h2>출장마사지 이용 안내</h2>
<p>안산역·원곡동 생활권에서 출장마사지를 이용할 때는:</p>
<ul>
<li>정확한 빌딩명 또는 주소 전달</li>
<li>역 출구 번호 확인</li>
<li>상업지구 위치 특성 고려</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>안산역·원곡동 생활권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

sangnoksu_bono = create_lifestyle_page(
    path="area/sangnoksu-bono/",
    title="상록수·본오 생활권 출장마사지｜상록 중심 홈타이 안내",
    desc="상록수·본오 생활권 출장마사지·홈타이 예약 전 상록구 쇼핑 중심지를 확인하세요.",
    h1="상록수·본오 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("상록수·본오", "")],
    body_content="""
<section>
<h2>상록수·본오 생활권 소개</h2>
<p><strong>상록수·본오 생활권</strong>은 안산시 상록구의 중심으로, <a href="/station/sangnoksu-station/">상록수역</a>과 <a href="/sangnok-gu/bono-dong/">본오동</a>을 통합한 주요 상권입니다. 안산시에서 가장 발전된 상업지구로, 대규모 쇼핑몰과 현대식 건물이 밀집해 있습니다.</p>
<p>상록수·본오 생활권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>생활권 구성</h2>
<ul>
<li><a href="/station/sangnoksu-station/">상록수역</a> 역세권 — 대규모 쇼핑몰 중심</li>
<li><a href="/sangnok-gu/bono-dong/">본오동</a> — 상업 시설 집중</li>
<li><a href="/sangnok-gu/">상록구 전체</a> — 광역 정보</li>
</ul>
</section>

<section>
<h2>상록수·본오 생활권의 특징</h2>
<ul>
<li><strong>대규모 상권</strong>: 쇼핑몰, 음식점 집중</li>
<li><strong>현대식 시설</strong>: 새로운 상업 건물</li>
<li><strong>교통 중심</strong>: 상록수역 중심</li>
<li><strong>24시간 운영</strong>: 야간 편의시설 충분</li>
<li><strong>접근성</strong>: 최고의 대중교통 연결</li>
<li><strong>상업 밀집도</strong>: 가장 높은 수준</li>
</ul>
</section>

<section>
<h2>쇼핑 및 음식</h2>
<p>상록수·본오 생활권은 안산시에서 가장 다양한 쇼핑과 음식점 선택이 가능한 지역입니다. 대형 쇼핑몰, 의류점, 음식점, 카페 등이 모두 집중되어 있습니다.</p>
</section>

<section>
<h2>출장마사지 이용 안내</h2>
<p>상록수·본오 생활권에서 출장마사지를 이용할 때는:</p>
<ul>
<li>정확한 빌딩명 또는 상업시설명 전달</li>
<li>역 출구 번호 안내</li>
<li>주상복합 또는 오피스 건물 구분</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>상록수·본오 생활권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
<li>3시간: 210,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

hanyang_sa = create_lifestyle_page(
    path="area/hanyang-univ-sa-dong/",
    title="한대앞·사동 생활권 출장마사지｜대학가 홈타이 안내",
    desc="한대앞·사동 생활권 출장마사지·홈타이 예약 전 대학가, 상록 생활권을 확인하세요.",
    h1="한대앞·사동 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("한대앞·사동", "")],
    body_content="""
<section>
<h2>한대앞·사동 생활권 소개</h2>
<p><strong>한대앞·사동 생활권</strong>은 한양대학교(안산캠퍼스) 인근의 대학 중심 생활권으로, <a href="/station/hanyang-univ-at-ansan-station/">한대앞역</a>과 <a href="/sangnok-gu/sa-dong/">사동</a>을 통합합니다. 젊은 학생과 청년들이 많이 활동하는 활기찬 지역입니다.</p>
<p>한대앞·사동 생활권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>생활권 구성</h2>
<ul>
<li><a href="/station/hanyang-univ-at-ansan-station/">한대앞역</a> 역세권 — 대학 중심</li>
<li><a href="/sangnok-gu/sa-dong/">사동</a> — 주거·상업 혼합</li>
<li><a href="/sangnok-gu/">상록구 전체</a></li>
</ul>
</section>

<section>
<h2>한대앞·사동 생활권의 특징</h2>
<ul>
<li><strong>대학 중심</strong>: 한양대학교 인근</li>
<li><strong>젊은 분위기</strong>: 학생·청년 주민</li>
<li><strong>활발한 상권</strong>: 음식점, 카페 많음</li>
<li><strong>문화시설</strong>: 노래방, 영화관</li>
<li><strong>야간 활동</strong>: 야간 운영 시설 충분</li>
<li><strong>교통 편의</strong>: 한대앞역 중심</li>
</ul>
</section>

<section>
<h2>출장마사지 이용 안내</h2>
<p>한대앞·사동 생활권에서 출장마사지를 이용할 때는:</p>
<ul>
<li>건물명 또는 주소 정확히 전달</li>
<li>역 출구 번호 확인</li>
<li>대학 캠퍼스 인근 특성 고려</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>한대앞·사동 생활권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

seonbu_lifestyle = create_lifestyle_page(
    path="area/seonbu-station/",
    title="선부역·선부동 생활권 출장마사지｜온천 생활권 홈타이 안내",
    desc="선부역·선부동 생활권 출장마사지·홈타이 예약 전 온천, 신길온천 생활권을 확인하세요.",
    h1="선부역·선부동 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("선부역·선부동", "")],
    body_content="""
<section>
<h2>선부역·선부동 생활권 소개</h2>
<p><strong>선부역·선부동 생활권</strong>은 신길온천 시설이 있는 특색있는 생활권으로, <a href="/station/seonbu-station/">선부역</a>과 <a href="/danwon-gu/seonbu-dong/">선부동</a>을 통합합니다. 온천 문화와 관광 기능이 발달한 지역입니다.</p>
<p>선부역·선부동 생활권의 출장마사지·홈타이 서비스는 간다GO에서 전문적으로 관리합니다.</p>
</section>

<section>
<h2>생활권 구성</h2>
<ul>
<li><a href="/station/seonbu-station/">선부역</a> 역세권 — 온천 인접</li>
<li><a href="/danwon-gu/seonbu-dong/">선부동</a> — 주거·온천 혼합</li>
<li><a href="/station/shingiloncheon-station/">신길온천역</a> — 인접역</li>
</ul>
</section>

<section>
<h2>선부역·선부동 생활권의 특징</h2>
<ul>
<li><strong>온천 시설</strong>: 신길온천 인근</li>
<li><strong>관광 기능</strong>: 문화시설 발달</li>
<li><strong>주거 환경</strong>: 주택과 주거시설</li>
<li><strong>교통 편의</strong>: 선부역 중심</li>
<li><strong>휴양 기능</strong>: 온천 이용 가능</li>
<li><strong>특색 지역</strong>: 온천문화 중심</li>
</ul>
</section>

<section>
<h2>신길온천</h2>
<p>선부역·선부동 생활권의 가장 큰 특징은 신길온천 시설입니다. 온천 문화와 휴양 기능이 발달했으며, 관광지로도 알려져 있습니다.</p>
</section>

<section>
<h2>출장마사지 이용 안내</h2>
<p>선부역·선부동 생활권에서 출장마사지를 이용할 때는:</p>
<ul>
<li>정확한 주소 전달</li>
<li>선부역 또는 신길온천역 근처 구분</li>
<li>온천시설 인근 특성 고려</li>
<li><a href="/check/">이용 전 확인사항</a> 참조</li>
</ul>
<p><a href="tel:0508-202-4719">예약: 0508-202-4719</a></p>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><strong>선부역·선부동 생활권 출장마사지 기본 요금</strong></p>
<ul>
<li>1시간: 70,000원~</li>
<li>2시간: 140,000원~</li>
</ul>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

# 추가 6개 생활권 (간소화 버전)
gohsan_shinshi = create_lifestyle_page(
    path="area/gojan-shinshi/",
    title="고잔신도시·호수공원 생활권 출장마사지｜신도시 홈타이 안내",
    desc="고잔신도시·호수공원 생활권 출장마사지·홈타이 예약을 확인하세요.",
    h1="고잔신도시·호수공원 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("고잔신도시·호수공원", "")],
    body_content="""
<section>
<h2>고잔신도시·호수공원 생활권 소개</h2>
<p><strong>고잔신도시·호수공원 생활권</strong>은 현대적 신도시와 자연이 함께하는 생활권입니다. <a href="/danwon-gu/gojan-dong/">고잔동</a>의 신도시와 <a href="/danwon-gu/hasu-dong/">호수동</a>의 공원 환경이 조화됩니다.</p>
<p>이 생활권의 출장마사지·홈타이 서비스는 간다GO에서 관리합니다.</p>
</section>

<section>
<h2>생활권의 특징</h2>
<ul>
<li><strong>신도시 설계</strong>: 계획된 구조</li>
<li><strong>아파트 단지</strong>: 현대식 주거</li>
<li><strong>자연 환경</strong>: 호수공원 인근</li>
<li><strong>공원 시설</strong>: 산책로, 휴게공간</li>
</ul>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/danwon-gu/gojan-dong/">고잔동</a></li>
<li><a href="/danwon-gu/hasu-dong/">호수동</a></li>
<li><a href="/station/gojan-station/">고잔역</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

wolpi_seongu = create_lifestyle_page(
    path="area/wolpi-seongu/",
    title="월피·성포 생활권 출장마사지｜상업·산업 혼합 홈타이 안내",
    desc="월피·성포 생활권 출장마사지·홈타이 예약을 확인하세요.",
    h1="월피·성포 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("월피·성포", "")],
    body_content="""
<section>
<h2>월피·성포 생활권 소개</h2>
<p><strong>월피·성포 생활권</strong>은 <a href="/sangnok-gu/wolpi-dong/">월피동</a>과 <a href="/danwon-gu/seongu-dong/">성포동</a>의 상업·산업 혼합 지역입니다.</p>
</section>

<section>
<h2>생활권의 특징</h2>
<ul>
<li><strong>혼합 지역</strong>: 상업·산업</li>
<li><strong>지역 상권</strong>: 소규모 상점</li>
<li><strong>근로 환경</strong>: 산업 지역</li>
</ul>
</section>

<section>
<h2>관련 페이지</h2>
<ul>
<li><a href="/sangnok-gu/wolpi-dong/">월피동</a></li>
<li><a href="/danwon-gu/seongu-dong/">성포동</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

banwol_gungun = create_lifestyle_page(
    path="area/banwol-gungun/",
    title="반월·건건 생활권 출장마사지｜공단 지역 홈타이 안내",
    desc="반월·건건 생활권 출장마사지·홈타이 예약을 확인하세요.",
    h1="반월·건건 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("반월·건건", "")],
    body_content="""
<section>
<h2>반월·건건 생활권 소개</h2>
<p><strong>반월·건건 생활권</strong>은 반월공단 중심의 산업 지역입니다.</p>
</section>

<section>
<h2>생활권의 특징</h2>
<ul>
<li><strong>공단 중심</strong>: 반월공단</li>
<li><strong>산업 활동</strong>: 다양한 기업</li>
<li><strong>근로 환경</strong>: 근로자 중심</li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

wonsi_sihwa = create_lifestyle_page(
    path="area/wonsi-sihwa/",
    title="원시·시화공단 생활권 출장마사지｜산업 지역 홈타이 안내",
    desc="원시·시화공단 생활권 출장마사지·홈타이 예약을 확인하세요.",
    h1="원시·시화공단 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("원시·시화공단", "")],
    body_content="""
<section>
<h2>원시·시화공단 생활권 소개</h2>
<p><strong>원시·시화공단 생활권</strong>은 시화공단 인근의 산업 중심 지역입니다.</p>
</section>

<section>
<h2>생활권의 특징</h2>
<ul>
<li><strong>공단 지역</strong>: 시화공단</li>
<li><strong>산업 활동</strong>: 대규모 공장</li>
<li><strong>근로 환경</strong>: 근로자 중심</li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

shinggil_neungil = create_lifestyle_page(
    path="area/shinggil-neungil/",
    title="신길·능길 생활권 출장마사지｜혼합 생활권 홈타이 안내",
    desc="신길·능길 생활권 출장마사지·홈타이 예약을 확인하세요.",
    h1="신길·능길 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("신길·능길", "")],
    body_content="""
<section>
<h2>신길·능길 생활권 소개</h2>
<p><strong>신길·능길 생활권</strong>은 신길온천 인근과 능길 지역의 혼합 생활권입니다.</p>
</section>

<section>
<h2>생활권의 특징</h2>
<ul>
<li><strong>온천 시설</strong>: 신길온천</li>
<li><strong>혼합 지역</strong>: 주거·상업</li>
<li><strong>관광 기능</strong>: 온천문화</li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

daebu_island = create_lifestyle_page(
    path="area/daebu-island/",
    title="대부도 생활권 출장마사지｜섬 지역 홈타이 안내",
    desc="대부도 생활권 출장마사지·홈타이 예약 전 섬 지역을 확인하세요.",
    h1="대부도 생활권",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/"), ("대부도", "")],
    body_content="""
<section>
<h2>대부도 생활권 소개</h2>
<p><strong>대부도 생활권</strong>은 안산시의 섬 지역으로, 해양 문화와 관광 자원이 풍부합니다.</p>
</section>

<section>
<h2>생활권의 특징</h2>
<ul>
<li><strong>섬 지역</strong>: 대부도</li>
<li><strong>해양 문화</strong>: 해변 시설</li>
<li><strong>관광 자원</strong>: 자연경관</li>
<li><strong>레저 활동</strong>: 해수욕, 낚시</li>
</ul>
</section>

<section><h2>관련 페이지</h2>
<ul>
<li><a href="/danwon-gu/daebu-dong/">대부도 안내</a></li>
</ul>
</section>

<section class="pricing">
<h3>기본 요금</h3>
<p><a href="tel:0508-202-4719">0508-202-4719</a></p>
</section>
"""
)

# PAGES 리스트에 모든 생활권 페이지 집계
PAGES = [
    jungang_gojan,
    choji_lifestyle,
    ansan_wongok,
    sangnoksu_bono,
    hanyang_sa,
    seonbu_lifestyle,
    gohsan_shinshi,
    wolpi_seongu,
    banwol_gungun,
    wonsi_sihwa,
    shinggil_neungil,
    daebu_island,
]
