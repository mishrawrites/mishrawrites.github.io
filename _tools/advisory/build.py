"""Build /advisory/ from content.py and a manifest of source images.
Usage: python3 build.py <manifest.json>
manifest: {"items": {slug: [[src_path, caption], ...]}, "tags": {slug: [advisory tags]}, "cover": {slug: src_path}}
"""
import json, os, sys, html, math, shutil
from PIL import Image, ImageChops, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import BRANDS, SECTION, ROLE, ALSO
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
M = json.load(open(sys.argv[1]))
E = html.escape

def load(p):
    im = Image.open(p)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA'); bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im); im = bg
    return im.convert('RGB')

def trim(im):
    diff = ImageChops.difference(im, Image.new('RGB', im.size, (255, 255, 255))).convert('L').point(lambda x: 255 if x > 12 else 0)
    box = diff.getbbox()
    if not box: return im
    pad = int(max(im.size) * 0.03); l, t, r, b = box
    return im.crop((max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad)))

def cover_from(im, out):
    C = 800; inner = int(C * 0.8); im = trim(im); im.thumbnail((inner, inner), Image.LANCZOS)
    if max(im.size) < inner:
        f = inner / max(im.size); im = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
    cv = Image.new('RGB', (C, C), (255, 255, 255)); cv.paste(im, ((C - im.width) // 2, (C - im.height) // 2))
    cv.save(out, 'WEBP', quality=80, method=6)

def text_cover(name, out):
    C = 800; cv = Image.new('RGB', (C, C), (246, 243, 236)); d = ImageDraw.Draw(cv)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 120)
    except Exception: f = ImageFont.load_default()
    w = d.textlength(name, font=f); d.text(((C - w) / 2, C / 2 - 70), name, font=f, fill=(74, 14, 14))
    cv.save(out, 'WEBP', quality=80)

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta name="robots" content="noindex, nofollow"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&amp;family=Montserrat:wght@500;600&amp;display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/advisory/advisory.css"/>
</head>
<body>
<nav><a class="nav-logo" href="/">Gaurav Mishra</a><a class="nav-link" href="/advisory/">{section}</a></nav>
<main>
'''
FOOT = '''</main>
<footer><a href="/">mishrawrites.com</a><span>gaurav@mishrawrites.com · +91 73878 88951</span></footer>
<dialog id="lb"><img alt=""/><p></p><button aria-label="Close">×</button></dialog>
<script>
const lb=document.getElementById('lb');
document.querySelectorAll('.shot a').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();lb.querySelector('img').src=a.href;lb.querySelector('img').alt=a.dataset.cap;lb.querySelector('p').textContent=a.dataset.cap;lb.showModal();}));
lb.addEventListener('click',()=>lb.close());
</script>
</body>
</html>
'''
GROUPS = [('Dairy', 'Milk, ghee and milk sweets'), ('Bakery', 'Bread, buns and tea-time'), ('Beverages', 'Drinks'),
          ('Snacks', 'Namkeen, chips and farsan'), ('Pantry', 'Pickles, sauces, mixes, oils and sugar'), ('Identity', 'Beyond the pack')]

def score(slug):
    n, g, c, brief, _, scope, url = BRANDS[slug]
    return len(M['tags'].get(slug, [])) + len(scope or []) + len(M['items'].get(slug, [])) / 100

order = sorted(BRANDS, key=lambda s: (-score(s), BRANDS[s][0]))
# clear old brand folders that are no longer listed
adv = f'{REPO}/advisory'
for d in os.listdir(adv):
    if os.path.isdir(f'{adv}/{d}') and d not in BRANDS: shutil.rmtree(f'{adv}/{d}')
for d in os.listdir(f'{REPO}/media/advisory'):
    if d not in BRANDS: shutil.rmtree(f'{REPO}/media/advisory/{d}')

cards = []
for i, slug in enumerate(order):
    name, group, cat, brief, _, scope, url = BRANDS[slug]
    od = f'{REPO}/media/advisory/{slug}'
    if os.path.isdir(od): shutil.rmtree(od)
    os.makedirs(od)
    shots = []
    for j, (src, cap) in enumerate(M['items'].get(slug, []), 1):
        im = trim(load(src)); im.thumbnail((1400, 1400), Image.LANCZOS)
        fn = f'{j:02d}.webp'; im.save(f'{od}/{fn}', 'WEBP', quality=80, method=6)
        th = im.copy(); th.thumbnail((720, 720)); th.save(f'{od}/{j:02d}-sm.webp', 'WEBP', quality=78, method=6)
        shots.append((fn, f'{j:02d}-sm.webp', cap, im.size))
    csrc = M['cover'].get(slug)
    if csrc: cover_from(load(csrc), f'{od}/cover.webp')
    elif shots: cover_from(load(M['items'][slug][0][0]), f'{od}/cover.webp')
    else: text_cover(name, f'{od}/cover.webp')

    def fig(k, big=False):
        fn, sm, cap, sz = shots[k]
        return (f'<figure class="shot"><a href="/media/advisory/{slug}/{fn}" data-cap="{E(cap)}"><img src="/media/advisory/{slug}/{fn if big else sm}" '
                f'alt="{E(name)}: {E(cap)}" loading="lazy" width="{sz[0]}" height="{sz[1]}"/></a><figcaption>{E(cap)}</figcaption></figure>')
    asp = [s[3][0] / s[3][1] for s in shots]
    idx = list(range(len(shots)))
    g = ''
    if shots:
        wide = [k for k in idx if asp[k] >= 1.25]
        lead = max(wide, key=lambda k: asp[k]) if wide and len(shots) > 1 else None
        rest = [k for k in idx if k != lead]
        banners = [k for k in rest if asp[k] >= 1.9]
        others = [k for k in rest if k not in banners]
        if lead is not None:
            g += f'<div class="lead" style="--ar:{round(min(2.7, max(1.33, asp[lead])), 3)}">' + fig(lead, True) + '</div>'
        tail = None
        if len(banners) > 1 and len(banners) % 2 == 1:
            tail = banners.pop()
        if banners:
            cols = 1 if len(banners) == 1 else 2
            g += f'<div class="row cols-{cols} banners" style="--ar:{round(min(2.7, math.exp(sum(math.log(asp[k]) for k in banners) / len(banners))), 3)}">' + ''.join(fig(k, cols == 1) for k in banners) + '</div>'
        if tail is not None:
            g += f'<div class="lead" style="--ar:{round(min(2.7, max(1.33, asp[tail])), 3)}">' + fig(tail, True) + '</div>'
        if others:
            n = len(others)
            cols = {1: 1, 2: 2, 3: 3, 4: 2}.get(n, 3 if n % 3 == 0 else (2 if n % 2 == 0 else 3))
            gm = math.exp(sum(math.log(asp[k]) for k in others) / n)
            g += f'<div class="row cols-{cols}{" solo" if n == 1 else ""}" style="--ar:{round(min(1.33, max(0.75, gm)), 3)}">' + ''.join(fig(k, n == 1) for k in others) + '</div>'
    tags = M['tags'].get(slug, [])
    facts = ''
    if tags: facts += f'<div><dt>Advisory</dt><dd>{E(" · ".join(tags))}</dd></div>'
    if scope: facts += f'<div><dt>Studio scope</dt><dd>{E(" · ".join(scope))}</dd></div>'
    link = f'<p class="case"><a href="{url}" target="_blank" rel="noopener">Full case study at Black Buck Studios →</a></p>' if url else ''
    prev = order[i - 1]; nxt = order[(i + 1) % len(order)]
    count = f'{len(shots)} {"image" if len(shots) == 1 else "images"}' if shots else 'Images to follow'
    body = f'''<header class="brand-head wrap">
<a class="back" href="/advisory/">← All brands</a>
<p class="label">{E(group)} · {E(cat)}</p>
<h1>{E(name)}</h1>
<p class="brief">{E(brief)}</p>
{f'<dl class="facts">{facts}</dl>' if facts else ''}
{link}
<p class="meta">{count}</p>
</header>
{f'<section class="gallery wrap">{g}</section>' if g else ''}
<nav class="pager wrap"><a href="/advisory/{prev}/">← {E(BRANDS[prev][0])}</a><a href="/advisory/{nxt}/">{E(BRANDS[nxt][0])} →</a></nav>
'''
    os.makedirs(f'{adv}/{slug}', exist_ok=True)
    open(f'{adv}/{slug}/index.html', 'w').write(HEAD.format(title=f'{E(name)} · {SECTION} · Gaurav Mishra', desc=E(brief[:150]), section=SECTION) + body + FOOT)
    cards.append((slug, name, group, cat, len(shots)))

present = [gname for gname, _ in GROUPS if any(c[2] == gname for c in cards)]
sec = '<div class="filters wrap" role="group" aria-label="Filter by category"><button class="on" data-f="all">All <span>' + str(len(cards)) + '</span></button>'
for gname in present:
    sec += f'<button data-f="{gname.lower()}">{gname} <span>{sum(1 for c in cards if c[2] == gname)}</span></button>'
sec += '</div>\n<section class="cards wrap">'
for s, n, gname, c, k in cards:
    cnt = f'{k} {"image" if k == 1 else "images"}' if k else 'Images to follow'
    sec += (f'<a class="card" data-g="{gname.lower()}" href="/advisory/{s}/"><span class="thumb"><img src="/media/advisory/{s}/cover.webp" alt="" loading="lazy" width="800" height="800"/></span>'
            f'<span class="ctext"><span class="cgroup">{gname}</span><span class="cname">{E(n)}</span><span class="ccat">{E(c)}</span><span class="ccount">{cnt}</span></span></a>')
sec += '</section>\n'
if ALSO:
    sec += f'<p class="also wrap">Also advised through the studio: {E(" and ".join([", ".join(ALSO[:-1]), ALSO[-1]] if len(ALSO) > 1 else ALSO))}.</p>\n'
total = sum(c[4] for c in cards)
role = E(ROLE).replace('Black Buck Studios', '<a href="https://blackbuckstudios.com/" target="_blank" rel="noopener">Black Buck Studios</a>', 1)
intro = f'''<header class="hero wrap">
<p class="label">{SECTION}</p>
<h1>Packs that have to win on a crowded shelf.</h1>
<p class="brief">{role}</p>
<p class="brief">The brands below are the studio's clients, most of them family-run food businesses in Maharashtra. Each page has a short brief, what the advisory covered and the work the studio team delivered.</p>
<p class="meta">{len(cards)} brands · {total} images</p>
</header>
'''
FILTER = '''
const fb=document.querySelectorAll('.filters button');
function setF(f){fb.forEach(b=>b.classList.toggle('on',b.dataset.f===f));document.querySelectorAll('.card').forEach(c=>c.hidden=!(f==='all'||c.dataset.g===f));}
fb.forEach(b=>b.addEventListener('click',()=>{setF(b.dataset.f);history.replaceState(null,'',b.dataset.f==='all'?location.pathname:'#'+b.dataset.f);}));
if(location.hash)setF(location.hash.slice(1));
'''
open(f'{adv}/index.html', 'w').write(HEAD.format(title=f'{SECTION} · Gaurav Mishra', desc='Brand and packaging advisory for food and FMCG brands, with Black Buck Studios.', section=SECTION)
                                     + intro + sec + FOOT.replace('</script>', FILTER + '</script>'))
print('built', len(cards), 'brands,', total, 'images; order:', ', '.join(order))
