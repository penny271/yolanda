#
#^ 参考 - キノコード:https://www.youtube.com/watch?v=4ZCsUYVLuIM
#^ 参考 - キノコード:https://kino-code.com/webscraping04/

#! 使用スプレッドシート1:https://docs.google.com/spreadsheets/d/14dIr0oJviWG0J55fCmOHMxQlxr4utPTT/edit#gid=1272147749
#! 使用スプレッドシート2(NG_1_to_ssh.py使用後作成excelファイルより):https://docs.google.com/spreadsheets/d/1dCLITBsc35tq_e23KPh_rNLsKjrxZ3Ie/edit#gid=577585531
#日付: 2022/02/22


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

a2=['https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/9.jpg']

a3=['https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233921/01/39780/9.jpg']

a4=['https://cdn2.2ndstreet.jp/img/pc/goods/233908/01/89960/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233908/01/89960/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233908/01/89960/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233908/01/89960/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233908/01/89960/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233908/01/89960/6.jpg']

a5=['https://cdn2.2ndstreet.jp/img/pc/goods/232814/06/49643/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232814/06/49643/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232814/06/49643/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232814/06/49643/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232814/06/49643/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232814/06/49643/6.jpg']

a6=['https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/16995/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/16995/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/16995/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/16995/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/16995/5.jpg']

a7=['https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/21183/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/21183/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/21183/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/21183/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/21183/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/21183/6.jpg']

a8=['https://cdn2.2ndstreet.jp/img/pc/goods/234179/00/22796/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234179/00/22796/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234179/00/22796/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234179/00/22796/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234179/00/22796/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234179/00/22796/6.jpg']

a9=['https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/82868/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/82868/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/82868/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/82868/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/82868/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/82868/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/82868/7.jpg']

a10=['https://cdn2.2ndstreet.jp/img/pc/goods/234045/00/34742/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234045/00/34742/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234045/00/34742/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234045/00/34742/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234045/00/34742/5.jpg']

a11=['https://cdn2.2ndstreet.jp/img/pc/goods/233995/01/02709/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233995/01/02709/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233995/01/02709/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233995/01/02709/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233995/01/02709/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233995/01/02709/6.jpg']

a12=['https://cdn2.2ndstreet.jp/img/pc/goods/233414/01/63942/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233414/01/63942/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233414/01/63942/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233414/01/63942/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233414/01/63942/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233414/01/63942/6.jpg']

a13=['https://cdn2.2ndstreet.jp/img/pc/goods/234034/00/75572/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234034/00/75572/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234034/00/75572/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234034/00/75572/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234034/00/75572/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234034/00/75572/6.jpg']

a14=['https://cdn2.2ndstreet.jp/img/pc/goods/232856/07/24487/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232856/07/24487/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232856/07/24487/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232856/07/24487/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232856/07/24487/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232856/07/24487/6.jpg']

a15=['https://cdn2.2ndstreet.jp/img/pc/goods/232000/07/36111/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232000/07/36111/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232000/07/36111/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232000/07/36111/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232000/07/36111/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232000/07/36111/6.jpg']

a16=['https://cdn2.2ndstreet.jp/img/pc/goods/232057/06/18510/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232057/06/18510/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232057/06/18510/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232057/06/18510/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232057/06/18510/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232057/06/18510/6.jpg']

a17=['https://cdn2.2ndstreet.jp/img/pc/goods/233375/04/37207/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233375/04/37207/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233375/04/37207/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233375/04/37207/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233375/04/37207/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233375/04/37207/6.jpg']

a18=['https://cdn2.2ndstreet.jp/img/pc/goods/232926/03/63044/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232926/03/63044/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232926/03/63044/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232926/03/63044/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232926/03/63044/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232926/03/63044/6.jpg']

a19=['https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/72220/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/72220/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/72220/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/72220/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/72220/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/72220/6.jpg']

a20=['https://cdn2.2ndstreet.jp/img/pc/goods/233283/03/14827/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233283/03/14827/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233283/03/14827/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233283/03/14827/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233283/03/14827/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233283/03/14827/6.jpg']

a21=['https://cdn2.2ndstreet.jp/img/pc/goods/233864/03/22366/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233864/03/22366/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233864/03/22366/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233864/03/22366/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233864/03/22366/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233864/03/22366/6.jpg']

a22=['https://cdn2.2ndstreet.jp/img/pc/goods/232010/04/50092/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232010/04/50092/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232010/04/50092/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232010/04/50092/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232010/04/50092/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232010/04/50092/6.jpg']

a23=['https://cdn2.2ndstreet.jp/img/pc/goods/234032/00/78265/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234032/00/78265/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234032/00/78265/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234032/00/78265/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234032/00/78265/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234032/00/78265/6.jpg']

a24=['https://cdn2.2ndstreet.jp/img/pc/goods/234124/00/60699/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234124/00/60699/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234124/00/60699/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234124/00/60699/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234124/00/60699/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234124/00/60699/6.jpg']

a25=['https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/29323/9.jpg']

a26=['https://cdn2.2ndstreet.jp/img/pc/goods/231916/05/52402/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231916/05/52402/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231916/05/52402/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231916/05/52402/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231916/05/52402/5.jpg']

a27=['https://cdn2.2ndstreet.jp/img/pc/goods/233391/03/75417/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233391/03/75417/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233391/03/75417/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233391/03/75417/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233391/03/75417/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233391/03/75417/6.jpg']

a28=['https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233763/01/87947/9.jpg']

a29=['https://cdn2.2ndstreet.jp/img/pc/goods/233654/02/02009/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233654/02/02009/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233654/02/02009/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233654/02/02009/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233654/02/02009/5.jpg']

a30=['https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233277/04/87735/8.jpg']

a31=['https://cdn2.2ndstreet.jp/img/pc/goods/233514/03/57805/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233514/03/57805/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233514/03/57805/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233514/03/57805/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233514/03/57805/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233514/03/57805/6.jpg']

a32=['https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234130/02/23859/8.jpg']

a33=['https://cdn2.2ndstreet.jp/img/pc/goods/231861/05/21371/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231861/05/21371/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231861/05/21371/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231861/05/21371/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231861/05/21371/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231861/05/21371/6.jpg']

a34=['https://cdn2.2ndstreet.jp/img/pc/goods/233639/01/97739/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233639/01/97739/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233639/01/97739/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233639/01/97739/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233639/01/97739/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233639/01/97739/6.jpg']

a35=['https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/47999/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/47999/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/47999/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/47999/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/47999/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/47999/6.jpg']

a36=['https://cdn2.2ndstreet.jp/img/pc/goods/234208/00/35502/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234208/00/35502/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234208/00/35502/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234208/00/35502/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234208/00/35502/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234208/00/35502/6.jpg']

a37=['https://cdn2.2ndstreet.jp/img/pc/goods/234070/00/72845/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234070/00/72845/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234070/00/72845/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234070/00/72845/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234070/00/72845/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234070/00/72845/6.jpg']

a38=['https://cdn2.2ndstreet.jp/img/pc/goods/232987/02/39036/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232987/02/39036/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232987/02/39036/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232987/02/39036/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232987/02/39036/5.jpg']

a39=['https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234189/00/44117/8.jpg']

a40=['https://cdn2.2ndstreet.jp/img/pc/goods/233519/06/88799/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233519/06/88799/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233519/06/88799/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233519/06/88799/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233519/06/88799/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233519/06/88799/6.jpg']

a41=['https://cdn2.2ndstreet.jp/img/pc/goods/231955/07/10726/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231955/07/10726/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231955/07/10726/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231955/07/10726/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231955/07/10726/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231955/07/10726/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231955/07/10726/7.jpg']

a42=['https://cdn2.2ndstreet.jp/img/pc/goods/231986/16/34308/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231986/16/34308/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231986/16/34308/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231986/16/34308/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231986/16/34308/5.jpg']

a43=['https://cdn2.2ndstreet.jp/img/pc/goods/232489/03/40618/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232489/03/40618/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232489/03/40618/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232489/03/40618/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232489/03/40618/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232489/03/40618/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232489/03/40618/7.jpg']

a44=['https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/87841/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/87841/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/87841/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/87841/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/87841/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/87841/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234159/00/87841/7.jpg']

a45=['https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233006/05/65910/8.jpg']

a46=['https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/37276/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/37276/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/37276/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/37276/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/37276/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/37276/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234091/00/37276/7.jpg']

a47=['https://cdn2.2ndstreet.jp/img/pc/goods/233670/02/68616/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233670/02/68616/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233670/02/68616/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233670/02/68616/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233670/02/68616/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233670/02/68616/6.jpg']

a48=['https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233483/01/86152/9.jpg']

a49=['https://cdn2.2ndstreet.jp/img/pc/goods/232046/06/70178/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232046/06/70178/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232046/06/70178/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232046/06/70178/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232046/06/70178/5.jpg']

a50=['https://cdn2.2ndstreet.jp/img/pc/goods/231910/02/66581/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231910/02/66581/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231910/02/66581/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231910/02/66581/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231910/02/66581/5.jpg']

a51=['https://cdn2.2ndstreet.jp/img/pc/goods/233731/03/02325/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233731/03/02325/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233731/03/02325/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233731/03/02325/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233731/03/02325/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233731/03/02325/6.jpg']

a52=['https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/09332/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/09332/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/09332/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/09332/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/09332/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233410/04/09332/6.jpg']

a53=['https://cdn2.2ndstreet.jp/img/pc/goods/231998/08/78454/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231998/08/78454/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231998/08/78454/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231998/08/78454/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231998/08/78454/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231998/08/78454/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231998/08/78454/7.jpg']

a54=['https://cdn2.2ndstreet.jp/img/pc/goods/233631/02/02925/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233631/02/02925/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233631/02/02925/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233631/02/02925/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233631/02/02925/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233631/02/02925/6.jpg']

a55=['https://cdn2.2ndstreet.jp/img/pc/goods/233482/05/89185/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233482/05/89185/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233482/05/89185/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233482/05/89185/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233482/05/89185/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233482/05/89185/6.jpg']

images_list = [
a2,
a3,
a4,
a5,
a6,
a7,
a8,
a9,
a10,
a11,
a12,
a13,
a14,
a15,
a16,
a17,
a18,
a19,
a20,
a21,
a22,
a23,
a24,
a25,
a26,
a27,
a28,
a29,
a30,
a31,
a32,
a33,
a34,
a35,
a36,
a37,
a38,
a39,
a40,
a41,
a42,
a43,
a44,
a45,
a46,
a47,
a48,
a49,
a50,
a51,
a52,
a53,
a54,
a55,
]



# pics_set=[['https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/5.jpg']]


# for abc in pics_set:
#     print('abc loop: ',abc)
    # pics_set.append(abc)
#結果:
#abc loop:  ['https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/5.jpg']


r = requests.get('https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/1.jpg', headers = headers, timeout=3)

print('=============サクセス===============')

pics_set=[]

for loop in images_list:
    # print('loop: ',loop)
    pics_set.append(loop)

#! 結果
# loop:  (['https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232012/03/19454/9.jpg'],)

# print('images_list', images_list)

import os

# os.mkdir('./images/abc') #! 1回限りで良い

for y, image_data in enumerate(pics_set):
    print('loop y Start ===',y)
    # y+=1
    #!ここから
    for z, pic_data in enumerate(image_data):
        # print('pic_data',z,pic_data)
        r = requests.get(pic_data, headers = headers, timeout=3)
        sleep(1)
        # print('yyyyyyyy:',y,'---','zzzzzzzz:',z)
        # image_file = open(f'./images/2nd_20220221/{str(i)}'/str(i+1), 'wb')
        # image_file = open(f'./images/2nd_20220221/{str(i+2)}' +'-'+ str(y+1)+'.png', 'wb')
        image_file = open(f'./abc/{str(y+2)}' +'-'+ str(z+1)+'.png', 'wb')
        image_file.write(r.content)
        image_file.close()
    print('loop y END ===',y,'loop y END ===')

print("=End=")

#- for test
# image_data = a35[-1]
# print(a35[-1])
# r = requests.get(image_data)
# sleep(1)
# image_file = open('./images/2nd_20220221/' + str(1) +'.png', 'wb')
# image_file.write(r.content)
# image_file.close()
