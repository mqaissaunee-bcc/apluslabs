import re, pathlib, html
from shell import CSS, HEADER, FOOTER, JS_COMMON, JS_LAB
from labs import LABS, READY
from markup import convert

OUT = pathlib.Path("site"); OUT.mkdir(exist_ok=True)

def page(title, desc, body_attrs, header_extra, inner, js):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<style>{CSS}</style>
</head>
<body{body_attrs}>
{HEADER.replace("{{EXTRA_CTL}}", header_extra)}
{inner}
{FOOTER}
<p id="live" class="sr" aria-live="polite"></p>
<script>{js}</script>
</body>
</html>
"""

def labfile(L): return f"aplus_lab{L['id']}_companion.html"

def build_lab(L):
    src = pathlib.Path(f"bodies/lab{L['id']}.txt")
    if src.exists():
        raw=src.read_text(); meta={}
        keep=[]
        for ln in raw.split("\n"):
            if ln.startswith("@"): k,v=ln[1:].split(" ",1); meta[k]=v.strip()
            else: keep.append(ln)
        L.update(meta); raw="\n".join(keep)
    body = convert(raw, L["cores"]) if src.exists() else pathlib.Path(f"bodies/lab{L['id']}.html").read_text()
    # inject done-rows into tracked sections and build TOC
    toc = []
    def sec(m):
        sid, track, inner = m.group(1), m.group(2), m.group(3)
        h2 = re.search(r"<h2>(.*?)</h2>", inner).group(1)
        toc.append((sid, re.sub("<.*?>", "", h2), bool(track)))
        if track:
            inner += (f'\n<div class="done-row"><input type="checkbox" id="done-{sid}" data-done="{sid}">'
                      f'<label for="done-{sid}">Mark this section reviewed</label></div>\n')
        return f'<section id="{sid}" aria-labelledby="h-{sid}">' + inner.replace("<h2>", f'<h2 id="h-{sid}">', 1) + "</section>"
    body = re.sub(r'<section id="([\w-]+)"( data-track)?>(.*?)</section>', sec, body, flags=re.S)
    items = "\n".join(f'<li><a href="#{s}"><span>{t}</span><span class="tick" aria-hidden="true"></span></a></li>' for s,t,_ in toc)
    fields = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k,v in [
        ("Time", L["mins"] + " min"), ("Difficulty", L["diff"]),
        ("Machines", L.get("vms","Win7, Win8.1, Win10")), ("Exam domains", "<br>".join(L["cores"]))])
    inner = f"""<div class="ticket"><div class="ticket-in">
  <div class="stub"><span class="lbl">Lab</span><span class="no">{L['num']}</span><span class="series">CompTIA A+ Lab Series v4</span></div>
  <div class="tk-body"><h1>{L['title']}</h1><p class="lede">{L['lede']}</p><dl class="fields">{fields}</dl></div>
</div></div>
<div class="wrap">
<nav class="toc" aria-label="On this page"><details><summary>On this page</summary>
<div id="meter" class="meter" role="progressbar" aria-label="Sections reviewed" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><span id="meter-bar"></span></div>
<p id="meter-txt" class="meter-txt"></p>
<ol>{items}</ol></details></nav>
<main id="main" tabindex="-1">
{body}
</main></div>"""
    title = f"Lab {L['num']} Companion: {L['title']} | A+ Lab Companion"
    out = page(title, L["short"], f' data-prefix="aplus-lab{L["id"]}-v1:"',
               '<button type="button" id="clear">Clear progress</button>', inner, JS_COMMON + JS_LAB)
    (OUT/labfile(L)).write_text(out)

def build_index():
    cards = []
    for i,L in enumerate(LABS):
        ready = L["id"] in READY
        ttl = f'<a href="{labfile(L)}">{L["title"]}</a>' if ready else f'{L["title"]}'
        status = '' if ready else '<span class="st soon">In progress</span>'
        badges = "".join(f'<span class="badge">{c}</span>' for c in L["cores"])
        cards.append(f"""<li class="lab{'' if ready else ' soon'}" data-order="{i}" data-group="{L['group']}" data-core="{' '.join('c1' if c.startswith('Core 1') else 'c2' for c in L['cores'])}" data-id="{L['id']}">
  <div class="lstub"><span class="sr">Lab </span>{L['num']}</div>
  <div class="lbody"><h3>{ttl}</h3>{status}<p>{L['short']}</p>
  <p class="tools"><span class="sr">Tools: </span>{L['tools']}</p>
  <div class="badges">{badges}</div><p class="prog" data-prog="{L['id']}"></p></div></li>""")
    inner = f"""<div class="ticket"><div class="ticket-in">
  <div class="stub"><span class="lbl">Labs</span><span class="no">18</span><span class="series">CompTIA A+ Lab Series v4</span></div>
  <div class="tk-body"><h1>Hands-on companion for the A+ labs</h1>
  <p class="lede">Each lab gets a guide you keep open beside NETLAB: what the lab is for, every step explained, where students get stuck, how each step looks on Windows 11, what the A+ exams expect, and the screenshots to submit.</p>
  <dl class="fields"><div><dt>Exams</dt><dd>220-1201 (Core 1)<br>220-1202 (Core 2)</dd></div><div><dt>Lab platform</dt><dd>NDG NETLAB+</dd></div><div><dt>Lab machines</dt><dd>Windows 7, 8.1, 10; Lubuntu</dd></div><div><dt>Ready now</dt><dd>{len(READY)} of {len(LABS)}</dd></div></dl></div>
</div></div>
<main id="main" tabindex="-1" class="home">
<section aria-labelledby="h-how"><h2 id="h-how">How to use a companion page</h2>
<p>Open the lab in NETLAB and its companion in a second window. Read the overview and "Then vs. now" before you start, follow the walkthrough as you work, and take a screenshot wherever you see <span class="shot">Screenshot</span>. The evidence checklist at the end of each page lists every screenshot to submit. Your checkmarks are saved in this browser only.</p>
<p>The lab machines run Windows 7, 8.1, and 10, which are now retired. Each page shows where the same setting lives on Windows 11, which is what the current A+ exams and most workplaces expect.</p></section>
<section aria-labelledby="h-labs" class="labs-sec"><h2 id="h-labs">The labs</h2>
<div class="filters">
  <label for="sort">Sort by</label>
  <select id="sort"><option value="order">Lab number</option><option value="group">Topic</option><option value="core">Exam (Core 1 first)</option></select>
  <div role="group" aria-label="Filter by exam" class="seg">
    <button type="button" class="btn" data-f="all" aria-pressed="true">All labs</button>
    <button type="button" class="btn" data-f="c1" aria-pressed="false">Core 1</button>
    <button type="button" class="btn" data-f="c2" aria-pressed="false">Core 2</button>
  </div>
</div>
<p id="count" class="meter-txt" aria-live="polite"></p>
<ol class="cards" id="cards">
{''.join(cards)}
</ol></section>
</main>"""
    css = """
.home{max-width:76rem;margin:0 auto;padding:1.5rem 1rem 3rem;display:block}
.home section{max-width:none}
.home section p{max-width:72ch}
.filters{display:flex;flex-wrap:wrap;gap:.6rem 1rem;align-items:center;margin:.25rem 0 .75rem}
.filters select{min-height:44px;font:inherit;padding:.3rem .5rem;border:1px solid var(--rule);border-radius:6px;background:var(--surface-2);color:var(--ink)}
.seg{display:flex;gap:.35rem;flex-wrap:wrap}
.seg .btn[aria-pressed="true"]{background:var(--ink);color:var(--surface);border-color:var(--ink)}
.cards{list-style:none;margin:0;padding:0;display:grid;gap:.9rem;grid-template-columns:repeat(auto-fill,minmax(20rem,1fr))}
.lab{display:grid;grid-template-columns:4.5rem 1fr;border:1px solid var(--rule);border-radius:8px;overflow:hidden;background:var(--surface)}
.lstub{background:var(--tag);color:var(--tag-ink);font-family:var(--f-display);font-weight:700;font-size:1.35rem;display:grid;place-items:start center;padding-top:.9rem;border-right:2px dashed var(--tag-ink)}
.lab.soon .lstub{background:var(--surface-2);color:var(--ink-2);border-right-color:var(--rule)}
.lbody{padding:.8rem 1rem}
.lbody h3{margin:0 0 .3rem;font-size:1.05rem;line-height:1.3}
.lbody p{margin:.35rem 0;font-size:.93rem}
.tools{font-family:var(--f-mono);font-size:.82rem!important;color:var(--ink-2)}
.st{font-size:.78rem;font-weight:700;border-radius:3px;padding:.05rem .45rem}
.st.ok{background:var(--tip-bg);color:var(--tip);border:1px solid var(--tip)}
.st.soon{background:var(--surface-2);color:var(--ink-2);border:1px solid var(--rule)}
.prog{color:var(--tip);font-weight:600}
.lab[hidden]{display:none}
"""
    js_index = r"""
(function(){
  var S=window.__S, list=document.getElementById('cards'), cards=[].slice.call(list.children);
  cards.forEach(function(c){var m; try{m=JSON.parse(S.get('aplus-lab'+c.getAttribute('data-id')+'-v1:meta'))}catch(e){}
    if(m&&m.total){c.querySelector('.prog').textContent='Your progress: '+m.done+' of '+m.total+' sections reviewed';}});
  var sortSel=document.getElementById('sort'), filt='all';
  function apply(){
    var k=sortSel.value, arr=cards.slice();
    arr.sort(function(a,b){var o=a.dataset.order-b.dataset.order;
      if(k==='group') return a.dataset.group.localeCompare(b.dataset.group)||o;
      if(k==='core'){var ca=a.dataset.core.indexOf('c1')>-1?0:1, cb=b.dataset.core.indexOf('c1')>-1?0:1; return ca-cb||o;}
      return o;});
    var n=0; arr.forEach(function(c){var show=filt==='all'||c.dataset.core.indexOf(filt)>-1; c.hidden=!show; if(show)n++; list.appendChild(c);});
    document.getElementById('count').textContent='Showing '+n+' of '+cards.length+' labs';
  }
  sortSel.addEventListener('change',apply);
  [].forEach.call(document.querySelectorAll('[data-f]'),function(b){b.addEventListener('click',function(){
    filt=b.dataset.f; [].forEach.call(document.querySelectorAll('[data-f]'),function(x){x.setAttribute('aria-pressed',x===b?'true':'false');}); apply();});});
  apply();
})();
"""
    out = page("A+ Lab Companion | CompTIA A+ Lab Series v4", 
               "Student companion guides for the 18 NDG CompTIA A+ v4 labs, mapped to the 220-1201 and 220-1202 exams.",
               "", "", inner, JS_COMMON + js_index).replace("</style>", css + "</style>", 1)
    (OUT/"index.html").write_text(out)

for L in LABS:
    if L["id"] in READY: build_lab(L)
build_index()
print("built:", sorted(p.name for p in OUT.iterdir()))
