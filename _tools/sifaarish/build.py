"""Build the Sifaarish Monoblog post. python3 build.py <out.html> [--preview]
--preview adds a panel to toggle each visual layer and strips site-only parts (comments, analytics)."""
import sys, html
OUT = sys.argv[1]; PREVIEW = '--preview' in sys.argv
SLUG = 'sifaarish-evolution-of-influencing'
URL = f'https://mishrawrites.com/monoblog/{SLUG}/'
TITLE = 'Sifaarish'
DEK = 'Who put in a word for whom. 1917 to this morning.'
DESC = 'Who put in a word for whom, from Bernays and the Four Minute Men to your feed: a short history of borrowed trust, and what it costs when it is called in.'
E = html.escape

# (dateline_big, dateline_small, paragraphs(list), chain(benefits, voucher, believer), artefact_key)
ENTRIES = [
("1917", "Washington", [
 "A government needs a country to want a war. It does not make the argument itself. It recruits seventy-five thousand ordinary men, gives them four minutes each, and sends them into cinemas between reels. Your neighbour, the one who sold you your insurance, stands up and explains why this is necessary. You believe him, because you know him. One of the young men working for the committee behind it is called Edward Bernays. He is twenty-five, and he has just watched the method work on an entire nation."],
 ("A government", "Your neighbour", "A nation"), None),
("1929", "New York", [
 "He is thirty-seven and working for a tobacco company that cannot sell to half the population, because a woman smoking in the street is still a scandal. He hires ten debutantes to walk in the Easter parade and light cigarettes in front of the photographers. He tells the press to call them Torches of Freedom. Not one newspaper mentions Lucky Strike. Smoking among women climbs for the next decade, and every woman climbing believes she thought of it herself."],
 ("A tobacco company", "Ten debutantes", "Every woman watching"), "paper"),
("1946", "An American medical convention", [
 "Free packs are placed in every doctor's hands at the company's booth. As they leave the exhibit hall, a surveyor asks those same doctors which cigarette they smoke. The answer becomes years of advertising. More doctors smoke Camels than any other cigarette. Read it again. Every word of it is true."],
 ("A cigarette brand", "The doctors", "Every smoker"), "ad"),
("1954", "Guatemala City", [
 "A fruit company has a problem with a government that wants its unused land back. The company does not argue about land. It flies American journalists on arranged tours and hands its press office's material to newsrooms. The stories run. A coup follows. The reporters were not paid and most of them were not lying, which is precisely why it worked. Bernays is on the account."],
 ("A fruit company", "American journalists", "American readers"), None),
("1965", "New York", [
 "Bernays publishes his memoirs. In them he records being told that his first book sat on Goebbels' shelf. He does not dwell on it. A technique holds no opinion about who picks it up."],
 ("The technique", "Whoever picks it up", "Anyone listening"), None),
("Every election since", "India", [
 "A country where faith is older than the republic, and where the men who speak for faith are trusted further than anyone who stands for election. So the stage gets shared. A politician sits a little lower than the guru, takes the blessing, touches the feet, and the photograph does the rest. The guru endorses nobody. He has no need to. Tens of millions of people who would never take a politician's word have just watched him vouched for by the one voice in their life that has never had to prove anything. Every party has worked this out. They differ only in how good they are at it, and in how convincingly they call it devotion."],
 ("A politician", "The guru", "Tens of millions"), None),
("Tuesday", "Your phone", [
 "You follow someone. Not a celebrity, just somebody whose taste you rate. They repost a stranger's opinion. You watch it all the way through, which you would not have done had it arrived on its own, and then you repost it yourself. Count who gained. The stranger got an audience they could not have bought. The person you follow got to look discerning at no cost. And the third party, the one in the room the whole time, learned exactly how much longer you watch a thing when someone you trust hands it to you. Bernays had to pay his debutantes. This one got it free, from you, and has been refining the measurement since before you had an account."],
 ("The platform", "Someone you follow", "You"), "phone"),
("This quarter", "A preventive health brand", [
 "Say you sell prevention: full-body checkups, heart scans, early markers, the things nobody books until something frightens them. Your problem is that you are the least believable person in the room on this subject, because you are the one who profits from the fear.",
 "So you stop talking.",
 "You find who your buyer already believes. A thirty-eight-year-old with a desk job and a father on blood pressure tablets does not believe a fitness influencer. He believes the cardiologist who treated his father. He believes the trainer at his gym who has never sold him anything. He believes his company's HR when they email about a health camp, because HR has no reason to lie to him about his own body.",
 "In India, that cardiologist cannot endorse you. The rules do not allow it. He can publish.",
 "So you fund what he would publish anyway. A screening study, run with a hospital's cardiology department, on desk workers under forty. A heart-risk calculator the clinic puts its own name on. The explainer he wanted to write and never had the evening to finish. Free screening camps through company HR, under the hospital's banner, not yours. Put no logo on any of it.",
 "Your name appears once, in the study's acknowledgements, where the people who look will find it and the people who do not will never know to.",
 "Your buyer hears no claim from you. He hears his father's cardiologist say the number matters. Then he goes looking for someone who measures it, and you are standing there with a slot open on Saturday.",
 "That is the 1946 survey, run by somebody who happens to be right. Being right is not the mechanism. It is only the part that lets you sleep."],
 ("A health brand", "His father's cardiologist", "The man at the desk"), "study"),
("Tonight", "Bengaluru", [
 "A brand marketer writes this down. He is not confessing. He has run this on purpose and he is good at it. He knows which lever to pull and which bolt to tighten. He knows which word, put in by which person, in front of which room, will move something, and which will sit there doing nothing at all, and he can do it again for anybody willing to walk that path.",
 "He is also publishing this on a blog that exists, in part, to make strangers trust him enough to hire him.",
 "Both of those are true at the same time. He is not going to pretend otherwise, and he is not going to apologise for knowing how the thing works."],
 ("A brand marketer", "This blog", "Strangers who might hire him"), None),
("Right now", "Wherever you are", [
 "You have read nine of these. Somewhere around the third one you decided this was worth finishing, and that decision was about the person writing it rather than anything written in it. You made it before you had any way to check.",
 "You have not once checked whether a single claim on this page is true."],
 ("The writer", "You", "Whoever you send this to"), None),
]
RULES = [
 "Trust that came from somebody else is still theirs. It goes back when they go down, and it goes back at the speed they fall.",
 "It works only while it looks like nobody was paid. Put a tag on it and it does not soften, it flips, and you end up further behind than saying nothing would have left you.",
 "Nobody checked you. So when the person who vouched falls, there is nothing underneath you, because no one ever looked.",
 "The only thing that stays yours is what you proved while somebody else's name was holding the door. Almost nobody builds that, because the shortcut keeps working.",
]
SOURCES = [
 ("The Four Minute Men and the Committee on Public Information, 1917", "https://daily.jstor.org/the-us-propaganda-machine-of-world-war-i"),
 ("Edward Bernays: the committee's Latin American bureau, Torches of Freedom, United Fruit, his 1965 memoir and the Goebbels story", "https://en.wikipedia.org/wiki/Edward_Bernays"),
 ("Torches of Freedom, Easter Sunday 1929", "https://en.wikipedia.org/wiki/Torches_of_Freedom"),
 ("\"More Doctors Smoke Camels\": the convention surveys", "https://tobacco.stanford.edu/ad_tags/doctor/page/2/"),
 ("The doctors' campaigns and their end in the early 1950s (American Journal of Public Health)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1470496"),
 ("United Fruit, the press tours and the 1954 coup in Guatemala", "https://en.wikipedia.org/wiki/1954_Guatemalan_coup_d%27%C3%A9tat"),
 ("Doctors in India may not endorse products: Indian Medical Council (Professional Conduct, Etiquette and Ethics) Regulations, 2002, clause 6.8.1(h), added 2009", "https://bpni.org/News/Ethics-Regulations-MCI.pdf"),
]

def chain(c, last=False):
    b, v, a = c
    return (f'<div class="chain{" you" if last else ""}" aria-label="Who benefits: {E(b)}. Who puts in the word: {E(v)}. Who believes it: {E(a)}.">'
            f'<div class="node"><span class="role">Benefits</span><b>{E(b)}</b></div><span class="arr" aria-hidden="true"></span>'
            f'<div class="node mid"><span class="role">Puts in the word</span><b>{E(v)}</b></div><span class="arr" aria-hidden="true"></span>'
            f'<div class="node"><span class="role">Believes it</span><b>{E(a)}</b></div></div>')

ART = {
"paper": '''<figure class="art art-paper" data-art="paper"><div class="clip"><div class="mast">New York · Monday, April 1, 1929</div><div class="hl">Group of Girls Puff at Cigarettes as a Gesture of &lsquo;Freedom&rsquo;</div><div class="cols"><i></i><i></i><i></i><i></i><i></i><i></i></div></div><figcaption>The next morning's headline. Count the brand names in it.</figcaption></figure>''',
"ad": '''<figure class="art art-ad" data-art="ad"><div class="ad"><div class="ad-k">According to a nationwide survey</div><div class="ad-h">More doctors smoke <span>Camels</span><br>than any other cigarette</div><div class="ad-f">Asked as they left the exhibit hall, with a free pack in hand</div></div><figcaption>Recreated in type. Every word of it true.</figcaption></figure>''',
"phone": '''<figure class="art art-phone" data-art="phone"><div class="phone"><div class="ph-top"><span></span></div><div class="ph-rep">&#8635; <b>Someone you follow</b> reposted</div><div class="ph-card"><div class="ph-who"><i></i><div><b>A stranger</b><small>2,140 followers</small></div></div><div class="ph-body"><i></i><i></i><i class="s"></i></div><div class="ph-vid"><div class="ph-bar"><span></span></div><small>Watched to the end</small></div></div><div class="ph-you">&#8635; <b>You</b> reposted</div></div><figcaption>The third party saw all of it.</figcaption></figure>''',
"study": '''<figure class="art art-study" data-art="study"><div class="study"><div class="st-k">Department of Cardiology</div><div class="st-h">Cardiometabolic risk in desk workers under forty: a screening study</div><div class="st-a">Results and methods · 24 pages</div><div class="st-lines"><i></i><i></i><i></i><i></i><i class="s"></i></div><div class="st-ack"><b>Acknowledgements.</b> Supported by an unrestricted grant from a preventive health company.</div></div><figcaption>The only place the brand's name appears.</figcaption></figure>''',
}

CSS = r'''
:root{--ink:#1A1A1D;--mar:#4A0E0E;--gold:#C9A44C;--cop:#AE611C;--white:#FFFFFF;--cream:#FFFFFF;--tint:rgba(201,164,76,.12);--line:rgba(201,164,76,.45);--mute:rgba(26,26,29,.72)}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--cream);color:var(--ink);font-family:Montserrat,system-ui,sans-serif;font-size:17px;line-height:1.7}
a{color:var(--cop)}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header.top{display:flex;justify-content:space-between;align-items:center;padding:22px 0}
.brandmark{font-family:Poppins;font-weight:700;font-size:18px;color:var(--mar);text-decoration:none}
.brandmark i{color:var(--cop);font-style:normal}
.topnav{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.topnav a{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);text-decoration:none}
.topnav a:hover{color:var(--cop)}.topnav a.crumb{color:var(--mar)}
.topnav a.cta{background:var(--cop);color:var(--white);padding:8px 12px;border-radius:3px}
.kick{font-size:12px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--mar)}
h1{font-family:Poppins;font-weight:700;font-size:clamp(44px,9vw,84px);line-height:1;color:var(--mar);margin:18px 0 14px;letter-spacing:-1px}
.fs{color:var(--cop)}
.dek{font-size:clamp(17px,2.2vw,20px);color:var(--mute);font-style:italic;max-width:640px}
.meta{margin-top:18px;font-size:13px;color:var(--mute)}.meta b{color:var(--mar)}
h2{font-family:Poppins;font-weight:600;font-size:clamp(24px,3.4vw,32px);line-height:1.2;color:var(--mar);margin:0 0 22px}
p{margin:0 0 18px}
.intro{margin:44px 0 10px;padding-top:30px;border-top:1px solid var(--line)}
.intro .pull{font-family:Poppins;font-weight:600;font-size:clamp(20px,2.8vw,24px);line-height:1.35;color:var(--mar)}
/* entries */
.list{margin:30px 0 0}
.entry{padding:34px 0 10px;border-top:1px solid var(--line)}
.dl{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px;margin-bottom:14px}
.dl .big{font-family:Poppins;font-weight:700;font-size:clamp(26px,4vw,34px);line-height:1.1;color:var(--mar)}
.dl .small{font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--cop)}
/* timeline layer */
body.v-timeline .list{position:relative;padding-left:136px}
body.v-timeline .list:before{content:"";position:absolute;left:114px;top:0;bottom:-90px;width:2px;background:linear-gradient(var(--gold),var(--gold) 85%,transparent)}
body.v-timeline .entry{position:relative;border-top:0;padding-top:26px}
body.v-timeline .entry:before{content:"";position:absolute;left:-28px;top:38px;width:14px;height:14px;border-radius:50%;background:var(--white);border:3px solid var(--cop)}
body.v-timeline .entry.now:before{background:var(--cop);box-shadow:0 0 0 6px rgba(174,97,28,.18)}
body.v-timeline .dl{display:block}
body.v-timeline .dl .big{position:absolute;left:-136px;top:30px;width:96px;text-align:right;font-size:22px}
body.v-timeline .dl .big.long{font-size:13px;line-height:1.25;letter-spacing:.02em}
body.v-timeline .dl .small{display:block;padding-top:6px}
/* chain layer */
.chain{display:none}
body.v-chain .chain{display:grid;grid-template-columns:1fr 26px 1fr 26px 1fr;align-items:stretch;margin:4px 0 26px}
.chain .node{background:var(--white);border:1px solid var(--line);padding:9px 11px;border-radius:3px;min-width:0}
.chain .node b{display:block;font-family:Poppins;font-weight:600;font-size:14px;line-height:1.3;color:var(--ink)}
.chain .role{display:block;font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin-bottom:3px}
.chain .node.mid{background:var(--tint);border-color:var(--gold)}
.chain .node.mid b{color:var(--mar)}
.chain .arr{align-self:center;height:2px;background:var(--cop);position:relative;margin:0 4px}
.chain .arr:after{content:"";position:absolute;right:-1px;top:-4px;border-left:7px solid var(--cop);border-top:5px solid transparent;border-bottom:5px solid transparent}
.chain.you .node.mid{background:var(--mar);border-color:var(--mar)}
.chain.you .node.mid b{color:var(--white)}.chain.you .node.mid .role{color:var(--gold)}
/* artefacts */
.art{display:none;margin:8px 0 30px}
body.v-art-paper .art-paper,body.v-art-ad .art-ad,body.v-art-phone .art-phone,body.v-art-study .art-study{display:block}
figcaption{font-size:13px;color:var(--mute);margin-top:10px}
.clip{background:#F4EEDF;border:1px solid #D8CCAE;padding:20px 24px 22px;max-width:520px;transform:rotate(-.6deg);box-shadow:0 1px 0 #D8CCAE}
.clip .mast{font-family:Georgia,"Times New Roman",serif;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#4a4436;border-bottom:3px double #4a4436;padding-bottom:6px;margin-bottom:12px}
.clip .hl{font-family:Georgia,"Times New Roman",serif;font-weight:700;font-size:clamp(20px,3.2vw,26px);line-height:1.15;color:#1f1b14}
.clip .cols{display:grid;grid-template-columns:1fr 1fr;gap:6px 16px;margin-top:14px}
.clip .cols i{display:block;height:6px;background:#CFC4A8;border-radius:2px}
.ad{background:var(--mar);color:var(--white);padding:26px 26px 22px;max-width:520px;text-align:center;border:6px double var(--gold)}
.ad-k{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.ad-h{font-family:Poppins;font-weight:700;font-size:clamp(22px,3.6vw,30px);line-height:1.15;margin:10px 0 12px;text-transform:uppercase}
.ad-h span{color:var(--gold)}
.ad-f{font-size:12px;font-style:italic;opacity:.85}
.phone{width:280px;max-width:100%;border:10px solid var(--ink);border-radius:30px;background:var(--white);padding:10px 12px 14px;font-size:13px;line-height:1.4}
.ph-top{display:flex;justify-content:center;margin-bottom:8px}.ph-top span{width:70px;height:6px;border-radius:3px;background:var(--ink)}
.ph-rep,.ph-you{color:var(--mute);font-size:12px;padding:4px 2px}
.ph-you{color:var(--cop);font-weight:600;margin-top:6px}
.ph-card{border:1px solid #e5e1d8;border-radius:10px;padding:10px}
.ph-who{display:flex;gap:8px;align-items:center;margin-bottom:8px}.ph-who i{width:30px;height:30px;border-radius:50%;background:#d9d4c7}
.ph-who b{display:block;font-size:13px}.ph-who small{color:var(--mute);font-size:11px}
.ph-body i{display:block;height:6px;border-radius:3px;background:#e7e2d6;margin:6px 0}.ph-body i.s{width:60%}
.ph-vid{margin-top:8px;background:#f3efe6;border-radius:6px;padding:28px 10px 8px}
.ph-bar{height:4px;background:#ddd6c6;border-radius:2px}.ph-bar span{display:block;height:100%;width:100%;background:var(--cop);border-radius:2px}
.ph-vid small{display:block;font-size:11px;color:var(--mute);margin-top:5px}
.study{background:var(--white);border:1px solid #d9d4c7;max-width:420px;padding:26px 26px 18px;box-shadow:6px 6px 0 var(--tint)}
.st-k{font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--mute)}
.st-h{font-family:Georgia,"Times New Roman",serif;font-size:20px;line-height:1.25;margin:8px 0 6px;color:var(--ink)}
.st-a{font-size:12px;color:var(--mute)}
.st-lines{margin:14px 0}.st-lines i{display:block;height:5px;background:#ebe7dd;border-radius:2px;margin:7px 0}.st-lines i.s{width:55%}
.st-ack{font-size:9.5px;line-height:1.4;color:var(--mute);border-top:1px solid #ebe7dd;padding-top:8px}
.st-ack b{color:var(--ink)}
/* live layer */
.live{display:none}
body.v-live .live{display:inline}
body.v-live .static{display:none}
.timer{display:none;margin:0 0 18px;font-size:14px;color:var(--cop);font-weight:600}
body.v-live .timer{display:block}
/* closing */
.rules{background:var(--mar);color:var(--white);padding:34px 30px;margin:44px 0 10px}
.rules h2{color:var(--white)}.rules h2 .fs{color:var(--gold)}
.rules ol{list-style:none;counter-reset:r}
.rules li{counter-increment:r;position:relative;padding-left:46px;margin-bottom:16px}
.rules li:before{content:counter(r,decimal-leading-zero);position:absolute;left:0;top:-1px;font-family:Poppins;font-weight:700;color:var(--gold)}
.closer{font-family:Poppins;font-weight:600;font-size:clamp(20px,2.8vw,24px);color:var(--mar);margin:36px 0 10px}
.sources{border-top:1px solid var(--line);margin-top:40px;padding-top:28px;font-size:14px}
.sources h2{font-size:20px;margin-bottom:12px}
.sources ol{padding-left:20px}.sources li{margin-bottom:8px}
.end{display:flex;justify-content:center;padding:44px 0 20px}.end i{width:18px;height:18px;border-radius:50%;background:var(--cop)}
.comments{border-top:1px solid var(--line);margin-top:40px;padding-top:36px}
.comment-note{font-size:13px;color:var(--mute);margin-top:12px}
.related{border-top:1px solid var(--line);margin-top:40px;padding-top:32px}
.related-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px}
.related a{display:block;border:1px solid var(--ink);padding:16px 18px;text-decoration:none;color:var(--ink);background:var(--white)}
.related a:hover{background:var(--ink);color:var(--white)}
.related .k{display:block;font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:6px}
.related .t{display:block;font-family:Poppins;font-weight:600;font-size:16px;line-height:1.35}
footer{border-top:1px solid var(--line);padding:22px 0 40px;font-size:13px;color:var(--mute);display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}
@media (max-width:760px){
 body{font-size:16px}
 .related-grid{grid-template-columns:1fr}.topnav{gap:12px}.topnav a:not(.crumb):not(.cta){display:none}
 body.v-timeline .list{padding-left:26px}
 body.v-timeline .list:before{left:6px}
 body.v-timeline .entry:before{left:-26px;top:32px}
 body.v-timeline .dl{display:flex}
 body.v-timeline .dl .big{position:static;width:auto;text-align:left;font-size:24px}
 body.v-timeline .dl .big.long{font-size:20px}
 body.v-chain .chain{grid-template-columns:1fr;gap:0}
 .chain .arr{width:2px;height:16px;margin:0 0 0 18px;justify-self:start}
 .chain .arr:after{right:-4px;top:auto;bottom:-1px;border-left:5px solid transparent;border-right:5px solid transparent;border-top:7px solid var(--cop);border-bottom:0}
 .rules{padding:28px 20px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''
PANEL_CSS = r'''
.pv{position:fixed;left:12px;right:12px;bottom:12px;z-index:50;background:var(--ink);color:#fff;border-radius:10px;padding:10px 14px;font-size:13px;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;box-shadow:0 6px 24px rgba(0,0,0,.25);max-width:980px;margin:0 auto}
.pv b{color:var(--gold);font-size:11px;letter-spacing:.14em;text-transform:uppercase;margin-right:4px}
.pv label{display:inline-flex;gap:5px;align-items:center;cursor:pointer;white-space:nowrap}
.pv input{accent-color:var(--gold)}
.pv button{background:none;border:1px solid rgba(255,255,255,.35);color:#fff;border-radius:999px;padding:3px 10px;font:inherit;font-size:12px;cursor:pointer}
body{padding-bottom:110px}
'''
LAYERS = [("v-timeline", "1 Timeline spine"), ("v-chain", "2 Who-vouched diagrams"), ("v-art-paper", "3a 1929 headline"),
          ("v-art-ad", "3b 1946 ad"), ("v-art-phone", "3c Tuesday phone"), ("v-art-study", "3d Study page"), ("v-live", "4 Live 'Right now'")]

entries = ''
for i, (big, small, paras, ch, art) in enumerate(ENTRIES):
    last = i == len(ENTRIES) - 1
    long = ' long' if len(big) > 10 else ''
    if last:
        dl = (f'<div class="dl"><span class="big{long}">Right now</span><span class="small"><span class="static">Wherever you are</span>'
              f'<span class="live"><span data-clock>…</span> · wherever you are</span></span></div>')
    else:
        dl = f'<div class="dl"><span class="big{long}">{E(big)}</span><span class="small">{E(small)}</span></div>'
    body = ''.join(f'<p>{E(p)}</p>' for p in paras)
    if last:
        body = '<p class="timer">You have been on this page for <span data-timer>under a minute</span>.</p>' + body
    entries += f'<article class="entry{" now" if last else ""}">{dl}{chain(ch, last)}{ART.get(art, "") if art else ""}{body}</article>\n'

rules = ''.join(f'<li>{E(r)}</li>' for r in RULES)
sources = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in SOURCES)
words = sum(len(p.split()) for e in ENTRIES for p in e[2]) + sum(len(r.split()) for r in RULES) + 80
mins = max(1, round(words / 220))

LIVE_JS = r'''
(function(){
 var t0=Date.now();
 function fmt(){var c=document.querySelector('[data-clock]');if(c){try{c.textContent=new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})}catch(e){}}
  var s=Math.floor((Date.now()-t0)/1000),m=Math.floor(s/60),el=document.querySelector('[data-timer]');
  if(el){el.textContent=m<1?'under a minute':(m===1?'1 minute':m+' minutes')}}
 fmt();setInterval(fmt,15000);
})();
'''
PANEL_JS = r'''
(function(){
 document.querySelectorAll('.pv input').forEach(function(cb){cb.addEventListener('change',function(){document.body.classList.toggle(cb.value,cb.checked)})});
 document.getElementById('pv-all').addEventListener('click',function(){document.querySelectorAll('.pv input').forEach(function(cb){cb.checked=true;document.body.classList.add(cb.value)})});
 document.getElementById('pv-none').addEventListener('click',function(){document.querySelectorAll('.pv input').forEach(function(cb){cb.checked=false;document.body.classList.remove(cb.value)})});
})();
'''
layers_on = ' '.join(k for k, _ in LAYERS)
panel = ''
if PREVIEW:
    panel = ('<div class="pv" role="group" aria-label="Preview layers"><b>Visual layers</b>' +
             ''.join(f'<label><input type="checkbox" value="{k}" checked> {E(l)}</label>' for k, l in LAYERS) +
             '<button id="pv-all" type="button">All</button><button id="pv-none" type="button">Text only</button></div>')

head = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE} · Monoblog · Gaurav Mishra</title>
<link rel="canonical" href="{URL}">
<meta property="og:type" content="article"><meta property="og:site_name" content="Gaurav Mishra">
<meta property="og:title" content="{TITLE}"><meta property="og:description" content="{E(DESC)}">
<meta property="og:url" content="{URL}"><meta property="og:image" content="https://mishrawrites.com/media/og/{SLUG}.png"><meta content="1200" property="og:image:width"/><meta content="630" property="og:image:height"/><meta content="{TITLE}: {E(DEK)}" property="og:image:alt"/>
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{TITLE}"><meta name="twitter:description" content="{E(DESC)}"><meta name="twitter:image" content="https://mishrawrites.com/media/og/{SLUG}.png">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{TITLE}","description":"{E(DESC)}","datePublished":"2026-11-17","author":{{"@type":"Person","name":"Gaurav Mishra","url":"https://mishrawrites.com/"}},"url":"{URL}"}}</script>
<link href="/favicon.ico" rel="icon" sizes="any"><link href="/favicon.svg" rel="icon" type="image/svg+xml"><link href="/apple-touch-icon.png" rel="apple-touch-icon">
<meta name="description" content="{E(DESC)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>{CSS}{PANEL_CSS if PREVIEW else ''}</style></head>
<body class="{layers_on}">
'''
comments = '' if PREVIEW else '''<section class="comments" aria-label="Comments"><h2>Comments<span class="fs">.</span></h2>
  <div class="giscus"></div>
  <p class="comment-note">Comments use GitHub. Sign in with a free GitHub account to join in.</p>
  <script defer src="/comments.js"></script>
 </section>'''
analytics = '' if PREVIEW else '<script async data-goatcounter="https://mishrawrites.goatcounter.com/count" src="//gc.zgo.at/count.js"></script>'
page = head + f'''<div class="wrap"><header class="top"><a class="brandmark" href="/">Gaurav Mishra<i>.</i></a><nav class="topnav" aria-label="Site"><a href="/#work">Work</a><a class="crumb" href="/monoblog/" aria-current="page">Monoblog</a><a href="/Gaurav-Mishra-CV.pdf">CV</a><a class="cta" href="/#contact">Let's talk</a></nav></header></div>
<main class="wrap">
 <div class="kick" style="margin-top:30px">Influence · Trust · History</div>
 <h1>{TITLE}<span class="fs">.</span></h1>
 <p class="dek">{E(DEK)}</p>
 <div class="meta">By <b>Gaurav Mishra</b> · 17 November 2026 · {mins} min read</div>
 <div class="intro"><p class="pull">No entry here records a lie. That is the part worth sitting with.</p>
 <p>What follows is a list of occasions on which somebody put in a word for somebody else. Nothing was promised. Nothing was proven. Everything worked.</p></div>
 <div class="list">
{entries} </div>
 <div class="rules"><h2>Before you run it<span class="fs">.</span></h2><ol>{rules}</ol></div>
 <p class="closer">This list is still being written. You are already on it.</p>
 <section class="sources" aria-label="Sources"><h2>Sources, if you'd like to check<span class="fs">.</span></h2><ol>{sources}</ol></section>
 <div class="end" aria-hidden="true"><i></i></div>
 {comments}
 <section class="related" aria-label="Keep reading"><h2>Keep reading<span class="fs">.</span></h2>
  <div class="related-grid">
   <a href="/monoblog/they-sold-you-an-automatic-door/"><span class="k">Monoblog</span><span class="t">They Sold You an Automatic Door</span></a>
   <a href="/monoblog/lies-about-marketing/"><span class="k">Monoblog</span><span class="t">The lies about marketing that marketeers tell</span></a>
   <a href="/#work"><span class="k">The work</span><span class="t">Case studies and projects, numbers attached</span></a>
  </div>
 </section>
 <footer><span>Gaurav Mishra · <a href="/monoblog/">Monoblog</a></span><span><a href="/#work">The work</a> · <a href="/">mishrawrites.com</a></span></footer>
</main>
{panel}
<script>{LIVE_JS}{PANEL_JS if PREVIEW else ''}</script>
{analytics}
</body></html>
'''
open(OUT, 'w').write(page)
print('ok', OUT, mins, 'min')
