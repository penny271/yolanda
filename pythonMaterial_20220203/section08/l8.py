from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')

driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)
#- ウェブサイトが呼び込むのを何秒待つかを指定できる
driver.implicitly_wait(10)

driver.get('https://news.yahoo.co.jp/')
sleep(3)


#- 要素を一つを見つける場合
# e = driver.find_element_by_tag_name('h2')
# print(e.text)
# print(e.get_attribute('outerHTML'))
# findと同じ意味

#- 要素を複数を見つける場合 - find_elements_ と複数形になる
h2_tags = driver.find_elements_by_tag_name('h2')

for h2_tag in h2_tags:
  print(h2_tag.text)
  print(h2_tag.get_attribute('outerHTML'))


#- ブラウザを閉じる (command + q)
driver.quit()
