import requests

url = 'https://www.python.org/'
# url = 'https://www.python.org/zzz'
r = requests.get(url)

print(r.url)
print(r.status_code)

print(r.history)

print(r.history[0].url)
# print(r.history[0].status_code)

r.raise_for_status()

print('=====Success!!!=====')
