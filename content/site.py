# 안산시 출장마사지 사이트 공통 설정

BASE_URL = "https://ansan-massage1.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "간"  # 헤더 로고 원형 마크 글자
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시
NAV = [
    ("안산", "/", []),
    ("구별 안내", "/", [
        ("상록구", "/sangnok-gu/"),
        ("단원구", "/danwon-gu/"),
    ]),
    ("지역별 안내", "/", [
        ("중앙동", "/danwon-gu/jungang-dong/"),
        ("고잔동", "/danwon-gu/gojan-dong/"),
        ("초지동", "/danwon-gu/choji-dong/"),
        ("원곡동", "/danwon-gu/wongok-dong/"),
        ("선부동", "/danwon-gu/seonbu-dong/"),
        ("본오동", "/sangnok-gu/bono-dong/"),
        ("사동", "/sangnok-gu/sa-dong/"),
        ("월피동", "/sangnok-gu/wolpi-dong/"),
    ]),
    ("역세권 안내", "/", [
        ("상록수역", "/station/sangnoksu-station/"),
        ("한대앞역", "/station/hanyang-univ-at-ansan-station/"),
        ("중앙역", "/station/jungang-station/"),
        ("고잔역", "/station/gojan-station/"),
        ("초지역", "/station/choji-station/"),
        ("안산역", "/station/ansan-station/"),
        ("선부역", "/station/seonbu-station/"),
        ("원곡역", "/station/wongok-station/"),
        ("원시역", "/station/wonsi-station/"),
    ]),
    ("생활권 안내", "/", [
        ("중앙역·고잔", "/area/jungang-gojan/"),
        ("초지역·초지동", "/area/choji-dong/"),
        ("안산역·원곡동", "/area/ansan-station-wongok/"),
        ("상록수·본오", "/area/sangnoksu-bono/"),
        ("선부역·선부동", "/area/seonbu-station/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/check/", []),
    ("고객센터", "/support/", [
        ("개인정보처리방침", "/support/privacy/"),
    ]),
]
