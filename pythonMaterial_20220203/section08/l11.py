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

#¥ 67. 8-11. 検索ボックスの取り扱い(入力・検索・削除)
#- inputタグの.クラス名
search_box = driver.find_element_by_css_selector('input.sc-kgoBCf')
sleep(3)

search_box.send_keys('Python')
sleep(5)

#! websiteによっては動かないことがある clear()
# search_box.clear()
text = search_box.get_attribute('value')
search_box.send_keys(Keys.BACK_SPACE * len(text))

sleep(5)

search_box.send_keys('機械学習')
sleep(5)

search_box.submit()
sleep(3)

#- ブラウザを閉じる (command + q)
driver.quit()
