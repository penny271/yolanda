#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

# -*- coding: utf-8 -*-
import os #! 汎用的なファイル名の設定
from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--incognito')

# -*- coding: utf-8 -*-

driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)
#- ウェブサイトが呼び込むのを何秒待つかを指定できる
driver.implicitly_wait(10)

driver.get('https://www.mizuhobank.co.jp/retail/takarakuji/check/numbers/backnumber/index.html')
sleep(3)

#- 1. トップページでurl一覧を取得する
latest_links = driver.find_elements_by_css_selector('tr.js-backnumber-temp-a > td:first-of-type > a')
backnumber_links = driver.find_elements_by_css_selector('tr.js-backnumber-temp-b > td > a')

#! 高度な表記方法 4'45秒あたり リストの結合 https://tinyurl.com/y8pck3mc
urls = [e.get_attribute('href') for e in latest_links+backnumber_links]
#- 2. Seleniumで各URLにアクセスして、ページのHTMLを取得する
#! 汎用的なファイル名の設定
dir_name = os.path.dirname(os.path.abspath(__file__))
for i, url in enumerate(urls):
  print('='*30, i, '='*30)
  print(url)
  driver.get(url) #アクセス先
  sleep(5)

  html = driver.page_source #アクセス先からhtmlを取得

  #! driver.title タイトルを取得する
  # p = f'/Users/aokihirotaka/Desktop/python_lesson_20220203/html/{driver.title}.html'
  #! driver.title タイトルを取得する 汎用的なファイル名の設定
  p = os.path.join(dir_name, 'html', f'{driver.title}.html')

  with open(p, 'w') as f:
    f.write(html)

sleep(3)
driver.quit()
