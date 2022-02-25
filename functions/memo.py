from time import sleep, time
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')

driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)

#- seleniumで特定の要素のhtmlをとってくる方法
e = driver.find_element_by_tag_name('h2')
print(e.text)
#! h2のhtmlを取得
print(e.get_attribute('outerHTML'))


#-----
a_tag = driver.find_element_by_css_selector('div.sc-iUpOdG > div > ul > li:nth-of-type(2) > a')
print(a_tag.text)
print(a_tag.get_attribute('href'))
a_tag.click()
sleep(3)

height = 500
while height < 3000:
  driver.execute_script(f'window.scrollTo(0, {height})')
  height += 100
  sleep(1)

#-----
height = driver.execute_script('return document.body.scrollHeight')
sleep(1)

driver.execute_script(f'window.scrollTo(0, {height})')
sleep(1)


#- 8-14 もっと見るボタンを存在し続ける限り押し続ける処理
while True:
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  sleep(1)

  #!!あえて find_elements_by_css~ にする!! エラーを避け、動作が止まるのを防ぐため -> 要素がなくても空のリストが作られるだけでエラーが出ない
  button = driver.find_elements_by_css_selector('div.newsFeed > div > span > button')
  sleep(1)

  #! エラーを避けるためリストでbuttonを取得しているので、一番目のものを取得する button[0].click()
  if button:
    button[0].click()
  else:
    break

#- 8-15 Seleniumを使用したスクレイピングのベストプラクティス
#! タグの取得などはBeautifulSoupに任せる => 処理が早い

#¥ urlの最後に /robots.txt を加え、検索することでどのpathにuserAgentがアクセスしてはいけないかを確認できる

# https://note.nkmk.me/python-string-concat/
# 文字列のリスト（配列）を連結・結合: join()

l = ['aaa', 'bbb', 'ccc']

s = ''.join(l)
print(s)
# aaabbbccc

s = ','.join(l)
print(s)
# aaa,bbb,ccc

s = '-'.join(l)
print(s)
# aaa-bbb-ccc

#!!!!  trefac_item_list.pyより 20220209
#- もし表記が統一されていれば、下記が使えた。
  size_width_cm = int(page_soup.select_one('dl.sizedescription_size > div:nth-of-type(2)> div:first-of-type > dd.sizedescription_size_desc').text.replace('約',' ').replace('cm', ''))
  size_height_cm = int(page_soup.select_one('dl.sizedescription_size > div:nth-of-type(2)> div:nth-of-type(2) > dd.sizedescription_size_desc').text.replace('約',' ').replace('cm', ''))
  size_depth_cm = int(page_soup.select_one('dl.sizedescription_size > div:nth-of-type(2)> div:nth-of-type(3) > dd.sizedescription_size_desc').text.replace('約',' ').replace('cm', ''))

  size_width_inch = round(size_width_cm / 2.54, 2)
  size_height_inch = round(size_height_cm / 2.54, 2)
  size_depth_inch = round(size_depth_cm / 2.54, 2)

  actual_size_cm = 'Approx size(height / width / depth): ' + str(size_width_cm) + 'cm / ' + str(size_height_cm) + 'cm / ' + str(size_depth_cm) + 'cm'

  actual_size_inch = 'Approx size(height / width / depth): ' + str(size_width_inch) + 'inch / ' + str(size_height_inch) + 'inch / ' + str(size_depth_inch) + 'inch'

  print('cm - inch -' *10)
  print(actual_size_cm)
  print(actual_size_inch)


#- 3-9. レベルアップ知識①：完全一致で指定したテキストを持つ要素を取得する
print(post.find(text='Latest News'))
print(post.find(text='Latest News').parent)
print(post.find(href='/about/').parent)

#- 3-10. レベルアップ知識②：部分一致で指定したテキストを持つ要素を取得する
#! 正規表現をpythonにimportする必要あり
import re

#Pythonが入っている全ての要素を取得する
print(soup.find_all(text=re.compile('Python')))

for text in soup.find_all(text=re.compile('Python')
  print(text)
  #!部分一致した文字列が格納されているhtmlを取得できる
  print(text.parent)

#¥ aタグでPythonが入っている全ての要素を取得する
for text in soup.find_all('a',text=re.compile('Python')):
  print(text)

in soup.find_all('a',href=re.compile('docs.python.org')):
  print(text)

#- 49. 6-8. テキストを元に要素を指定する css-selector
print(soup.select('li:contains("Python")')) #!非推奨
print(soup.select('li:-soup-contains("Python")'))

model = page_soup.select_one('table th:-soup-contains("型番") + td')

model = page_soup.select_one('th:-soup-contains("型番")+ td')

#- 操作して表示数や表示形式をseleniumで動かす処理_20220209
#! 最初からソートした状態のurlを渡したほうが楽かも
# driver.get('https://www.trefac.jp/store/tcpsb/?srchword=tumi&step=1&disp_num=30')
#! New 検証用
#to ブランド名入力 -> レディース or メンズ => カテゴリのバッグ の順で絞り込み
driver.get('https://www.trefac.jp/store/tc94psb/?srchword=tumi&step=1&order=new')
sleep(2)

num_button_select = driver.find_element_by_css_selector('div.displayoption_num > div > button')
print(num_button_select.get_attribute('outerHTML'))
sleep(1)

#to 表示件数を30から90に変更する処理
# num_button_select.click()
# sleep(1)

num_button = driver.find_element_by_css_selector('div.displayoption_num_inner > div > ul > li:nth-of-type(3) > button')
sleep(1)

# num_button.click()
# sleep(1)
#to --表示件数を30から90に変更する処理_終わり--

#to 表示順を関連度順から価格の安い順に変更する処理
price_order_select = driver.find_element_by_css_selector('div.displayoption_sort_inner > button')
sleep(1)

# price_order_select.click()
# sleep(1)

price_order = driver.find_element_by_css_selector('div.displayoption_sort_inner > div > ul > li:nth-of-type(3) > button')
print(price_order.get_attribute('outerHTML'))
sleep(1)

# price_order.click()
# sleep(1)
#to --表示順を関連度順から価格の安い順に変更する処理_終わり----


#- tryで回避可能! => floatに変えることで tryの使用不要
if page_soup.select_one('dt:-soup-contains("マチ") + dd'):
  depth_cm = page_soup.select_one('dt:-soup-contains("マチ") + dd')
  try:
    # depth_cm = int(float(depth_cm.text.replace('約',' ').replace('cm', ''))) if depth_cm else None
    depth_cm = float(depth_cm.text.replace('約',' ').replace('cm', '')) if depth_cm else None
    print('try', depth_cm)
  except ValueError as e:
    print(e)
else:
  pass
