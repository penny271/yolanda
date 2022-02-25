from bs4 import BeautifulSoup

html1 = """
    <h1>タイトル</h1>
    <ol id="step1", class="study-list">
        <li>Python基礎</li>
        <li>HTML基礎</li>
    </ol>
"""

html2 = """
    <h1>タイトル</h1>
    <ol id="step1", class="study-list"><li>Python基礎</li><li>HTML基礎</li></ol>
"""


soup1 = BeautifulSoup(html1, 'lxml')
print(soup1.find('ol').contents)

soup2 = BeautifulSoup(html2, 'lxml')
print(soup2.find('ol').contents)
