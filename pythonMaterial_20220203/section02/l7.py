 import requests

url = 'https://www.python.org/'
r = requests.get(url, timeout=3)

print(r.url)
print(r.status_code)
