---
作成日: 2026-05-22
分類: Buzz Plus LP・デザイン正本
承認: 嶋田社長「これ！イメージ通り！」
公開URL: https://shimada-runbird.github.io/ranbird/buzz-plus-lp/
---

# Buzz Plus LP — ヒーロー（トップ）デザイン確定

**この構成を今後の Buzz Plus LP 改修・類似LP制作の正本とする。社長承認済み（2026-05-22）。**

## コンセプト（覚えておくこと）

| 項目 | 指定 |
|------|------|
| レイアウト | AIX-EC型・**中央寄せ**・枠なし |
| 背景 | **1枚のビジュアル**を画面全体（100vh）に `cover` |
| 背景の濃さ | 画像 **opacity 0.72** ＋ 白ベール（下記CSS）で**少し薄く** |
| 文字 | **背景の上に直置き**（大きな白パネル・縁・枠は付けない） |
| 読みやすさ | 見出し・本文は **白系 text-shadow** のみ |
| 例外 | NEWバッジ・数字3つのピルだけ **小さな白カード**（視認性） |

## 背景画像

- **ファイル:** `buzz-plus-lp/images/hero-bg.png`
- **HTML:** `<img class="hero-bg__scene" src="images/hero-bg.png?v=2">` ＋ CSS `background` 二重指定（表示漏れ防止）
- **差し替え時:** 同パスに上書きし、`?v=` のクエリを increment

## 確定CSS（抜粋・正本は `styles.css` の `.hero--aix` ブロック）

```css
.hero--aix { min-height: 100vh; min-height: 100dvh; }

.hero-bg {
  background: #0a1628 url("images/hero-bg.png?v=2") center / cover no-repeat;
}

.hero-bg__scene {
  opacity: 0.72;
  filter: saturate(1.05) contrast(1.02);
}

.hero-bg__veil {
  background:
    linear-gradient(180deg, rgba(255,255,255,0.28) 0%, rgba(255,255,255,0.38) 48%, rgba(255,255,255,0.32) 100%),
    radial-gradient(ellipse 90% 70% at 50% 42%, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.42) 100%);
}

.hero-center {
  background: none;
  border: none;
  box-shadow: none;
}

.hero-benefit {
  background: none;
  border: none;
  box-shadow: none;
}
```

## コンテンツ構成（HTML順）

1. `hero-badge` — NEW ＋ 店舗・企業向け AI動画サブスク
2. `h1` — 短納期・低コスト／売れる動画を毎月届ける
3. `hero-brand` — **BUZZ** + **+**（オレンジ）
4. `hero-sub` — AI動画サブスクサービス
5. `hero-benefit` — 60%・1/5・月3.3万〜（枠なし・直置き）
6. `hero-stats-bar` — 3ピル（60% / 1/5 / 月3.3万〜）
7. `hero-actions` — 無料相談・訴求動画の種類を見る

## やってはいけないこと（過去の迷走）

- 6枚コラージュ背景だけに戻さない
- 全面の白ベール（opacity 0.6〜0.9）で画像を消さない
- 中央の大きな白枠パネルを復活させない
- 左右スマホモックをヒーローに戻さない（確定版は中央のみ）

## 微調整の目安

| 要望 | 調整箇所 |
|------|----------|
| もっと背景を見せる | `.hero-bg__scene` opacity ↑、`.hero-bg__veil` の白 ↓ |
| もっと薄く | opacity ↓（0.65前後）、veil の白 ↑ |
| 文字が読みにくい | `text-shadow` を強める（枠は付けない） |

## 実装ファイル

- `buzz-plus-lp/index.html` — `.hero.hero--aix`
- `buzz-plus-lp/styles.css` — `/* ── Hero：背景写真（すかし）＋中央コンテンツ ── */`
- Git: `shimada-runbird/ranbird` main（commit `c6ceac9` 以降）

## 出典

- 社長承認コメント: 2026-05-22 チャット「これ！イメージ通り！これ覚えておいて。保存」
- 参考レイアウト: [AIX-EC LP](https://rank-quest.jp/lp/aix-ec02/)（背景画像のみ Buzz Plus 用に差し替え）
