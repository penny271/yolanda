from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')

for li in post.find_all('li'):
  print(li.find('time').text)
  print(li.find('a').text)

# 見やすくする Pythonのenumerate()関数を使うと、forループの中でリストやタプルなどのイテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる。
for i, li in enumerate(post.find_all('li')):
    print('='*30, i, '='*30)
    print('タイトル : ', li.find('a').text)
    print('日付 : ', li.find('time').text)
