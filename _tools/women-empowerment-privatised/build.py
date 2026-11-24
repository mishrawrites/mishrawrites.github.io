"""Build the 'Women Empowerment! Privatised.' e-book for the site.
python3 _tools/women-empowerment-privatised/build.py
Reads book.html (the same source as the claude.ai artifact), writes:
  monoblog/women-empowerment-privatised/index.html  (web version, site chrome)
  _tools/women-empowerment-privatised/_print.html  (book only, for the PDF render: see pdf.js)"""
import html, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'women-empowerment-privatised'
URL = f'https://mishrawrites.com/monoblog/{SLUG}/'
PDF = f'{SLUG}.pdf'
TITLE = 'Women Empowerment! Privatised.'
DEK = "Brands that tried, and brands that made a difference. A storyteller's viewpoint."
DESC = ('A free e-book for founders and brand leaders: eleven Indian brand stories on women, '
        'what the evidence says, a playbook for women\'s health brands, and a toolkit of free data most teams never open.')
DATE = '2026-11-24'
E = html.escape
book = open(os.path.join(HERE, 'book.html'), encoding='utf8').read()
book = re.sub(r'^<title>.*?</title>\s*<meta name="claude:viewport-fit-sides"[^>]*>\s*', '', book, flags=re.S)
style_end = book.index('</style>') + len('</style>')
book_head, book_body = book[:style_end], book[style_end:]

SITE_CSS = '''
.site{max-width:820px;margin:0 auto 18px;display:flex;justify-content:space-between;align-items:center;gap:12px;padding:0 16px}
.brandmark{white-space:nowrap;font-family:var(--display);font-weight:700;font-size:18px;color:var(--maroon);text-decoration:none}
.brandmark i{color:var(--copper);font-style:normal}
.topnav{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.topnav a{font-family:var(--label);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);text-decoration:none}
.topnav a:hover{color:var(--copper)}.topnav a.crumb{color:var(--maroon)}
.topnav a.cta{background:var(--copper);color:#fff;padding:8px 12px;border-radius:3px}
.dl{max-width:820px;margin:0 auto 28px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;background:var(--paper);border:1px solid var(--line);padding:14px 18px;box-shadow:0 10px 30px rgba(60,40,20,.08)}
.dl p{margin:0;font-size:.9rem;line-height:1.45;color:var(--soft)}.dl p b{color:var(--maroon)}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--maroon);color:#fff;text-decoration:none;font-family:var(--label);font-weight:700;font-size:.78rem;letter-spacing:.06em;padding:11px 16px;border-radius:999px}
.btn:hover{background:var(--copper)}
.btn.ghost{background:transparent;color:var(--maroon);border:1.5px solid var(--maroon)}
.next{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.related{max-width:820px;margin:0 auto;padding:8px 16px 0}
.related h2{font-size:1.3rem;margin:0 0 12px}
.related-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.related a{display:block;border:1px solid var(--ink);padding:14px 16px;text-decoration:none;color:var(--ink);background:var(--paper)}
.related a:hover{background:var(--ink);color:#fff}
.related .k{display:block;font-family:var(--label);font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:6px}
.related .t{display:block;font-weight:600;font-size:15px;line-height:1.35}
.sitefoot{max-width:820px;margin:24px auto 0;padding:18px 16px 36px;border-top:1px solid #d6cab4;font-size:13px;color:var(--soft);display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}
.sitefoot a{color:var(--maroon)}
.topnav{flex-wrap:nowrap}
@media (max-width:700px){body{padding-top:14px}.topnav{gap:10px}.topnav a{font-size:11px}.topnav a:not(.crumb):not(.cta){display:none}.dl{margin:0 0 12px;box-shadow:none}.related-grid{grid-template-columns:1fr}}
@media print{.site,.dl,.related,.sitefoot,.next{display:none}}
'''
DL_ICON = '<svg class="ico"><use href="#i-doc"/></svg>'
dl = (f'<div class="dl"><p><b>Free to read here, free to keep.</b> No form, no email. '
      f'Download the PDF to read offline or pass it on.</p>'
      f'<a class="btn" href="{PDF}" download>{DL_ICON}Download the PDF</a></div>')
nxt = ('<div class="next">'
       f'<a class="btn" href="{PDF}" download>{DL_ICON}Download the PDF</a>'
       '<a class="btn ghost" href="mailto:gaurav@mishrawrites.com?subject=Send%20me%20the%20next%20one">'
       '<svg class="ico"><use href="#i-mail"/></svg>Want the next one? Write to me</a></div>')

web_body = book_body
# site version: drop the book's own end footer, add download + next-one buttons after the closing line
web_body = re.sub(r'<footer class="page end">.*?</footer>', '', web_body, flags=re.S)
closer = 'And now you know the difference.</p>'
assert closer in web_body
web_body = web_body.replace('<p class="closer">Spend a weekend', '<p class="closer">Spend a weekend', 1)
tk_end = 'you will know exactly what to ask it.</p>'
assert tk_end in web_body
web_body = web_body.replace(tk_end, tk_end + nxt, 1)
cover_end = web_body.index('</header>') + len('</header>')
web_body = web_body[:cover_end] + '\n' + dl + web_body[cover_end:]

ld = ('{"@context":"https://schema.org","@type":"Book","name":"%s","description":"%s","datePublished":"%s",'
      '"author":{"@type":"Person","name":"Gaurav Mishra","url":"https://mishrawrites.com/"},"url":"%s","isAccessibleForFree":true,"inLanguage":"en-IN"}'
      % (TITLE, E(DESC), DATE, URL))
head = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{TITLE} · Monoblog · Gaurav Mishra</title>
<meta name="description" content="{E(DESC)}">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="article"><meta property="og:site_name" content="Gaurav Mishra">
<meta property="og:title" content="{TITLE}"><meta property="og:description" content="{E(DEK)} A free e-book.">
<meta property="og:url" content="{URL}"><meta property="og:image" content="https://mishrawrites.com/media/og/{SLUG}.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{TITLE} {E(DEK)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{TITLE}"><meta name="twitter:description" content="{E(DESC)}"><meta name="twitter:image" content="https://mishrawrites.com/media/og/{SLUG}.png">
<script type="application/ld+json">{ld}</script>
<link href="/favicon.ico" rel="icon" sizes="any"><link href="/favicon.svg" rel="icon" type="image/svg+xml"><link href="/apple-touch-icon.png" rel="apple-touch-icon">
'''
site_top = ('<div class="site"><a class="brandmark" href="/">Gaurav Mishra<i>.</i></a><nav class="topnav" aria-label="Site">'
            '<a href="/#work">Work</a><a class="crumb" href="/monoblog/" aria-current="page">Monoblog</a>'
            '<a href="/Gaurav-Mishra-CV.pdf">CV</a><a class="cta" href="/#contact">Let\'s talk</a></nav></div>')
related = ('<section class="related" aria-label="Keep reading"><h2>Keep reading</h2><div class="related-grid">'
           '<a href="/monoblog/sifaarish-evolution-of-influencing/"><span class="k">Monoblog</span><span class="t">Sifaarish</span></a>'
           '<a href="/monoblog/they-sold-you-an-automatic-door/"><span class="k">Monoblog</span><span class="t">They Sold You an Automatic Door</span></a>'
           '<a href="/#work"><span class="k">The work</span><span class="t">Case studies and projects, numbers attached</span></a>'
           '</div></section>'
           '<footer class="sitefoot"><span>Gaurav Mishra · <a href="/monoblog/">Monoblog</a></span>'
           '<span><a href="/#work">The work</a> · <a href="/">mishrawrites.com</a></span></footer>')
web = (head + book_head.replace('</style>', SITE_CSS + '</style>') + '</head>\n<body>\n' + site_top + web_body + related +
       '\n<script async data-goatcounter="https://mishrawrites.goatcounter.com/count" src="//gc.zgo.at/count.js"></script>\n</body></html>\n')
out = os.path.join(ROOT, 'monoblog', SLUG, 'index.html')
open(out, 'w', encoding='utf8').write(web)

# print version: book only (its own footer kept), assets resolved from the site folder
pr = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>{TITLE}</title><base href="file://{os.path.join(ROOT, "monoblog", SLUG)}/">' + book_head +
      '<style>@page{size:820px 1160px;margin:0}body{padding:0;background:#fff}.page{margin:0;box-shadow:none}#src{break-after:auto}</style></head><body>' + book_body + '</body></html>')
open(os.path.join(HERE, '_print.html'), 'w', encoding='utf8').write(pr)
print('wrote', out)
