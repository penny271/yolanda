#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

from time import sleep

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests #! いらない
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--incognito')
#! ChromeDriver起動時にdetachオプションを設定し、quit()やclose()を呼ばなければ、Selenium実行後もChromeを開いたままにできる。
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)
#- ウェブサイトが呼び込むのを何秒待つかを指定できる
driver.implicitly_wait(10)

sleep(2)
driver.get('https://store.shopping.yahoo.co.jp/brandear/search.html?p=tumi&x=0&y=0&strcid=a5d0a5c3a5&X=2#CentSrchFilter1')

d_list = []

base_url ='https://store.shopping.yahoo.co.jp/brandear/search.html?p=tumi&x=0&y=0&strcid=a5d0a5c3a5&X=2&page={}#CentSrchFilter1'


# 'https://www.yourshoppingmap.com/brand/295-moorer?page=2#boutiques'

#! 要range()の中の数字をページ数に合わせること!
for i in range(1):
  print('='*30, i, '='*30)
  url = base_url.format(i)
  print('url============',url)
  sleep(2)

  if i == 0:
    pass
  else:
    driver.get(url)
    sleep(4)

  soup = BeautifulSoup(driver.page_source, 'lxml')
  # a_tags = soup.select('div.mdSearchResult > ul > li > div > div > div > a.elImageLink')
  a_tags = soup.select('div.mdSearchResult a.elImageLink')

  #! ループ2回目で認証が入り、
  for i, a_tag in enumerate(a_tags):
    page_url = a_tag.get('href')
    print('loop',i,'=========',page_url)
    driver.get(page_url)
    sleep(2)

    # driver.click()

    first_thumbnail = driver.find_element_by_css_selector('ul.elThumbnailItems > li:first-of-type')

    first_thumbnail.click()

    #! これであっているか検証 <= 意味がなかった。BeautifulSoupでは隠れている要素を指定して持ってくることはできなかった - 他の要素を取得する際には使えそう
    # page_soup = BeautifulSoup(driver.page_source, 'lxml')

    # pictures = page_soup.select('body > div:nth-of-type(2).uiShoppingModule ul.elThumbnailCarouselPanel > li > a')
    pictures = driver.find_elements_by_css_selector('div.elHeader.elCloned + div.elMain > ul > li > img')
    print('pictures ==== ', pictures) #! 取れてきていない

    picture_set = []
    # pictures = page_soup.select('div[class="goods_popname"] > ul > li')
    for i, picture in enumerate(pictures):
      picture_set.append(picture.get_attribute('src'))
      print('====',i,picture.get_attribute('src'))
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
