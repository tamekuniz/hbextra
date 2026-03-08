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

ブラウザで http://localhost:8000 を開く。

## 依存パッケージ

| パッケージ | 必須 | 用途 |
|-----------|------|------|
| flask | Yes | Webサーバー |
| pykakasi | No | 日本語ひらがな変換（検索精度向上） |

## データベース

- `hbextra.db`（SQLite）がプロジェクトディレクトリに自動作成されます
- 記事、ブックマーク数、スター、非表示設定などが保存されます

## トラブルシューティング

**ポート8000が使用中の場合：**
`hbextra.py` 末尾の `port=8000` を別のポート番号に変更してください。

**pykakasi のインストールに失敗する場合：**
pykakasi なしでも動作します。検索時のひらがな変換が無効になるだけです。

**LAN内の他端末からアクセスしたい場合：**
`hbextra.py` 末尾の `host='127.0.0.1'` を `host='0.0.0.0'` に変更してください。
