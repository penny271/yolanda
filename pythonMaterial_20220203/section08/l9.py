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

#! idで指定された中の要素も全てprintされる!
# e = driver.find_element_by_id('uamods-topics')
# print(e)
# print(e.text)

a_tags = driver.find_elements_by_class_name('sc-frDJqD')

for a_tag in a_tags:
  print(a_tag)
  print(a_tag.get_attribute('href'))
  print(a_tag.text)


#- ブラウザを閉じる (command + q)
driver.quit()
