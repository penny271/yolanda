#
#to 参考 csv結合: https://coffee-blue-mountain.com/python-csv-comb2/#toc3

#to 参考 時間 : https://atmarkit.itmedia.co.jp/ait/articles/2111/09/news015.html

import pandas as pd
import glob
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
print(repr(now))

d = now.strftime('%Y%m%d%H%M%S')
print(d)  # 20211104173728 秒まで

d = now.strftime('%Y%m%d%H%M')
print(d)  # 202111041737 分まで

# パスで指定したファイルの一覧をリスト形式で取得. （ここでは一階層下のtestファイル以下）
# excel_files = glob.glob('csv_folder/*.xlsx')
excel_files = glob.glob('csv_folder/csv_for_concat/*.xlsx')

#読み込むファイルのリストを表示
for excel_file in excel_files:
    print('excel_file: ', excel_file)

#csvファイルの中身を追加していくリストを用意
data_list = []

#読み込むファイルのリストを走査
for file in excel_files:
    data_list.append(pd.read_excel(file))

#リストを全て行方向に結合

# print('data_list',data_list)

df = pd.concat(data_list)
excel_title  = 'main_data_'+ d+'.xlsx'
print(excel_title)

#! bag_women.xlsxのFXの残りの部分が縦にも横にも長過ぎたためか、普通にconcatをしたら、最初の二行だけ出力されて残りが出てこなかったと思ったが、FXの行が長すぎただけで、恐らくずっと下のほうに値は存在していた。ブランド名でフィルターかけてみて今後は確認してみよう!
#- 要停止
# df_add = pd.read_excel('e_category_no/bag_women.xlsx')

#¥ pandas.errors.InvalidIndexError: Reindexing only valid with uniquely valued Index objects
#to 参考:   https://tinyurl.com/ya3uv8gk
df.reset_index(inplace=True, drop=True)

#! 一時停止 => concatがうまく行かなかった場合用
# df_complete = pd.concat([df,df_add],axis=1)

#¥ this is where the new csv file is created
# df.to_excel("csv_folder/"+excel_title,index=False)

#^ 要復活
df.to_excel("csv_folder/csv_for_concat/"+excel_title,index=False)

#! #! 一時停止 => concatがうまく行かなかった場合用
# df_complete.to_excel("csv_folder/csv_for_concat/"+excel_title,index=False)
