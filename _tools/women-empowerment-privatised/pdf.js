// Renders the A4 PDF (cover + body with running footer + back cover) and the share image.
// Run after build.py:  NODE_PATH=$(npm root -g) node _tools/women-empowerment-privatised/pdf.js
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');const {execFileSync}=require('child_process');
(async()=>{const here=__dirname, root=path.resolve(here,'..','..'), slug='women-empowerment-privatised';
const b=await chromium.launch();
async function render(file,out,opts){const p=await b.newPage();await p.goto('file://'+path.join(here,file),{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
 await p.pdf(Object.assign({path:path.join(here,out),format:'A4',printBackground:true,preferCSSPageSize:true},opts));await p.close();}
const foot=`<div style="width:100%;margin:0 15mm;padding-top:2mm;border-top:0.5px solid #E7DCC6;font-family:Helvetica,Arial,sans-serif;font-size:7.5px;color:#7A746C;display:flex;justify-content:space-between;align-items:center">
<span>Women Empowerment! Privatised. · Gaurav Mishra</span><span style="color:#AE611C;font-weight:bold;letter-spacing:.4px">mishrawrites.com</span><span class="pageNumber"></span></div>`;
await render('_print_cover.html','_p1.pdf',{});
await render('_print_body.html','_p2.pdf',{displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:foot});
await render('_print_back.html','_p3.pdf',{});
const out=path.join(root,'monoblog',slug,slug+'.pdf');
execFileSync('python3',['-c',`import sys
from pypdf import PdfWriter
w=PdfWriter()
for f in sys.argv[1:4]: w.append(f)
w.add_metadata({'/Title':'Women Empowerment! Privatised.','/Author':'Gaurav Mishra','/Subject':'Brands that tried, and brands that made a difference. mishrawrites.com','/Keywords':'brand, marketing, women, India, period care, mishrawrites.com'})
w.write(sys.argv[4])`,path.join(here,'_p1.pdf'),path.join(here,'_p2.pdf'),path.join(here,'_p3.pdf'),out]);
for(const f of ['_p1.pdf','_p2.pdf','_p3.pdf'])fs.unlinkSync(path.join(here,f));
// share image
const o=await b.newPage({viewport:{width:1200,height:630}});
const img=f=>'data:image/jpeg;base64,'+fs.readFileSync(path.join(root,'monoblog',slug,'img',f)).toString('base64');
await o.setContent(`<html><head><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@800&family=Montserrat:wght@700&family=Fraunces:ital,opsz,wght@1,9..144,400&display=swap"></head>
<body style="margin:0;width:1200px;height:630px;background:#4A0E0E;display:grid;grid-template-columns:660px 540px;overflow:hidden">
<div style="padding:56px 48px;display:flex;flex-direction:column;justify-content:flex-end;color:#fff">
<div style="font:700 15px Montserrat;letter-spacing:.2em;color:#C9A44C;text-transform:uppercase">A free e-book for founders and brand leaders</div>
<div style="font:800 64px/0.98 Poppins;letter-spacing:-.02em;margin:18px 0 16px">Women<br>Empowerment!<br><span style="color:#C9A44C">Privatised.</span></div>
<div style="font:italic 400 26px/1.3 Fraunces;color:#F6E9D6">Brands that tried, and brands that made a difference.</div>
<div style="font:700 16px Montserrat;letter-spacing:.06em;color:#E9D7B5;margin-top:22px">GAURAV MISHRA · mishrawrites.com</div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:4px;padding:4px">
${['hero.jpg','whisper.jpg','ariel-dads.jpg','vicks.jpg','tanishq.jpg','fittr.jpg'].map(f=>`<div style="background:url(${img(f)}) center/cover;filter:grayscale(25%)"></div>`).join('')}
</div></body></html>`,{waitUntil:'networkidle'});
await o.evaluate(()=>document.fonts.ready);
await o.screenshot({path:path.join(root,'media','og',slug+'.png')});
await b.close();console.log('pdf + og done');})();
