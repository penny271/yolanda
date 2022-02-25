import requests

# url = 'https://tech-diary.net/?s=python'
# r = requests.get(url)

url = 'https://tech-diary.net/'
r = requests.get(url, params={'s': 'python'})

print(r.url)
print(r.status_code)
