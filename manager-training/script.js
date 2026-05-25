(function () {
  var slides = document.querySelectorAll(".slide");
  var navLinks = document.querySelectorAll(".deck-nav__links a");
  var progress = document.getElementById("slide-progress");

  if (!slides.length) return;

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          var id = entry.target.id;
          navLinks.forEach(function (link) {
            link.classList.toggle("is-active", link.getAttribute("href") === "#" + id);
          });
          var num = entry.target.getAttribute("data-slide");
          if (progress && num) {
            progress.textContent = num + " / " + slides.length;
          }
        }
      });
    },
    { threshold: 0.35, rootMargin: "-120px 0px -20% 0px" }
  );

  slides.forEach(function (slide) {
    observer.observe(slide);
  });

  if (slides[0]) {
    slides[0].classList.add("is-visible");
  }

  var copyBtn = document.getElementById("copy-url-btn");
  var urlEl = document.getElementById("public-url");
  if (copyBtn && urlEl && navigator.clipboard) {
    copyBtn.addEventListener("click", function () {
      navigator.clipboard.writeText(urlEl.href).then(function () {
        copyBtn.textContent = "コピーしました";
        setTimeout(function () {
          copyBtn.textContent = "URLをコピー";
        }, 2000);
      });
    });
  }
})();
