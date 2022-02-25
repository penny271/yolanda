import requests

url = 'http://www.python.org/'
r = requests.get(url, timeout=3, allow_redirects=False)

print(r.url)
print(r.history)
