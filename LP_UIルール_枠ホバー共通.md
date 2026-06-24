---
作成日: 2026-05-22
分類: LP制作・UI共通ルール
承認: 嶋田社長「今後もカーソルを合わせた縁は全て動くようにして。これ保存」
適用: ランバード縦型LP・HTML資料（Buzz Plus 以降すべて）
---

# LP UIルール — 枠ホバー（ふわっと浮く）

## ルール（必須）

**白枠・カード・角丸ボックスなど「縁のあるUI」は、マウスホバー（タップ端末では不要）で必ずふわっと浮く。**

| 項目 | 指定 |
|------|------|
| 動き | `translateY(-10px)` ＋ シャドウ強化 |
| 時間 | `0.5s` · `cubic-bezier(0.34, 1.2, 0.64, 1)` |
| 写真付き | 枠に加え、画像は `scale(1.04〜1.05)` |
| 対象外 | テキストリンクのみ・ヘッダナビ1行・フォーム入力1項目・アイコン単体 |

## 実装方法（2通り）

### A. 新規枠にはクラスを付ける（推奨）

```html
<article class="lp-frame pain-card">...</article>
```

```css
.lp-frame {
  transition: transform 0.5s cubic-bezier(0.34, 1.2, 0.64, 1), box-shadow 0.5s ease;
}

.lp-frame:hover {
  transform: translateY(-10px);
  box-shadow: 0 22px 50px rgba(16, 29, 63, 0.16);
}
```

**新しく追加する枠は必ず `lp-frame` を付与する。**

### B. 既存プロジェクトはセレクタ一覧に追加

Buzz Plus 正本: `buzz-plus-lp/styles.css` の  
`/* ── 枠共通：ホバーでふわっと浮く ── */` ブロック。

新しいカードクラスを作ったら、**:is() リストに必ず追記**する。

## 初出・実装正本

- **CSS実装:** `共有/04_テスト制作/ranbird/buzz-plus-lp/styles.css`（commit `d5d8d96` 以降）
- **LP例:** https://shimada-runbird.github.io/ranbird/buzz-plus-lp/

## 新規LPを作るとき

1. `lp-starter-ec-style` または `buzz-plus-lp/styles.css` から**枠ホバーブロックをコピー**
2. カードHTMLに `lp-frame` を付ける（既存クラスと併用可）
3. 漏れチェック: 角丸＋border＋背景白の要素がホバーで動くかプレビュー確認

## やらないこと

- ホバーなしの静的カードだけのLP
- 激しいバウンス（`scale` 1.1以上、0.2s以下の急な動き）
- ボタン（`.btn`）のホバーは既存の `-2px` でよい（枠ルールと別）

## 関連ドキュメント

- `buzz-plus-lp/HEROデザイン確定.md` — トップ画面のみ別正本
- `LP品質基準_AIX-EC参考_一発制作.md` — LP全体品質
- `04_テスト制作/CLAUDE.md` — AI運用入口

## 出典

- 社長指示: 2026-05-22「こういう枠にカーソルを合わせるとふわっと動く」→「全ての枠」→「今後も…保存」
