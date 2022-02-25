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

#¥ 68. 8-12. 自動で要素をクリックする
a_tag = driver.find_element_by_css_selector('div.sc-iUpOdG > div > ul > li:nth-of-type(3) > a')

sleep(3)

a_tag.click()
sleep(3)

#- ブラウザを閉じる (command + q)
driver.quit()
