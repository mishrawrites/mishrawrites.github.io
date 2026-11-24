// Renders the PDF and the share image. Run after build.py:
//   NODE_PATH=$(npm root -g) node _tools/women-empowerment-privatised/pdf.js
const {chromium}=require('playwright');const path=require('path');
(async()=>{const here=__dirname, root=path.resolve(here,'..','..'), slug='women-empowerment-privatised';
const b=await chromium.launch();
const p=await b.newPage({viewport:{width:820,height:1160}});
await p.goto('file://'+here+'/_print.html',{waitUntil:'networkidle'});
await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:path.join(root,'monoblog',slug,slug+'.pdf'),width:'820px',height:'1160px',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});
const o=await b.newPage({viewport:{width:1200,height:630}});
const fs=require('fs');const img=f=>'data:image/jpeg;base64,'+fs.readFileSync(path.join(root,'monoblog',slug,'img',f)).toString('base64');
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
