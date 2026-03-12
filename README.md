# HBExtra

はてなブックマークのホットエントリー・新着エントリーを閲覧するRSSリーダー。

## 必要なもの

- Python 3.8以上
- インターネット接続（RSSフィード取得用）

## インストール

### Mac

```bash
# リポジトリをクローン
git clone https://github.com/tamekuniz/hbextra.git
cd hbextra

# 依存パッケージをインストール
pip3 install flask pykakasi
```

### Windows

1. Python 3をインストール（https://www.python.org/downloads/）
   - **「Add Python to PATH」にチェックを入れること**

```cmd
# リポジトリをクローン
git clone https://github.com/tamekuniz/hbextra.git
cd hbextra

# 依存パッケージをインストール
pip install flask pykakasi
```

> `pip` が見つからない場合は `python -m pip install flask pykakasi` を試してください。

## 起動

### Mac

```bash
python3 hbextra.py
```

### Windows

```cmd
python hbextra.py
```

ブラウザで http://localhost:8000 を開く。初回アクセス時にユーザー登録画面が表示されます。

LAN内の他端末からもアクセスできます（`http://<IPアドレス>:8000`）。

## 依存パッケージ

| パッケージ | 必須 | 用途 |
|-----------|------|------|
| flask | Yes | Webサーバー |
| pykakasi | No | 日本語ひらがな変換（検索精度向上） |

## 機能

- 新着/人気エントリーの一覧表示（10カテゴリ対応）
- キーボード操作（j/k移動、v プレビュー、s スター、d 非表示、b 開く）
- スター・非表示管理（ユーザーごとに独立）
- タグクラウド（期間・並び順変更、ローマ字検索）
- エクスポート・インポート
- マルチユーザー対応（ユーザー登録/ログイン）

## データベース

- `hbextra.db`（SQLite）がプロジェクトディレクトリに自動作成されます
- 記事データは全ユーザーで共有、スター・非表示はユーザーごとに管理されます

## トラブルシューティング

**ポート8000が使用中の場合：**
`hbextra.py` 末尾の `port=8000` を別のポート番号に変更してください。

**pykakasi のインストールに失敗する場合：**
pykakasi なしでも動作します。検索時のひらがな変換が無効になるだけです。

## ライセンス

MIT
