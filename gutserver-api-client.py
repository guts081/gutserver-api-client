import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
REFRESH_TOKEN_FILE = os.getenv("REFRESH_TOKEN_FILE", "refresh_token.txt")

# 最初の REFRESH_TOKEN を読み込み
if os.path.exists(REFRESH_TOKEN_FILE):
    with open(REFRESH_TOKEN_FILE, "r") as f:
        REFRESH_TOKEN = f.read().strip()
else:
    REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

if not API_BASE_URL or not REFRESH_TOKEN:
    raise RuntimeError("API_BASE_URL または REFRESH_TOKEN が設定されていません")


def save_refresh_token(token: str):
    """新しいRefresh Tokenを永続保存"""
    with open(REFRESH_TOKEN_FILE, "w") as f:
        f.write(token)


def refresh_access_token():
    """
    Refresh Token から Access Token を取得
    """
    global REFRESH_TOKEN

    url = f"{API_BASE_URL}/api/token/refresh/"
    res = requests.post(url, json={"refresh": REFRESH_TOKEN})

    if res.status_code != 200:
        raise RuntimeError(
            f"Failed to refresh token: {res.status_code} {res.text}"
        )

    data = res.json()
    access = data["access"]

    # 新しい Refresh Token が返ってきたら保存
    if "refresh" in data:
        REFRESH_TOKEN = data["refresh"]
        save_refresh_token(REFRESH_TOKEN)

    return access


def request_api(method, path, **kwargs):
    access = refresh_access_token()

    url = f"{API_BASE_URL}{path}"
    headers = {"Authorization": f"Bearer {access}"}
    res = requests.request(method, url, headers=headers, **kwargs)

    if res.status_code == 401:
        access = refresh_access_token()
        headers["Authorization"] = f"Bearer {access}"
        res = requests.request(method, url, headers=headers, **kwargs)

    if not res.ok:
        raise RuntimeError(f"API error: {res.status_code} {res.text}")

    try:
        return res.json()
    except Exception:
        return res.text


def get(path, params=None):
    return request_api("GET", path, params=params)

def post(path, json=None):
    return request_api("POST", path, json=json)

def put(path, json=None):
    return request_api("PUT", path, json=json)

def delete(path):
    return request_api("DELETE", path)


if __name__ == "__main__":
    print(get("/ja/gen9/api/pokemon-list/"))
