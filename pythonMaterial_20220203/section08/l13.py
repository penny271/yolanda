from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--incognito')

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

height = 500
# while height < 3000:
#! 文字列の中で変数を使う方法 fと{}を使う
#- 徐々にスクロールしていく処理
  # driver.execute_script('window.scrollTo(0, 500)')
  # driver.execute_script(f'window.scrollTo(0, {height})')
  # height += 200
  # sleep(0.5)

#- スクロールで下まで行く処理
height = driver.execute_script('return document.body.scrollHeight')
sleep(2)

#! 文字列の中で変数を使う方法 fと{}を使う
driver.execute_script(f'window.scrollTo(0, {height})')
sleep(2)

#- ブラウザを閉じる (command + q)
driver.quit()
