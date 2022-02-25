from re import search
from time import sleep
from selenium import webdriver


options = webdriver.ChromeOptions()
# 1. ヘッドレスモードでの使用 argumentは引数という意味
#- ブラウザを立ち上げずにseleniumを使うモード
# options.add_argument('--headless')

#2. シークレットモードでの使用
options.add_argument('--incognito')


#3. User-Agentの設定
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36')


# STEP1 : Driverの作成
driver = webdriver.Chrome(executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver', options=options)

# STEP2 : driver.get()でサイトにアクセスする
# driver.get('https://www.google.co.jp')
#! websiteにアクセスする動作を挟んだのでsleepを入れる
driver.get('https://testpage.jp/tool/ip_user_agent.php')
sleep(3)

# STEP3 : 要素を取得して何らかの処理をする

driver.quit()
