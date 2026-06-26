# 경기 출장마사지 사이트 공통 설정

BASE_URL = "https://gyeonggi-massage.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "간"  # 헤더 로고 원형 마크 글자
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

AREA_SERVED = "경기도"
TAGLINE = "경기 전지역 방문 관리"

# 상단 메뉴 — 키워드(출장마사지) 반복 없이 권역·지역명만 표시
NAV = [
    ("경기", "/gyeonggi/", []),
    ("권역별 안내", "/gyeonggi/", [
        ("경기남부", "/gyeonggi/zone/south/"),
        ("경기북부", "/gyeonggi/zone/north/"),
        ("경기서부", "/gyeonggi/zone/west/"),
        ("경기동부", "/gyeonggi/zone/east/"),
        ("경기외곽", "/gyeonggi/zone/outer-area/"),
    ]),
    ("시군별 안내", "/gyeonggi/", [
        ("수원", "/gyeonggi/suwon/"),
        ("성남", "/gyeonggi/seongnam/"),
        ("용인", "/gyeonggi/yongin/"),
        ("고양", "/gyeonggi/goyang/"),
        ("화성", "/gyeonggi/hwaseong/"),
        ("부천", "/gyeonggi/bucheon/"),
        ("안산", "/gyeonggi/ansan/"),
        ("안양", "/gyeonggi/anyang/"),
        ("김포", "/gyeonggi/gimpo/"),
        ("남양주", "/gyeonggi/namyangju/"),
        ("의정부", "/gyeonggi/uijeongbu/"),
        ("하남", "/gyeonggi/hanam/"),
    ]),
    ("예약 안내", "/gyeonggi/reservation/", []),
    ("이용 전 확인사항", "/gyeonggi/check/", []),
    ("고객센터", "/gyeonggi/support/", [
        ("개인정보처리방침", "/gyeonggi/privacy/"),
    ]),
]
