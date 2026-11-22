import os
import requests

url = "https://api.github.com/repos/python/cpython"

headers = {"Accept": "application/vnd.github+json"}
token = os.environ.get("GITHUB_TOKEN")
if token:
    headers["Authorization"] = f"Bearer {token}"

resp = requests.get(url, headers=headers)
print("状态码：", resp.status_code)
print("剩余额度：", resp.headers.get("x-ratelimit-remaining"))

if resp.status_code != 200:
    print("请求失败，服务器说：")
    print(resp.text[:500])
    raise SystemExit(1)

data = resp.json()
print("仓库：", data["full_name"])
print("星标：", data["stargazers_count"])
print("简介：", data["description"])
