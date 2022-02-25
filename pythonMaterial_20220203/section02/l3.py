import requests

url = 'https://www.python.org/'
r = requests.get(url)

print(r.text[:10])
print(type(r.text[:10]))
print()
print(r.content[:10])
print(type(r.content[:10]))
