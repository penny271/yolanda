#! 再現できなかったが、次の商品詳細のページに遷移するタイミングで認証が起きている模様
from ast import keyword
from cgitb import text
from concurrent.futures import thread
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import random
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re #正規表現を使うため - テキストの部分一致を取得するため
from tkinter import messagebox #_ to use a messagebox
import sys
# from tqdm import tqdm

# The content of the messagebox. Return => True or False
is_category_men = messagebox.askyesno(title = 'Confirm', message = 'Is gender category "Men"??',icon='warning')

user_agent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15']

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
options.add_argument('--incognito')
options.add_experimental_option('detach', True)

options.add_experimental_option('excludeSwitches', ['enable-logging'])

#! Change executable path according to your chrome webdriver location

service = Service("/Users/aokihirotaka/Desktop/python_lesson_20220203/tools/chromedriver")
# service = Service("C:\\chromedriver")
driver = webdriver.Chrome(service=service,options=options)
# driver.maximize_window()

#you can change the search keyword from here
# searchKeyword = 'nike'
# driver.get('https://www.2ndstreet.jp/search?category=950001&keyword=%s&sortBy=arrival&page=1'% (searchKeyword))

d_list = []
#! ebayのFXで付加する項目を認識するためのflag
ebay_category =''
iterated_num = 0 #タイトルを一意のものにするために付加する番号
#! for storing pictures url for inserting downloaded photos directly to ebay
DL_pic_list = []

#^ 絞り込みした複数の条件のときのurlを下記にペーストする
driver.get('https://www.2ndstreet.jp/search?category=951001&keyword=ARMANI&sortBy=cost-low')

base_url = 'https://www.2ndstreet.jp/search?category=951001&keyword=ARMANI&sortBy=cost-low&page={}'

iterated_num = 0 #タイトルを一意のものにするために付加する番号

#To find the total number of pages
page_number = driver.find_element(By.CLASS_NAME, 'pager').text[4]

#For storing products links
product_link_list= []

#For storing all the products images link
img_links_list=[]

#Page numbers range LOOP.
#Automatically get the whole page numbers so no need to adjust.
#! rang(1,x)と設定しているため、iは1から始まる
for i in range(1,int(page_number)+1):

    #- This line will open chrome with provided page number url
    # driver.get('https://www.2ndstreet.jp/search?category=950001&keyword=%s&sortBy=arrival&page=%i'% (searchKeyword,i))
    # driver.implicitly_wait(3)

    print('rangeのi', i)

    if i > 1:
        base_url = base_url.format(i+1)
        driver.get(base_url)
        sleep(2)
        driver.implicitly_wait(3)
    else:
        pass

    #This will get the whole div in which the products are present
    products_list = driver.find_element(By.CLASS_NAME, 'itemList')

    #This will find all the link tag in the div
    products_links = products_list.find_elements(By.TAG_NAME, 'a')

    #Variable to hold Products links on a specific page
    products_page=[]

    #Looping through all the products to get the images
    for product_link in products_links:

        #After visiting each product the website asks for login so in order to bypass that
        if product_link.get_attribute('href') == 'https://www.2ndstreet.jp/user/login':
            pass
        else:
            products_page.append(product_link.get_attribute('href'))

    #- product is each item page
    for index, product in enumerate(products_page):
        driver.get(product)
        sleep(2)

        print('='*15,index,'='*15)

        item_url = product
        iterated_num += 3
        page_soup = BeautifulSoup(driver.page_source, 'lxml')
        zoom_pictures = []
        pictures = page_soup.select('div[class="goods_popname"] > ul > li')

        for i, picture in enumerate(pictures):
            picture = picture.select_one('img').get('data-src')
            zoom_pictures.append(picture)
            #¥ storing for downloaded pictures
            DL_pic_list.append(picture)
        #- 新しいリストを作成 <= img_links
        zoom_pictures = '|'.join(zoom_pictures)
        DL_pic_list = ','.join(DL_pic_list)

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        item_title = page_soup.select_one('p.productName').text

        # category  不要

        #- 関数1
        def purify_size(x,y):
            if page_soup.find(text=re.compile(x)):
                try:
                    size_cm = float(page_soup.find(text=re.compile(x)).replace(x,'').replace('/',''))
                    return size_cm
                #example: 幅:24-36 <= string so float() cannot be used
                #caused ValueError
                except ValueError as e:
                    #! string形式で代入し、inchは''で表示させる
                    #厚み / <= / を取り除くための2つ目のreplace()
                    size_cm = page_soup.find(text=re.compile(x)).replace(x,'').replace('/','')
                    print('exceptのエラーメッセージ: ',e)
                    print('except ValueError(String型): ',size_cm)
                    return size_cm
            elif page_soup.find(text=re.compile(y)):
                try:
                    size_cm = float(page_soup.find(text=re.compile(y)).replace(y,'').replace('/',''))
                    return size_cm
                except ValueError as e:
                    #! string形式で代入し、inchは''で表示させる
                    size_cm = page_soup.find(text=re.compile(y)).replace(y,'').replace('/','')
                    print('exceptのエラーメッセージ: ',e)
                    print('except ValueError(String型): ',size_cm)
                    return size_cm
            else:
                size_cm = ''
                return size_cm

        #- 関数2
        def to_actual_size(handle, depth, height, width, unit):
            result = 'Approx size(handle / depth / height / width: ' + str(handle) + unit + ' / ' + str(depth) + unit + ' / ' + str(height) + unit + ' / ' + str(width) + unit + ')'
            return result

        handle_cm = purify_size('持ち手 ','no-css_selector')
        # size_handle_cm = float(page_soup.find(text=re.compile('持ち手')).replace('持ち手 ','' ))

        depth_cm = purify_size('マチ ','厚み ')

        height_cm = purify_size('高さ ','縦 ')

        width_cm = purify_size('幅 ','横 ')

        handle_inch = round(handle_cm / 2.54, 2) if handle_cm and type(handle_cm)== float  else ''
        depth_inch = round(depth_cm / 2.54, 2) if depth_cm and type(depth_cm)== float  else ''
        height_inch = round(height_cm / 2.54, 2) if height_cm and type(height_cm)== float  else ''
        width_inch = round(width_cm / 2.54, 2) if width_cm and type(width_cm)== float else ''

        actual_size_cm = to_actual_size(handle_cm, depth_cm, height_cm, width_cm, 'cm')

        actual_size_inch = to_actual_size(handle_inch, depth_inch, height_inch, width_inch, 'inch')

        bland_name = page_soup.select_one('p.blandName').text.strip()
        product_name = page_soup.select_one('p.productName').text.replace('/',' ').strip()
        item_title = bland_name+' '+product_name

        # category  不要
        if page_soup.select_one('dt:-soup-contains("型番")+dd'):
            model = page_soup.select_one('dt:-soup-contains("型番")+dd').text.strip()
            model='' if model == 'ー' else model

            color = page_soup.select_one('dt:-soup-contains("カラー")+dd').text.strip()

            pattern = page_soup.select_one('dt:-soup-contains("柄")+dd').text.strip()

            material = page_soup.select_one('dt:-soup-contains("素材・生地")+dd').text.strip()
            material='' if material == 'ー' else material

            category_complete = []
            category_whole = page_soup.select('section#breadcrumb > span > a')
            category_brand = page_soup.select_one('section#breadcrumb > span:nth-of-type(2) > a > span').text
            for category in category_whole:
                category_complete += [category.text]

            category_complete = ' '.join(category_complete)
            category_complete = category_complete.replace('ホーム','').replace(category_brand,'').replace('商品詳細','').replace('バッグ','',1).strip()

            brand_name = category_brand

            #! decompose 指定した要素を完全に削除し破壊するメソッド いらない子要素を削除
            # https://tinyurl.com/ycd9sqr3
            page_soup.select_one('div.conditionStatus > div').decompose()

            #- 目的のもののみ取得できた! 20220220
            condition = page_soup.select_one('div.conditionStatus').text.strip().replace( '\n' , '' )

            print('decompose後のcondition', condition)

            try:
                #- split('店頭')で余分な言葉を省いている
                condition_detail = page_soup.select_one('div#shopComment').text.strip().split('店頭')[0]
            except AttributeError as e:
                print('ErrorMessage:',e)
                condition_detail = ''

            #- 属性の値を取得
            item_price = int(page_soup.select_one('span.priceNum').get('content').strip())

            d_list.append({
                '*Action(SiteID=US|Country=JP|Currency=USD|Version=745|CC=UTF-8)': 'Add',
                'DL-eb-category': 'bag_m:52357 / bag_w:169291',
                'X-number': str(iterated_num).zfill(3),
                '*Title': '',
                # 'U-title': item_title,
                'U-title': item_title,
                'X-category':category_complete,
                'Ref-title_category_combined':'Dont use this time',
                'Ref-translation':'"=if(E2="","",googletranslate(E2,"ja","en"))',
                #- モデル名の参照を削除-すでにタイトルに含まれているため
                'URef-title-completed':'"=H2&" "&"Bag"&" "&"from Japan"&" "&C2',
                'Ref-len()': '"=len(D2)',
                'Ref-material_translation': '"=if(Y2="","",googletranslate(Y2,"ja","en"))',
                'URef-size_for_ConditionDescription':'"=M2&" | "&N2&" | "&" Model: "&X2&" | "&"Material: "&K2&" | "&"For more details, please check the pictures carefully and judge the condition.',
                'X-actual_size_inch': actual_size_inch,
                'X-actual_size_cm': actual_size_cm,
                'CustomLabel' : '',
                '*Description' : '',
                #¥ New 20220211
                #- ConditionDescription にはサイズや型番、状態が入る
                'ConditionDescription': '',
                '*StartPrice' : '',
                'MinimumBestOfferPrice': '"¥=R2',
                'url': item_url,
                'costPrice + s/p': item_price + 770,
                # 'combined':'=c{num}+h{num}'.format(num = i+2),
                'ConditionID' : '3000',
                'PicURL':zoom_pictures,
                'X-model': model,
                'X-material': material,
                'X-condition': condition,
                'X-condition_detail': condition_detail,
                'C:Brand': brand_name,
                # 'C:Brand': delete_brackets.delete_brackets(brand_name),
                'X-color': color,
                'X-gender': '',
                # 'X-all_sizes': store_all_sizes,
            })
        else:
            #! elseのif どのくらいの頻度で倉庫取り寄せ品があるか知るために
            #! あえてexcelファイルに出力するようにしている。
            d_list.append({
                '*Action(SiteID=US|Country=JP|Currency=USD|Version=745|CC=UTF-8)': 'Dont Use this item. Delete this row',
                'DL-eb-category': 'Dont Use this item. Delete this row',
                'X-number': str(iterated_num).zfill(3),
                '*Title': 'Dont Use this item. Delete this row.Dont Use this item. Delete this row.Dont Use this item. Delete this row',
                # 'U-title': item_title,
                'U-title': 'Dont Use this item. Delete this row',
                'X-category':'Dont Use this item. Delete this row',
                'Ref-title_category_combined':'Dont Use this item. Delete this row',
                'Ref-translation':'Dont Use this item. Delete this row',
                #- モデル名の参照を削除-すでにタイトルに含まれているため
                'URef-title-completed':'Dont Use this item. Delete this row',
                'Ref-material_translation': 'Dont Use this item. Delete this row',
                'URef-size_for_ConditionDescription':'Dont Use this item. Delete this row',
                'X-actual_size_inch': 'Dont Use this item. Delete this row',
                'X-actual_size_cm': 'Dont Use this item. Delete this row',
                'CustomLabel' : 'Dont Use this item. Delete this row',
                '*Description' : 'Dont Use this item. Delete this row',
                #¥ New 20220211
                #- ConditionDescription にはサイズや型番、状態が入る
                'ConditionDescription': 'Dont Use this item. Delete this row',
                '*StartPrice' : 'Dont Use this item. Delete this row',
                'MinimumBestOfferPrice': '"¥=R2',
                'url': item_url,
                'costPrice + s/p': 0,
                # 'combined':'=c{num}+h{num}'.format(num = i+2),
                'ConditionID' : 'Dont Use this item. Delete this row',
                'PicURL':'Dont Use this item. Delete this row',
                'X-model':'Dont Use this item. Delete this row',
                'X-material': 'Dont Use this item. Delete this row',
                'X-condition': 'Dont Use this item. Delete this row',
                'X-condition_detail': 'Dont Use this item. Delete this row',
                'C:Brand': 'Dont Use this item. Delete this row',
                # 'C:Brand': delete_brackets.delete_brackets(brand_name),
                'X-color': 'Dont Use this item. Delete this row',
                'X-gender': 'Dont Use this item. Delete this row',
                # 'X-all_sizes': store_all_sizes,
                #¥ 追加_20220221
                'DL-pic': '',
            })
            print('='*30)
            print('除外: 倉庫より出荷: ',d_list[-1])


    #残りの項目を取得していく
#It will create a new file inside the project
# with open('new_file.csv', 'w+', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['PicURL'])
#     writer.writerows(img_links_list)

#It will create a new file inside the project
df = pd.DataFrame(d_list)

if is_category_men == True:
    df_add = pd.read_excel('e_category_no/bag_men.xlsx')
else:
    df_add = pd.read_excel('e_category_no/bag_women.xlsx')

df_complete = pd.concat([df,df_add],axis=1)

#! change the file name every time
df_complete.to_excel('2st_Armani_m200k-300k_bag_men_ver2_.xlsx', index=False)
