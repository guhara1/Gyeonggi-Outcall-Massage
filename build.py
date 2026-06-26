#!/usr/bin/env python3
"""안산 출장마사지 — 정적 사이트 빌드 스크립트.

content/ 패키지의 페이지 정의를 읽어 정적 HTML을 생성한다.

규칙(자동 적용):
  - 본문 텍스트 2,000자 미만 페이지는 robots noindex 처리
  - sitemap.xml 에는 index 허용 페이지만 포함
"""
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import PAGES
from content.site import (BASE_URL, BRAND, BRAND_MARK, NAV, PHONE,
                          PHONE_DISPLAY, AREA_SERVED, TAGLINE)

ROOT = os.path.dirname(os.path.abspath(__file__))
# Cloudflare Pages가 빌드를 실행하지 않고 저장소 루트를 그대로 배포하므로
# 빌드 결과물을 저장소 루트에 직접 출력한다.
PUBLIC_DIR = ROOT
MIN_INDEX_CHARS = 1300


def text_length(body_html: str) -> int:
    """태그를 제거한 본문 글자수(공백 포함, 연속 공백은 1자).
    공통 요금 블록은 페이지 고유 본문이 아니므로 측정에서 제외한다."""
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def render_nav(current_path: str) -> str:
    items = []
    for label, href, children in NAV:
        active = " is-active" if href == "/" + current_path else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>'
                for c_label, c_href in children
            )
            items.append(
                f'<li class="nav-item has-sub{active}">'
                f'<a href="{href}">{label}</a>'
                f'<ul class="sub-menu">{sub}</ul></li>'
            )
        else:
            items.append(
                f'<li class="nav-item{active}"><a href="{href}">{label}</a></li>'
            )
    return "".join(items)


def render_breadcrumb(crumbs) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumb" aria-label="현재 위치"><ol>']
    parts.append('<li><a href="/">홈</a></li>')
    for label, href in crumbs:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f"<li><span>{label}</span></li>")
    parts.append("</ol></nav>")
    return "".join(parts)


def inject_toc(body: str):
    """본문 섹션(h2)에 id를 보장하고 좌측 목차 데이터를 만든다."""
    items = []
    counter = [0]

    def repl(m):
        attrs, title = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid = idm.group(1)
            opening = f"<section{attrs}>"
        else:
            counter[0] += 1
            sid = f"sec-{counter[0]}"
            opening = f'<section id="{sid}"{attrs}>'
        label = re.sub(r"<[^>]+>", "", title).strip()
        items.append((sid, label))
        return f"{opening}<h2>{title}</h2>"

    body = re.sub(r"<section([^>]*)>\s*<h2>(.*?)</h2>", repl, body, flags=re.S)
    return body, items


def render_toc(items) -> str:
    if len(items) < 3:
        return ""
    links = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label in items
    )
    return (
        '<aside class="page-toc"><nav aria-label="페이지 목차">'
        '<p class="toc-title">목차</p>'
        f"<ul>{links}</ul></nav></aside>"
    )


def _ld(obj: dict) -> str:
    """JSON-LD 스크립트 블록 1개를 만든다."""
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(obj, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )


def make_org_schema() -> dict:
    """사이트 전역 Organization 스키마 (모든 페이지 공통)."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": base + "/#organization",
        "name": BRAND,
        "url": base + "/",
        "logo": base + "/assets/apple-touch-icon.png",
        "image": base + "/assets/og-image.png",
        "telephone": PHONE,
        "areaServed": {"@type": "AdministrativeArea", "name": AREA_SERVED},
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": PHONE,
            "contactType": "reservations",
            "availableLanguage": ["ko"],
            "areaServed": "KR",
        },
    }


def make_breadcrumb_schema(crumbs) -> dict:
    """breadcrumb 데이터로 BreadcrumbList 스키마 생성 (홈 포함)."""
    base = BASE_URL.rstrip("/")
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "홈",
        "item": base + "/",
    }]
    # breadcrumb 데이터의 첫 항목이 루트("/")를 가리키면 홈과 중복되므로 건너뛴다.
    rest = crumbs[1:] if crumbs and crumbs[0][1] == "/" else crumbs
    for i, (label, href) in enumerate(rest, start=2):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = base + href
        items.append(entry)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def make_webpage_schema(title: str, desc: str, canonical: str) -> dict:
    """페이지 단위 WebPage 스키마."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "ko",
        "isPartOf": {"@id": base + "/#organization"},
        "publisher": {"@id": base + "/#organization"},
    }


def render_page(page: dict) -> str:
    path = page["path"]
    title = page["title"]
    desc = page["desc"]
    h1 = page["h1"]
    body = page["body"]
    crumbs = page.get("breadcrumb") or []
    extra_head = page.get("extra_head", "")
    hero = page.get("hero", "")

    chars = text_length(body)
    noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if noindex
        else '<meta name="robots" content="index,follow">'
    )
    canonical = BASE_URL.rstrip("/") + "/" + path

    # 히어로가 있는 페이지(메인)는 H1을 히어로 안에서 출력한다.
    if hero:
        page_head = hero
    else:
        page_head = ""

    h1_html = "" if hero else f"<h1>{h1}</h1>"

    body, toc_items = inject_toc(body)
    toc_html = render_toc(toc_items)
    layout_cls = "page-layout has-toc" if toc_html else "page-layout"

    # 스키마 자동 주입.
    # 메인(hero 보유)은 main.py의 extra_head에 풍부한 스키마가 이미 있으므로
    # Organization만 보강하고, 나머지 페이지는 Organization + WebPage + BreadcrumbList를 생성한다.
    if hero:
        auto_schema = _ld(make_org_schema())
    else:
        blocks = [make_org_schema(), make_webpage_schema(title, desc, canonical)]
        if crumbs:
            blocks.append(make_breadcrumb_schema(crumbs))
        auto_schema = "".join(_ld(b) for b in blocks)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg?v=2">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png?v=2">
<link rel="icon" href="/favicon.ico?v=2" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png?v=2">
<meta name="theme-color" content="#0a1120">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<link rel="stylesheet" href="/assets/style.css">
{auto_schema}{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-accent" aria-hidden="true"></div>
  <div class="header-top">
    <div class="header-inner">
      <a class="brand" href="/gyeonggi/"><span class="brand-mark">{BRAND_MARK}</span> <span class="brand-text">{BRAND}</span></a>
      <p class="header-tagline"><span class="tag-gem">◆</span> {TAGLINE} <span class="tag-gem">◆</span> 24시간 상담</p>
      <a class="header-call" href="tel:{PHONE}"><span class="call-label">예약전화</span> {PHONE_DISPLAY}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <div class="nav-inner"><ul class="nav-list">{render_nav(path)}</ul></div>
  </nav>
</header>
{page_head}<main class="site-main">
  <div class="container {layout_cls}">
    {toc_html}
    <article class="page-content">
      {render_breadcrumb(crumbs)}
      {h1_html}
      {body}
    </article>
  </div>
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-about">
      <p class="footer-brand">{BRAND}</p>
      <p class="footer-desc">경기 전지역 방문 출장마사지·홈타이 안내 사이트입니다. 모든 서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.</p>
      <address class="footer-contact">
        <span class="footer-contact-row"><span class="footer-label">예약전화</span> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></span>
        <span class="footer-contact-row"><span class="footer-label">상담시간</span> 연중무휴 24시간</span>
        <span class="footer-contact-row"><span class="footer-label">서비스 지역</span> 경기 전지역 (남부·북부·서부·동부·외곽)</span>
      </address>
    </div>
    <nav class="footer-col" aria-label="권역·시군 안내">
      <p class="footer-title">권역·시군</p>
      <ul>
        <li><a href="/gyeonggi/">경기 출장마사지·홈타이 생활권 안내</a></li>
        <li><a href="/gyeonggi/zone/south/">경기남부 수원·분당·동탄 생활권</a></li>
        <li><a href="/gyeonggi/zone/north/">경기북부 일산·의정부·다산 생활권</a></li>
        <li><a href="/gyeonggi/zone/west/">경기서부 부천·안산·김포 생활권</a></li>
        <li><a href="/gyeonggi/suwon/">수원 출장마사지 생활권 안내</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="이용 안내">
      <p class="footer-title">이용 안내</p>
      <ul>
        <li><a href="/gyeonggi/reservation/">예약안내</a></li>
        <li><a href="/gyeonggi/check/">이용 전 확인사항</a></li>
        <li><a href="/gyeonggi/support/">고객센터</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="정책 및 기준">
      <p class="footer-title">정책·기관 안내</p>
      <ul>
        <li><a href="/gyeonggi/privacy/">개인정보처리방침</a></li>
        <li><a href="https://www.gg.go.kr/" target="_blank" rel="noopener">경기도청 공식 홈페이지</a></li>
        <li><a href="https://www.pipc.go.kr/" target="_blank" rel="noopener">개인정보보호위원회</a></li>
        <li><a href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow">문의하기</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p class="footer-copy">&copy; {BRAND}. All rights reserved.</p>
      <p class="footer-note">건전한 방문 관리 서비스를 운영하며, 불법적인 요청은 어떤 경우에도 응하지 않습니다.</p>
      <div class="footer-actions">
        <a class="btn-telegram" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="웹사이트 제작문의">📱 웹사이트 제작문의</a>
        <a class="btn-partnership" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="제휴문의">🤝 제휴문의</a>
      </div>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:{PHONE}" aria-label="전화 예약 {PHONE_DISPLAY}">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  <span class="call-fab-label">예약 전화</span>
</a>
<script src="/assets/nav.js"></script>
</body>
</html>
"""


def build() -> None:
    report = []
    sitemap_urls = []

    # public 디렉터리가 없으면 생성
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    for page in PAGES:
        path = page["path"]
        out_dir = os.path.join(PUBLIC_DIR, path)
        os.makedirs(out_dir, exist_ok=True)
        html_out = render_page(page)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        chars = text_length(page["body"])
        noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
        if not noindex:
            sitemap_urls.append(BASE_URL.rstrip("/") + "/" + path)
        report.append((path or "/", chars, "noindex" if noindex else "index"))

    # sitemap.xml
    urls = "\n".join(
        f"  <url><loc>{u}</loc></url>" for u in sitemap_urls
    )
    with open(os.path.join(PUBLIC_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n"
        )

    # robots.txt
    with open(os.path.join(PUBLIC_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {BASE_URL.rstrip('/')}/sitemap.xml\n"
        )

    # .nojekyll (GitHub Pages)
    open(os.path.join(PUBLIC_DIR, ".nojekyll"), "w").close()

    width = max(len(p) for p, _, _ in report)
    print(f"{'PATH'.ljust(width)}  CHARS  ROBOTS")
    for p, c, r in sorted(report):
        flag = "" if (r == "noindex" or MIN_INDEX_CHARS <= c <= 2500) else "  ⚠"
        print(f"{p.ljust(width)}  {str(c).rjust(5)}  {r}{flag}")
    print(f"\n{len(report)} pages built, {len(sitemap_urls)} in sitemap.")


if __name__ == "__main__":
    build()
