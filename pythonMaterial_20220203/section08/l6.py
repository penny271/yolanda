from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)
#- ウェブサイトが呼び込むのを何秒待つかを指定できる
driver.implicitly_wait(10)

driver.get('https://news.yahoo.co.jp/')
sleep(3)

driver.find_element_by_id('pppppppppp')

#- ブラウザを閉じる (command + q)
# driver.quit()
#- ページを閉じる (ctrl + w)
driver.close()
