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

# ---- print edition (A4). Three parts, merged by pdf.js: cover, body (running footer), back cover.
BASE = f'<base href="file://{os.path.join(ROOT, "monoblog", SLUG)}/">'
PRINT_CSS = """
@page{size:A4;margin:16mm 15mm 17mm}
html{font-size:11.5px}
body{background:#fff;padding:0;font-size:11.4px;line-height:1.55;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{max-width:none;margin:0;box-shadow:none;overflow:visible;break-before:page;background:#fff}
.in{padding:0}
.part{height:262mm;min-height:0;aspect-ratio:auto;border-radius:6px;overflow:hidden;background:var(--maroon)}
.part .in{padding:16mm 14mm}
.part .big{font-size:9rem}
.chap .in{padding-top:9mm}
.opener{padding:0}
.frame img{aspect-ratio:auto;height:68mm;object-fit:cover}
.fig img{height:46mm;object-fit:cover}.fig{margin:12px 0}
.stats{gap:8px;margin:4px 0 12px}.stat{padding:12px}.stat b{font-size:1.9rem}.chart{padding:12px 14px 6px;margin:10px 0 14px}.bar{margin:6px 0}.track{height:22px}
.tool{padding:9px 12px;gap:10px}.tool p{font-size:.8rem;margin:2px 0 4px;line-height:1.4}.tools{gap:7px}.tg{margin:12px 0 7px}
.cat{padding:10px}.cats{gap:8px;margin:10px 0 14px}.cat span{font-size:.72rem}
h3{margin:20px 0 8px}
#t2 .frame img{height:52mm}#t2 .fig img{height:34mm}
.mini img{height:28mm}
.receipt{padding:10px 14px;margin:14px 0}.lesson{padding:12px 16px;margin:14px 0}.lesson p{font-size:1.15rem}
p{margin:0 0 .8em}.meta{margin-bottom:12px}.logos{margin:-4px 0 14px;padding:8px 0}.lg{height:40px}.lg img{height:28px}
.chap h2{margin:4px 0 4px}
.num{left:14px;bottom:-28px;font-size:5.6rem;text-shadow:0 3px 0 #fff,0 -3px 0 #fff,3px 0 0 #fff,-3px 0 0 #fff}
.artboard{aspect-ratio:auto;height:68mm}
h2{font-size:2.3rem}.chap h2{font-size:2.1rem}
.receipt,.lesson,.tool,.cat,.rung,.billc,.thread,.rules li,.stat,.fig,.mini a,.logos,.grade,.who>div,.tear,.order,.chart,.mine,.closer,.author,.toc li,.parts,tr,.bar,.ladder,.heckle{break-inside:avoid}
h2,h3,h4,.tg,.eyebrow,.meta,.climb,.thead{break-after:avoid}
p{orphans:3;widows:3}
.tablewrap{overflow:visible}
.watch a{padding:6px 11px;font-size:.72rem}
#toolkit .tools{gap:8px}
.toc li:last-child:nth-child(odd){grid-column:1/-1}
"""
def doc(body, extra):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{TITLE}</title>' + BASE + book_head + '<style>' + extra + '</style></head><body>' + body + '</body></html>')
cover_html = re.search(r'<header class="page cover">.*?</header>', book_body, re.S).group(0)
sprite = re.search(r'<svg width="0" height="0".*?</svg>', book_body, re.S).group(0)
body_only = re.sub(r'<header class="page cover">.*?</header>', '', book_body, flags=re.S)
body_only = re.sub(r'<footer class="page end">.*?</footer>', '', body_only, flags=re.S)
COVER_CSS = """@page{size:A4;margin:0}html,body{margin:0;padding:0;background:#4A0E0E;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cover{width:210mm;height:297mm;min-height:0;aspect-ratio:auto;margin:0;box-shadow:none;display:flex;flex-direction:column}
.mosaic{padding:6mm 6mm 0;gap:3mm}.cover-in{padding:0 16mm 18mm;margin-top:auto}
.cover h1{font-size:5.2rem}.cover .sub{font-size:1.6rem}.cover .by{font-size:1rem;margin-top:10mm}
.free{display:inline-block;margin-top:6mm;font-family:var(--label);font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#4A0E0E;background:var(--gold);padding:6px 12px;border-radius:3px}"""
cover_print = cover_html.replace('<div class="by">', '<span class="free">Free e-book · 2026</span><div class="by">')
BACK = f"""<section class="back"><div class="bk">
<div class="eyebrow">Thanks for reading</div>
<p class="t">{TITLE}</p>
<div class="who2"><div class="mono">GM</div><div><b>Gaurav Mishra</b><span>Brand &amp; product strategist · open to senior roles in brand, marketing and growth</span></div></div>
<p class="c">gaurav@mishrawrites.com<br>+91 73878 88951</p>
<p class="site">mishrawrites.com</p>
<p class="small">Read it online, with every film and source linked:<br>mishrawrites.com/monoblog/women-empowerment-privatised</p>
<p class="small">Free to share. Please credit mishrawrites.com.</p></div></section>"""
BACK_CSS = """@page{size:A4;margin:0}html,body{margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.back{width:210mm;height:297mm;background:#4A0E0E;color:#F6E9D6;display:flex;align-items:flex-end}
.bk{padding:0 18mm 22mm}.back .eyebrow{color:var(--gold)}
.back .t{font-family:var(--display);font-weight:800;font-size:2.6rem;line-height:1.05;color:#fff;margin:6mm 0 12mm;max-width:14ch}
.who2{display:flex;gap:14px;align-items:center}.who2 .mono{width:64px;height:64px;border-radius:50%;background:var(--gold);color:#4A0E0E;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.4rem}
.who2 b{display:block;color:#fff;font-size:1.3rem}.who2 span{display:block;font-size:.95rem;color:#E9D7B5;max-width:42ch}
.back .c{font-size:1.05rem;margin:9mm 0 2mm;line-height:1.6}
.back .site{font-family:var(--display);font-weight:800;font-size:2.4rem;color:var(--gold);margin:4mm 0 8mm}
.back .small{font-size:.82rem;color:#D9C7A8;margin:0 0 3mm}"""
open(os.path.join(HERE, '_print_cover.html'), 'w', encoding='utf8').write(doc(sprite + cover_print, COVER_CSS))
open(os.path.join(HERE, '_print_body.html'), 'w', encoding='utf8').write(doc(body_only, PRINT_CSS))
open(os.path.join(HERE, '_print_back.html'), 'w', encoding='utf8').write(doc(BACK, BACK_CSS))
print('wrote', out)
