# ライブラリのインポート
from email import header
import requests

# urlの設定
# url = 'https://tech-diary.net/?s=python'
# url = 'https://tech-diary.net/'
# url = 'https://httpbin.org/headers'
url = 'http://yahoo.co.jp'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

# url= 'https://httpbin.org/headers'

# requests.get()でサイトにアクセス
# r = requests.get(url, params={'s':'python'})
#* useragentの偽装
# r = requests.get(url, headers=headers)
#* リダイレクトを無効にする - ページが存在しない場合にトップページに飛ばされるのを防ぐ
r = requests.get(url, timeout=3, allow_redirects=False)

print(r.url)
print(r.history)
# print(r.status_code)

print(r.text)

r.raise_for_status()

print('Success')
