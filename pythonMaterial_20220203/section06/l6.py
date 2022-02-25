from bs4 import BeautifulSoup

#! ターミナルで以下のエラーメッセージが出た場合_20220204
#! SyntaxError: Non-ASCII character vscode内ターミナルを再起動する!=> env環境で開き直す

html = """
<body>
  <h1>タイトル</h1>
  <h2>演習内容</h2>
  <ol id="step1" class="study-list">
    <li>Python基礎</li>
    <li id="target">HTML基礎</li>
    <li>JS基礎</li>
    <li>Pythonライブラリの基礎</li>
  </ol>
</body>
"""

soup = BeautifulSoup(html, 'lxml')

# print(soup.find(id='step2').find_all('li'))
#- cssセレクタで書く場合 cssを書くように記載する
# print(soup.select('#step2 li'))
#! 空白 #step2中の全てのspanを取得
# print(soup.select('#step2 span'))
#! > #step2 直下のspanを取得
# print(soup.select('#step2 > span'))
# print(soup.select('#step2 > li > span'))

#- 6-5. CSSセレクタで何番目の要素か指定する
# print(soup.select_one('li:first-of-type'))
# print(soup.select_one('li:last-of-type'))
# print(soup.select_one('li:nth-of-type(2)'))

#- 6-6 id targetを除くliタグを全て取得 否定疑似クラス「:not」
print(soup.select('li:not(#target)'))
