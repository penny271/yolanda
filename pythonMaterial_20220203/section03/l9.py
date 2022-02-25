from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')

#* 完全一致したテキストを見つける
print(post.find(text='Latest News').parent)
print(soup.find(href='/about/'))
