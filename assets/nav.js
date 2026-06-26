// 모바일 네비게이션 토글
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      nav.classList.toggle('open');
      toggle.classList.toggle('open');
      toggle.setAttribute('aria-expanded', toggle.classList.contains('open'));
    });

    // 링크 클릭 시 메뉴 닫기
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });

    // 뷰포트 크기 변경 시 메뉴 초기화
    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        nav.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }
});
