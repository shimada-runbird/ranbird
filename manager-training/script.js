(function () {
  var deck = document.getElementById("deck");
  var navContainer = document.getElementById("navLinks");
  var progress = document.getElementById("progress");
  if (!deck) return;

  var slides = deck.querySelectorAll(".slide");
  var total = slides.length;

  slides.forEach(function (slide, i) {
    var num = String(i + 1).padStart(2, "0");
    slide.setAttribute("data-slide", num);
    var title = slide.getAttribute("data-title") || num;
    if (navContainer) {
      var a = document.createElement("a");
      a.href = "#" + slide.id;
      a.textContent = title;
      navContainer.appendChild(a);
    }
  });

  var navLinks = navContainer ? navContainer.querySelectorAll("a") : [];

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        var id = entry.target.id;
        navLinks.forEach(function (link) {
          link.classList.toggle("is-active", link.getAttribute("href") === "#" + id);
        });
        var num = entry.target.getAttribute("data-slide");
        if (progress && num) {
          progress.textContent = num + " / " + String(total).padStart(2, "0");
        }
      });
    },
    { threshold: 0.35, rootMargin: "-120px 0px -20% 0px" }
  );

  slides.forEach(function (slide) {
    observer.observe(slide);
  });

  if (slides[0]) slides[0].classList.add("is-visible");
})();
