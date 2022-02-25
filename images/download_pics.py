#
#^ 参考 - キノコード:https://www.youtube.com/watch?v=4ZCsUYVLuIM
#^ 参考 - キノコード:https://kino-code.com/webscraping04/


from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import random

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36']

# headers = {
#     'User-Agent' : ua
# }

ua = user_agent[random.randrange(0, len(user_agent), 1)]
# print(ua)


headers = {
    'User-Agent' : ua
}

#^  参考 - キノコード:https://www.youtube.com/watch?v=4ZCsUYVLuIM
#^ 参考 - キノコード:https://kino-code.com/webscraping04/

pics_set=[['https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/5.jpg']]

import os

# os.mkdir('./images/abc') #! 1回限りで良い

for i, image_datas in enumerate(pics_set):
    for j, image_data in enumerate(image_datas):
        r = requests.get(image_data, headers = headers, timeout=3)
        sleep(1)
        #! NGディレクトリが違う!!  image_file = open(f'./images/2nd_20220221/{str(i)}'/str(i+1), 'wb')
        #- downloaded file name starts with 2 not 1
        image_file = open(f'./2nd_20220221/{str(i+2)}' +'-'+ str(j+1)+'.png', 'wb') #- actual-use
        # image_file = open(f'./abc/{str(i+2)}' +'-'+ str(j+1)+'.png', 'wb') #- test-use only
        image_file.write(r.content)
        image_file.close()
print('='*20, 'End', '='*20)

#- for test
# image_data = a35[-1]
# print(a35[-1])
# r = requests.get(image_data)
# sleep(1)
# image_file = open('./images/2nd_20220221/' + str(1) +'.png', 'wb')
# image_file.write(r.content)
# image_file.close()
