import re
#- 出典: https://qiita.com/wrblue_mica34/items/9253d6ba7e0baf5cc714

#正規表現
pattern=r'([+-]?[0-9]+\.?[0-9]*)'
#検索テキスト
text = "縦：約21.5cm横：約28cmマチ：約8cmショルダー全長：約99cm"

print('pattern:',pattern,'text:',text)
print('match:',re.match(pattern,text))
print('search:',re.search(pattern,text))
print('findall:',re.findall(pattern,text))

#結果
# pattern: ([+-]?[0-9]+\.?[0-9]*) text: 縦：約21.5cm横：約28cmマチ：約8cmショルダー全長：約99cm
# match: None
# search: <re.Match object; span=(3, 7), match='21.5'>
# findall: ['21.5', '28', '8', '99']

#リストに保存
lists=re.findall(pattern,text)

inch_list=[]

for list in lists:
    inch = round(float(list) / 2.54,2)
    inch = str(inch) + 'inch'
    inch_list.append(inch)

print('='*30,'inch',inch_list)
print('='*30,'inch',' / '.join(inch_list))


#! NG ========================================
# import re

# #- https://niwakomablog.com/python-number-extract/

# s = "縦：約21.5cm横：約28cmマチ：約8cmショルダー全長：約99cm"
# # result = re.findall(r"\d+", s)
# result = re.findall(r"\d+", s)
# # より正確な書き方 → re.compile(r"\d+").findall(s)
# print(result)


# #! NG 実行結果 小数点を認識できない
# # ['21', '5', '28', '8', '99']
