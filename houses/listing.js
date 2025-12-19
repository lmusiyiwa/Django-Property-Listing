// listing.js - tabs, modal gallery, hero thumb click, sticky header

document.addEventListener('DOMContentLoaded', function () {

  // Tabs behavior
  const tabs = document.querySelectorAll('.tab');
  tabs.forEach(t => t.addEventListener('click', function() {
    tabs.forEach(x => x.classList.remove('active'));
    this.classList.add('active');
    const target = this.dataset.tab;
    document.querySelectorAll('.gallery').forEach(g => g.classList.remove('active'));
    const el = document.getElementById(target);
    if (el) el.classList.add('active');
    // scroll to gallery
    el && el.scrollIntoView({behavior:'smooth', block:'start'});
  }));

  // Hero small thumbnails click -> change main hero image
  document.querySelectorAll('.thumb-sm').forEach(thumb => {
    thumb.addEventListener('click', function() {
      const src = this.dataset.src || this.src;
      const hero = document.getElementById('heroImage');
      if (hero) hero.src = src;
    });
  });

  // Modal
  const modal = document.getElementById('modal');
  const modalImg = document.getElementById('modalImg');
  const modalThumbs = document.querySelectorAll('.modal-thumb');
  const showAllBtn = document.getElementById('showAll');
  const closeBtn = document.getElementById('modalClose');
  let currentIndex = 0;
  // collect all modal thumb srcs
  const modalSrcs = Array.from(modalThumbs).map(t => t.dataset.src || t.src);

  function openModal(index) {
    if (!modal) return;
    modal.style.display = 'flex';
    currentIndex = index || 0;
    modalImg.src = modalSrcs[currentIndex];
    highlightActiveThumb();
    document.body.style.overflow = 'hidden';
  }
  function closeModal() {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
  function highlightActiveThumb() {
    modalThumbs.forEach((t,i) => {
      t.classList.toggle('active', i === currentIndex);
    });
  }
  function showNext(n) {
    currentIndex = (currentIndex + n + modalSrcs.length) % modalSrcs.length;
    modalImg.src = modalSrcs[currentIndex];
    highlightActiveThumb();
  }

  if (showAllBtn) showAllBtn.addEventListener('click', () => openModal(0));
  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  document.getElementById('prevSlide')?.addEventListener('click', () => showNext(-1));
  document.getElementById('nextSlide')?.addEventListener('click', () => showNext(1));

  modalThumbs.forEach((thumb, idx) => {
    thumb.addEventListener('click', function() {
      currentIndex = idx;
      modalImg.src = this.dataset.src || this.src;
      highlightActiveThumb();
    });
  });

  // close modal on background click
  modal.addEventListener('click', function(e) {
    if (e.target === modal) closeModal();
  });

  // Sticky header on scroll
  const sticky = document.getElementById('stickyHeader');
  const showStickyAfter = 250;
  window.addEventListener('scroll', () => {
    if (!sticky) return;
    if (window.scrollY > showStickyAfter) {
      sticky.style.display = 'block';
    } else {
      sticky.style.display = 'none';
    }
  });

});
