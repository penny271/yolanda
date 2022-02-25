#! seleniumなどモジュールがインストールされていないというエラーが出たら、vscodeをanacondaのenv環境で開けていないため、ANACONDA.NAVIGATORを起動させてから、ターミナルを起動する!! _2022/02/07

#- ライブラリのインポート
import os
#! ファイル一覧の取得のためのライブラリ
from glob import glob
from weakref import KeyedRef

from bs4 import BeautifulSoup
import pandas as pd

#¥ 使い回すための関数を作成
def parse(soup, f_name):
  d_list = []
  # 直近一年分の情報取得
  if 'ナンバーズ3' in f_name:
    tables = soup.select('table.typeTK')
    for table in tables:
      time = table.select_one('thead > tr > th:last-of-type').text
      day = table.select_one('tbody > tr:first-of-type > td').text
      number = table.select_one('tbody > tr:nth-of-type(2) > td').text

      d = {
        'time':time,
        'day': day,
        'number': number
      }
      d_list.append(d)

  # 直近一年分の情報取得
  else:
    trs = soup.select('table.typeTK > tbody > tr')

    for tr in trs:
      time = tr.select_one('th').text
      day = tr.select_one('td:first-of-type').text
      number = tr.select_one('tr:nth-of-type(2)').text

      d = {
        'time':time,
        'day': day,
        'number': number
      }
      d_list.append(d)
  return d_list


#- htmlを読み込むためのPATHの設定
dir_name = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(dir_name, 'html', '*') # htmlフォルダまでのパスを取得し、中にある全てのファイルを選択
print(html_path)

# print(glob(html_path))
# print(glob(html_path)[0])
# print(len(glob(html_path)))

#- for loopでHTMLの読み込み
for path in glob(html_path):
  with open(path, 'r') as f:
    html = f.read()


  ##- BeautifulSoupでHTMLを解析してあげて、
  f_name = os.path.basename(path)
  print(f_name)
  break

  soup = BeautifulSoup(html, 'lxml')
  # xxx = parse(soup, key)






##- 必要な部分だけを取得して変数d_listに格納する


#- dataframeの作成


# to_csvを使う
