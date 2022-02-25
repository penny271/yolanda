import os
from time import sleep

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(
    executable_path='',
    options=options
)
driver.implicitly_wait(10)

top_page_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/numbers/backnumber/index.html'

driver.get(top_page_url)
sleep(3)

latest_links = driver.find_elements_by_css_selector(
    '.js-backnumber-temp-a > td:first-of-type > a')

backnumber_links = driver.find_elements_by_css_selector(
    '.js-backnumber-temp-b > td > a')

urls = [e.get_attribute('href') for e in latest_links+backnumber_links]

print(len(urls))

dir_path = os.path.dirname(os.path.abspath(__file__))
for i, url in enumerate(urls):
    print('='*30, i, '='*30)
    print(url)
    driver.get(url)
    sleep(5)

    html = driver.page_source

    p = os.path.join(dir_path, 'html', f'{driver.title}.html')
    with open(p, 'w') as f:
        f.write(html)

sleep(3)
driver.quit()