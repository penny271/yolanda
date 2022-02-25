#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')

# -*- coding: utf-8 -*-

driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)
#- ウェブサイトが呼び込むのを何秒待つかを指定できる
driver.implicitly_wait(10)

driver.get('https://atsumaru.jp/area/7/list?sagid=all')
sleep(3)

#! execute_script()の中にはjavaScriptを記述する
height = driver.execute_script('return document.body.scrollHeight') #1000
new_height = 0

while True:
  print(height)
  #! 直接、変数を使わずにdriver.execute_script('return document.body.scrollHeight')を入れている
  # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  driver.execute_script(f'window.scrollTo(0, {height})') #1000 (height分スクロールする)
  sleep(3)

  new_height = driver.execute_script('return document.body.scrollHeight') #2000

  #! 下までスクロールして下がれなくなったらループを止める
  if height == new_height:
    break
  height = new_height #height = 2000 これらを繰り返す

#- ページのhtmlを保存
# 'w'は、writeの省略
with open('company_list.html','w') as f:
  f.write(driver.page_source)

driver.quit()
