from bs4 import BeautifulSoup

#! ターミナルで以下のエラーメッセージが出た場合_20220204
#! SyntaxError: Non-ASCII character vscode内ターミナルを再起動する!=> env環境で開き直す

html = """
<body>
  <h1>タイトル</h1>
  <h2>演習内容</h2>
  <ol id="step1" , class="study-list">
    <li class="python-list">Python基礎</li>
    <li class="html-list" value="3">HTML基礎</li>
    <li class="js-list">JS基礎</li>
    <li class="python-list2" value="10">Pythonライブラリの基礎</li>
    <li class="html-js-list">フロントエンド基礎</li>
  </ol>
</body>
"""

soup = BeautifulSoup(html, 'lxml')

#- 6-5. CSSセレクタで何番目の要素か指定する
# print(soup.select_one('li:first-of-type'))
# print(soup.select_one('li:last-of-type'))
# print(soup.select_one('li:nth-of-type(2)'))

#- 6-6 id targetを除くliタグを全て取得 否定疑似クラス「:not」
# print(soup.select('li:not(#target)'))

#- 6-7 特定の属性をもつ値を取得
# print(soup.select('li[value]'))
# print(soup.select('li[value = "10"]'))
# ↓ 非推奨 ↓
# print(soup.find_all('li',attrs={'value':10}))

#^ 特定のクラス名で部分一致したクラスの要素を取得
# print(soup.select('li[class*=js]'))
#^ 特定のクラス名で頭の部分が部分一致したクラスの要素を取得
# print(soup.select('li[class^=js]'))
#^ 特定のクラス名で最後の部分が部分一致したクラスの要素を取得
# print(soup.select('li[class$="2"]'))

#- 6-8. テキストを元に要素を指定する
#! 非推奨
# print(soup.select('li:contains("Python")'))
print(soup.select('li:-soup-contains("Python")'))
