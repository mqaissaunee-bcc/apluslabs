import re, html as H
TRACK_OFF = {"check","evidence","cheat"}
MACH = {"Win7":("\U0001FA9F","win7"),"Win8.1":("\U0001FA9F","win81"),"Win10":("\U0001FA9F","win10"),
        "Lubuntu":("\U0001F427","lub"),"New-Lubuntu":("\U0001F427","newlub")}
def mtag(name):
    ic,cls=MACH[name]; return ic,cls
def inline(s):
    keep=[]
    def stash(x): keep.append(x); return f"\x00{len(keep)-1}\x00"
    s=re.sub(r"`([^`]+)`", lambda m: stash(f'<code class="inl">{H.escape(m.group(1),quote=False)}</code>'), s)
    s=re.sub(r"\[\[(.+?)\]\]", lambda m: stash(f"<kbd>{H.escape(m.group(1),quote=False)}</kbd>"), s)
    s=re.sub(r"\{\{on ([\w.\-]+)\}\}", lambda m: stash(f'<span class="onm m-{MACH[m.group(1)][1]}"><span aria-hidden="true">{MACH[m.group(1)][0]}</span> On {m.group(1)}:</span>'), s)
    s=re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s=re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s=re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], s)
    return s
def table(rows):
    cells=[[c.strip().replace("\x01","|") for c in r.strip().replace("\\|","\x01").strip("|").split("|")] for r in rows]
    head="".join(f'<th scope="col">{inline(c)}</th>' for c in cells[0])
    body="".join("<tr>"+"".join(f"<td>{inline(c)}</td>" for c in r)+"</tr>" for r in cells[1:])
    return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
def convert(src, cores):
    out=[]; sec=None; stepn=0; in_step=False; cheat_open=False; col_open=False; band=False
    lines=src.split("\n"); i=0
    def close_step():
        nonlocal in_step
        if in_step: out.append("</div>"); in_step=False
    def close_cols():
        nonlocal col_open
        if col_open: out.append("</div>"); col_open=False
    def close_band():
        nonlocal band
        close_step()
        if band: out.append("</div>"); band=False
    def close_sec():
        nonlocal sec, cheat_open
        close_band(); close_cols()
        if cheat_open: out.append("</div></div>"); cheat_open=False
        if sec: out.append("</section>")
    while i < len(lines):
        l=lines[i].rstrip(); i+=1
        if not l.strip(): continue
        if l.startswith("== "):
            close_sec()
            sid,title=[x.strip() for x in l[3:].split("|",1)]; sec=sid
            out.append(f'<section id="{sid}"{"" if sid in TRACK_OFF else " data-track"}>\n<h2>{inline(title)}</h2>')
            if sid=="exam": out.append('<div class="badges">'+"".join(f'<span class="badge">{H.escape(c)}</span>' for c in cores)+"</div>")
            if sid=="cheat": out.append('<div class="cheat"><div class="grid">'); cheat_open=True
            continue
        if l.startswith("@@ "):
            close_band(); name=l[3:].strip(); ic,cls=MACH[name]; band=True
            out.append(f'<div class="mrun m-{cls}"><p class="mband"><span aria-hidden="true">{ic}</span> On {H.escape(name)}</p>'); continue
        if l.startswith("## "):
            close_band()
            ref=""
            mm=re.search(r"\s*<<(.+?)>>\s*$",l)
            if mm: ref=f' <span class="pdfref">PDF {H.escape(mm.group(1))}</span>'; l=l[:mm.start()]
            if sec=="cheat":
                close_cols(); out.append(f"<div><h3>{inline(l[3:])}</h3>"); col_open=True
            else: out.append(f'<p class="task-head">{inline(l[3:])}{ref}</p>')
            continue
        if l.startswith("### "):
            if sec=="walkthrough":
                close_step(); stepn+=1; in_step=True
                out.append(f'<div class="step">\n<h3><span class="n">{stepn}</span>{inline(l[4:])}</h3>')
            else: out.append(f"<h3>{inline(l[4:])}</h3>")
            continue
        if l.startswith("```"):
            info=l[3:].strip(); prompt=""; fname=""
            if info.startswith("file "): fname=info[5:].strip()
            elif info: prompt=info
            code=[]
            while i < len(lines) and not lines[i].startswith("```"):
                c=lines[i]; i+=1
                if c.startswith(">> "): prompt=c[3:].strip(); continue
                if c.startswith("%% "): code.append(f'<span class="c">{H.escape(c[3:],quote=False)}</span>'); continue
                if not c.strip(): code.append(""); continue
                pr=f'<span class="pr" aria-hidden="true">{H.escape(prompt,quote=False)} </span>' if prompt and not fname else ""
                code.append(pr+H.escape(c,quote=False))
            i+=1
            cap=f'<p class="fcap">File <code class="inl">{H.escape(fname)}</code>: type this into the editor, not the prompt</p>' if fname else ""
            out.append(cap+f'<pre class="cmd{" file" if fname else ""}"{" data-prompt=\"" + H.escape(prompt) + "\"" if prompt else ""}><code>'+"\n".join(code)+"</code></pre>"); continue
        m=re.match(r"!(stuck|tip|now)\s*(.*)",l)
        if m:
            kind,rest=m.groups()
            title,text=(rest.split("|",1) if "|" in rest else ({"stuck":"Where people get stuck","tip":"Good to know","now":"On Windows 11"}[kind],rest))
            paras="".join(f"<p>{inline(x.strip())}</p>" for x in text.split(" // "))
            out.append(f'<div class="call {kind}"><span class="k">{inline(title.strip())}</span>{paras}</div>'); continue
        if l.startswith("!shot "):
            out.append(f'<p class="shotline"><span class="shot">Screenshot</span>{inline(l[6:])}</p>'); continue
        if l.startswith("|"):
            rows=[l]
            while i < len(lines) and lines[i].startswith("|"): rows.append(lines[i]); i+=1
            out.append(table(rows)); continue
        if l.startswith("- "):
            items=[l]
            while i < len(lines) and lines[i].startswith("- "): items.append(lines[i]); i+=1
            out.append("<ul>"+"".join(f"<li>{inline(x[2:])}</li>" for x in items)+"</ul>"); continue
        if l.startswith("?? "):
            n=sum(1 for x in out if 'class="q"' in x)+1
            a=lines[i].rstrip(); i+=1
            assert a.startswith("=> "), l
            out.append(f'<div class="q"><p class="ask">{n}. {inline(l[3:])}</p><button type="button" class="btn reveal" aria-expanded="false">Show answer</button><div class="ans">{inline(a[3:])}</div></div>'); continue
        if l.startswith("[] "):
            items=[l]
            while i < len(lines) and lines[i].startswith("[] "): items.append(lines[i]); i+=1
            lis=[]
            for k,x in enumerate(items,1):
                lab,txt=x[3:].split("|",1)
                lis.append(f'<li><input type="checkbox" id="ev{k}" data-evidence="ev{k}"><label for="ev{k}"><span class="shot">{inline(lab.strip())}</span>{inline(txt.strip())}</label></li>')
            out.append('<div class="evidence"><ul>'+"".join(lis)+"</ul></div>"); continue
        if l.startswith("<"): out.append(l); continue
        out.append(f"<p>{inline(l)}</p>")
    close_sec()
    return "\n".join(out)
