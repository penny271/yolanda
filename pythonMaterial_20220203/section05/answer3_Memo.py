# 何度もリクエストを送る場合に必要-サーバーに不可を与えないようにするため
from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

#- for inループ文で{}に数字が入るようにしたい 動的にpage = {}の部分を変化させる
#^ => ページ遷移できる!
base_url = 'https://doda.jp/DodaFront/View/JobSearchList.action?pr=13&pic=1&ds=0&oc=0104M&so=50&k=%E5%96%B6%E6%A5%AD&kwc=1&pf=0&tp=1&page={}&usrclk_searchList=PC-logoutJobSearchList_searchResultHeaderArea_pagination_prev'
# 'https://doda.jp/DodaFront/View/JobSearchList.action?pr=13&pic=1&ds=0&oc=0104M&so=50&k=%E5%96%B6%E6%A5%AD&kwc=1&pf=0&tp=1&page=1&usrclk_searchList=PC-logoutJobSearchList_searchResultHeaderArea_pagination_prev'
# 'https://doda.jp/DodaFront/View/JobSearchList.action?pr=13&pic=1&ds=0&oc=0104M&so=50&k=%E5%96%B6%E6%A5%AD&kwc=1&pf=0&tp=1&page=2&usrclk_searchList=PC-logoutJobSearchList_searchResultHeaderArea_pagination_prev'
# 'https://doda.jp/DodaFront/View/JobSearchList.action?pr=13&pic=1&ds=0&oc=0104M&so=50&k=%E5%96%B6%E6%A5%AD&kwc=1&pf=0&tp=1&page=3&usrclk_searchList=PC-logoutJobSearchList_searchResultHeaderArea_pagination_prev'

d_list = []
#! range()関数 - 第2引数は変数に代入されない
for i in range(1,3):
  url = base_url.format(i)

  # 折返しは、option + z
  # url = 'https://doda.jp/DodaFront/View/JobSearchList.action?k=%E5%96%B6%E6%A5%AD&kwc=1&pr=13&oc=0104M&ss=1&pic=1&ds=0&tp=1&bf=1&mpsc_sid=10&oldestDayWdtno=0&leftPanelType=1&usrclk_searchList=PC-logoutJobSearchList_searchConditionArea_jobModal_kyujinSearchButton-ocM-locPrefecture-kwdInclude'
  #! for文の中でrequests文がある場合、requests文の前にsleep()を入れる!

  sleep(3)

  #- アクセスするwebページがメンテンス中だと永遠とリクエストを送ってしまうのでtimeoutを設定する
  r = requests.get(url, timeout=3)
  #- webページのurlが間違っていたらエラーをすぐに返す
  r.raise_for_status()

  soup = BeautifulSoup(r.content,'lxml')

  companies = soup.find_all('div', class_='layoutList02')
  # 50個分配列の中身が入っていれば問題ない
  # print(len(companies))

  #! ここに d_list があると、2ページ目取得のループ時にd_list = []は空になってしまう
  #! => 一番外側のループの外に d_list = [] を定義する必要あり
  # d_list = []
  for i, company in enumerate(companies):
    print('='*30, i, '='*30)
    company_name = company.find('span', class_="company").text
    #- 詳細ページのurlを取得 - get('href')でurlを持っていきている
    page_url = company.find('a', class_='btnJob03').get('href')
    #^ タブの切替 一部分しか変化しないため、page_urlを取得後、replaceで目的のタブのurlに入替える
    # 'https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3005530779/-tab__pr/-fm__jobdetail/'
    # 'https://doda.jp/DodaFront/View/JobSearchDetail/j_jid__3005530779/-tab__jd/-fm__jobdetail/'
    page_url = page_url.replace('-tab__pr', '-tab__jd')

    #! for文の中でrequests.get()を使っているのでsleepを設定する - 3秒休止してからrequestsを送る
    sleep(3)

    #- アクセスするwebページがメンテンス中だと永遠とリクエストを送ってしまうのでtimeoutを設定する
    page_r = requests.get(page_url,timeout=3)
    #- webページのurlが間違っていたらエラーをすぐに返す
    page_r.raise_for_status()

    page_soup = BeautifulSoup(page_r.content,'lxml')

    table = page_soup.find('table', id = 'company_profile_table')
    #! AttributeError: 'NoneType' object has no attribute 'get'
    #! aタグがない場合は、table.find('a')で取得できないので上記のエラーが発生する
    # company_url = table.find('a').get('href')
    #- if文でエラーを回避する!
    company_url = table.find('a')
    if company_url:
      company_url = company_url.get('href')
      #¥ urlが存在しなかった場合は、company_url = Noneになる

    # csvに書き出す土台となる列名とそれに対応する行の文字列
    d_list.append({
      'company_name' : company_name,
      'compnay_url' : company_url
  })

  # 最後のインデックスだけprintする 大本のindexは50社全てはいっており、printごとに1,2,3,4,5,と増えていってしまう
  # print(d_list[-1])

df = pd.DataFrame(d_list)
df.to_csv('company_list.csv', index= None, encoding='utf-8-sig')
df.to_csv('company_list_v2.csv', index= None, encoding='utf-8-sig')



  # print(company_name)
  # print(page_url)
