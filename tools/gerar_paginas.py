#!/usr/bin/env python3
"""Gera as páginas de SEO (uma por curso), o sitemap.xml e o robots.txt a partir dos dados do index.html.
Uso: python3 tools/gerar_paginas.py   (precisa do Node.js instalado)
"""
import json, os, re, subprocess, unicodedata, html, datetime
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://edilson-666.github.io/Grade-curricular-ufsc/"
HOJE = datetime.date.today().isoformat()

def dados():
    src = open(os.path.join(RAIZ, "index.html"), encoding="utf-8").read()
    ini = src.index("const P1=")
    fim = src.index("\n", src.index("Object.assign(C,", ini))
    js = src[ini:fim] + "\n;process.stdout.write(JSON.stringify(C));"
    return json.loads(subprocess.run(["node", "-"], input=js, capture_output=True, text=True, check=True).stdout)

def slugify(t):
    t = unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

e = lambda t: html.escape(str(t), quote=True)

CSS = """:root{color-scheme:light dark;--bg:light-dark(#f6f7f9,#000);--panel:light-dark(#fff,#0c0d10);--soft:light-dark(#eceef2,#18191e);--ink:light-dark(#0d0e12,#f4f5f7);--mute:light-dark(#5f6470,#8b8f99);--line:light-dark(#e1e4e9,#1d1f24);--line2:light-dark(#c4c9d2,#2f3138);--ufsc:light-dark(#0855a1,#3d8fe0);--av:light-dark(#2563eb,#4d8dff)}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--av)}.in{max-width:980px;margin:0 auto;padding:0 max(4vw,16px)}
header{border-bottom:1px solid var(--line);background:var(--panel)}header .in{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:12px;padding-bottom:12px}
.brand{display:flex;align-items:center;gap:12px;color:var(--ink);text-decoration:none;font-weight:800;font-size:20px;letter-spacing:-.03em}.brand img{height:40px;width:auto}.brand em{font-style:normal;color:var(--ufsc)}
nav.bc{font-size:13px;color:var(--mute);margin:22px 0 6px}nav.bc a{color:var(--mute)}
h1{font-size:clamp(28px,5vw,40px);line-height:1.12;letter-spacing:-.035em;margin:0 0 10px}h2{font-size:21px;letter-spacing:-.02em;margin:34px 0 10px}
.lead{color:var(--mute);margin:0 0 18px;max-width:720px}
.kpis{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px;padding:0;list-style:none}.kpis li{padding:8px 14px;border-radius:12px;background:var(--panel);border:1px solid var(--line);font-size:14px}.kpis b{font-size:17px}
.cta{display:inline-flex;align-items:center;justify-content:center;text-align:center;line-height:1.25;gap:10px;min-height:50px;padding:10px 22px;border-radius:99px;background:var(--av);color:#fff;font-weight:800;text-decoration:none;box-shadow:0 10px 24px -12px var(--av)}
.note{margin:18px 0 0;padding:12px 14px;border-radius:14px;border:1px solid color-mix(in srgb,#ca8a04 40%,transparent);background:color-mix(in srgb,#ca8a04 9%,transparent);font-size:14px}
.ph{margin:14px 0;border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--panel)}
.ph h3{margin:0;padding:10px 14px;font-size:15px;display:flex;justify-content:space-between;background:var(--soft)}.ph h3 span{color:var(--mute);font-weight:600}
table{width:100%;border-collapse:collapse;font-size:14px}td,th{text-align:left;padding:9px 14px;border-top:1px solid var(--line);vertical-align:top}th{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--mute)}
td.c{white-space:nowrap;font-weight:700;color:var(--av)}td.h{white-space:nowrap;color:var(--mute)}td.p{color:var(--mute)}
@media(max-width:640px){th.p,td.p{display:none}td,th{padding:8px 10px}}
ul.opts{columns:2;gap:24px;padding-left:18px;font-size:14px}@media(max-width:640px){ul.opts{columns:1}}
.cursos{display:flex;flex-wrap:wrap;gap:6px;padding:0;list-style:none}.cursos a{display:inline-block;padding:6px 12px;border-radius:99px;border:1px solid var(--line2);color:var(--ink);text-decoration:none;font-size:13.5px;background:var(--panel)}
footer{margin-top:44px;border-top:1px solid var(--line);padding:22px 0 40px;font-size:13px;color:var(--mute)}"""

GUARD = """<script>(function(){var ok=["edilson-666.github.io","localhost","127.0.0.1",""];if(ok.indexOf(location.hostname)<0){location.replace("%s"+location.pathname.replace(/^.*\\/cursos\\//,"cursos/"));return}if(window.top!==window.self){try{window.top.location.replace(location.href)}catch(e){document.documentElement.style.display="none"}}})();</script>""" % SITE

def head(title, desc, url, extra=""):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
{GUARD}
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#000000">
<link rel="icon" type="image/png" href="../favicon.png">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Grade UFSC">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
{extra}
</head>"""

def main():
    C = dados()
    keys = sorted(C, key=lambda k: unicodedata.normalize("NFD", C[k]["nome"]).lower())
    pag = {k: slugify(C[k]["nome"]) + ".html" for k in keys}
    assert len(set(pag.values())) == len(pag), "slugs repetidos"
    os.makedirs(os.path.join(RAIZ, "cursos"), exist_ok=True)
    lista = lambda atual=None: "<ul class=\"cursos\">" + "".join(
        f'<li><a href="{pag[k]}"{" aria-current=\"page\"" if k==atual else ""}>{e(C[k]["nome"])}</a></li>' for k in keys) + "</ul>"
    for k in keys:
        c = C[k]; D = c["D"]; nome = c["nome"]
        names = {d[0]: d[1] for d in D}; names.update({o[0]: o[1] for o in c.get("opts", [])})
        nf = max(d[3] for d in D); cur = c["cur"].replace("currículo", "Currículo")
        url = SITE + "cursos/" + pag[k]
        title = f"Grade Curricular de {nome} UFSC – Pré-requisitos por fase"
        desc = (f"Grade curricular de {nome} da UFSC ({cur}): {len(D)} disciplinas em {nf} fases, "
                f"{c['total']} horas-aula, com pré-requisitos de cada disciplina e mapa interativo para marcar seu progresso.")
        def pre(p):
            if not p: return "—"
            return "; ".join(" ou ".join(e(names.get(x, x)) for x in ([g] if isinstance(g, str) else g)) for g in p)
        fases = ""
        for f in range(1, nf + 1):
            ds = [d for d in D if d[3] == f]
            if not ds: continue
            rows = "".join(
                f'<tr><td class="c">{e(d[0]) if not re.match(r"^(OPT|PROJ|ESC|POOL|EST$)", d[0]) else "—"}</td><td>{e(d[1])}'
                f'{" <small>(exige " + str(d[5]) + " h/a cursadas)</small>" if len(d) > 5 and d[5] else ""}</td>'
                f'<td class="h">{d[2]} h/a</td><td class="p">{pre(d[4])}</td></tr>' for d in ds)
            fases += (f'<section class="ph"><h3>{f}ª fase <span>{sum(d[2] for d in ds)} h/a</span></h3>'
                      f'<table><thead><tr><th>Código</th><th>Disciplina</th><th>Carga</th><th class="p">Pré-requisitos</th></tr></thead><tbody>{rows}</tbody></table></section>')
        opts = c.get("opts") or []
        optsec = (f'<h2>Disciplinas optativas ({len(opts)})</h2><ul class="opts">' +
                  "".join(f"<li>{e(o[1])} <small>({e(o[0])})</small></li>" for o in opts) + "</ul>") if opts else ""
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "Course", "name": f"{nome} – UFSC", "description": desc, "url": url, "inLanguage": "pt-BR",
             "educationalCredentialAwarded": "Graduação", "numberOfCredits": c["total"],
             "provider": {"@type": "CollegeOrUniversity", "name": "Universidade Federal de Santa Catarina", "alternateName": "UFSC", "sameAs": "https://ufsc.br"},
             "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Presencial", "courseWorkload": f"{c['total']} horas-aula"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Grade UFSC", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": "Cursos", "item": SITE + "cursos/"},
                {"@type": "ListItem", "position": 3, "name": nome, "item": url}]}]}
        out = head(title, desc, url, f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>') + f"""
<body>
<header><div class="in"><a class="brand" href="../"><img src="../brasao-ufsc.webp" alt="Brasão da UFSC" width="36" height="40">Grade <em>UFSC</em></a><a class="cta" style="min-height:40px;padding:0 16px;font-size:14px" href="../#{e(c['slug'])}">Abrir mapa</a></div></header>
<main class="in">
<nav class="bc" aria-label="Você está em"><a href="../">Grade UFSC</a> › <a href="./">Cursos</a> › {e(nome)}</nav>
<h1>Grade curricular de {e(nome)} – UFSC</h1>
<p class="lead">Todas as disciplinas de {e(nome)} da Universidade Federal de Santa Catarina, organizadas por fase, com carga horária e pré-requisitos. No mapa interativo você marca o que já foi aprovado e vê o que pode cursar agora.</p>
<ul class="kpis"><li><b>{nf}</b> fases</li><li><b>{len(D)}</b> disciplinas</li><li><b>{c['total']}</b> horas-aula</li><li>{e(cur)}</li></ul>
<a class="cta" href="../#{e(c['slug'])}">Abrir o mapa interativo de {e(nome)} →</a>
<p class="note"><b>Atenção:</b> confira sempre o PDF do currículo do seu curso no CAGR. Este é um projeto independente, sem vínculo oficial com a UFSC.</p>
<h2>Disciplinas por fase</h2>
{fases}
{optsec}
<h2>Outros cursos da UFSC</h2>
{lista(k)}
</main>
<footer><div class="in">Dados extraídos dos currículos oficiais publicados no CAGR/UFSC. Atualizado em {HOJE}. Projeto independente, sem vínculo oficial com a UFSC.</div></footer>
</body>
</html>
"""
        open(os.path.join(RAIZ, "cursos", pag[k]), "w", encoding="utf-8").write(out)
    # índice de cursos
    url = SITE + "cursos/"
    title = "Grades curriculares da UFSC – todos os cursos de graduação"
    desc = f"Grade curricular e pré-requisitos de {len(keys)} cursos de graduação da UFSC, com mapa interativo por fase."
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": title,
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + "cursos/" + pag[k], "name": C[k]["nome"]} for i, k in enumerate(keys)]}
    out = head(title, desc, url, f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>') + f"""
<body>
<header><div class="in"><a class="brand" href="../"><img src="../brasao-ufsc.webp" alt="Brasão da UFSC" width="36" height="40">Grade <em>UFSC</em></a><a class="cta" style="min-height:40px;padding:0 16px;font-size:14px" href="../">Abrir mapa</a></div></header>
<main class="in"><nav class="bc"><a href="../">Grade UFSC</a> › Cursos</nav>
<h1>Grades curriculares da UFSC</h1><p class="lead">{e(desc)} Escolha o curso para ver as disciplinas de cada fase e seus pré-requisitos.</p>
{lista()}</main>
<footer><div class="in">Projeto independente, sem vínculo oficial com a UFSC. Atualizado em {HOJE}.</div></footer>
</body></html>
"""
    open(os.path.join(RAIZ, "cursos", "index.html"), "w", encoding="utf-8").write(out)
    # sitemap e robots
    urls = [(SITE, "1.0"), (SITE + "cursos/", "0.9")] + [(SITE + "cursos/" + pag[k], "0.8") for k in keys]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{u}</loc><lastmod>{HOJE}</lastmod><changefreq>monthly</changefreq><priority>{p}</priority></url>\n" for u, p in urls) + "</urlset>\n"
    open(os.path.join(RAIZ, "sitemap.xml"), "w").write(sm)
    open(os.path.join(RAIZ, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")
    # lista de links para o index (bloco entre marcadores)
    links = "".join(f'<li><a href="cursos/{pag[k]}">{e(C[k]["nome"])}</a></li>' for k in keys)
    idx = os.path.join(RAIZ, "index.html"); s = open(idx, encoding="utf-8").read()
    a, b = "<!--CURSOS-SEO-->", "<!--/CURSOS-SEO-->"
    if a in s:
        s = s[:s.index(a) + len(a)] + f'<ul class="clinks">{links}</ul>' + s[s.index(b):]
        open(idx, "w", encoding="utf-8").write(s)
    print(f"{len(keys)} páginas de curso, sitemap com {len(urls)} URLs.")

if __name__ == "__main__":
    main()
