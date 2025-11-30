# gutserver-api-client (Python)

Django + SimpleJWT ベースの API を安全に叩くための  
**1ファイル完結の Python クライアント**です。

ファイル名は **`gutserver-api-client.py`** です。

- `.env` から設定を読み込み
- Refresh Token から Access Token を自動取得
- Refresh Token のローテーションに対応（更新内容をファイルに保存）
- GET / POST / PUT / DELETE の簡易 API ラッパー

---

## 🚀 特徴

- **1ファイルで動作：`gutserver-api-client.py`**
- **dotenv 対応（`.env` に設定を書く）**
- **Refresh Token のローテーション完全対応**
- **401 が返った場合は Access Token を自動更新して再実行**

---

## 📦 インストール
```pip install requests python-dotenv```

## 🔧 `.env` を準備

プロジェクトルートに `.env` を作成：
```
API_BASE_URL=https://zakoyama.com
REFRESH_TOKEN=ここにスタッフ権限で発行したRefreshToken
REFRESH_TOKEN_FILE=refresh_token.txt
```

- `API_BASE_URL`：あなたの Django API の URL  
- `REFRESH_TOKEN`：最初に手動発行したもの（管理画面など）  
- `REFRESH_TOKEN_FILE`：更新済みの Refresh Token を保存するファイル  

※ これらは **絶対に GitHub にコミットしないでください**