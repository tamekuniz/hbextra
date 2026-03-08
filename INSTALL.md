# はてブニュース+ インストール手順

## 必要なもの
- Mac（macOS 12以降推奨）
- Python 3（macOS には標準でインストール済み）

---

## 手順

### 1. ファイルをコピー

以下の2ファイルを、新しいMacの任意のフォルダにコピーする。

```
hbnews.py
hbnews.html
```

例：`/Users/（ユーザー名）/ClaudeCode/` に置く

---

### 2. Pythonパッケージをインストール

ターミナルを開いて以下を実行：

```bash
pip3 install flask pykakasi
```

> `pip3` が見つからない場合は `pip install flask pykakasi` を試す

---

### 3. 起動する

```bash
cd /Users/（ユーザー名）/ClaudeCode
python3 hbnews.py
```

起動後、ブラウザで以下にアクセス：

```
http://localhost:8000
```

---

### 4. 停止する

ターミナルで `Ctrl + C` を押す

---

## トラブルシューティング

### 「flask が見つからない」エラーが出る
```bash
pip3 install flask pykakasi
```
を再実行する。それでも出る場合：
```bash
python3 -m pip install flask pykakasi
```

### ポート8000が使用中と出る
`hbnews.py` の末尾近くにある以下の行を探して、`8000` を別の番号（例：`8001`）に変更する：
```python
app.run(host='0.0.0.0', port=8000, ...)
```

---

## データについて
- 記事データは `hbnews.db`（SQLite）に自動保存される
- スター・非表示の情報も `hbnews.db` に入っている
- 別のMacにデータを移したい場合は `hbnews.db` もコピーする
- バックアップはアプリ内の「エクスポート」ボタンからも可能
