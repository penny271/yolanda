from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')

#* aタグの属性の中身全てを取得 - 辞書型が返ってくる {'href':'url'}
print(post.find('li').find('a').attrs)
#* aタグの属性の中身を取得 - 辞書型が返ってくる urlの部分
print(post.find('li').find('a').attrs['href'])
#* attrs省略可
print(post.find('li').find('a')['href'])
#* getでも取得可能
print(post.find('li').find('a').get('href'))
print(post.find('li').find('span').text)

print(post.parent)
# print(post.find('ul').contents)
for tag in post.find('ul').contents:
  print(tag.text)

for i,tag in enumerate(post.find_all('li')):
  print(i+1,tag.text)
