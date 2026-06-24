#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

M = "di" + "v"
o, c = f"<{M}", f"</{M}>"

def hd(n):
    return f'<header class="hd"><span class="logo">RUNBIRD</span><span class="pg num">{n:02d} / 20</span></header>'

SVG_HUB = """<svg viewBox="0 0 400 340" width="100%" aria-hidden="true">
<defs><linearGradient id="gO" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ff8a00"/><stop offset="100%" stop-color="#ffd84d"/></linearGradient></defs>
<circle cx="200" cy="170" r="95" fill="none" stroke="rgba(52,213,255,.25)" stroke-width="2"/>
<rect x="145" y="125" width="110" height="88" rx="12" fill="#fff"/><rect x="155" y="168" width="55" height="24" rx="6" fill="url(#gO)"/>
<text x="182" y="184" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">問合せ</text>
<circle cx="70" cy="85" r="32" fill="url(#gO)"/><text x="70" y="88" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">AI</text>
<circle cx="330" cy="90" r="28" fill="#4f8cff"/><text x="330" y="95" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">G</text>
<rect x="300" y="215" width="52" height="88" rx="12" fill="#0b2f3f"/><rect x="308" y="228" width="36" height="58" rx="4" fill="#fff"/><rect x="314" y="278" width="24" height="8" rx="3" fill="#06c755"/>
<text x="326" y="208" fill="#06c755" font-size="8" font-weight="bold" text-anchor="middle">LINE</text>
<circle cx="65" cy="245" r="22" fill="none" stroke="#ff8a00" stroke-width="2"/><text x="65" y="250" fill="#fff" font-size="14" text-anchor="middle">📞</text>
<path d="M102 130 Q140 120 145 140" stroke="#ffd84d" stroke-width="2" fill="none"/><path d="M255 145 Q290 110 302 100" stroke="#93c5fd" stroke-width="2" fill="none"/><path d="M255 165 Q295 195 308 228" stroke="#6ee7a0" stroke-width="2" fill="none"/>
</svg>"""

def ba_item(text):
    return f'{o} class="ba-item">{text}{c}'

slides = f"""
      <!-- s01 Cover -->
      <section class="slide" id="s01">
        {o} class="orb orb-o">{c}
        {o} class="orb orb-c">{c}
        {hd(1)}
        {o} class="slide-inner cover-g" style="flex:1;min-height:0">
          {o}>
            <span class="cat en">AI HOMEPAGE SALES BOOK</span>
            <h1 class="h1" style="max-width:14ch;margin-top:8px">AIに選ばれる。<br><span style="color:var(--cyan)">あなたに届く。</span></h1>
            <p class="hero-sub" style="margin-top:10px">問い合わせが来るHPを、月額で育てる。</p>
            {o} class="tags-row">
              <span class="tag-lbl">早期納品 14〜21営業日</span>
              <span class="tag-lbl">LINEで更新</span>
              <span class="tag-lbl">SEO＋AIO</span>
            {c}
          {c}
          {SVG_HUB}
        {c}
        <svg class="wave-bottom" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true">
          <path fill="rgba(52,213,255,0.1)" d="M0,120 Q300,40 600,100 T1200,80 L1200,200 L0,200 Z"/>
          <path fill="none" stroke="rgba(255,138,0,0.35)" stroke-width="1.5" d="M0,155 Q400,95 800,135 T1200,115"/>
        </svg>
        <footer class="slide-foot"><strong>株式会社ランバード</strong> — AIホームページ 営業資料</footer>
      </section>

      <!-- s02 Company -->
      <section class="slide" id="s02">
        {hd(2)}
        {o} class="slide-inner">
          <span class="cat en">COMPANY</span>
          {o} class="pillars">
            {o} class="pillar"><p class="mega num">4</p><h2 style="font-size:clamp(.85rem,1.2vw,1rem);font-weight:900;margin-top:6px;color:var(--gold)">全国4拠点</h2>{c}
            {o} class="pillar"><p class="mega" style="font-size:clamp(1.6rem,3vw,2.4rem)">一気通貫</p><h2 style="font-size:clamp(.85rem,1.2vw,1rem);font-weight:900;margin-top:6px;color:var(--gold)">Web集客</h2>{c}
            {o} class="pillar"><p class="mega num">2019</p><h2 style="font-size:clamp(.85rem,1.2vw,1rem);font-weight:900;margin-top:6px;color:var(--gold)">設立</h2>{c}
          {c}
          {o} class="map4">
            {o}><strong>東京</strong>新宿{c}
            {o}><strong>大阪</strong>梅田{c}
            {o}><strong>福岡</strong>天神{c}
            {o}><strong>沖縄</strong>那覇{c}
          {c}
          {o} class="icons6"><span>HP</span><span>MEO</span><span>SEO</span><span>動画</span><span>AI</span><span>広告</span>{c}
          <p class="tiny-foot">株式会社ランバード｜runbird.net｜03-5843-6996</p>
        {c}
      </section>

      <!-- s03 Campaign -->
      <section class="slide bg-close" id="s03">
        {hd(3)}
        {o} class="slide-inner s03-center">
          <span class="cat">CAMPAIGN</span>
          <p class="mega">1エリア×1業種×1店舗限定</p>
          {o} class="cond-box">
            <ul>
              <li>各エリア・各業種 1店舗のみ</li>
              <li>事例掲載・取材のご協力</li>
              <li>エリア・業種は要確認</li>
              <li>枠が埋まり次第 募集終了</li>
            </ul>
          {c}
          {o} class="slots">
            {o} class="slot hot">美容室<span class="badge-sm ok">募集中</span>{c}
            {o} class="slot hot">飲食店<span class="badge-sm ok">募集中</span>{c}
            {o} class="slot">クリニック<span class="badge-sm ng">終了</span>{c}
            {o} class="slot">士業<span class="badge-sm ng">終了</span>{c}
          {c}
        {c}
      </section>

      <!-- s04 System -->
      <section class="slide" id="s04">
        {hd(4)}
        {o} class="slide-inner">
          <span class="cat">SYSTEM</span>
          <p class="msg-y">信頼・問い合わせの受け皿</p>
          {o} class="s04g">
            {o} class="pyr">
              {o} class="pyr-l a">広告（止めると止まる）{c}
              {o} class="pyr-l b">MEO（マップで比較）{c}
              {o} class="pyr-l c">AIホームページ（資産）{c}
            {c}
            {o} class="hub-radial" style="min-height:220px">
              {o} class="hub-center">AI<br>ホームページ{c}
              <span class="orbit" style="top:2%;left:50%;transform:translateX(-50%)">Google検索</span>
              <span class="orbit" style="top:20%;right:4%">AI検索</span>
              <span class="orbit" style="bottom:20%;right:6%">MEO</span>
              <span class="orbit" style="bottom:4%;left:50%;transform:translateX(-50%)">LINE</span>
              <span class="orbit" style="top:20%;left:4%">電話</span>
            {c}
          {c}
        {c}
      </section>

      <!-- s05 Why now -->
      <section class="slide bg-alert" id="s05">
        {hd(5)}
        {o} class="slide-inner">
          <span class="cat">WHY NOW</span>
          <h1 class="h1">なぜ<span style="color:var(--orange)">今</span>HPを変えるのか</h1>
          {o} class="stat3">
            {o} class="box"><p class="mega num">24%</p><p class="hero-sub">AI検索利用率</p>{c}
            {o} class="box"><p class="mega num">4.5%</p><p class="hero-sub">HPクリック率</p>{c}
            {o} class="box"><p class="mega num">79%</p><p class="hero-sub">マップ比較率</p>{c}
          {c}
          {o} class="flow14">
            <span class="s">AIに質問</span><span class="a">→</span><span class="s on">マップ比較</span><span class="a">→</span><span class="s on">HPで信頼</span><span class="a">→</span><span class="s on">LINE/電話</span>
          {c}
          <p class="banner-y">放置HPは、選ばれない時代へ</p>
        {c}
      </section>

      <!-- s06 Before/After -->
      <section class="slide" id="s06">
        {hd(6)}
        {o} class="slide-inner">
          <span class="cat">SOLUTION</span>
          <p class="ba-head">必要なことを、全部おまかせ</p>
          {o} class="ba5">
            {o} class="ba-side before">
              <h3>Before：放置HP</h3>
              {ba_item("古い・スマホ非対応")}
              {ba_item("問合せ導線がない")}
              {ba_item("更新が止まっている")}
              {ba_item("AIに拾われない")}
              {ba_item("マップから逃げる")}
            {c}
            {o} class="ba-mid">→{c}
            {o} class="ba-side after">
              <h3>After：AIホームページ</h3>
              {ba_item("14〜21営業日で公開")}
              {ba_item("LINEで簡単更新")}
              {ba_item("SEO＋AIO設計")}
              {ba_item("導線・信頼を設計")}
              {ba_item("月次レポート")}
            {c}
          {c}
        {c}
      </section>

      <!-- s07 Framework -->
      <section class="slide" id="s07">
        {hd(7)}
        {o} class="slide-inner">
          <span class="cat">FRAMEWORK</span>
          {o} class="cycle">
            {o} class="cycle-c">問い合わせが<br>来るHP{c}
            {o} class="cycle-n" style="top:0;left:50%;transform:translateX(-50%)"><span>①</span>導線設計{c}
            {o} class="cycle-n" style="bottom:8%;left:0"><span>②</span>信頼設計{c}
            {o} class="cycle-n" style="bottom:8%;right:0"><span>③</span>継続更新{c}
          {c}
          <p class="cycle-foot">この3つがないHPは、見られても問い合わせにつながらない</p>
        {c}
      </section>

      <!-- s08 Focus -->
      <section class="slide bg-alert" id="s08">
        {hd(8)}
        {o} class="slide-inner dual8">
          {o}>
            <span class="cat">FOCUS</span>
            <ul class="chk">
              <li>電話・LINE・予約を1クリック</li>
              <li>マップ流入を逃さない</li>
              <li>AI検索に拾われるFAQ</li>
              <li>月次で改善サイクル</li>
            </ul>
            {o} class="gicons"><span>📞 電話</span><span>LINE</span><span>予約</span><span>AI検索</span>{c}
          {c}
          {o} class="gwords">
            <p class="gword"><mark>問い合わせ導線</mark></p>
            <p class="gword"><mark>更新＋AIO</mark></p>
          {c}
        {c}
      </section>

      <!-- s09 Speed -->
      <section class="slide" id="s09">
        {hd(9)}
        {o} class="slide-inner s09g">
          {o}>
            <span class="cat">SPEED</span>
            {o} class="duel-row"><span class="duel-lbl">外注</span>{o} class="duel-trk">{o} class="duel-old">3〜6ヶ月{c}{c}{c}
            {o} class="duel-row"><span class="duel-lbl">当社</span>{o} class="duel-trk">{o} class="duel-new">14〜21営業日{c}{c}{c}
            <p class="copy-huge">LINEで送るだけ</p>
            <span class="pill-y">2〜3営業日で反映</span>
          {c}
          {o} class="phones" style="flex:1">
            {o} class="phone" style="border-color:#06c755">LINE<br>送信{c}
            <span class="ph-arr">→</span>
            {o} class="phone on">運用<br>チーム{c}
            <span class="ph-arr">→</span>
            {o} class="phone">HP<br>反映{c}
          {c}
        {c}
      </section>

      <!-- s10 SEO+AIO -->
      <section class="slide" id="s10">
        {hd(10)}
        {o} class="slide-inner">
          <span class="cat">AI ERA</span>
          <h1 class="h1" style="font-size:clamp(1.2rem,2.2vw,1.6rem)">Googleだけでなく、AIにも選ばれる設計へ</h1>
          {o} class="s10g">
            {o} style="display:flex;justify-content:center;align-items:center;gap:8px;margin-bottom:8px">
              <span class="glass" style="padding:8px 14px;font-weight:800">Google</span><span class="ph-arr">→</span>
              <span class="glass" style="padding:8px 14px;font-weight:800;border-color:var(--orange)">御社HP</span><span class="ph-arr">←</span>
              <span class="glass" style="padding:8px 14px;font-weight:800">ChatGPT</span>
            {c}
            {o} class="cmp2">
              {o} class="col g"><h4>SEO</h4><ul><li>検索順位・KW</li><li>構造化データ</li><li>内部リンク</li></ul>{c}
              {o} class="col a"><h4>AIO</h4><ul><li>FAQ・回答設計</li><li>AI引用対策</li><li>継続更新</li></ul>{c}
            {c}
          {c}
          <p class="tiny-foot" style="margin-top:6px">※効果は業種・競合により異なります</p>
        {c}
      </section>

      <!-- s11 All support -->
      <section class="slide" id="s11">
        {hd(11)}
        {o} class="slide-inner">
          <span class="cat">ALL RUNBIRD</span>
          <h1 class="h1" style="font-size:clamp(1rem,1.8vw,1.35rem)">制作から運用まで、全部まとめてサポート</h1>
          {o} class="sun-wrap">
            {o} class="sun-core">RUNBIRD{c}
            <span class="ray" style="top:0;left:50%;transform:translateX(-50%)">導線</span>
            <span class="ray" style="top:16%;right:4%">LINE</span>
            <span class="ray" style="bottom:16%;right:4%">SEO</span>
            <span class="ray" style="bottom:0;left:50%;transform:translateX(-50%)">AIO</span>
            <span class="ray" style="bottom:16%;left:4%">レポート</span>
            <span class="ray" style="top:16%;left:4%">保守</span>
          {c}
        {c}
      </section>

      <!-- s12 Security -->
      <section class="slide bg-alert" id="s12">
        {hd(12)}
        {o} class="slide-inner s12c">
          <span class="cat">SECURITY</span>
          <svg class="shield-lg" viewBox="0 0 64 80" fill="none"><path d="M32 4L8 16v20c0 16 11 30 24 32 13-2 24-16 24-32V16L32 4z" stroke="#34d5ff" stroke-width="3" fill="rgba(52,213,255,.2)"/></svg>
          <p class="s12-msg">放置HPは、<br>閉店した店に見える</p>
          {o} class="sec3">
            {o}<svg viewBox="0 0 48 48" fill="none"><rect x="8" y="20" width="32" height="24" rx="3" stroke="#34d5ff" stroke-width="2"/><path d="M24 8v32" stroke="#ff8a00" stroke-width="2"/></svg>SSL{c}
            {o}<svg viewBox="0 0 48 48" fill="none"><circle cx="24" cy="24" r="16" stroke="#ff8a00" stroke-width="2"/><path d="M24 16v16M16 24h16" stroke="#ffd84d" stroke-width="2"/></svg>監視{c}
            {o}<svg viewBox="0 0 48 48" fill="none"><path d="M12 32V20l12-8 12 8v12" stroke="#34d5ff" stroke-width="2"/><path d="M20 28l4 4 8-8" stroke="#ff8a00" stroke-width="2"/></svg>バックアップ{c}
          {c}
        {c}
      </section>

      <!-- s13 All-in -->
      <section class="slide" id="s13">
        {hd(13)}
        {o} class="slide-inner">
          <span class="cat">ALL IN</span>
          <p class="ring-big">全部込み</p>
          <p class="msg-y" style="margin-bottom:6px">HP制作だけでなく、運用まで込み</p>
          {o} class="ring-wrap-lg">
            <span class="ring-dot" style="top:0;left:50%;transform:translateX(-50%)"><span class="ico">🌐</span>HP</span>
            <span class="ring-dot" style="top:14%;right:8%"><span class="ico">📈</span>SEO</span>
            <span class="ring-dot" style="top:42%;right:0"><span class="ico">🤖</span>AIO</span>
            <span class="ring-dot" style="bottom:14%;right:8%"><span class="ico">💬</span>LINE</span>
            <span class="ring-dot" style="bottom:0;left:50%;transform:translateX(-50%)"><span class="ico">🛡</span>保守</span>
            <span class="ring-dot" style="bottom:14%;left:8%"><span class="ico">📊</span>レポート</span>
            <span class="ring-dot" style="top:42%;left:0"><span class="ico">🔒</span>SSL</span>
            <span class="ring-dot" style="top:14%;left:8%"><span class="ico">☁</span>サーバー</span>
          {c}
          {o} class="ring-core4"><span>制作</span><span>更新</span><span>SEO/AIO</span><span>保守</span>{c}
        {c}
      </section>

      <!-- s14 Value -->
      <section class="slide bg-alert" id="s14">
        {hd(14)}
        {o} class="slide-inner">
          <span class="cat">VALUE</span>
          {o} class="vflow">
            {o} class="v"><h4>見つかる</h4><p>Google / AI</p>{c}
            <span class="ar">→</span>
            {o} class="v"><h4>信頼される</h4><p>比較・検討</p>{c}
            <span class="ar">→</span>
            {o} class="v"><h4>行動される</h4><p>LINE / 電話</p>{c}
          {c}
          <p class="goal-t">→ 問い合わせにつながる</p>
        {c}
      </section>

      <!-- s15 LINE -->
      <section class="slide" id="s15">
        {hd(15)}
        {o} class="slide-inner">
          <span class="cat">LINE OPS</span>
          <p class="line-big">オーナーはLINEで送るだけ</p>
          {o} class="lineflow-wrap">
            <span class="line-eval">Google / AI 評価↑</span>
            {o} class="lineflow">
              {o} class="ph ln">LINE<br>送信{c}
              <span class="ph-arr">→</span>
              {o} class="ph mid">運用<br>チーム{c}
              <span class="ph-arr">→</span>
              {o} class="ph hp">HP<br>更新{c}
            {c}
          {c}
        {c}
      </section>

      <!-- s16 Report -->
      <section class="slide" id="s16">
        {hd(16)}
        {o} class="slide-inner">
          <span class="cat">REPORT</span>
          <p class="dash-title">見えないものは、改善できない</p>
          {o} class="dash-grid">
            {o} class="kpi"><p class="v num">+24%</p><p class="l">アクセス</p><p class="up">前月比</p>{c}
            {o} class="kpi"><p class="v num">186</p><p class="l">電話クリック</p><p class="up">+12%</p>{c}
            {o} class="kpi"><p class="v num">94</p><p class="l">LINE</p><p class="up">+8%</p>{c}
            {o} class="kpi"><p class="v num">12</p><p class="l">更新回数</p>{c}
            {o} class="chart">
              <svg viewBox="0 0 200 80" width="100%" aria-hidden="true">
                <polyline points="0,70 40,55 80,45 120,35 160,25 200,15" fill="none" stroke="#34d5ff" stroke-width="3"/>
                <polyline points="0,70 40,62 80,58 120,50 160,42 200,38" fill="none" stroke="#ff8a00" stroke-width="2" stroke-dasharray="4 3" opacity=".7"/>
              </svg>
            {c}
          {c}
        {c}
      </section>

      <!-- s17 Pricing -->
      <section class="slide bg-price" id="s17">
        {hd(17)}
        {o} class="slide-inner">
          <span class="cat">PRICING</span>
          <p class="hero-sub" style="text-align:right">※表示は税抜</p>
          {o} class="price3">
            {o} class="pcol"><p class="tier">ライト</p><p class="tier-en">LIGHT</p><p class="yen">月額 <span class="num">¥18,000</span></p><p class="meta">初期10万 / 5P</p>{c}
            {o} class="pcol on"><span class="rec-lg">おすすめ</span><p class="tier">スタンダード</p><p class="tier-en">STANDARD</p><p class="yen">月額 <span class="num">¥33,000</span></p><p class="meta">初期15万 / 8P</p>{c}
            {o} class="pcol"><p class="tier">プロ</p><p class="tier-en">PRO</p><p class="yen">月額 <span class="num">¥45,000</span></p><p class="meta">初期20万 / 12P</p>{c}
          {c}
        {c}
      </section>

      <!-- s18 Campaign price -->
      <section class="slide bg-close" id="s18">
        {hd(18)}
        {o} class="slide-inner close18">
          <p class="limit-top">各エリア 1業種 1店舗限定</p>
          <h1 class="h1">活用事例店 限定キャンペーン</h1>
          {o} class="compare18">
            {o} class="off-disc"><p class="mega num">20%</p><p class="hero-sub">OFF</p>{c}
            {o} class="price-hero">
              <p class="was num">¥33,000/月</p>
              <p class="now num">¥26,400</p>
              <p class="hero-sub">スタンダードプラン月額（税抜）</p>
              <p class="init">初期 ¥120,000（通常15万）</p>
            {c}
          {c}
        {c}
      </section>

      <!-- s19 Options -->
      <section class="slide" id="s19">
        {hd(19)}
        {o} class="slide-inner flow19">
          <span class="cat">OPTIONS</span>
          <p class="flow19-top">広告・マップ・Webをワンストップで</p>
          {o} class="flow19m">
            <span class="s">MEOで見つける</span><span class="a">→</span><span class="s">HPで信頼</span><span class="a">→</span><span class="s">LINE予約</span><span class="a">→</span><span class="s">レポート改善</span>
          {c}
          {o} class="opts4">
            {o}><span class="i">📍</span>MEO{c}
            {o}><span class="i">🎬</span>AI動画{c}
            {o}><span class="i">🌐</span>ドメイン{c}
            {o}><span class="i">✨</span>大幅リニューアル{c}
          {c}
        {c}
      </section>

      <!-- s20 Closing -->
      <section class="slide bg-close" id="s20">
        {hd(20)}
        {o} class="slide-inner s20c">
          <p class="mega num" style="color:var(--cyan)">最短14〜21営業日で公開</p>
          {o} class="steps4">
            <span class="st">枠確認</span><span class="ar">→</span><span class="st">プラン選択</span><span class="ar">→</span><span class="st">素材準備</span><span class="ar">→</span><span class="st">公開</span>
          {c}
          {o} class="cards3">
            {o}>AIに選ばれるHP{c}
            {o}>LINEで運用{c}
            {o}>事例店でお得{c}
          {c}
          <a class="cta-big" href="#s03">事例店枠を確認する</a>
        {c}
      </section>
"""

# Fix broken tags like {o}> -> {o}>
slides = slides.replace(f"{o}>", f"{o}>")

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")
i0 = html.index("      <!-- s01 Cover -->")
i1 = html.index("      <!-- s20 Closing -->")
i1 = html.index("</section>", html.index('id="s20"')) + len("</section>") + 1

new_html = html[:i0] + slides + "\n" + html[i1:]
html_path.write_text(new_html, encoding="utf-8")
print("Patched index.html", len(slides), "chars")

# Sync canonical
canon = Path(__file__).parent.parent.parent.parent / "共有/01_IT事業/共有ITナレッジ/02_IS事業部/3_AIHP/営業資料/AIホームページ_オンライン営業ブック_20260519_プレゼン.html"
if canon.parent.exists():
    canon.write_text(new_html, encoding="utf-8")
    print("Synced", canon)
