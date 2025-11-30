# gutserver-api-client (Python)

Django + SimpleJWT ベースの API を安全に叩くための  
**1ファイル完結の Python クライアント**です。

ファイル名は **`gutserver-api-client.py`** です。

- `.env` から設定を読み込み
- Refresh Token から Access Token を自動取得
- Refresh Token のローテーションに対応（更新内容をファイルに保存）
- GET / POST / PUT / DELETE の簡易 API ラッパー

---

## 🚀 使用方法

以下の手順で `gutserver-api-client.py` を使用できます。

### 1. ライブラリをインストールする
```pip install requests python-dotenv```

### 2. `.env` ファイルを作成する（初回のみ）
プロジェクト直下に `.env` を作成し、以下を記述します：
```
API_BASE_URL=https://zakoyama.com
REFRESH_TOKEN=ここにスタッフ権限で発行したRefreshToken
REFRESH_TOKEN_FILE=refresh_token.txt
```

- `API_BASE_URL`：あなたの Django API の URL  
- `REFRESH_TOKEN`：最初に手動発行したもの（管理画面など）  
- `REFRESH_TOKEN_FILE`：更新済みの Refresh Token を保存するファイル  
※ `REFRESH_TOKEN` を設定するのは **この初回のみ** です。

### 3. `gutserver-api-client.py` を配置する
同じディレクトリに `gutserver-api-client.py` を置きます。

### 4. クライアントを実行して API にアクセスする
例：
```python
from gutserver_api_client import get, post

print(get("/ja/gen9/api/pokemon/25-0/"))
```

### 5. Refresh Token がローテーションされた場合

新しい Refresh Token は自動的に `refresh_token.txt` に保存されます

2回目以降は `.env` の値ではなく、
このファイルに保存された最新のトークンが使用されます

---

## ⚠️ 注意事項

- **Refresh Token は初回の1回だけ `.env` に設定してください**
  - 2回目以降は `.env` の値ではなく  
    **`refresh_token.txt` に保存された最新の Refresh Token が使用されます**

- **`.env` の Refresh Token を後から変更しても反映されません**
  - ローテーション済みのため、古いトークンでは認証エラーになります

- **Refresh Token を変更・リセットしたい場合は以下の手順で行ってください**
  1. `refresh_token.txt` を削除  
  2. `.env` の `REFRESH_TOKEN` に新しいトークンを設定  
  3. `gutserver-api-client.py` を再実行

- **`.env` と `refresh_token.txt` は機密情報です**
  - 必ず `.gitignore` へ追加し、  
    **GitHub 等に絶対にコミットしないようにしてください**

---