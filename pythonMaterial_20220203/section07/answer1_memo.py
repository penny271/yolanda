from socket import timeout
from time import sleep
from urllib import request

import requests
from bs4 import BeautifulSoup
import pandas as pd

d_list = []
#1 トップページへのアクセス
url = 'https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?wrk_plc_long_cd=0313000000&wrk_plc_long_cd=0313100000&wrk_plc_long_cd=0314000000&jb_type_long_cd=0100000000'
r = requests.get(url, timeout=3)
r.raise_for_status()

soup = BeautifulSoup(r.content,'lxml')

# 全ての企業ページボタンのaタグを取得
page_urls = soup.select('a:-soup-contains("企業ページ")')

for page_url in page_urls:
#! href="/company/cmi3940624006/" と書かれており、リンク先の情報が不足しているため情報の追記が必要
#- 複数の文字列を連結・結合: +, +=演算子 https://tinyurl.com/yagx4xmz
  page_url = 'https://next.rikunabi.com/' + page_url.get('href')

  sleep(3)

  page_r = requests.get(page_url, timeout=3)
  page_r.raise_for_status()

  page_soup = BeautifulSoup(page_r.content, 'lxml')

  # page_soup.select_one('ul[class=rnn-breadcrumb]')
  #- パンくずリストの一番最後の企業名を取得
  company_name = page_soup.select_one('.rnn-breadcrumb > li:last-of-type').text
  #- .rnn-col-11クラスの一番最後の値を取得 その下にあるaタグを取得 > を使わない理由は直下にaタグがないため
  url_in_tag = page_soup.select_one('.rnn-col-11:last-of-type a')
  #! 企業urlがない可能性があるためif文でエラーを避ける
  #¥ 三項演算子
  company_url = url_in_tag.get('href') if url_in_tag else None
  # if url_in_tag:
  #   company_url = url_in_tag.get('href')
  # else:
  #   company_url = None

  print('='*50)
  d_list.append({
    'company Name': company_name
    'company_url':company_url,
  })
  print(d_list[-1])
  # print(company_name)
  # print(company_url)

df = pd.DataFrame(d_list)
df.to_csv('company_list.csv', index=None, encoding='utf-8-sig')

