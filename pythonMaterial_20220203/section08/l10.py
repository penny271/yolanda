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

# a_tags = driver.find_elements_by_class_name('sc-frDJqD')

#¥ 66. 8-10. SeleniumでCSSセレクタを元に情報抽出する
# a_tags = driver.find_elements_by_css_selector('.sc-frDJqD')

# for a_tag in a_tags:
#   # print(a_tag)
#   print(a_tag.get_attribute('href'))
#   print(a_tag.text)

#¥ 66. 8-10. SeleniumでCSSセレクタを元に情報抽出する
a_tag = driver.find_element_by_css_selector('div.sc-iUpOdG > div > ul > li:nth-of-type(3) > a')

print(a_tag.get_attribute('href'))
print(a_tag.text)

#- ブラウザを閉じる (command + q)
driver.quit()
