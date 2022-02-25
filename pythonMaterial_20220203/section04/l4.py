from time import sleep

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.python.org/'
r = requests.get(url)
sleep(2)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')

d_list = []
for li in post.find_all('li'):
    post_url = li.find('a').get('href')
    post_r = requests.get(post_url)
    sleep(2)

    post_soup = BeautifulSoup(post_r.content, 'lxml')
    post_h2 = [h2.text for h2 in post_soup.find_all('h2')]

    d = {
        'title': li.find('a').text,
        'url': post_url,
        'date': li.find('time').text,
        'post_h2': post_h2
    }
    d_list.append(d)
    print(d)

df = pd.DataFrame(d_list)
print(df)

df.to_csv('python_web_posts.csv', index=None, encoding='utf-8-sig')
