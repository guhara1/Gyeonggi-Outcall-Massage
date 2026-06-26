#!/usr/bin/env python3
"""IndexNow 일괄 색인 통보 — 빙·네이버·얀덱스 등에 즉시 통보.

사용법:
    python3 tools/indexnow.py            # sitemap.xml의 모든 URL 통보
    python3 tools/indexnow.py URL [URL]  # 지정한 URL만 통보(글 1건 올렸을 때)

키/도메인은 content/site.py(BASE_URL, INDEXNOW_KEY)에서 읽습니다.
키 파일(https://<도메인>/<KEY>.txt)이 배포되어 있어야 통보가 수락됩니다.
참고: 구글은 IndexNow에 참여하지 않습니다(구글은 sitemap + Search Console 사용).
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

# IndexNow 수신 엔드포인트 (하나만 보내도 참여 엔진끼리 공유되지만, 안전하게 다중 통보)
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]


def sitemap_urls():
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>([^<]+)</loc>", f.read())


def notify(urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"  {ep} → HTTP {r.status}")
        except Exception as e:  # noqa: BLE001
            print(f"  {ep} → 실패: {e}")


def main():
    urls = sys.argv[1:] or sitemap_urls()
    if not urls:
        print("통보할 URL이 없습니다. 먼저 python3 build.py 를 실행하세요.")
        return
    print(f"IndexNow 통보 — {len(urls)}개 URL (host={HOST}, key={INDEXNOW_KEY[:8]}…)")
    # IndexNow 1회 요청 최대 10,000 URL
    for i in range(0, len(urls), 10000):
        notify(urls[i:i + 10000])
    print("완료. 키 파일이 배포되어 있어야 수락됩니다:", KEY_LOCATION)


if __name__ == "__main__":
    main()
