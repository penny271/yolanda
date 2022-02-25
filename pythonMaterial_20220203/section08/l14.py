#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

driver.get('https://news.yahoo.co.jp/')
sleep(3)

#¥ 69. 8-13. JavaScriptを使ってページをスクロールする
#! execute_script()の中にはjavaScriptを記述する

#! 文字列の中で変数を使う方法 fと{}を使う
#- 徐々にスクロールしていく処理
search_box = driver.find_element_by_css_selector('input.sc-kgoBCf')
sleep(2)

search_box.send_keys('機会学習')
sleep(2)

search_box.submit()
sleep(2)

while True:
  # height = driver.execute_script('return document.body.scrollHeight')
  #- 1. スクロール
  # driver.execute_script(f'window.scrollTo(0,{height})')
  #! 直接、変数を使わずにdriver.execute_script('return document.body.scrollHeight')を入れている
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  sleep(2)

  #-2 ボタンのcssセレクタを取得する
  #! このコードだと最後の”もっと見る”ボタンが無くなったタイミングでエラーが発生する => Unable to locate element: {"method":"css selector","selector":"div.newsFeed > div > span > button"}
  # button = driver.find_element_by_css_selector('div.newsFeed > div > span > button')
  # sleep(2)

  #- find_elements_でリストでbuttonを取得することで、見つからなかった場合でも空の状態を返すだけなのでエラーを回避できる
  button = driver.find_elements_by_css_selector('div.newsFeed > div > span > button')
  sleep(2)

  #-3 ボタンを押す
  #! ループしないように終了する場合の処理を書く - 最終的に表示できる記事がなくなったらbuttonは消える
  if button:
    # button.click()
    button[0].click()
  else:
    break

a_tags = driver.find_elements_by_css_selector('.newsFeed_item_link')

for i, a_tag in enumerate(a_tags):
  print('='*30, i , '='*30)
  print(a_tag.find_element_by_css_selector('.newsFeed_item_title').text)
  print(a_tag.get_attribute('href'))

#- ブラウザを閉じる (command + q)
driver.quit()
