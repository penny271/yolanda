from bs4 import BeautifulSoup

html = """
<body>
  <h1>タイトル</h1>
  <h2>演習内容</h2>
  <ol id="step1" class="study-list">
    <li>Python基礎</li>
    <li>HTML基礎</li>
  </ol>
  <ol id="step1" class="study-list">
    <li>JS基礎</li>
    <li>Pythonライブラリの基礎</li>
  </ol>
</body>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.find('h2').text)
# print(soup.find('ol', class_='study-list').text)
# #- cssセレクタで最初の要素1つを選択する方法
# print(soup.select_one('h2').text)
# print(soup.select_one('#step1').text)
# print(soup.select_one('.study-list').text)

#- cssセレクタで指定の全ての要素1つを選択する方法
print(soup.select('.study-list'))

print(soup.select('.study-list')==(soup.find_all(class_='study-list')))
#¥ cssセレクタを使ったほうがコードを簡潔に書ける
