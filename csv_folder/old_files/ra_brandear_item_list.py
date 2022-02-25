#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

d_list = []
first_page_url ='https://search.rakuten.co.jp/search/mall/tumi/565210/?s=11&sid=304623'

base_url ='https://search.rakuten.co.jp/search/mall/tumi/565210/?{}s=11&sid=304623'

d_list = []


# 'https://www.yourshoppingmap.com/brand/295-moorer?page=2#boutiques'

#! 要range()の中の数字をページ数に合わせること!
for i in range(1):
  print('='*30, i, '='*30)
  url = base_url.format('p='+str((i+1))+'s=11')
  print('url============',url)
  sleep(2)

  #! timeoutを長くすることで次に以降できた
  r = requests.get(url, timeout=10)
  r.raise_for_status()

  soup = BeautifulSoup(r.content, 'lxml')
  # page_urls = soup.select('a:-soup-contains("企業ページ")')
  page_urls = soup.select('div.dui-cards > div.dui-card > div.image > a')

  #! ループ2回目で認証が入り、
  for i, page_url in enumerate(page_urls):
    page_url = page_url.get('href')
    print('ループ=========',page_url)
    print('ループ',i)
    sleep(2)

    page_req = requests.get(page_url, timeout = 15)
    page_req.raise_for_status()

    page_soup = BeautifulSoup(page_req.content, 'lxml')

    pictures = page_soup.select('tbody > tr > td > a')

    picture_set = []
    # pictures = page_soup.select('div[class="goods_popname"] > ul > li')
    for i, picture in enumerate(pictures):
      picture_set.append(picture.get('href'))
      print('====',i,picture)
      sleep(0.5)


  #! 要if分削除 if文は検証を楽にするために書いてあるだけなので。ifを使う場合はそれ以降のcsvに書き出す処理以外を全てに右に一つインデントを入れる必要あり また、elseの作成が必要


    # shop_address = page_soup.select_one('address')
    # #! 三項演算子
    # shop_address = shop_address.text if shop_address else None
    # #! 2つのクラスを含む要素の隣の要素aタグの要素
    # shop_url = page_soup.select_one('.icon.icon-world+span > a')
    # shop_url = shop_url.get('href') if shop_url else None
    # #! 2つのクラスを含む要素の隣の要素aタグの要素
    # shop_email = page_soup.select_one('.icon.icon-mail+span > a')
    # shop_email = shop_email.text if shop_email else None
    # #! 2つのクラスを含む要素の隣の要素の中のaタグの要素
    # shop_phone = page_soup.select_one('.icon.icon-phone+span > a')
    # shop_phone = shop_phone.text if shop_phone else None
