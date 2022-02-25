#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

#to date : https://atmarkit.itmedia.co.jp/ait/articles/2111/09/news015.html

# -*- coding: utf-8 -*-
from time import sleep
from numpy import delete
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests #! いらない
from bs4 import BeautifulSoup
import pandas as pd
import random
import datetime
#¥ 括弧内及び括弧内の文字を削除する関数をimport
from functions import delete_brackets

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
print(repr(now))

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
sleep(2)
driver.get('https://www.trefac.jp/store/search_result.html?srchword=&step=1&k_uid=iRZAizkTyUQPCXNzKJQ1E32okWpW5i&q=%E3%83%99%E3%83%A9%E3%83%BB%E3%83%96%E3%83%A9%E3%83%83%E3%83%89%E3%83%AA&searchbox=1')

d_list = []
# base_url ='https://www.trefac.jp/store/t1cpsb/?srchword=tumi&step=1&order=pdown&disp_num=90&key={}'

#! 検索するアイテムごとに修正が必要
#! 34行目のコードに &key={} をurlの最後に付け足す必要あり!
#to 45行目のrange()の数を取得するページ数に応じて変更の必要あり!
base_url ='https://www.trefac.jp/store/search_result.html?srchword=&step=1&k_uid=iRZAizkTyUQPCXNzKJQ1E32okWpW5i&q=%E3%83%99%E3%83%A9%E3%83%BB%E3%83%96%E3%83%A9%E3%83%83%E3%83%89%E3%83%AA&searchbox=1&key={}'

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
for i in range(1):
    # print('='*30, i, '='*30)
    url = base_url.format(i+1)
    #- seleniumで読み込み
    sleep(2)

    if i == 0:
        pass
    else:
        driver.get(url)
        sleep(4)

    #! 不要 BeautifulSoup(driver.page_source, 'lxml')で読み込むため
    # r = requests.get(url, timeout=3)
    # r.raise_for_status()

    soup = BeautifulSoup(driver.page_source, 'lxml')
    a_tags = soup.select('li.p-itemlist_item > a')

    #! 要if分削除 if文は検証を楽にするために書いてあるだけなので。ifを使う場合はそれ以降のcsvに書き出す処理以外を全てに右に一つインデントを入れる必要あり また、elseの作成が必要
    for i, a_tag in enumerate(a_tags):
        print('='*10,i,'='*10,)
        # if i < 2:
        page_url = a_tag.get('href')
        #- 毎回ここでa_tagが切り替わるたびにそのaタグのurlを読み込む
        driver.get(page_url)
        sleep(2)
        #¥ seleniumの処理 zoom画像の抜き出し
        thumbnails = driver.find_elements_by_css_selector('li.gdimage_thumb_list_item')

        #- zoomした写真をひとまとまりにする必要あり url|url|url|
        zoom_pictures = []

        #! 最初の一枚はもとから拡大写真のため写真をクリックする操作が不要
        for i, thumbnail in enumerate(thumbnails):
            if i==0:
                zoom_picture = driver.find_element_by_css_selector('div.zoomPad > img').get_attribute('src')
                sleep(0.5)
                zoom_pictures.append(zoom_picture)
            else:
                #-!!!! 要削除 検証のためbreakを入れている
                # break
                thumbnail.click()
                sleep(0.5)
                zoom_picture = driver.find_element_by_css_selector('div.zoomPad > img').get_attribute('src')
                zoom_pictures.append(zoom_picture)

        #- わかりやすいように変数名を soup から page_soupに変えた
        page_soup = BeautifulSoup(driver.page_source, 'lxml')

        #! 複数のセレクタで対象を絞り込む(区切り文字なし) 対象の2つのクラスを持つもののみ(間にスペースを入れない)を指定 strip()で空白削除 '.gdbrand.p-typo_body1_a'
        #^ 関数_1使用
        brand_name = strip_text('.gdbrand.p-typo_body1_a > a')
        item_name = strip_text('.gdname.p-typo_head3_a')

        # brand_name = page_soup.select_one('.gdbrand.p-typo_body1_a > a').text.strip()
        # item_name = page_soup.select_one('.gdname.p-typo_head3_a').text.strip()
        item_title = brand_name + ' ' + item_name
        item_url = page_url
        #! replace()で余分なコンマや文字を消し、最後に整数にした
        item_price = int(page_soup.select_one('.gdprice_main').text.replace('￥','').replace(',','').replace('税込',''))
        shipping_cost = page_soup.select_one('td:-soup-contains(全国一律)').text.strip()

        # url|url|url|url
        zoom_pictures = '|'.join(zoom_pictures)

        # gender = page_soup.select_one('tbody.gddescription_attr_body > tr:first-of-type > td').text.strip()
        gender = strip_text('tbody.gddescription_attr_body > tr:first-of-type > td')

        category_big = strip_text('th:-soup-contains(カテゴリー) + td > a:first-of-type')
        #! new
        # category_big = page_soup.select_one('th:-soup-contains(カテゴリー) + td > a:first-of-type').text.strip()
        # print('big',category_big)

        category_small = page_soup.select_one('th:-soup-contains(カテゴリー) + td > a:nth-of-type(2)').text.replace('/', ' ').strip()
        print('small',category_small)

        #- カテゴリーがaタグで２つに別れていたのを一つにまとめた
        category_whole = category_big + ' ' + category_small
        print('whole', category_whole)

        condition = strip_text('tbody.gddescription_attr_body > tr:nth-of-type(4) > td')

        # condition = page_soup.select_one('tbody.gddescription_attr_body > tr:nth-of-type(4) > td').text.strip()

        accessories = strip_text('tbody.gddescription_attr_body > tr:nth-of-type(5) > td')

        #- 文字列で要素を取得! - soup.select('li:-soup-contains("Python")')
        #! 事前に変数の用意が必要
        staff_comment = ''
        color = ''
        model = ''
        material = ''
        manufactured = ''
        remark = ''
        condition_detail = ''

        item_detail = page_soup.select_one('p.gddescription_free')
        #- アイテムの詳細がpタグ一つで全て文章で書いてある場合と、tableタグで作られている場合の2パターンがあるので分岐
        if item_detail:
            item_detail = page_soup.select_one('p.gddescription_free').text
        else:
            staff_comment = page_soup.select_one('th:-soup-contains("スタッフコメント") + td')
            staff_comment = staff_comment.text if staff_comment else None

            color = page_soup.select_one('th:-soup-contains("カラー")+ td')
            color = color.text if color else None

            model = page_soup.select_one('th:-soup-contains("型番")+ td')
            model = model.text if model else None

            material = page_soup.select_one('th:-soup-contains("素材")+ td')
            material = material.text if material else None

            manufactured = page_soup.select_one('th:-soup-contains("製造国")+ td')
            manufactured = manufactured.text if manufactured else None

            remark = page_soup.select_one('th:-soup-contains("備考")+ td')
            remark = remark.text if remark else None

            condition_detail = page_soup.select_one('th:-soup-contains("状態")+ td')
            condition_detail = condition_detail.text if condition_detail else None

        #-サイズ取得
        height_cm = ''
        width_cm = ''
        depth_cm = ''
        handle_cm = ''
        shoulder_strap_cm = ''

        height_cm = purify_size('dt:-soup-contains("高さ") + dd','dt:-soup-contains("縦") + dd')
        print('='*10,'213',height_cm)

        # if page_soup.select_one('dt:-soup-contains("高さ") + dd'):
        #   height_cm = page_soup.select_one('dt:-soup-contains("高さ") + dd')
        #   #! オンラインショップ上のサイズ表記が間違っており "約c33m" と記載されており、エラーになったため修正
        #   # height_cm = float(height_cm.text.replace('約',' ').replace('cm', '')) if height_cm else None
        #   height_cm = float(height_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if height_cm else None
        # elif page_soup.select_one('dt:-soup-contains("縦") + dd'):
        #   height_cm = page_soup.select_one('dt:-soup-contains("縦") + dd')
        #   height_cm = float(height_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if height_cm else None
        # else:
        #   pass

        width_cm = purify_size('dt:-soup-contains("幅") + dd','dt:-soup-contains("横") + dd')
        print('='*10,'227',width_cm)

        # if page_soup.select_one('dt:-soup-contains("幅") + dd'):
        #   width_cm = page_soup.select_one('dt:-soup-contains("幅") + dd')
        #   width_cm = float(width_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if width_cm else None
        # elif page_soup.select_one('dt:-soup-contains("横") + dd'):
        #   width_cm = page_soup.select_one('dt:-soup-contains("横") + dd')
        #   width_cm = float(width_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if width_cm else None
        # else:
        #   pass

        #¥  aaaa
        depth_cm = purify_size('dt:-soup-contains("マチ") + dd','no-css_selector')
        print('='*10,'240',depth_cm)

        # if page_soup.select_one('dt:-soup-contains("マチ") + dd'):
        #   depth_cm = page_soup.select_one('dt:-soup-contains("マチ") + dd')
        #   depth_cm = float(depth_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if depth_cm else None

        #¥  aaaa
        handle_cm = purify_size('dt:-soup-contains("持ち手の長さ") + dd','no-css_selector')
        print('='*10,'248',handle_cm)

        # if page_soup.select_one('dt:-soup-contains("持ち手の長さ") + dd'):
        #   handle_cm = page_soup.select_one('dt:-soup-contains("持ち手の長さ") + dd')
        #   handle_cm = float(handle_cm.text.replace('約',' ').replace('c', '').replace('m', ''))  if handle_cm else None
        # else:
        #   pass

        #! ショルダーバッグの紐の長さが "約87-" となっていることから float()できなかった
        #- in演算子と or演算子を使って条件を記載する
        if page_soup.select_one('dt:-soup-contains("ショルダー") + dd'):
            shoulder_strap_cm = page_soup.select_one('dt:-soup-contains("ショルダー") + dd')
            if '-' in shoulder_strap_cm.text or '~' in shoulder_strap_cm.text:
                shoulder_strap_cm = ""
                print('='*30)
                print('Success')
            else:
                shoulder_strap_cm = float(shoulder_strap_cm.text.replace('約',' ').replace('c', '').replace('m', '')) if shoulder_strap_cm else None
        else:
            shoulder_strap_cm = ''

        # shop_address = shop_address.text if shop_address else None
        #- else Noneの代わりに ''で入力可能!!
        width_inch = round(width_cm / 2.54, 2) if width_cm else ''
        height_inch = round(height_cm / 2.54, 2) if height_cm else ''
        depth_inch = round(depth_cm / 2.54, 2) if depth_cm else ''
        handle_inch = round(handle_cm / 2.54, 2) if handle_cm else ''
        shoulder_strap_inch = round(shoulder_strap_cm / 2.54, 2) if shoulder_strap_cm else ''

        #- 関数_3を使用
        actual_size_cm = to_actual_size(height_cm, width_cm,depth_cm,handle_cm,shoulder_strap_cm, 'cm')
        print('='*10,'247',actual_size_cm)

        actual_size_inch = to_actual_size(height_inch, width_inch,depth_inch,handle_inch,shoulder_strap_inch, 'inch')
        print('='*10,'255',actual_size_inch)

        # actual_size_cm = 'Approx size(height / width / depth / handle / shoulder-strap): ' + str(height_cm) + 'cm / ' + str(width_cm) + 'cm / ' + str(depth_cm) + 'cm / ' + str(handle_cm) + 'cm / ' + str(shoulder_strap_cm) + 'cm'

        # actual_size_inch = 'Approx size(height / width / depth / handle / shoulder-strap): ' + str(height_inch) + 'inch / ' + str(width_inch) + 'inch / ' + str(depth_inch) + 'inch / ' + str(handle_inch) + 'inch / ' + str(shoulder_strap_inch) + 'inch'

        # print('cm - inch -' *10)
        # print(actual_size_cm)
        # print(actual_size_inch)

        d_list.append({
            '*Action(SiteID=US|Country=JP|Currency=USD|Version=745|CC=UTF-8)': 'Add',
            'DL-eb-category': 'bag_m:52357 / bag_w:169291',
            '*Category': '',
            '*Title': '',
            #! NEW 20220211 最終的に*Titleにコピペするための
            #! ご操作を防ぐために別にタイトルを記載
            # 'U-title': item_title,
            'U-title': delete_brackets.delete_brackets(item_title),
            #! NEW 20220210 タイトルに付属させる用途
            'X-category':category_whole,
            'Ref-title_category_combined':'"=D2&" "&E2',
            'Ref-translation':'"=if(F2="","",googletranslate(F2,"ja","en"))',
            'URef-title-completed':'"=G2&" "&"ship from Japan"',
            'Ref-len()': '"=len(C2)',
            'URef-size_for_ConditionDescription': '"=AH2&" | "&AI2&" | "&" Model: "&AB2&" | "&"Material: "&AC2&" | "&"An item has been used previously. For more details, please check the pictures carefully and judge the condition."',
            'url': item_url,
            'costPrice + s/p': item_price + 550,
            's/p': shipping_cost,
            '+word': 'ship from Japan',
            # 'combined':'=c{num}+h{num}'.format(num = i+2),
            'PicURL':zoom_pictures,
            'ConditionID' : '3000',
            # 'C:Brand': brand_name,
            'C:Brand': delete_brackets.delete_brackets(brand_name),
            '*StartPrice' : '',
            'CustomLabel' : '',
            '*Description' : '',
            #¥ New 20220211
            #- ConditionDescription にはサイズや型番、状態が入る
            'ConditionDescription': '',
            'X-gender': gender,
            'X-condition': condition,
            'X-accessories': accessories,
            'X-item_detail': item_detail,
            'X-staff_comment': staff_comment,
            'X-color': color,
            'X-model': model,
            'Ref-material_translation': '"=if(AD2="","",googletranslate(AD2,"ja","en"))',
            'X-material': material,
            'X-manufactured': manufactured,
            'X-remark': remark,
            'X-condition_detail': condition_detail,
            'X-actual_size_inch': actual_size_inch,
            'X-actual_size_cm': actual_size_cm,
            'MinimumBestOfferPrice': '"=R2',
            # 'X-all_sizes': store_all_sizes,
        })
        # print('='*30)
        # print(d_list[-1])
        # print('='*30)


    print('============終わり===============')
    sleep(1)

    #! 約87-
    #¥ 要検証!ショルダーの長さが ''でcsv上に表示されるか確認!   https://www.trefac.jp/store/3004006854145040/c927194/

df = pd.DataFrame(d_list)
# df.to_csv('tf_testtest_bag_women_ver2_' + today + '.csv', index=None, encoding='utf-8-sig')
df.to_csv('tf_VeraBradley_bag_women_ver2_' + today + '.csv', index=None, encoding='utf-8-sig')

    # ¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥

    # shop_address = page_soup.select_one('address')
    # #! 三項演算子
    # shop_address = shop_address.text if shop_address else None
    # #! 2つのクラスを含む要素の隣の要素aタグの要素
    # shop_url = page_soup.select_one('.icon.icon-world+span > a')
    # shop_url = shop_url.get('href') if shop_url else None
    # #! 2つのクラスを含む要素の隣の要素aタグの要素
    # shop_email = page_soup.select_one('.icon.icon-mail+span > a')
    # shop_email = shop_email.text if shop_email else None
    # #! 2つのクラスを含む要素の隣の要素の中のaタグの要素
    # shop_phone = page_soup.select_one('.icon.icon-phone+span > a')
    # shop_phone = shop_phone.text if shop_phone else None
