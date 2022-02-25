import re
import os
from glob import glob

from bs4 import BeautifulSoup
import pandas as pd


def parse(soup, f_name):
    if 'ナンバーズ3' in f_name:
        tables = soup.select('table.typeTK')

        for table in tables:
            time = table.select_one('thead > tr > th:last-of-type').text
            day = table.select_one('tbody > tr:first-of-type > td').text
            number = table.select_one('tbody > tr:nth-of-type(2) > td').text

            yield {
                'time': time,
                'day': day,
                'number': number
            }
    else:
        tr_tags = soup.select(
            'div.spTableScroll > table.typeTK:first-of-type > tbody > tr')

        for tr_tag in tr_tags:
            time = tr_tag.select_one('th.bgf7f7f7').text
            day = tr_tag.select_one('td:first-of-type').text
            number = tr_tag.select_one('td:nth-of-type(2)').text

            yield {
                'time': time,
                'day': day,
                'number': number
            }


html_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'html', '*')

d_list = []
for path in glob(html_path):
    with open(path, 'r') as f:
        html = f.read()

    f_name = os.path.basename(path)
    soup = BeautifulSoup(html, 'lxml')

    parsed_dicts = parse(soup, f_name)
    d_list += list(parsed_dicts)

    print(len(d_list))


print('='*50)
df = pd.DataFrame(d_list)


df['no'] = df.time.map(lambda s: re.sub('第|回', '', s)).astype(int)
df = df.sort_values('no').set_index('no')
print(df)
df.to_csv('numbers.csv', index=None, encoding='utf-8-sig')