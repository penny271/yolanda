from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)

driver.get('https://news.yahoo.co.jp/')
sleep(3)

print(driver.title)
print(driver.current_url)

driver.get('https://google.com')
sleep(3)

print(driver.title)
print(driver.current_url)

driver.back()
sleep(3)

driver.forward()
sleep(3)

driver.refresh()
sleep(3)

#- ブラウザを閉じる (command + q)
# driver.quit()
#- ページを閉じる (ctrl + w)
driver.close()
