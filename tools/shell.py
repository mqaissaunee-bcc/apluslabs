LIGHT = """
  --bg:#E8ECF0; --surface:#FFFFFF; --surface-2:#F3F5F8; --ink:#14233A; --ink-2:#47576C;
  --rule:#C7D0DA; --accent:#1C5689; --accent-ink:#FFFFFF; --tag:#F2B705; --tag-ink:#2E2300;
  --stuck:#A3241C; --stuck-bg:#FBEDEB; --tip:#1D6644; --tip-bg:#E7F3EC;
  --now:#5B3D99; --now-bg:#F1ECFA; --code-bg:#13202F; --code-ink:#E4ECF5; --code-dim:#93A6BC;
  --focus:#1C5689; --shadow:0 1px 0 #C7D0DA;"""
DARK = """
  --bg:#0E1621; --surface:#152131; --surface-2:#1B293B; --ink:#E5EBF2; --ink-2:#A9B6C6;
  --rule:#2D3D52; --accent:#86BDEB; --accent-ink:#0E1621; --tag:#F2B705; --tag-ink:#2E2300;
  --stuck:#FF968C; --stuck-bg:#33201F; --tip:#86D3AE; --tip-bg:#15302A;
  --now:#C4AEF5; --now-bg:#251F3A; --code-bg:#0A111A; --code-ink:#E4ECF5; --code-dim:#8597AC;
  --focus:#F2B705; --shadow:0 1px 0 #2D3D52;"""

CSS = """
:root{""" + LIGHT + """
  --f-display:"Bahnschrift","DIN Alternate","DIN 2014","Arial Narrow",system-ui,sans-serif;
  --f-body:"Segoe UI",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
  --f-mono:"Cascadia Mono","Cascadia Code",Consolas,"SFMono-Regular",Menlo,monospace;
  --fs:1rem; color-scheme:light;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){""" + DARK + """ color-scheme:dark;}}
:root[data-theme="dark"]{""" + DARK + """ color-scheme:dark;}
*,*::before,*::after{box-sizing:border-box}
html{font-size:calc(100% * var(--scale,1));scroll-padding-top:4.5rem}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f-body);line-height:1.6}
a{color:var(--accent)} a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.skip-link{position:absolute;left:-999px;top:0;background:var(--tag);color:var(--tag-ink);padding:.7rem 1rem;z-index:20}
.skip-link:focus{left:1rem;top:1rem}
code,pre,kbd{font-family:var(--f-mono)}
code.inl{background:var(--surface-2);border:1px solid var(--rule);border-radius:3px;padding:0 .3em;font-size:.92em}
kbd{display:inline-block;border:1px solid var(--rule);border-bottom-width:3px;border-radius:4px;padding:0 .4em;background:var(--surface);font-size:.85em;line-height:1.5}

/* top bar */
.bar{position:sticky;top:0;z-index:10;background:var(--surface);border-bottom:1px solid var(--rule)}
.bar-in{max-width:76rem;margin:0 auto;padding:.4rem 1rem;display:flex;gap:.75rem;align-items:center;flex-wrap:wrap}
.brand{font-family:var(--f-display);font-weight:700;font-size:1.1rem;color:var(--ink);text-decoration:none;margin-right:auto;display:flex;gap:.5rem;align-items:center}
.brand .plug{display:inline-grid;place-items:center;width:2rem;height:2rem;background:var(--tag);color:var(--tag-ink);border-radius:4px;font-size:1rem}
.ctl{display:flex;gap:.35rem;flex-wrap:wrap}
.ctl button,.btn{min-height:44px;min-width:44px;padding:.3rem .75rem;border:1px solid var(--rule);background:var(--surface-2);color:var(--ink);border-radius:6px;font:inherit;font-size:.9rem;cursor:pointer}
.ctl button:hover,.btn:hover{border-color:var(--accent)}
.btn.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}

/* hero ticket — the one bold element */
.ticket{max-width:76rem;margin:1.5rem auto 0;padding:0 1rem}
.ticket-in{display:grid;grid-template-columns:1fr;background:var(--surface);border:1px solid var(--rule);border-radius:10px;overflow:hidden}
.stub{background:var(--tag);color:var(--tag-ink);padding:1rem 1.25rem;display:flex;flex-direction:column;justify-content:space-between;gap:.5rem;position:relative}
.stub .lbl{font-size:.85rem;font-weight:600}
.stub .no{font-family:var(--f-display);font-weight:700;white-space:nowrap;font-size:clamp(2.4rem,6vw,3.5rem);line-height:1;letter-spacing:-.01em}
.stub .series{font-size:.8rem}
.tk-body{padding:1.25rem 1.5rem 1.5rem}
.tk-body h1{font-family:var(--f-display);font-weight:700;font-size:clamp(1.6rem,3.6vw,2.4rem);line-height:1.15;margin:0 0 .6rem;max-width:30ch}
.lede{font-size:1.08rem;color:var(--ink-2);max-width:62ch;margin:0 0 1rem}
.fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:0;border-top:1px dashed var(--rule);margin:0}
.fields div{padding:.6rem .75rem .5rem 0;border-bottom:1px dashed var(--rule)}
.fields dt{font-size:.78rem;color:var(--ink-2)}
.fields dd{margin:0;font-weight:600;font-size:.95rem}
@media (min-width:720px){
  .ticket-in{grid-template-columns:12rem 1fr}
  .stub{border-right:2px dashed var(--tag-ink)}
  .stub::before,.stub::after{content:"";position:absolute;right:-11px;width:20px;height:20px;border-radius:50%;background:var(--bg);border:1px solid var(--rule)}
  .stub::before{top:-11px} .stub::after{bottom:-11px}
}

/* layout */
.wrap{max-width:76rem;margin:0 auto;padding:1.5rem 1rem 3rem;display:grid;gap:2rem;grid-template-columns:1fr}
@media (min-width:1000px){.wrap{grid-template-columns:15rem minmax(0,1fr)}}
.toc{align-self:start}
@media (min-width:1000px){.toc{position:sticky;top:4.5rem}}
.toc details{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:.5rem .9rem}
.toc summary{cursor:pointer;font-weight:600;min-height:44px;display:flex;align-items:center}
.toc ol{list-style:none;margin:.25rem 0 .5rem;padding:0}
.toc li a{display:flex;justify-content:space-between;gap:.5rem;padding:.3rem .4rem;border-radius:4px;text-decoration:none;color:var(--ink);font-size:.92rem}
.toc li a:hover{background:var(--surface-2)}
.toc li a[aria-current="true"]{background:var(--surface-2);box-shadow:inset 3px 0 0 var(--accent)}
.toc .tick{color:var(--tip);font-weight:700}
.meter{margin:.5rem 0 .25rem;height:10px;background:var(--surface-2);border:1px solid var(--rule);border-radius:5px;overflow:hidden}
.meter span{display:block;height:100%;width:0;background:var(--tip);transition:width .3s}
.meter-txt{font-size:.85rem;color:var(--ink-2);margin:0}
main{min-width:0}
main section{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:1.25rem 1.5rem;margin:0 0 1.25rem;max-width:56rem}
@media (max-width:600px){main section{padding:1rem}.ctl button{padding:.3rem .55rem}}
main h2{font-family:var(--f-display);font-weight:700;font-size:1.55rem;line-height:1.2;margin:0 0 .75rem}
main h3{font-size:1.1rem;margin:1.25rem 0 .4rem}
main p,main li{max-width:68ch}
.task-head{font-family:var(--f-display);font-weight:700;font-size:1.15rem;margin:1.75rem 0 .5rem;padding-top:1rem;border-top:2px solid var(--ink)}
.task-head:first-of-type{border-top:0;padding-top:0}
.step{border-left:3px solid var(--rule);padding:.1rem 0 .1rem 1rem;margin:1rem 0}
.step h3{margin-top:0;display:flex;gap:.6rem;align-items:baseline}
.step h3 .n{flex:none;display:inline-grid;place-items:center;min-width:1.8rem;height:1.8rem;border-radius:50%;background:var(--ink);color:var(--surface);font-size:.9rem}
.call{border-radius:8px;padding:.75rem 1rem;margin:1rem 0;border:1px solid}
.call .k{display:block;font-weight:700;margin-bottom:.2rem}
.call p{margin:.25rem 0}
.call.stuck{background:var(--stuck-bg);border-color:var(--stuck)} .call.stuck .k{color:var(--stuck)}
.call.tip{background:var(--tip-bg);border-color:var(--tip)} .call.tip .k{color:var(--tip)}
.call.now{background:var(--now-bg);border-color:var(--now)} .call.now .k{color:var(--now)}
.shot{display:inline-block;background:var(--tag);color:var(--tag-ink);font-weight:700;font-size:.85rem;padding:.05rem .5rem;border-radius:3px;margin-right:.35rem}
.shot::before{content:"\\1F4F7\\FE0E  "}
p.shotline{margin:.5rem 0}
pre.cmd{position:relative;background:var(--code-bg);color:var(--code-ink);border-radius:6px;padding:.8rem 4.8rem .8rem 1rem;overflow-x:auto;font-size:.92rem;margin:.6rem 0}
pre.cmd .c{color:var(--code-dim)}
.copy{position:absolute;top:.4rem;right:.4rem;min-height:36px;padding:.2rem .6rem;border:1px solid var(--code-dim);background:transparent;color:var(--code-ink);border-radius:4px;font:inherit;font-size:.8rem;cursor:pointer}
.tbl{overflow-x:auto;margin:.75rem 0}
table{border-collapse:collapse;width:100%;font-size:.94rem}
th,td{text-align:left;vertical-align:top;padding:.5rem .6rem;border-bottom:1px solid var(--rule)}
th{background:var(--surface-2);font-weight:600}
td code{white-space:nowrap}
.done-row{display:flex;gap:.6rem;align-items:center;margin-top:1.25rem;padding-top:.75rem;border-top:1px dashed var(--rule)}
input[type=checkbox]{width:1.3rem;height:1.3rem;accent-color:var(--tip);flex:none}
.done-row label{min-height:44px;display:flex;align-items:center;cursor:pointer}
.q{border-top:1px solid var(--rule);padding:.75rem 0}
.q .ask{font-weight:600;margin:0 0 .4rem}
.ans{display:none;margin-top:.5rem;padding:.6rem .8rem;background:var(--surface-2);border-radius:6px}
.ans.open{display:block}
.evidence ul{list-style:none;padding:0;margin:0}
.evidence li{display:flex;gap:.7rem;align-items:flex-start;padding:.6rem 0;border-bottom:1px dashed var(--rule)}
.evidence li label{cursor:pointer}
.cheat{border:2px solid var(--ink);border-radius:8px;padding:1rem 1.25rem}
.cheat .grid{display:grid;gap:1rem 1.5rem;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr))}
.cheat h3{margin:0 0 .3rem;font-family:var(--f-display)}
.cheat ul{margin:0;padding-left:1.1rem;font-size:.93rem}
.badges{display:flex;flex-wrap:wrap;gap:.4rem;margin:.5rem 0}
.badge{border:1px solid var(--accent);color:var(--accent);border-radius:999px;padding:.05rem .65rem;font-size:.82rem;font-weight:600}
footer{border-top:1px solid var(--rule);background:var(--surface);color:var(--ink-2);font-size:.88rem}
footer .in{max-width:76rem;margin:0 auto;padding:1.25rem 1rem}
footer p{margin:.25rem 0;max-width:80ch}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
@media print{
  .bar,.toc,.copy,.done-row,.reveal,.skip-link{display:none!important}
  body{background:#fff;color:#000} .wrap{display:block;padding:0}
  main section{border:0;padding:0;margin:0 0 1rem;break-inside:auto}
  .ans{display:block!important} pre.cmd{background:#f2f2f2;color:#000;border:1px solid #999}
  .stub{background:#fff;border:2px solid #000}
}
"""

HEADER = """<a href="#main" class="skip-link">Skip to main content</a>
<header class="bar"><div class="bar-in">
  <a class="brand" href="index.html"><span class="plug" aria-hidden="true">A+</span>A+ Lab Companion</a>
  <div class="ctl" role="group" aria-label="Page controls">
    <button type="button" id="fs-down" aria-label="Decrease text size">A&minus;</button>
    <button type="button" id="fs-up" aria-label="Increase text size">A+</button>
    <button type="button" id="theme" aria-pressed="false">Dark mode</button>
    <button type="button" id="print">Print</button>
    {{EXTRA_CTL}}
  </div>
</div></header>"""

FOOTER = """<footer><div class="in">
  <p>Built for CompTIA A+ hands-on practice at Brookdale Community College, 2026. Open educational resource.</p>
  <p>Companion to the NDG CompTIA A+ Lab Series v4 labs. This guide is independent and is not affiliated with or endorsed by CompTIA or Network Development Group. CompTIA A+ is a registered trademark of CompTIA, Inc.</p>
</div></footer>"""

# Shared JS: theme + text size (site-wide keys), plus lab-page features when PREFIX is set
JS_COMMON = r"""
(function(){
  var S={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},
         set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}},
         del:function(k){try{localStorage.removeItem(k)}catch(e){}}};
  window.__S=S;
  var root=document.documentElement, tb=document.getElementById('theme');
  function isDark(){var t=root.getAttribute('data-theme'); if(t) return t==='dark';
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches;}
  function paintTheme(){var d=isDark(); tb.setAttribute('aria-pressed',d?'true':'false'); tb.textContent=d?'Light mode':'Dark mode';}
  var saved=S.get('aplus-theme'); if(saved) root.setAttribute('data-theme',saved);
  paintTheme();
  tb.addEventListener('click',function(){var n=isDark()?'light':'dark'; root.setAttribute('data-theme',n); S.set('aplus-theme',n); paintTheme();});
  var sc=parseFloat(S.get('aplus-scale'))||1;
  function setScale(v){sc=Math.min(1.4,Math.max(.85,Math.round(v*100)/100)); root.style.setProperty('--scale',sc); S.set('aplus-scale',sc);}
  setScale(sc);
  document.getElementById('fs-up').addEventListener('click',function(){setScale(sc+.1)});
  document.getElementById('fs-down').addEventListener('click',function(){setScale(sc-.1)});
  document.getElementById('print').addEventListener('click',function(){window.print()});
})();
"""

JS_LAB = r"""
(function(){
  var S=window.__S, P=document.body.getAttribute('data-prefix');
  var live=document.getElementById('live');
  function say(t){live.textContent=t;}
  function load(k){try{return JSON.parse(S.get(P+k))||{}}catch(e){return {}}}
  var done=load('done'), ev=load('evidence');
  var tracks=[].slice.call(document.querySelectorAll('[data-done]'));
  var bar=document.getElementById('meter-bar'), txt=document.getElementById('meter-txt'), meter=document.getElementById('meter');
  function refresh(){
    var n=0; tracks.forEach(function(c){ if(c.checked) n++;
      var a=document.querySelector('.toc a[href="#'+c.getAttribute('data-done')+'"] .tick'); if(a) a.textContent=c.checked?'\u2713':'';});
    var pct=tracks.length?Math.round(n/tracks.length*100):0;
    bar.style.width=pct+'%'; meter.setAttribute('aria-valuenow',pct);
    txt.textContent=n+' of '+tracks.length+' sections reviewed';
    S.set(P+'meta',JSON.stringify({done:n,total:tracks.length}));
  }
  tracks.forEach(function(c){ c.checked=!!done[c.getAttribute('data-done')];
    c.addEventListener('change',function(){done[c.getAttribute('data-done')]=c.checked; S.set(P+'done',JSON.stringify(done)); refresh();});});
  refresh();
  [].forEach.call(document.querySelectorAll('[data-evidence]'),function(c){ c.checked=!!ev[c.getAttribute('data-evidence')];
    c.addEventListener('change',function(){ev[c.getAttribute('data-evidence')]=c.checked; S.set(P+'evidence',JSON.stringify(ev));});});
  document.getElementById('clear').addEventListener('click',function(){
    if(!window.confirm('Clear your checkmarks on this lab page?')) return;
    S.del(P+'done'); S.del(P+'evidence'); done={}; ev={};
    [].forEach.call(document.querySelectorAll('[data-done],[data-evidence]'),function(c){c.checked=false;});
    refresh(); say('Progress cleared for this lab.');});
  [].forEach.call(document.querySelectorAll('.reveal'),function(b){
    b.addEventListener('click',function(){var a=b.nextElementSibling, o=a.classList.toggle('open');
      b.setAttribute('aria-expanded',o?'true':'false'); b.textContent=o?'Hide answer':'Show answer';});});
  [].forEach.call(document.querySelectorAll('pre.cmd'),function(pre){
    var b=document.createElement('button'); b.type='button'; b.className='copy'; b.textContent='Copy';
    b.setAttribute('aria-label','Copy command'); pre.appendChild(b);
    b.addEventListener('click',function(){
      var code=pre.querySelector('code'), clone=code.cloneNode(true);
      [].forEach.call(clone.querySelectorAll('.c'),function(x){x.remove();});
      var t=clone.textContent.replace(/\n{2,}/g,'\n').trim();
      function ok(){b.textContent='Copied'; say('Command copied.'); setTimeout(function(){b.textContent='Copy'},1500);}
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,fallback);} else fallback();
      function fallback(){var ta=document.createElement('textarea'); ta.value=t; document.body.appendChild(ta); ta.select();
        try{document.execCommand('copy'); ok();}catch(e){say('Copy failed; select the text instead.');} ta.remove();}
    });});
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){ if(e.isIntersecting){
      links.forEach(function(l){l.setAttribute('aria-current', l.getAttribute('href')==='#'+e.target.id?'true':'false');});}});},
      {rootMargin:'-20% 0px -70% 0px'});
    [].forEach.call(document.querySelectorAll('main section[id]'),function(s){io.observe(s);});
  }
  var det=document.querySelector('.toc details');
  if(window.matchMedia('(min-width:1000px)').matches) det.open=true;
})();
"""
