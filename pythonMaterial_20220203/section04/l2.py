import pandas as pd

#* 列名の入れ方
df = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Peach'],
    'Price': [100,120,150]
})
print(df)

#* リスト内に辞書を格納することも可能
#- スクレイピングの結果を保存するにはこの方法を使う
df2 = pd.DataFrame([
    {'Fruit': 'Apple', 'Price': 100},
    {'Fruit': 'Banana', 'Price': 120},
    {'Fruit': 'Peach', 'Price': 150},
])

print(df2)
