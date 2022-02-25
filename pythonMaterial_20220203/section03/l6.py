from bs4 import BeautifulSoup
import requests

url = 'https://www.anaconda.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
#* 属性の指定  <div data-barba="container">
print(soup.find_all(attrs={'data-barba':'container'}))
print(soup.find('h2', class_='mb-1'))
#- 上記の属性を使った別の書き方
print(soup.find(attrs={'class':'mb-1'}))
