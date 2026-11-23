const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:600,height:840}});
for(const f of fs.readdirSync('html')){await p.goto('file://'+process.cwd()+'/html/'+f);await p.waitForTimeout(150);await p.screenshot({path:'out/'+f.replace('.html','.png')});}
await b.close()})();
