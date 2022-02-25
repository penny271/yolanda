from bs4 import BeautifulSoup

html = """
<body>
    <h1>タイトル</h1>
    <h2>演習内容</h2>
    <ol id="step1", class="study-list">
        <li>Python基礎</li>
        <li>HTML基礎</li>
    </ol>
    <ol id="step2" class="study-list">
        <li>JS基礎</li>
        <li>Pythonライブラリの基礎</li>
    </ol>
</body>
"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(['h1','h2']))
#! NG!! cssセレクタの場合一組のアポストロフィーで囲む
# print(soup.select('h1', 'h2'))
print(soup.select('h1, h2'))
