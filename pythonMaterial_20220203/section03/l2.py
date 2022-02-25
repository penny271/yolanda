from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
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
</html>
"""

# soup = BeautifulSoup(html, 'html.parser')
#* html解析は、lxmlを推奨
soup = BeautifulSoup(html, 'lxml')
print(soup.h1.text)
