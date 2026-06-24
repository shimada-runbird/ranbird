#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build AI HP sales deck v5 — presentation-grade, not web page."""
from pathlib import Path

OUT = Path(__file__).parent / "index.html"
M = "di" + "v"
o, c = f"<{M}", f"</{M}>"

def hd(n):
    return f'<header class="sh"><span class="brand">RUNBIRD</span><span class="pg num">{n:02d}</span></header>'

CSS = r"""
:root{
  --n0:#02060c;--n1:#061826;--n2:#0a2a3d;--n3:#0d4a55;
  --w:#f8fafc;--sub:#a8c8d4;--mute:#5a8a9a;
  --o:#ff8a00;--y:#ffd84d;--r:#ff4d4d;--c:#34d5ff;--lg:#06c755;
  --nav:40px;
  --slide-w:min(96vw,1280px);
  --pad:clamp(28px,3.8vw,48px);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden}
body{font-family:"Noto Sans JP",sans-serif;background:var(--n0);color:var(--w);-webkit-font-smoothing:antialiased}
.num{font-family:Outfit,sans-serif}
.nav{position:fixed;inset:0 0 auto;z-index:999;height:var(--nav);display:flex;align-items:center;gap:1px;padding:0 8px;background:rgba(2,6,12,.97);border-bottom:1px solid rgba(255,255,255,.06)}
.nav .logo{margin-right:auto;font-family:Outfit,sans-serif;font-size:.58rem;font-weight:800;letter-spacing:.16em;color:var(--o)}
.nav a{color:var(--mute);text-decoration:none;font-family:Outfit,sans-serif;font-size:.52rem;font-weight:700;padding:2px 4px}
.nav a:hover{color:var(--w)}
.viewport{position:fixed;top:var(--nav);left:0;right:0;bottom:0;overflow-y:auto;scroll-snap-type:y mandatory;background:#000}
.deck{display:flex;flex-direction:column;align-items:center;padding:8px 0 16px;gap:10px}

/* === SLIDE SHELL: fixed 16:9 presentation canvas === */
.sl{
  scroll-snap-align:start;scroll-snap-stop:always;
  width:var(--slide-w);
  aspect-ratio:16/9;
  max-height:calc(100vh - var(--nav) - 16px);
  position:relative;overflow:hidden;
  display:grid;
  grid-template-rows:auto 1fr;
  padding:var(--pad);
  border:1px solid rgba(255,255,255,.08);
  box-shadow:0 32px 100px rgba(0,0,0,.65);
  page-break-after:always;
}
.sl>*{position:relative;z-index:2}
.sl .bg{position:absolute;inset:0;z-index:0;pointer-events:none}
.sl .frame{position:absolute;inset:10px;border:1px solid rgba(255,255,255,.05);pointer-events:none;z-index:1;border-radius:2px}

.sh{display:flex;justify-content:space-between;align-items:center;margin-bottom:clamp(8px,1.2vh,14px)}
.sh .brand{font-family:Outfit,sans-serif;font-size:.55rem;font-weight:800;letter-spacing:.2em;color:var(--c)}
.sh .pg{font-family:Outfit,sans-serif;font-size:.6rem;font-weight:700;color:var(--mute)}
.body{min-height:0;display:flex;flex-direction:column;justify-content:center;flex:1}

/* backgrounds by role */
.bg-cover{background:radial-gradient(ellipse 90% 70% at 70% 20%,rgba(52,213,255,.22),transparent 50%),radial-gradient(ellipse 60% 50% at 10% 90%,rgba(255,138,0,.18),transparent 45%),linear-gradient(155deg,#02060c,#061826 40%,#0a3d4a 75%,#0d4a55)}
.bg-quiet{background:linear-gradient(160deg,#0a1420,#0f2435 60%,#122a3a)}
.bg-camp{background:radial-gradient(circle at 50% 30%,rgba(255,216,77,.15),transparent 45%),linear-gradient(165deg,#1a0800,#061826,#0a2040)}
.bg-alert{background:linear-gradient(165deg,#080810,#0a1628 50%,#180800)}
.bg-hero{background:linear-gradient(145deg,#061826,#0a2840 50%,#0d2030)}
.bg-price{background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(255,216,77,.12),transparent 50%),linear-gradient(180deg,#0a1a28,#02060c)}
.bg-close{background:radial-gradient(circle at 40% 25%,rgba(255,138,0,.2),transparent 40%),linear-gradient(150deg,#1a0e00,#061826,#0a2a3d)}

/* typography */
.cat{font-size:clamp(.48rem,.65vw,.58rem);font-weight:800;letter-spacing:.28em;color:var(--c);text-transform:uppercase}
.h-xl{font-size:clamp(2rem,4.8vw,4.2rem);font-weight:900;line-height:1.05;letter-spacing:-.02em}
.h-lg{font-size:clamp(1.35rem,2.6vw,2.1rem);font-weight:900;line-height:1.1}
.h-md{font-size:clamp(1rem,1.8vw,1.35rem);font-weight:900;line-height:1.2}
.sub{font-size:clamp(.62rem,.85vw,.75rem);color:var(--sub);line-height:1.45}
.mini{font-size:clamp(.46rem,.6vw,.54rem);color:var(--mute)}
.mark{background:linear-gradient(transparent 55%,rgba(255,216,77,.6) 55%)}
.num-xl{font-family:Outfit,sans-serif;font-size:clamp(3.5rem,9vw,8.75rem);font-weight:900;line-height:.9;letter-spacing:-.03em}
.num-lg{font-family:Outfit,sans-serif;font-size:clamp(2.2rem,5.5vw,5.5rem);font-weight:900;line-height:1}
.num-md{font-family:Outfit,sans-serif;font-size:clamp(1.6rem,3.5vw,3.2rem);font-weight:900;line-height:1}
.accent-o{color:var(--o)}.accent-y{color:var(--y)}.accent-c{color:var(--c)}.accent-r{color:var(--r)}
.glow-t{text-shadow:0 0 60px rgba(52,213,255,.35),0 0 120px rgba(52,213,255,.15)}

/* layouts */
.split{display:grid;grid-template-columns:1fr 1fr;gap:clamp(16px,3vw,32px);align-items:center;height:100%}
.split-55{grid-template-columns:1.1fr .9fr}
.split-45{grid-template-columns:.9fr 1.1fr}
.center-col{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:clamp(10px,1.5vh,16px);height:100%}

/* cover */
.cover-left{display:flex;flex-direction:column;justify-content:center;gap:clamp(12px,2vh,20px)}
.tags{display:flex;flex-wrap:wrap;gap:8px}
.tag{padding:8px 16px;border-radius:8px;font-size:clamp(.58rem,.8vw,.7rem);font-weight:800;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);backdrop-filter:blur(8px)}
.wave-b{position:absolute;bottom:0;left:0;right:0;height:22%;opacity:.45;z-index:1}

/* quiet company */
.stat-row{display:flex;gap:clamp(20px,4vw,48px);justify-content:center;align-items:flex-end;margin-bottom:clamp(16px,2.5vh,24px)}
.stat-item{text-align:center}
.stat-item .num-lg{color:var(--y)}
.stat-item .lbl{font-size:clamp(.55rem,.75vw,.65rem);font-weight:700;color:var(--sub);margin-top:6px}
.map-svg{width:100%;max-height:clamp(80px,14vh,120px);opacity:.85}

/* campaign slots */
.limit-mega{font-size:clamp(2rem,5.5vw,4.5rem);font-weight:900;line-height:1.05;color:var(--y);text-shadow:0 0 80px rgba(255,216,77,.35);max-width:14ch}
.slot-bar{display:flex;gap:clamp(8px,1.2vw,14px);width:100%;max-width:640px}
.slot-item{flex:1;text-align:center;padding:clamp(12px,1.5vw,16px) 6px;border-radius:12px;border:2px solid rgba(255,255,255,.15);background:rgba(0,0,0,.35)}
.slot-item.hot{border-color:var(--y);box-shadow:0 0 30px rgba(255,216,77,.2)}
.slot-item .nm{font-size:clamp(.58rem,.8vw,.68rem);font-weight:800}
.slot-item .st{font-size:clamp(.46rem,.6vw,.52rem);font-weight:900;margin-top:6px;padding:3px 8px;border-radius:4px;display:inline-block}
.slot-item .st.ok{background:rgba(52,213,255,.35)}.slot-item .st.ng{background:rgba(100,100,100,.4);opacity:.7}
.cond-strip{display:flex;gap:clamp(12px,2vw,20px);flex-wrap:wrap;justify-content:center}
.cond-strip span{font-size:clamp(.52rem,.72vw,.62rem);font-weight:700;padding:6px 12px;background:rgba(255,255,255,.08);border-radius:6px}

/* pyramid + hub */
.diagram-row{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(16px,2.5vw,28px);align-items:center;height:100%}
.pyramid{display:flex;flex-direction:column;align-items:center;gap:5px}
.pyr{width:100%;padding:clamp(8px,1vh,12px);text-align:center;font-weight:800;font-size:clamp(.52rem,.75vw,.65rem);color:#fff;border-radius:8px}
.pyr.a{width:100%;background:linear-gradient(90deg,#8b2020,#c0392b)}
.pyr.b{width:85%;background:linear-gradient(90deg,#1a5276,#2980b9)}
.pyr.c{width:68%;background:linear-gradient(90deg,#c45c00,var(--o));box-shadow:0 0 40px rgba(255,138,0,.4)}

/* crisis stats */
.crisis-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,2vw,20px);margin:clamp(12px,2vh,20px) 0}
.crisis-box{text-align:center;padding:clamp(16px,2vw,24px) 8px 0;border-top:4px solid var(--c)}
.crisis-box:nth-child(2){border-color:var(--y)}.crisis-box:nth-child(3){border-color:var(--r)}
.crisis-box .lbl{margin-top:8px}
.banner-crisis{text-align:center;font-size:clamp(.9rem,1.6vw,1.15rem);font-weight:900;color:var(--y);letter-spacing:.08em;margin-top:clamp(8px,1.5vh,14px)}

/* before after split */
.ba-split{display:grid;grid-template-columns:1fr 48px 1fr;align-items:stretch;height:100%;gap:0}
.ba-pane{padding:clamp(14px,2vw,20px);display:flex;flex-direction:column;gap:8px;border-radius:14px}
.ba-pane.bad{background:linear-gradient(145deg,rgba(40,45,55,.9),rgba(30,35,45,.95));border:1px solid rgba(120,130,150,.25)}
.ba-pane.good{background:linear-gradient(145deg,rgba(52,213,255,.08),rgba(255,138,0,.06));border:1px solid rgba(255,138,0,.35);box-shadow:0 0 40px rgba(255,138,0,.1)}
.ba-pane h3{font-size:clamp(.7rem,1vw,.82rem);font-weight:900;margin-bottom:4px}
.ba-pane.bad h3{color:#94a3b8}.ba-pane.good h3{color:var(--y)}
.ba-line{font-size:clamp(.52rem,.72vw,.62rem);font-weight:700;padding:8px 10px;border-radius:8px;background:rgba(0,0,0,.25)}
.ba-arrow{display:flex;align-items:center;justify-content:center;font-size:clamp(1.8rem,3vw,2.4rem);color:var(--o);font-weight:900}

/* focus dual */
.focus-split{display:grid;grid-template-columns:.95fr 1.05fr;gap:clamp(24px,4vw,48px);align-items:center;height:100%}
.chk{list-style:none}
.chk li{font-size:clamp(.68rem,.95vw,.78rem);font-weight:800;padding:clamp(10px,1.2vh,14px) 0;border-bottom:1px solid rgba(255,255,255,.07);display:flex;gap:10px}
.chk li::before{content:"✓";color:var(--y);font-weight:900;font-size:1.15em}
.word-stack{display:flex;flex-direction:column;gap:clamp(14px,2.5vh,22px)}
.word-huge{font-size:clamp(2.2rem,5.2vw,4rem);font-weight:900;line-height:1.05}

/* speed compare */
.speed-split{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,3.5vw,36px);align-items:center;height:100%}
.bar-compare{width:100%}
.bar-row{margin-bottom:clamp(14px,2vh,18px)}
.bar-lbl{font-size:clamp(.55rem,.75vw,.65rem);font-weight:800;color:var(--sub);margin-bottom:6px}
.bar-track{height:clamp(36px,5.5vh,52px);background:rgba(0,0,0,.45);border-radius:10px;overflow:hidden}
.bar-fill{height:100%;display:flex;align-items:center;padding-left:14px;font-weight:900;font-size:clamp(.62rem,.85vw,.72rem)}
.bar-fill.slow{width:92%;background:linear-gradient(90deg,#4a5568,#2d3748);color:var(--sub)}
.bar-fill.fast{width:32%;min-width:9em;background:linear-gradient(90deg,var(--o),var(--y));color:#1a0a00;box-shadow:0 0 30px rgba(255,138,0,.4)}
.copy-mega{font-size:clamp(1.3rem,2.6vw,1.9rem);font-weight:900;color:var(--y);margin-top:12px}
.badge-pill{display:inline-block;margin-top:10px;padding:10px 22px;border-radius:999px;background:var(--y);color:#1a1000;font-size:clamp(.62rem,.85vw,.72rem);font-weight:900}

/* price towers */
.price-stage{display:flex;align-items:flex-end;justify-content:center;gap:clamp(10px,2vw,18px);flex:1}
.tower{flex:1;max-width:240px;text-align:center;padding:clamp(16px,2vw,24px) clamp(10px,1.2vw,14px);border-radius:16px;background:rgba(0,0,0,.4);border:1px solid rgba(255,255,255,.1)}
.tower.featured{flex:1.15;transform:scale(1.08);border:2px solid var(--o);background:linear-gradient(180deg,rgba(255,138,0,.15),rgba(0,0,0,.5));box-shadow:0 0 60px rgba(255,138,0,.25)}
.tower .plan{font-size:clamp(.75rem,1.1vw,.9rem);font-weight:900}
.tower .plan-en{font-family:Outfit,sans-serif;font-size:clamp(.46rem,.6vw,.54rem);letter-spacing:.2em;color:var(--mute);margin:2px 0 10px}
.tower.featured .plan-en{color:rgba(255,138,0,.9)}
.tower .price{font-family:Outfit,sans-serif;font-size:clamp(1.6rem,3.2vw,4.5rem);font-weight:900;color:var(--o);line-height:1}
.tower.featured .price{font-size:clamp(2rem,4.5vw,5.5rem)}
.tower .init{font-size:clamp(.48rem,.65vw,.58rem);color:var(--sub);margin-top:8px}
.rec-star{display:inline-block;margin-bottom:8px;padding:5px 12px;border-radius:6px;background:var(--o);font-size:clamp(.48rem,.62vw,.56rem);font-weight:900}

/* campaign close */
.close-stage{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:clamp(6px,1vh,10px);height:100%}
.close-stage .limit{font-size:clamp(.62rem,.88vw,.75rem);font-weight:900;color:var(--y);letter-spacing:.16em}
.off-ring{width:clamp(110px,17vw,160px);height:clamp(110px,17vw,160px);border-radius:50%;border:6px solid var(--y);display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 80px rgba(255,216,77,.35),inset 0 0 40px rgba(255,216,77,.08)}
.off-ring .pct{font-family:Outfit,sans-serif;font-size:clamp(2.2rem,5vw,3.8rem);font-weight:900;color:var(--y);line-height:1}
.price-block .was{font-size:clamp(1rem,1.8vw,1.35rem);text-decoration:line-through;opacity:.45;color:var(--sub)}
.price-block .now{font-family:Outfit,sans-serif;font-size:clamp(3rem,7.5vw,7.5rem);font-weight:900;color:var(--c);line-height:.95;text-shadow:0 0 80px rgba(52,213,255,.3)}
.price-row{display:flex;align-items:center;justify-content:center;gap:clamp(24px,5vw,56px);margin:clamp(8px,1.5vh,14px) 0}

/* CTA */
.cta{display:inline-block;padding:clamp(14px,1.8vh,18px) clamp(36px,5vw,56px);border-radius:14px;background:linear-gradient(135deg,var(--o),#e07000);color:#fff;font-size:clamp(.78rem,1.1vw,.92rem);font-weight:900;text-decoration:none;letter-spacing:.1em;box-shadow:0 16px 50px rgba(255,138,0,.5),0 0 0 1px rgba(255,255,255,.1)}
.steps{display:flex;align-items:center;gap:6px;flex-wrap:wrap;justify-content:center}
.step{font-size:clamp(.52rem,.72vw,.62rem);font-weight:800;padding:8px 14px;border-radius:8px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1)}
.step-ar{color:var(--o);font-weight:900}

/* SVG containers */
.svg-main{width:100%;height:100%;max-height:min(42vh,340px)}
.svg-flow{width:100%;max-height:clamp(100px,16vh,140px)}

@media print{
  .nav{display:none}.viewport{position:static;overflow:visible}
  .sl{max-height:none;width:100%;page-break-after:always;-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
@media(max-width:800px){
  .split,.split-55,.split-45,.diagram-row,.ba-split,.focus-split,.speed-split{grid-template-columns:1fr}
  .ba-arrow{display:none}.crisis-grid{grid-template-columns:1fr}
}
"""

# SVG assets
SVG_COVER = """<svg class="svg-main" viewBox="0 0 420 380" aria-hidden="true">
<defs>
  <linearGradient id="go" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ff8a00"/><stop offset="100%" stop-color="#ffd84d"/></linearGradient>
  <filter id="glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <radialGradient id="hubg" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(52,213,255,.3)"/><stop offset="100%" stop-color="transparent"/></radialGradient>
</defs>
<circle cx="210" cy="190" r="120" fill="url(#hubg)"/>
<circle cx="210" cy="190" r="100" fill="none" stroke="rgba(52,213,255,.25)" stroke-width="2" stroke-dasharray="8 6"/>
<rect x="155" y="145" width="110" height="90" rx="14" fill="#fff" filter="url(#glow)"/>
<rect x="168" y="195" width="50" height="26" rx="8" fill="url(#go)"/>
<text x="193" y="212" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">問合せ</text>
<circle cx="75" cy="75" r="38" fill="url(#go)"/><text x="75" y="72" fill="#fff" font-size="16" font-weight="bold" text-anchor="middle">AI</text><text x="75" y="88" fill="#fff" font-size="8" text-anchor="middle">検索</text>
<circle cx="350" cy="80" r="34" fill="#4285f4"/><text x="350" y="86" fill="#fff" font-size="14" font-weight="bold" text-anchor="middle">G</text>
<rect x="320" y="240" width="56" height="100" rx="14" fill="#0a2838" stroke="#06c755" stroke-width="2"/>
<rect x="328" y="255" width="40" height="65" rx="6" fill="#fff"/><rect x="336" y="310" width="24" height="10" rx="4" fill="#06c755"/>
<text x="348" y="232" fill="#06c755" font-size="9" font-weight="bold" text-anchor="middle">LINE</text>
<ellipse cx="60" cy="280" rx="28" ry="28" fill="none" stroke="#ff8a00" stroke-width="2.5"/>
<text x="60" y="286" fill="#fff" font-size="18" text-anchor="middle">📞</text>
<rect x="300" y="55" width="36" height="36" rx="8" fill="#ea4335" opacity=".9"/><text x="318" y="78" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">MAP</text>
<path d="M113 115 Q150 105 155 145" stroke="#ffd84d" stroke-width="2.5" fill="none" marker-end="url(#ar)"/>
<path d="M265 155 Q310 100 318 75" stroke="#93c5fd" stroke-width="2.5" fill="none"/>
<path d="M265 175 Q310 210 328 255" stroke="#6ee7a0" stroke-width="2.5" fill="none"/>
<path d="M88 265 Q120 220 155 200" stroke="#ff8a00" stroke-width="2.5" fill="none"/>
<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffd84d"/></marker></defs>
</svg>"""

SVG_MAP = """<svg class="map-svg" viewBox="0 0 400 120" aria-hidden="true">
<path d="M80,80 Q120,40 200,50 Q280,60 320,75 L340,90 Q300,100 200,95 Q100,90 80,80Z" fill="rgba(52,213,255,.08)" stroke="rgba(52,213,255,.25)" stroke-width="1.5"/>
<circle cx="280" cy="55" r="8" fill="#ff8a00"/><text x="280" y="72" fill="#fff" font-size="8" text-anchor="middle" font-weight="bold">東京</text>
<circle cx="200" cy="62" r="8" fill="#ff8a00"/><text x="200" y="79" fill="#fff" font-size="8" text-anchor="middle" font-weight="bold">大阪</text>
<circle cx="130" cy="70" r="8" fill="#ff8a00"/><text x="130" y="87" fill="#fff" font-size="8" text-anchor="middle" font-weight="bold">福岡</text>
<circle cx="95" cy="85" r="8" fill="#ff8a00"/><text x="95" y="102" fill="#fff" font-size="8" text-anchor="middle" font-weight="bold">沖縄</text>
</svg>"""

SVG_HUB = """<svg class="svg-main" viewBox="0 0 400 360" aria-hidden="true">
<defs><linearGradient id="hc" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ff8a00"/><stop offset="100%" stop-color="#ffd84d"/></linearGradient></defs>
<ellipse cx="200" cy="180" rx="150" ry="140" fill="none" stroke="rgba(52,213,255,.15)" stroke-width="2"/>
<circle cx="200" cy="180" r="55" fill="url(#hc)" filter="url(#glow)"/><text x="200" y="175" fill="#1a0a00" font-size="11" font-weight="bold" text-anchor="middle">AI</text><text x="200" y="190" fill="#1a0a00" font-size="11" font-weight="bold" text-anchor="middle">HP</text>
<rect x="165" y="25" width="70" height="32" rx="16" fill="rgba(0,0,0,.5)" stroke="rgba(255,255,255,.2)"/><text x="200" y="46" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Google</text>
<rect x="310" y="100" width="70" height="32" rx="16" fill="rgba(0,0,0,.5)" stroke="rgba(255,255,255,.2)"/><text x="345" y="121" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">AI検索</text>
<rect x="310" y="230" width="70" height="32" rx="16" fill="rgba(0,0,0,.5)" stroke="rgba(255,255,255,.2)"/><text x="345" y="251" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">MEO</text>
<rect x="165" y="305" width="70" height="32" rx="16" fill="rgba(0,0,0,.5)" stroke="#06c755"/><text x="200" y="326" fill="#06c755" font-size="10" font-weight="bold" text-anchor="middle">LINE</text>
<rect x="20" y="160" width="70" height="32" rx="16" fill="rgba(0,0,0,.5)" stroke="#ff8a00"/><text x="55" y="181" fill="#ff8a00" font-size="10" font-weight="bold" text-anchor="middle">電話</text>
<path d="M200 57 Q200 120 200 125" stroke="#93c5fd" stroke-width="2" fill="none"/><path d="M310 116 Q250 150 255 180" stroke="#ffd84d" stroke-width="2" fill="none"/>
<path d="M310 246 Q250 210 255 180" stroke="#6ee7a0" stroke-width="2" fill="none"/><path d="M200 305 Q200 240 200 235" stroke="#06c755" stroke-width="2" fill="none"/>
<path d="M90 176 Q130 180 145 180" stroke="#ff8a00" stroke-width="2" fill="none"/>
</svg>"""

SVG_FLOW = """<svg class="svg-flow" viewBox="0 0 700 100" aria-hidden="true">
<rect x="10" y="20" width="120" height="60" rx="12" fill="rgba(0,0,0,.4)" stroke="rgba(255,255,255,.15)"/>
<text x="70" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">AIに質問</text>
<path d="M140 50 H170" stroke="#ffd84d" stroke-width="3" marker-end="url(#a2)"/>
<rect x="180" y="20" width="120" height="60" rx="12" fill="rgba(255,138,0,.15)" stroke="#ff8a00"/>
<text x="240" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">マップ比較</text>
<path d="M310 50 H340" stroke="#ffd84d" stroke-width="3" marker-end="url(#a2)"/>
<rect x="350" y="20" width="120" height="60" rx="12" fill="rgba(52,213,255,.12)" stroke="#34d5ff"/>
<text x="410" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">HPで信頼</text>
<path d="M480 50 H510" stroke="#ffd84d" stroke-width="3" marker-end="url(#a2)"/>
<rect x="520" y="20" width="160" height="60" rx="12" fill="rgba(6,199,85,.15)" stroke="#06c755"/>
<text x="600" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">LINE / 電話</text>
<defs><marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffd84d"/></marker></defs>
</svg>"""

SVG_CYCLE = """<svg class="svg-main" viewBox="0 0 360 360" aria-hidden="true">
<defs><linearGradient id="cc" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ff8a00"/><stop offset="100%" stop-color="#ffd84d"/></linearGradient></defs>
<circle cx="180" cy="180" r="130" fill="none" stroke="rgba(255,138,0,.4)" stroke-width="3" stroke-dasharray="12 8"/>
<circle cx="180" cy="180" r="58" fill="url(#cc)"/><text x="180" y="172" fill="#1a0a00" font-size="10" font-weight="bold" text-anchor="middle">問い合わせが</text><text x="180" y="188" fill="#1a0a00" font-size="10" font-weight="bold" text-anchor="middle">来るHP</text>
<rect x="140" y="20" width="80" height="36" rx="10" fill="rgba(0,0,0,.45)" stroke="rgba(255,255,255,.2)"/><text x="180" y="43" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">①導線設計</text>
<rect x="20" y="250" width="80" height="36" rx="10" fill="rgba(0,0,0,.45)" stroke="rgba(255,255,255,.2)"/><text x="60" y="273" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">②信頼設計</text>
<rect x="260" y="250" width="80" height="36" rx="10" fill="rgba(0,0,0,.45)" stroke="rgba(255,255,255,.2)"/><text x="300" y="273" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">③継続更新</text>
<path d="M180 56 Q220 100 250 150" stroke="#34d5ff" stroke-width="2" fill="none" marker-end="url(#mc)"/>
<path d="M250 200 Q200 250 100 260" stroke="#34d5ff" stroke-width="2" fill="none"/>
<path d="M100 220 Q120 120 180 56" stroke="#34d5ff" stroke-width="2" fill="none"/>
<defs><marker id="mc" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#34d5ff"/></marker></defs>
</svg>"""

SVG_PHONE_LINE = """<svg class="svg-main" viewBox="0 0 500 320" aria-hidden="true">
<rect x="20" y="30" width="100" height="200" rx="18" fill="#0a2838" stroke="#06c755" stroke-width="3"/>
<rect x="32" y="50" width="76" height="140" rx="6" fill="#fff"/>
<rect x="40" y="60" width="50" height="8" rx="4" fill="#06c755" opacity=".6"/>
<rect x="40" y="75" width="60" height="6" rx="3" fill="#ddd"/>
<rect x="40" y="88" width="55" height="6" rx="3" fill="#ddd"/>
<text x="70" y="250" fill="#06c755" font-size="10" font-weight="bold" text-anchor="middle">LINE送信</text>
<path d="M130 130 H180" stroke="#ffd84d" stroke-width="3" marker-end="url(#pl)"/>
<circle cx="250" cy="130" r="50" fill="rgba(255,138,0,.2)" stroke="#ff8a00" stroke-width="2"/>
<text x="250" y="125" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">運用</text><text x="250" y="140" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">チーム</text>
<path d="M310 130 H360" stroke="#ffd84d" stroke-width="3" marker-end="url(#pl)"/>
<rect x="370" y="30" width="110" height="200" rx="8" fill="#fff" stroke="#34d5ff" stroke-width="2"/>
<rect x="382" y="45" width="86" height="12" rx="2" fill="#0a2838"/>
<rect x="382" y="65" width="86" height="40" rx="4" fill="#f0f4f8"/>
<rect x="382" y="115" width="60" height="24" rx="6" fill="url(#go)"/>
<text x="425" y="250" fill="#34d5ff" font-size="10" font-weight="bold" text-anchor="middle">HP反映</text>
<rect x="400" y="5" width="90" height="24" rx="6" fill="rgba(52,213,255,.25)" stroke="#34d5ff"/>
<text x="445" y="21" fill="#34d5ff" font-size="8" font-weight="bold" text-anchor="middle">検索評価↑</text>
<defs><marker id="pl" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffd84d"/></marker></defs>
</svg>"""

SVG_SEO = """<svg class="svg-main" viewBox="0 0 420 280" aria-hidden="true">
<rect x="150" y="90" width="120" height="100" rx="12" fill="#fff" stroke="#ff8a00" stroke-width="2"/>
<text x="210" y="130" fill="#0a1628" font-size="12" font-weight="bold" text-anchor="middle">御社のHP</text>
<text x="210" y="150" fill="#0a1628" font-size="9" text-anchor="middle">信頼の受け皿</text>
<rect x="20" y="110" width="90" height="40" rx="20" fill="#4285f4"/><text x="65" y="135" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Google</text>
<rect x="310" y="110" width="90" height="40" rx="20" fill="url(#go)"/><text x="355" y="135" fill="#1a0a00" font-size="11" font-weight="bold" text-anchor="middle">ChatGPT</text>
<path d="M110 130 H145" stroke="#93c5fd" stroke-width="3" marker-end="url(#se)"/>
<path d="M310 130 H270" stroke="#ffd84d" stroke-width="3" marker-end="url(#se)"/>
<text x="65" y="200" fill="#60a5fa" font-size="9" font-weight="bold" text-anchor="middle">SEO</text>
<text x="355" y="200" fill="#ff8a00" font-size="9" font-weight="bold" text-anchor="middle">AIO</text>
<defs><marker id="se" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#93c5fd"/></marker></defs>
</svg>"""

SVG_SUN = """<svg class="svg-main" viewBox="0 0 400 360" aria-hidden="true">
<circle cx="200" cy="180" r="45" fill="url(#go)"/><text x="200" y="186" fill="#1a0a00" font-size="12" font-weight="bold" text-anchor="middle">RUNBIRD</text>
<line x1="200" y1="50" x2="200" y2="130" stroke="rgba(255,138,0,.5)" stroke-width="2"/><rect x="170" y="25" width="60" height="28" rx="8" fill="rgba(0,0,0,.5)"/><text x="200" y="44" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">導線</text>
<line x1="320" y1="100" x2="250" y2="150" stroke="rgba(255,138,0,.5)" stroke-width="2"/><rect x="310" y="75" width="60" height="28" rx="8" fill="rgba(0,0,0,.5)"/><text x="340" y="94" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">LINE</text>
<line x1="320" y1="260" x2="250" y2="210" stroke="rgba(255,138,0,.5)" stroke-width="2"/><rect x="310" y="245" width="60" height="28" rx="8" fill="rgba(0,0,0,.5)"/><text x="340" y="264" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">SEO</text>
<line x1="200" y1="310" x2="200" y2="230" stroke="rgba(255,138,0,.5)" stroke-width="2"/><rect x="170" y="305" width="60" height="28" rx="8" fill="rgba(0,0,0,.5)"/><text x="200" y="324" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">AIO</text>
<line x1="80" y1="260" x2="150" y2="210" stroke="rgba(255,138,0,.5)" stroke-width="2"/><rect x="30" y="245" width="70" height="28" rx="8" fill="rgba(0,0,0,.5)"/><text x="65" y="264" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">レポート</text>
<line x1="80" y1="100" x2="150" y2="150" stroke="rgba(255,138,0,.5)" stroke-width="2"/><rect x="30" y="75" width="60" height="28" rx="8" fill="rgba(0,0,0,.5)"/><text x="60" y="94" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">保守</text>
</svg>"""

SVG_DASH = """<svg class="svg-main" viewBox="0 0 480 260" aria-hidden="true">
<rect x="10" y="10" width="460" height="240" rx="12" fill="rgba(0,0,0,.5)" stroke="rgba(255,255,255,.1)"/>
<text x="30" y="35" fill="#ffd84d" font-size="10" font-weight="bold">月次レポート</text>
<rect x="30" y="50" width="95" height="55" rx="8" fill="rgba(52,213,255,.1)" stroke="#34d5ff"/><text x="77" y="72" fill="#34d5ff" font-size="18" font-weight="bold" text-anchor="middle">+24%</text><text x="77" y="92" fill="#a8c8d4" font-size="8" text-anchor="middle">アクセス</text>
<rect x="135" y="50" width="95" height="55" rx="8" fill="rgba(52,213,255,.1)" stroke="#34d5ff"/><text x="182" y="72" fill="#34d5ff" font-size="18" font-weight="bold" text-anchor="middle">186</text><text x="182" y="92" fill="#a8c8d4" font-size="8" text-anchor="middle">電話</text>
<rect x="240" y="50" width="95" height="55" rx="8" fill="rgba(52,213,255,.1)" stroke="#34d5ff"/><text x="287" y="72" fill="#34d5ff" font-size="18" font-weight="bold" text-anchor="middle">94</text><text x="287" y="92" fill="#a8c8d4" font-size="8" text-anchor="middle">LINE</text>
<rect x="345" y="50" width="95" height="55" rx="8" fill="rgba(255,138,0,.1)" stroke="#ff8a00"/><text x="392" y="72" fill="#ff8a00" font-size="18" font-weight="bold" text-anchor="middle">12</text><text x="392" y="92" fill="#a8c8d4" font-size="8" text-anchor="middle">更新</text>
<polyline points="40,200 120,170 200,150 280,120 360,100 440,80" fill="none" stroke="#34d5ff" stroke-width="3"/>
<polyline points="40,200 120,185 200,175 280,165 360,155 440,145" fill="none" stroke="#ff8a00" stroke-width="2" stroke-dasharray="6 4" opacity=".7"/>
</svg>"""

SVG_VALUE = """<svg class="svg-flow" viewBox="0 0 700 90" aria-hidden="true">
<rect x="20" y="15" width="150" height="60" rx="12" fill="rgba(52,213,255,.12)" stroke="#34d5ff" stroke-width="2"/>
<text x="95" y="42" fill="#ffd84d" font-size="14" font-weight="bold" text-anchor="middle">見つかる</text>
<text x="95" y="58" fill="#a8c8d4" font-size="9" text-anchor="middle">Google / AI</text>
<text x="200" y="50" fill="#ff8a00" font-size="24" font-weight="bold">→</text>
<rect x="230" y="15" width="150" height="60" rx="12" fill="rgba(255,138,0,.1)" stroke="#ff8a00" stroke-width="2"/>
<text x="305" y="42" fill="#ffd84d" font-size="14" font-weight="bold" text-anchor="middle">信頼される</text>
<text x="305" y="58" fill="#a8c8d4" font-size="9" text-anchor="middle">比較・検討</text>
<text x="410" y="50" fill="#ff8a00" font-size="24" font-weight="bold">→</text>
<rect x="440" y="15" width="150" height="60" rx="12" fill="rgba(6,199,85,.12)" stroke="#06c755" stroke-width="2"/>
<text x="515" y="42" fill="#ffd84d" font-size="14" font-weight="bold" text-anchor="middle">行動される</text>
<text x="515" y="58" fill="#a8c8d4" font-size="9" text-anchor="middle">LINE / 電話</text>
<text x="620" y="50" fill="#34d5ff" font-size="24" font-weight="bold">→</text>
<text x="670" y="42" fill="#34d5ff" font-size="11" font-weight="bold" text-anchor="middle">問合せ</text>
</svg>"""

SVG_ALLIN = """<svg class="svg-main" viewBox="0 0 400 360" aria-hidden="true">
<text x="200" y="175" fill="#ffd84d" font-size="28" font-weight="bold" text-anchor="middle">全部込み</text>
<circle cx="200" cy="180" r="130" fill="none" stroke="rgba(255,138,0,.25)" stroke-width="2"/>
<circle cx="200" cy="40" r="22" fill="rgba(0,0,0,.4)" stroke="rgba(255,255,255,.15)"/><text x="200" y="45" fill="#fff" font-size="8" text-anchor="middle">HP</text>
<circle cx="340" cy="100" r="22" fill="rgba(0,0,0,.4)" stroke="rgba(255,255,255,.15)"/><text x="340" y="105" fill="#fff" font-size="8" text-anchor="middle">SEO</text>
<circle cx="340" cy="260" r="22" fill="rgba(0,0,0,.4)" stroke="rgba(255,255,255,.15)"/><text x="340" y="265" fill="#fff" font-size="8" text-anchor="middle">AIO</text>
<circle cx="200" cy="320" r="22" fill="rgba(0,0,0,.4)" stroke="#06c755"/><text x="200" y="325" fill="#06c755" font-size="8" text-anchor="middle">LINE</text>
<circle cx="60" cy="260" r="22" fill="rgba(0,0,0,.4)" stroke="rgba(255,255,255,.15)"/><text x="60" y="265" fill="#fff" font-size="8" text-anchor="middle">保守</text>
<circle cx="60" cy="100" r="22" fill="rgba(0,0,0,.4)" stroke="rgba(255,255,255,.15)"/><text x="60" y="105" fill="#fff" font-size="8" text-anchor="middle">SSL</text>
</svg>"""

SVG_UPSELL = """<svg class="svg-flow" viewBox="0 0 700 100" aria-hidden="true">
<rect x="10" y="25" width="130" height="50" rx="10" fill="rgba(234,67,53,.2)" stroke="#ea4335"/><text x="75" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">MEO</text>
<path d="M150 50 H190" stroke="#ffd84d" stroke-width="3" marker-end="url(#u)"/>
<rect x="200" y="25" width="130" height="50" rx="10" fill="rgba(255,138,0,.15)" stroke="#ff8a00"/><text x="265" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">HP信頼</text>
<path d="M340 50 H380" stroke="#ffd84d" stroke-width="3" marker-end="url(#u)"/>
<rect x="390" y="25" width="130" height="50" rx="10" fill="rgba(6,199,85,.15)" stroke="#06c755"/><text x="455" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">LINE予約</text>
<path d="M530 50 H570" stroke="#ffd84d" stroke-width="3" marker-end="url(#u)"/>
<rect x="580" y="25" width="110" height="50" rx="10" fill="rgba(52,213,255,.12)" stroke="#34d5ff"/><text x="635" y="55" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">改善</text>
<defs><marker id="u" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ffd84d"/></marker></defs>
</svg>"""

WAVE = """<svg class="wave-b" viewBox="0 0 1200 120" preserveAspectRatio="none"><path fill="rgba(52,213,255,.12)" d="M0,70 Q250,20 500,55 T1000,45 T1200,60 L1200,120 L0,120Z"/><path fill="none" stroke="rgba(255,138,0,.4)" stroke-width="1.5" d="M0,85 Q350,40 700,70 T1200,55"/></svg>"""

slides_html = f"""
      <!-- 01 COVER -->
      <section class="sl bg-cover" id="s01">
        <div class="bg bg-cover"></motion>
        <motion class="frame"></motion>
        {WAVE}
        {hd(1)}
        <motion class="body split split-55">
          <motion class="cover-left">
            <p class="cat">AI HOMEPAGE</p>
            <h1 class="h-xl glow-t">AIに選ばれる。<br><span class="accent-c">あなたに届く。</span></h1>
            <p class="sub">問い合わせが来るHPを、月額で育てる。</p>
            <motion class="tags">
              <span class="tag">14〜21営業日</span>
              <span class="tag">LINE更新</span>
              <span class="tag">SEO＋AIO</span>
            </motion>
          </motion>
          {SVG_COVER}
        </motion>
        <p class="mini" style="position:absolute;bottom:12px;left:var(--pad);z-index:3">© RUNBIRD — AIホームページ 営業資料</p>
      </section>

      <!-- 02 COMPANY quiet -->
      <section class="sl bg-quiet" id="s02">
        <div class="bg bg-quiet"></motion>
        {hd(2)}
        <motion class="body center-col">
          <p class="cat">COMPANY</p>
          <motion class="stat-row">
            <motion class="stat-item"><p class="num-lg num">4</p><p class="lbl">全国拠点</p></motion>
            <motion class="stat-item"><p class="num-lg" style="font-size:clamp(1.8rem,4vw,3rem)">一気通貫</p><p class="lbl">Web集客</p></motion>
            <motion class="stat-item"><p class="num-lg num">2019</p><p class="lbl">設立</p></motion>
          </motion>
          {SVG_MAP}
          <p class="mini">HP / MEO / SEO / 動画 / AI / 広告　｜　runbird.net</p>
        </motion>
      </section>

      <!-- 03 CAMPAIGN -->
      <section class="sl bg-camp" id="s03">
        <div class="bg bg-camp"></motion>
        {hd(3)}
        <motion class="body center-col">
          <p class="cat">LIMITED</p>
          <h2 class="limit-mega">1エリア × 1業種 × 1店舗</h2>
          <motion class="slot-bar">
            <motion class="slot-item hot"><p class="nm">美容室</p><span class="st ok">募集中</span></motion>
            <motion class="slot-item hot"><p class="nm">飲食</p><span class="st ok">募集中</span></motion>
            <motion class="slot-item"><p class="nm">クリニック</p><span class="st ng">終了</span></motion>
            <motion class="slot-item"><p class="nm">士業</p><span class="st ng">終了</span></motion>
          </motion>
          <motion class="cond-strip">
            <span>事例掲載OK</span><span>エリア要確認</span><span>枠埋まり次第終了</span>
          </motion>
        </motion>
      </section>

      <!-- 04 SYSTEM -->
      <section class="sl bg-hero" id="s04">
        <motion class="bg bg-hero"></motion>
        {hd(4)}
        <motion class="body">
          <p class="cat">PRODUCT</p>
          <p class="h-md accent-y" style="margin-bottom:8px">信頼・問い合わせの受け皿</p>
          <motion class="diagram-row">
            <motion class="pyramid">
              <motion class="pyr a">広告（止めると止まる）</motion>
              <motion class="pyr b">MEO（マップ比較）</motion>
              <motion class="pyr c">AIホームページ</motion>
            </motion>
            {SVG_HUB}
          </motion>
        </motion>
      </section>

      <!-- 05 CRISIS -->
      <section class="sl bg-alert" id="s05">
        <motion class="bg bg-alert"></motion>
        {hd(5)}
        <motion class="body">
          <p class="cat">WHY NOW</p>
          <h2 class="h-lg">なぜ<span class="accent-r">今</span>、HPを変えるのか</h2>
          <motion class="crisis-grid">
            <motion class="crisis-box"><p class="num-lg num accent-c">24%</p><p class="lbl sub">AI検索利用率</p></motion>
            <motion class="crisis-box"><p class="num-lg num accent-y">4.5%</p><p class="lbl sub">HPクリック率</p></motion>
            <motion class="crisis-box"><p class="num-lg num accent-r">79%</p><p class="lbl sub">マップ比較率</p></motion>
          </motion>
          {SVG_FLOW}
          <p class="banner-crisis">放置HPは、選ばれない時代へ</p>
        </motion>
      </section>

      <!-- 06 BA -->
      <section class="sl bg-hero" id="s06">
        <motion class="bg bg-hero"></motion>
        {hd(6)}
        <motion class="body">
          <p class="cat">SOLUTION</p>
          <h2 class="h-md accent-y" style="text-align:center;margin-bottom:12px">必要なことを、全部おまかせ</h2>
          <motion class="ba-split">
            <motion class="ba-pane bad">
              <h3>Before｜放置HP</h3>
              <p class="ba-line">スマホで見づらい</p>
              <p class="ba-line">問合せ導線がない</p>
              <p class="ba-line">更新が止まっている</p>
              <p class="ba-line">AIに拾われない</p>
              <p class="ba-line">マップから逃げる</p>
            </motion>
            <motion class="ba-arrow">→</motion>
            <motion class="ba-pane good">
              <h3>After｜AIホームページ</h3>
              <p class="ba-line">14〜21営業日で公開</p>
              <p class="ba-line">LINEで簡単更新</p>
              <p class="ba-line">SEO＋AIO設計</p>
              <p class="ba-line">導線・信頼を設計</p>
              <p class="ba-line">月次レポート</p>
            </motion>
          </motion>
        </motion>
      </section>

      <!-- 07 FRAMEWORK -->
      <section class="sl bg-hero" id="s07">
        <motion class="bg bg-hero"></motion>
        {hd(7)}
        <motion class="body center-col">
          <p class="cat">FRAMEWORK</p>
          {SVG_CYCLE}
          <p class="sub" style="max-width:28em;text-align:center">この3つがないHPは、見られても問い合わせにつながらない</p>
        </motion>
      </section>

      <!-- 08 FOCUS -->
      <section class="sl bg-alert" id="s08">
        <motion class="bg bg-alert"></motion>
        {hd(8)}
        <motion class="body focus-split">
          <motion>
            <p class="cat">FOCUS</p>
            <ul class="chk">
              <li>電話・LINE・予約を1クリック</li>
              <li>マップ流入を逃さない</li>
              <li>AI検索に拾われるFAQ</li>
            </ul>
          </motion>
          <motion class="word-stack">
            <p class="word-huge"><span class="mark">問い合わせ導線</span></p>
            <p class="word-huge"><span class="mark">更新＋AIO</span></p>
          </motion>
        </motion>
      </section>

      <!-- 09 SPEED -->
      <section class="sl bg-hero" id="s09">
        <motion class="bg bg-hero"></motion>
        {hd(9)}
        <motion class="body speed-split">
          <motion>
            <p class="cat">SPEED</p>
            <motion class="bar-compare">
              <motion class="bar-row"><p class="bar-lbl">一般的な制作</p><motion class="bar-track"><motion class="bar-fill slow">3〜6ヶ月</motion></motion></motion>
              <motion class="bar-row"><p class="bar-lbl">AIホームページ</p><motion class="bar-track"><motion class="bar-fill fast">14〜21営業日</motion></motion></motion>
            </motion>
            <p class="copy-mega">LINEで送るだけ</p>
            <span class="badge-pill">2〜3営業日で反映</span>
          </motion>
          {SVG_PHONE_LINE}
        </motion>
      </section>

      <!-- 10 SEO AIO -->
      <section class="sl bg-hero" id="s10">
        <motion class="bg bg-hero"></motion>
        {hd(10)}
        <motion class="body center-col">
          <p class="cat">AI ERA</p>
          <h2 class="h-md" style="text-align:center">Googleだけでなく<br><span class="accent-y">AIにも選ばれる</span>設計へ</h2>
          {SVG_SEO}
        </motion>
      </section>

      <!-- 11 ALL -->
      <section class="sl bg-hero" id="s11">
        <motion class="bg bg-hero"></motion>
        {hd(11)}
        <motion class="body center-col">
          <p class="cat">ALL RUNBIRD</p>
          <h2 class="h-md accent-y" style="text-align:center;margin-bottom:4px">制作から運用まで、全部まとめて</h2>
          {SVG_SUN}
        </motion>
      </section>

      <!-- 12 SECURITY -->
      <section class="sl bg-alert" id="s12">
        <motion class="bg bg-alert"></motion>
        {hd(12)}
        <motion class="body center-col">
          <p class="cat">SECURITY</p>
          <svg width="90" height="110" viewBox="0 0 64 80" fill="none"><path d="M32 4L8 16v20c0 16 11 30 24 32 13-2 24-16 24-32V16L32 4z" stroke="#34d5ff" stroke-width="3" fill="rgba(52,213,255,.2)"/></svg>
          <h2 class="h-lg" style="text-align:center;max-width:12ch">放置HPは、<br>閉店した店に<br>見える</h2>
          <motion class="cond-strip">
            <span>SSL</span><span>監視</span><span>バックアップ</span>
          </motion>
        </motion>
      </section>

      <!-- 13 ALL IN -->
      <section class="sl bg-hero" id="s13">
        <motion class="bg bg-hero"></motion>
        {hd(13)}
        <motion class="body center-col">
          <p class="cat">ALL IN ONE</p>
          <p class="sub" style="margin-bottom:4px">HP制作だけでなく、運用まで込み</p>
          {SVG_ALLIN}
        </motion>
      </section>

      <!-- 14 VALUE -->
      <section class="sl bg-alert" id="s14">
        <motion class="bg bg-alert"></motion>
        {hd(14)}
        <motion class="body center-col">
          <p class="cat">VALUE</p>
          {SVG_VALUE}
          <p class="h-md accent-c" style="margin-top:10px">→ 問い合わせにつながる</p>
        </motion>
      </section>

      <!-- 15 LINE -->
      <section class="sl bg-hero" id="s15">
        <motion class="bg bg-hero"></motion>
        {hd(15)}
        <motion class="body center-col">
          <p class="cat">LINE OPS</p>
          <h2 class="h-lg accent-y">オーナーはLINEで送るだけ</h2>
          {SVG_PHONE_LINE}
        </motion>
      </section>

      <!-- 16 REPORT -->
      <section class="sl bg-hero" id="s16">
        <motion class="bg bg-hero"></motion>
        {hd(16)}
        <motion class="body center-col">
          <p class="cat">REPORT</p>
          <h2 class="h-md accent-y">見えないものは、改善できない</h2>
          {SVG_DASH}
        </motion>
      </section>

      <!-- 17 PRICING -->
      <section class="sl bg-price" id="s17">
        <motion class="bg bg-price"></motion>
        {hd(17)}
        <motion class="body">
          <p class="cat">PRICING</p>
          <p class="mini" style="text-align:right;margin-bottom:8px">※税抜</p>
          <motion class="price-stage">
            <motion class="tower">
              <p class="plan">ライト</p><p class="plan-en">LIGHT</p>
              <p class="price num">¥18,000</p><p class="init">初期10万 / 5P</p>
            </motion>
            <motion class="tower featured">
              <span class="rec-star">おすすめ</span>
              <p class="plan">スタンダード</p><p class="plan-en">STANDARD</p>
              <p class="price num">¥33,000</p><p class="init">初期15万 / 8P</p>
            </motion>
            <motion class="tower">
              <p class="plan">プロ</p><p class="plan-en">PRO</p>
              <p class="price num">¥45,000</p><p class="init">初期20万 / 12P</p>
            </motion>
          </motion>
        </motion>
      </section>

      <!-- 18 CAMPAIGN PRICE -->
      <section class="sl bg-camp" id="s18">
        <motion class="bg bg-camp"></motion>
        {hd(18)}
        <motion class="body close-stage">
          <p class="limit">各エリア 1業種 1店舗限定</p>
          <h2 class="h-lg accent-y">活用事例店 限定キャンペーン</h2>
          <motion class="price-row">
            <motion class="off-ring"><p class="pct num">20%</p><p class="sub">OFF</p></motion>
            <motion class="price-block">
              <p class="was num">¥33,000</p>
              <p class="now num">¥26,400</p>
              <p class="sub">スタンダード月額</p>
              <p class="sub accent-y" style="font-weight:800;margin-top:6px">初期 ¥120,000（通常15万）</p>
            </motion>
          </motion>
        </motion>
      </section>

      <!-- 19 OPTIONS -->
      <section class="sl bg-hero" id="s19">
        <motion class="bg bg-hero"></motion>
        {hd(19)}
        <motion class="body center-col">
          <p class="cat">ONE STOP</p>
          <h2 class="h-md accent-y">広告・マップ・Webをワンストップ</h2>
          {SVG_UPSELL}
          <motion class="cond-strip" style="margin-top:12px">
            <span>MEO</span><span>AI動画</span><span>ドメイン</span><span>リニューアル</span>
          </motion>
        </motion>
      </section>

      <!-- 20 CLOSE -->
      <section class="sl bg-close" id="s20">
        <motion class="bg bg-close"></motion>
        {hd(20)}
        <motion class="body close-stage">
          <p class="num-xl num accent-c glow-t">14〜21</p>
          <p class="h-md">営業日で公開</p>
          <motion class="steps" style="margin:14px 0">
            <span class="step">枠確認</span><span class="step-ar">→</span>
            <span class="step">プラン</span><span class="step-ar">→</span>
            <span class="step">素材</span><span class="step-ar">→</span>
            <span class="step">公開</span>
          </motion>
          <a class="cta" href="#s03">事例店枠を確認する</a>
        </motion>
      </section>
"""

# Fix motion -> div
slides_html = slides_html.replace("motion", M)

nav_links = "".join(f'<a href="#s{n:02d}">{n:02d}</a>' for n in range(1, 21))

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AIホームページ 営業ブック | 株式会社ランバード</title>
  <meta name="robots" content="noindex, nofollow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>
  <nav class="nav">
    <span class="logo">RUNBIRD</span>
    {nav_links}
  </nav>
  <motion class="viewport">
    <motion class="deck">
{slides_html}
    </motion>
  </motion>
  <script>
    document.querySelectorAll('.nav a').forEach(function(a){{
      a.addEventListener('click',function(e){{
        var id=this.getAttribute('href');
        var el=document.querySelector(id);
        if(el){{e.preventDefault();el.scrollIntoView({{behavior:'smooth',block:'start'}});}}
      }});
    }});
  </script>
</body>
</html>
""".replace("motion", M)

OUT.write_text(html, encoding="utf-8")
print("Wrote", OUT, "bytes", OUT.stat().st_size)

canon = Path(__file__).parent.parent.parent.parent / "共有/01_IT事業/共有ITナレッジ/02_IS事業部/3_AIHP/営業資料/AIホームページ_オンライン営業ブック_20260519_プレゼン.html"
if canon.parent.exists():
    canon.write_text(html, encoding="utf-8")
    print("Synced", canon.name)
