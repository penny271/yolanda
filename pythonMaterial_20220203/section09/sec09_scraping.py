#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07
from time import sleep
from urllib import request

from bs4 import BeautifulSoup
import requests
import pandas as pd

# HTMLを読み込む
# 'r'は、readの省略
with open('company_list.html','r') as f:
  html = f.read()

# HTMLを解析する
soup = BeautifulSoup(html,'lxml')

# 会社名、住所、電話番号を取得する
a_tags = soup.select('span.exe > a')

print('掲載企業数 = a_tagsの数', len(a_tags))

d_list = []
for i, a_tag in enumerate(a_tags):
  url = 'https://atsumaru.jp/' + a_tag.get('href')
  r = requests.get(url)
  r.raise_for_status()

  sleep(3)

  page_soup = BeautifulSoup(r.content, 'lxml')

  company_name = page_soup.select_one('#detailBox > h2').text
  #- "地図はこちら" の文字を含んだtdタグの中の最初のpタグのデータ
  address = page_soup.select_one('td:-soup-contains("地図はこちら") > p:first-of-type').text
  tel = page_soup.select_one('div.telNo > p > strong > a').text

  d_list.append({
    'company_name': company_name,
    'address' : address,
    'tel' : tel
  })
  print('='*30, i, '='*30)
  print(d_list[-1])

  if i > 10:
    break

df = pd.DataFrame(d_list)
df.to_csv('s09_company_list.csv', index=None, encoding='utf-8-sig')
