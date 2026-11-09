# CLAUDE.md

Personal site of Gaurav Mishra (mishrawrites.com). Plain HTML, CSS and JS served by GitHub Pages from `main`. There is no build step, framework or package.json. Anything merged to `main` goes live.

## Map

- `index.html`: the whole home page (~77 KB). Don't read it in full: grep for what you need, then read that line range.
  - Sections are marked by comments: `HERO`, `BRANDS`, `HUSTLE`, `PROBLEMS I SOLVE`, `WORK CAROUSEL`, `CAREER IN A SNAP`, `ABOUT + CREDENTIALS`, `VOICES`, `CONTACT`, `ENQUIRY MODAL`.
  - Most content lives in JS data near the bottom: `PERSONAS`, `HERO`, `PROBLEMS`, `PROBLEM_ORDER`, `LOGO_W`, `WORK` (case-study and project cards), `ORDER` (card order per persona), `VOICES` (LinkedIn testimonials), `FN` (function bars). Change the data, not the render functions.
  - Personas: `none`, `founder`, `marketing`, `talent`, picked on the page or set with `/?for=` (aliases: ceo, cmo, brand, hr, ta, recruiter) and an optional `&co=CompanyName`.
- `monoblog/`: the blog. `monoblog/index.html` lists posts; each post is `monoblog/<slug>/index.html`, a self-contained page.
- `_cv/cv.html`: source for `Gaurav-Mishra-CV.pdf` (root). Rebuild: `node _cv/build-pdf.js "$PWD/_cv/cv.html" "$PWD/Gaurav-Mishra-CV.pdf"`. The CV must stay at two pages.
- `404.html`: redirects old URLs (old blog posts, case studies) to their new home. Update its map when a URL moves.
- `digitalpaani-booth/`: unlisted concept page. noindex, linked from nowhere. Keep it that way.
- `_archive/`: the old site. Folders starting with `_` are not published. Ignore unless asked.
- `media/`: card stills (`.webp`, `.jpg` fallback where present). `media/og/<slug>.png`: 1200x630 share images.
- Root `*-dark.png` / `*-white.png`: brand logos. White versions are used on image-less cards via `LOGO_W`.
- `comments.js` + `giscus-theme.css`: Giscus comments on posts. `sitemap.xml`, `robots.txt`, `CNAME`: leave alone unless the task needs them.

## Brand

- Colours: ink `#1A1A1D`, maroon `#4A0E0E`, gold `#C9A44C`, rust/copper `#AE611C`, white `#FFFFFF`. Tints of these only, no new hues (charts included).
- Fonts: Poppins for headings, Montserrat for body (Google Fonts).
- Copy: plain, specific, numbers attached.

## Recipes

**New work card:** add an object to `WORK` (id, co, yr, type "Case study" or "Project", img, optional v for a video link, fn, title, problem, m/ml metric, `h` lines for founder/marketing/talent). Then add its id to all four lists in `ORDER`, or it won't show.

**New Monoblog post:** copy the latest post folder as the template. Update title, canonical, description, og/twitter tags, JSON-LD `datePublished`, the byline date and read time. Make `media/og/<slug>.png` (1200x630, brand style). Add a `blog-card` to `monoblog/index.html` (newest first, `data-date`), add the URL to `sitemap.xml`, and refresh "Keep reading" links. Keep `comments.js` and GoatCounter tags.

**CV change:** edit `_cv/cv.html`, rebuild the PDF, check it's still two pages, commit both files.

## Integrations

- Forms: Web3Forms (`FORM_KEY` in `index.html`).
- Analytics: GoatCounter. Persona picks and card clicks are sent as events via `track()`.
- Comments: Giscus on this repo's Discussions ("Announcements").

## Working rules

- "Preview, not yet live" means the change is on a branch and not merged to `main`.
- Check visual changes with Playwright screenshots (Chromium is installed in cloud sessions) at phone (390px) and desktop widths.
- Commit messages: a short plain-English title, then what changed and why.
