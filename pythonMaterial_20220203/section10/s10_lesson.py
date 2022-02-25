#  汎用的なファイル名の設定

import os
from posixpath import dirname
from tkinter.tix import DirList

#- コードを実行するPCのファイルのフルパスを取得
# /Users/aokihirotaka/Desktop/python_lesson_20220203/s10_lesson.py
print(os.path.abspath(__file__))

#- 取得したファイルのフルパスのフォルダーを取得
# /Users/aokihirotaka/Desktop/python_lesson_20220203
print(os.path.dirname(os.path.abspath(__file__)))
dir_name = os.path.dirname(os.path.abspath(__file__))

print(os.path.join(dir_name, 'html', 'index.html'))

def parse():
  d_list = []
  for i in range(10):
    d = {
      'key1': i,
      'key2': i*2
    }
    d_list.append(d)
  return d_list

r = parse()
print('関数', r)

#- yieldを使う場合:
def parse2():
  for i in range(10):
    yield {
      'key1': i,
      'key2': i*2
    }

r2 = parse2()
print('関数2', r2)
print('関数2', list(r2))

#- リスト関数
d_list = []
lists = ['abc','apple', 'pine', 'egg']
#! globでhtmlファイルを全て取得
for each in lists:
  # with open(path, 'r') as f:
  #   html = f.read()


  ##- BeautifulSoupでHTMLを解析してあげて、
  # f_name = os.path.basename(path)
  # print(f_name)

  # soup = BeautifulSoup(html, 'lxml')

  ##- 必要な部分だけを取得して変数d_listに格納する
  # parsed_dicts = parse(soup, f_name)
  # list関数によるリストの作成
  # d_list += list(each)
  d_list += list(lists)

  print((d_list))
