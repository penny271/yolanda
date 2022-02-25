from bs4 import BeautifulSoup
import requests

url = 'https://www.anaconda.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
print(soup.h1.text)

# r.text r.content
# r.content ==> r.text
#* 文字化けしない r.content を推奨
