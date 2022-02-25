import requests
from bs4 import BeautifulSoup

url = 'https://www.anaconda.com/'
r = requests.get(url)


soup = BeautifulSoup(r.content, 'lxml')
# print(soup.h1.text)
#* メソッド使用推奨
# print(soup.find('h1').text)
# print(soup.find('span', id='getStartedButton').text)
#- classは予約語なので class_とする
# print(soup.find('h2', class_='pl-1').text)
print(soup.find('h2', class_='mb-1').text)
#* 純粋にallで全部とってきているが、.textは不可 配列の形となっている
# print(soup.find_all('h2', class_='mb-1'))

print("=========1==========")

#* 配列になっているのでfor文でループする必要有り - 全部取り出す場合
for h2 in soup.find_all('h2', class_='mb-1'):
  print(h2.text)

print("=========2==========")

#* 特定の配列の要素を指定して抜き出す
print(soup.find_all('h2',class_='mb-1')[1].text)
