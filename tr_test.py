#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

#to date : https://atmarkit.itmedia.co.jp/ait/articles/2111/09/news015.html

# -*- coding: utf-8 -*-
from tabnanny import filename_only
from time import sleep
from numpy import delete
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests #! いらない
from bs4 import BeautifulSoup
import pandas as pd
import random
import datetime
import glob
#¥ 括弧内及び括弧内の文字を削除する関数をimport
#^ パスの指定方法: https://tinyurl.com/ybfxc7av
from functions import delete_brackets
# _to use a messagebox
from tkinter import messagebox
import sys
import math

# The content of the messagebox. Return => True or False
is_category_men = messagebox.askyesno(title = 'Confirm', message = 'Is gender category "Men"??',icon='warning')

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
print(repr(now))

#! 要修正
today = now.strftime('%Y%m%d')

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36']

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])

options.add_argument('--incognito')
#! ChromeDriver起動時にdetachオプションを設定し、quit()やclose()を呼ばなければ、Selenium実行後もChromeを開いたままにできる。
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(
    executable_path='/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver',
    options=options
)
#- ウェブサイトが呼び込むのを何秒待つかを指定できる
driver.implicitly_wait(10)

#- ブランド名入力 -> レディース or メンズ選択 => カテゴリのバッグ の順で絞り込む()内は多分不要(page2へ移動し、そこからpage1に移動したところでpage1のurlを取得しdriver.get()の中に記載する => この移動をすることで語尾の &key を出現させる)
driver.get('https://www.trefac.jp/store/t2cpsb/?srchword=fendi%20%E3%83%90%E3%83%83%E3%82%B0&step=1&disp_num=90')
sleep(2)

d_list = []
# base_url ='https://www.trefac.jp/store/t1cpsb/?srchword=tumi&step=1&order=pdown&disp_num=90&key={}'

iterated_num = 0 #タイトルを一意のものにするために付加する番号

#! 検索するアイテムごとに修正が必要
#! 34行目のコードに &key={} をurlの最後に付け足す必要あり!
#to 45行目のrange()の数を取得するページ数に応じて変更の必要あり!
base_url ='https://www.trefac.jp/store/t2cpsb/?srchword=fendi%20%E3%83%90%E3%83%83%E3%82%B0&step=1&disp_num=90&key={}'

# 'https://www.yourshoppingmap.com/brand/295-moorer?page=2#boutiques'

#- 関数_1
def strip_text(css_selector):
    result = page_soup.select_one(css_selector).text.strip()
    return result

#- 関数_2
def purify_size(x,y):
    if page_soup.select_one(x):
        size_cm = page_soup.select_one(x)
        try:
            #! オンラインショップ上のサイズ表記が間違っており "約c33m" と記載されており、エラーになったため修正
            size_cm = float(size_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if size_cm else ''
            #! returnをつけ忘れないように! そうしないと計算した値を後から代入できない
            return size_cm

        except ValueError as e:
            print('catch ValueError:', e)
            #! 直でreturn 可能では? return float(size_cm.text.replace(...))
            #¥ 下記のように空白が必要か結果を確認する
            size_cm = ''
            return size_cm
    elif page_soup.select_one(y):
        size_cm = page_soup.select_one(y)
        try:
            size_cm = float(size_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if size_cm else ''
            return size_cm
        except ValueError as e:
            print('catch ValueError:', e)
        size_cm = ''
        return size_cm
    else:
        size_cm = ''
        return size_cm

#- 関数3
def to_actual_size(height, width, depth, handle, shoulder_strap, unit):
    result = 'Approx size(height / width / depth / handle / shoulder-strap: ' + str(height) + unit + ' / ' + str(width) + unit + ' / ' + str(depth) + unit + ' / ' + str(handle) + unit + ' / ' + str(shoulder_strap) + unit + ')'
    return result

#to 4 取得するページ数に応じて変更の必要あり!
#¥ range(x) 手動で変える必要がありそう => ページ数をrange()に入れる




#¥------------------修正箇所------------------¥¥¥¥¥¥¥
import math

# get total number of the items in all pages
search_result_number = int(driver.find_element_by_css_selector('span.search_result_num').text)
print('search_result_number=============',search_result_number)

# get total number of the items in the current page
current_item_number = int(driver.find_element_by_css_selector('span#displayoption_num_btn_current').text.replace('件',''))
print(current_item_number)

# get the total page number to decide how many loops you need
total_page_number = math.ceil(search_result_number / current_item_number)
print(total_page_number)


for i in range(total_page_number):
    # print('='*30, i, '='*30)
    url = base_url.format(i+1)
    #- seleniumで読み込み
    print('='*30)
    print("current_page_num:",i)

    if i == 0:
        pass
    else:
        driver.get(url)
        sleep(4)
        print('='*30)
        print("current_page_num: ")

    print('#'*30)
    print("End")
