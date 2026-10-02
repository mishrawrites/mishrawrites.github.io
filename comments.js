// Giscus comments for every Monoblog post.
// One-time setup: paste the two IDs from https://giscus.app below, then push this file.
(function () {
  var REPO_ID = "PASTE_REPO_ID";         // looks like R_kgDO...
  var CATEGORY_ID = "PASTE_CATEGORY_ID"; // looks like DIC_kwDO...

  var host = document.querySelector(".giscus");
  if (!host) return;
  if (REPO_ID.indexOf("PASTE") === 0 || CATEGORY_ID.indexOf("PASTE") === 0) {
    host.innerHTML = '<p class="comment-note">Comments open soon.</p>';
    return;
  }
  var s = document.createElement("script");
  s.src = "https://giscus.app/client.js";
  s.async = true;
  s.crossOrigin = "anonymous";
  var attrs = {
    "data-repo": "mishrawrites/mishrawrites.github.io",
    "data-repo-id": REPO_ID,
    "data-category": "Announcements",
    "data-category-id": CATEGORY_ID,
    "data-mapping": "pathname",
    "data-strict": "1",
    "data-reactions-enabled": "1",
    "data-emit-metadata": "0",
    "data-input-position": "top",
    "data-theme": "https://mishrawrites.com/giscus-theme.css",
    "data-lang": "en",
    "data-loading": "lazy"
  };
  for (var k in attrs) s.setAttribute(k, attrs[k]);
  host.appendChild(s);
})();
