#!/usr/bin/env python3
"""Gera privacidade.html e termos.html. Uso: python3 tools/gerar_legal.py"""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://edilson-666.github.io/Grade-curricular-ufsc/"
VIG = "27 de novembro de 2026"

CSS = """:root{color-scheme:light dark;--bg:light-dark(#f6f7f9,#000);--panel:light-dark(#fff,#0c0d10);--soft:light-dark(#eceef2,#16171c);--ink:light-dark(#0d0e12,#f4f5f7);--txt:light-dark(#2b2f38,#c9ced8);--mute:light-dark(#5f6470,#8b8f99);--line:light-dark(#e1e4e9,#1d1f24);--line2:light-dark(#c4c9d2,#2f3138);--ufsc:light-dark(#0855a1,#3d8fe0);--av:light-dark(#2563eb,#4d8dff)}
:root[data-theme=light]{color-scheme:light}:root[data-theme=dark]{color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--av)}.in{max-width:1100px;margin:0 auto;padding:0 max(4vw,16px)}
.bar{height:4px;background:linear-gradient(90deg,#0855a1 0 33.3%,#1fa855 33.3% 66.6%,#f5c542 66.6%)}
header.top{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--panel) 92%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
header.top .in{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:64px}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-weight:800;font-size:18px;letter-spacing:-.03em}.brand img{border-radius:10px}.brand em{font-style:normal;color:var(--ufsc)}
.back{display:inline-flex;align-items:center;gap:6px;min-height:40px;padding:0 16px;border-radius:99px;border:1px solid var(--line2);color:var(--ink);text-decoration:none;font-weight:700;font-size:14px}
.hero{padding:36px 0 26px;border-bottom:1px solid var(--line)}
.eyebrow{margin:0 0 8px;font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
h1{font-size:clamp(30px,5vw,46px);line-height:1.08;letter-spacing:-.04em;margin:0 0 12px}
.lead{color:var(--mute);margin:0;max-width:720px;font-size:17px}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 0;padding:0;list-style:none}.meta li{padding:6px 12px;border-radius:99px;background:var(--panel);border:1px solid var(--line);font-size:13px;color:var(--mute)}.meta b{color:var(--ink)}
.tabs{display:flex;gap:6px;margin:20px 0 0}.tabs a{padding:9px 16px;border-radius:99px;border:1px solid var(--line2);color:var(--ink);text-decoration:none;font-weight:700;font-size:14px}.tabs a[aria-current]{background:var(--ink);border-color:var(--ink);color:var(--bg)}
.wrapg{display:grid;grid-template-columns:240px minmax(0,1fr);gap:48px;padding:32px 0 20px}
@media(max-width:860px){.wrapg{grid-template-columns:1fr;gap:20px}}
.toc{position:sticky;top:84px;align-self:start;font-size:14px}
.toc p{margin:0 0 8px;font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.toc ol{margin:0;padding:0;list-style:none;counter-reset:t;border-left:1px solid var(--line)}
.toc li{counter-increment:t}.toc a{display:block;padding:6px 0 6px 14px;margin-left:-1px;border-left:2px solid transparent;color:var(--mute);text-decoration:none;line-height:1.35}
.toc a::before{content:counter(t) ". ";font-weight:700}.toc a:hover{color:var(--ink);border-left-color:var(--ink)}
@media(max-width:860px){.toc{position:static;padding:14px 16px;border-radius:16px;background:var(--panel);border:1px solid var(--line)}.toc ol{columns:2;column-gap:16px;border:0}.toc a{padding:4px 0;border:0}}
@media(max-width:480px){.toc ol{columns:1}}
.summary{margin:0 0 30px;padding:18px 20px;border-radius:18px;background:var(--panel);border:1px solid var(--line)}
.summary h2{margin:0 0 10px;font-size:16px;letter-spacing:-.01em;border:0;padding:0}
.summary ul{margin:0;padding:0;list-style:none;display:grid;gap:10px}
.summary li{display:grid;grid-template-columns:22px 1fr;gap:10px;color:var(--txt);line-height:1.5;font-size:15px}
.summary li::before{content:"";width:22px;height:22px;border-radius:99px;background:color-mix(in srgb,#16a34a 18%,transparent) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2316a34a' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E") center/13px no-repeat}
article section{padding:22px 0 8px;border-top:1px solid var(--line);scroll-margin-top:80px;counter-increment:s}
article{counter-reset:s}
article h2{display:flex;gap:12px;align-items:baseline;font-size:21px;letter-spacing:-.02em;margin:0 0 10px}
article h2::before{content:counter(s);flex:none;display:inline-grid;place-items:center;width:30px;height:30px;border-radius:10px;background:var(--soft);border:1px solid var(--line2);font-size:14px;color:var(--ink)}
article h3{font-size:16px;margin:16px 0 4px}
article p,article li{color:var(--txt)}article ul{padding-left:20px}article li{margin:5px 0}
.note{margin:14px 0;padding:12px 14px;border-radius:14px;border:1px solid color-mix(in srgb,#ca8a04 40%,transparent);background:color-mix(in srgb,#ca8a04 9%,transparent);font-size:14.5px;color:var(--txt)}
table{width:100%;border-collapse:collapse;margin:12px 0;font-size:14px;background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:block;overflow-x:auto}
th,td{text-align:left;padding:10px 12px;border-top:1px solid var(--line);vertical-align:top}th{background:var(--soft);font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);border-top:0}
td{color:var(--txt)}td b{color:var(--ink)}
footer{margin-top:30px;border-top:1px solid var(--line);background:var(--panel)}footer .in{display:flex;flex-wrap:wrap;justify-content:space-between;gap:14px;padding:22px max(4vw,16px) 36px;font-size:13px;color:var(--mute)}
footer nav{display:flex;flex-wrap:wrap;gap:6px 18px}footer nav a{color:var(--ink);text-decoration:none;font-weight:600}
.ulx{display:inline-flex;align-items:center;gap:6px;font-weight:800;color:var(--ink)}.ulx img{border-radius:6px}.ulx em{font-style:normal;color:#ff8a1c}"""

GUARD = """<script>try{var t=localStorage.getItem("grade-tema");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}catch(e){}(function(){var ok=["edilson-666.github.io","localhost","127.0.0.1",""];if(ok.indexOf(location.hostname)<0){location.replace("%s"+location.pathname.split("/").pop());return}if(window.top!==window.self){try{window.top.location.replace(location.href)}catch(e){document.documentElement.style.display="none"}}})();</script>""" % SITE

def page(fn, title, desc, eyebrow, h1, lead, summary, sections):
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, _ in sections)
    body = "".join(f'<section id="{i}"><h2>{t}</h2>{c}</section>' for i, t, c in sections)
    summ = "".join(f"<li><span>{x}</span></li>" for x in summary)
    tabs = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f==fn else ""}>{n}</a>' for f, n in [("privacidade.html","Privacidade"),("termos.html","Termos de uso")])
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
{GUARD}
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{SITE}{fn}">
<meta name="theme-color" content="#000000">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="bar" aria-hidden="true"></div>
<header class="top"><div class="in"><a class="brand" href="./"><img src="logo.svg" alt="" width="34" height="34"><span>Grade <em>UFSC</em></span></a><a class="back" href="./">← Voltar ao mapa</a></div></header>
<main class="in">
<div class="hero"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p>
<ul class="meta"><li>Vigente desde <b>{VIG}</b></li><li>Última atualização <b>{VIG}</b></li></ul>
<nav class="tabs" aria-label="Documentos legais">{tabs}</nav></div>
<div class="wrapg">
<nav class="toc" aria-label="Nesta página"><p>Nesta página</p><ol>{toc}</ol></nav>
<div><div class="summary"><h2>Em resumo</h2><ul>{summ}</ul></div><article>{body}</article></div>
</div>
</main>
<footer><div class="in"><span>© 2026 Grade UFSC · Em parceria com <span class="ulx"><img src="unilux.svg" alt="" width="18" height="18"><span>Uni<em>-lux</em></span></span></span><nav aria-label="Links"><a href="./">Mapa</a><a href="cursos/">Cursos</a><a href="privacidade.html">Privacidade</a><a href="termos.html">Termos de uso</a></nav></div></footer>
</body>
</html>
"""
    open(os.path.join(R, fn), "w", encoding="utf-8").write(html)

CONTATO = 'WhatsApp <a href="https://wa.me/5511982664943" target="_blank" rel="noopener">(11) 98266-4943</a> ou Instagram <a href="https://www.instagram.com/edils.ondavid/" target="_blank" rel="noopener">@edils.ondavid</a>'

page("privacidade.html", "Política de Privacidade – Grade UFSC",
 "Como a Grade UFSC trata informações pessoais, em conformidade com a LGPD e o Marco Civil da Internet.",
 "Documento legal", "Política de Privacidade",
 "Como a Grade UFSC trata informações ao usar o site e o aplicativo, de acordo com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018) e o Marco Civil da Internet (Lei nº 12.965/2014).",
 ["Não pedimos cadastro, nome, e-mail nem senha.",
  "Seu progresso fica <b>somente no seu aparelho</b>. Nós não recebemos nem armazenamos essas informações.",
  "Não usamos cookies de rastreamento, anúncios nem ferramentas de análise de audiência.",
  "Você pode apagar tudo quando quiser, direto no site ou no navegador."],
 [("controlador","Quem somos",
   "<p>A Grade UFSC é um projeto independente, gratuito e sem fins lucrativos, desenvolvido por estudante em parceria com a Uni-lux. O projeto <b>não tem vínculo oficial com a Universidade Federal de Santa Catarina</b>.</p><p>Para assuntos desta política, fale conosco pelos canais da seção <a href=\"#contato\">Contato</a>.</p>"),
  ("dados","Informações guardadas no seu aparelho",
   "<p>Para funcionar, o site usa o armazenamento local (<i>localStorage</i>) do seu navegador. Nada disso é enviado para nós.</p><table><thead><tr><th>Informação</th><th>Para quê</th><th>Onde fica</th></tr></thead><tbody>"
   "<tr><td><b>Situação das disciplinas</b> (aprovada, validada, cursando, reprovada) e optativas escolhidas</td><td>Mostrar seu progresso e o que você pode cursar</td><td>Seu navegador, separado por curso</td></tr>"
   "<tr><td><b>Último curso aberto</b></td><td>Reabrir o mesmo curso</td><td>Seu navegador</td></tr>"
   "<tr><td><b>Fase atual</b> indicada por você</td><td>Destacar “Você está aqui” no mapa</td><td>Seu navegador</td></tr>"
   "<tr><td><b>Tema</b> (claro ou escuro)</td><td>Manter a aparência escolhida</td><td>Seu navegador</td></tr>"
   "<tr><td><b>Cópia das páginas e imagens</b> (app instalado)</td><td>Abrir sem internet</td><td>Cache do aparelho, sem dados pessoais</td></tr>"
   "</tbody></table><p>Se você limpar os dados do navegador, desinstalar o app ou trocar de aparelho, essas informações são perdidas e não podem ser recuperadas por nós.</p>"),
  ("terceiros","Serviços de terceiros",
   "<ul><li><b>Hospedagem (GitHub Pages):</b> ao acessar qualquer site, o servidor recebe dados técnicos da conexão (endereço IP, navegador, data e hora) para entregar as páginas e manter a segurança. Esse tratamento é feito pelo GitHub, conforme a política de privacidade dele.</li>"
   "<li><b>Fontes (Google Fonts):</b> a fonte do texto é carregada dos servidores do Google, que recebem seu IP e dados do navegador para entregar o arquivo.</li>"
   "<li><b>Links externos:</b> WhatsApp, Instagram e outros sites mencionados são serviços independentes, com suas próprias políticas. Não temos controle sobre eles.</li></ul>"),
  ("contato-voluntario","Quando você entra em contato",
   "<p>Se você nos procurar (por exemplo, para pedir um curso ou relatar um erro), receberemos apenas o que você mesmo enviar: nome, telefone ou usuário, mensagem e eventuais arquivos, como o PDF do currículo.</p><p>Usamos essas informações só para responder e melhorar o site, com base no seu consentimento e no legítimo interesse (art. 7º, I e IX, da LGPD). Não vendemos nem compartilhamos, e apagamos quando deixam de ser necessárias ou quando você pedir.</p>"),
  ("nao-fazemos","O que não fazemos",
   "<ul><li>Não criamos contas nem pedimos login.</li><li>Não usamos cookies de publicidade, pixels de rastreamento nem estatísticas de acesso.</li><li>Não vendemos, alugamos nem compartilhamos dados pessoais.</li><li>Não tomamos decisões automatizadas sobre você.</li></ul>"),
  ("direitos","Seus direitos",
   "<p>Pela LGPD (art. 18), você pode pedir: confirmação de que tratamos seus dados, acesso, correção, anonimização ou eliminação, portabilidade, informação sobre compartilhamento e revogação do consentimento.</p><p>Como o progresso fica só no seu aparelho, você mesmo pode vê-lo e apagá-lo a qualquer momento pelo botão <b>“Apagar progresso deste curso”</b>. Você também pode apresentar reclamação à Autoridade Nacional de Proteção de Dados (ANPD).</p>"),
  ("seguranca","Segurança",
   "<p>O site usa conexão segura (HTTPS), política de segurança de conteúdo que bloqueia scripts de terceiros e o envio de dados para fora, e não pode ser aberto dentro de outros sites. Nenhum sistema é totalmente imune a falhas: mantenha seu navegador e aparelho atualizados.</p>"),
  ("menores","Crianças e adolescentes",
   "<p>O site é voltado a estudantes de graduação e não coleta dados pessoais no uso normal, por isso pode ser usado com segurança por qualquer idade.</p>"),
  ("alteracoes","Alterações desta política",
   "<p>Podemos atualizar esta política para refletir mudanças no site ou na lei. A data de atualização no topo indica a versão vigente. Se o site passar a coletar novos dados, esta página será atualizada antes.</p>"),
  ("contato","Contato",
   f"<p>Dúvidas, pedidos sobre dados pessoais ou relatos de problemas: {CONTATO}.</p>"),
 ])

page("termos.html", "Termos de Uso – Grade UFSC",
 "Regras de uso da Grade UFSC: o que o serviço oferece, limites de responsabilidade, propriedade intelectual e parceria.",
 "Documento legal", "Termos de Uso",
 "Ao usar a Grade UFSC (site ou aplicativo) você concorda com estes termos. Se não concordar, não utilize o serviço.",
 ["O serviço é gratuito e serve para <b>apoiar o planejamento</b> do seu curso.",
  "Não é um site oficial da UFSC. <b>Confira sempre o currículo no CAGR</b> e com a coordenação.",
  "É proibido copiar, clonar ou republicar o site em outro endereço.",
  "Projeto independente, desenvolvido em parceria com a Uni-lux."],
 [("servico","O serviço",
   "<p>A Grade UFSC é uma ferramenta gratuita para visualizar as disciplinas de cada fase dos cursos de graduação da UFSC, seus pré-requisitos e o seu progresso. Inclui mapa interativo, marcação individual e em lote, indicação da fase atual, ranking das disciplinas que mais travam o curso e páginas de consulta por curso.</p>"),
  ("vinculo","Sem vínculo oficial",
   "<p>A Grade UFSC é um projeto independente e <b>não é mantida, endossada nem representa</b> a Universidade Federal de Santa Catarina. Os nomes “UFSC”, “Universidade Federal de Santa Catarina” e “CAGR” pertencem aos seus titulares e são citados apenas para identificar a instituição e os cursos. Ferramentas externas eventualmente indicadas no site também não têm vínculo nem parceria com o projeto.</p>"),
  ("precisao","Precisão das informações",
   "<p>Os dados foram extraídos dos currículos publicados no CAGR (consulta em novembro de 2026) e podem conter erros, estar desatualizados ou não refletir regras específicas, como quebras de pré-requisito, equivalências, validações e mudanças de currículo.</p><p class=\"note\"><b>Importante:</b> o site é uma ferramenta de apoio. A responsabilidade pela matrícula e pela conferência com o currículo oficial e a coordenação do curso é do estudante.</p>"),
  ("responsabilidade","Limitação de responsabilidade",
   "<p>O serviço é oferecido “no estado em que se encontra”, sem garantia de disponibilidade contínua ou de ausência de erros. Na máxima extensão permitida pela lei, os responsáveis pelo projeto não respondem por prejuízos acadêmicos ou de qualquer natureza decorrentes do uso das informações, como problemas de matrícula, perda de prazos ou atraso na formatura, nem pela perda das marcações salvas no navegador.</p>"),
  ("uso","Uso permitido e proibido",
   "<h3>Você pode</h3><ul><li>usar o site e o aplicativo para fins pessoais e acadêmicos;</li><li>compartilhar o link oficial com colegas.</li></ul><h3>Não é permitido</h3><ul><li>copiar, clonar ou republicar o site, seu código, layout ou identidade visual em outro endereço, ou exibi-lo dentro de outros sites;</li><li>injetar código, explorar falhas, sobrecarregar o serviço ou burlar as proteções;</li><li>apresentar o conteúdo como oficial da UFSC ou usá-lo de forma enganosa.</li></ul><p>Se encontrar uma falha de segurança, avise pelos canais de contato.</p>"),
  ("propriedade","Propriedade intelectual",
   "<p>O código, o design, a marca “Grade UFSC” e sua logo, as páginas e os textos pertencem aos responsáveis pelo projeto. A marca e a logo <b>Uni-lux</b> pertencem à Uni-lux. As informações curriculares são de natureza pública e foram organizadas pelo projeto.</p>"),
  ("parceria","Parceria e participação",
   "<p>O projeto é desenvolvido em parceria com a <span class=\"ulx\"><img src=\"unilux.svg\" alt=\"\" width=\"18\" height=\"18\"><span>Uni<em>-lux</em></span></span>. Estudantes podem colaborar enviando currículos de novos cursos ou relatando erros. Ao enviar material, você declara que pode compartilhá-lo e autoriza seu uso, sem remuneração, para manter e melhorar o site.</p>"),
  ("privacidade","Privacidade",
   "<p>O tratamento de informações está descrito na <a href=\"privacidade.html\">Política de Privacidade</a>, que faz parte destes termos.</p>"),
  ("alteracoes","Alterações",
   "<p>Estes termos podem ser atualizados. A data no topo indica a versão vigente. O uso continuado após a atualização significa concordância com a nova versão.</p>"),
  ("lei","Lei aplicável",
   "<p>Aplicam-se as leis da República Federativa do Brasil, incluindo o Código de Defesa do Consumidor no que couber. Fica eleito o foro do domicílio do usuário para resolver eventuais controvérsias.</p>"),
  ("contato","Contato",
   f"<p>{CONTATO}.</p>"),
 ])
print("ok")
