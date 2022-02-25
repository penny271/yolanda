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

a1=['https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/9.jpg']
a2=['https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/5.jpg']
a3=['https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/5.jpg']
a4=['https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/6.jpg']
a5=['https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/6.jpg']
a6=['https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/6.jpg']
a7=['https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/6.jpg']
a8=['https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/6.jpg']
a9=['https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/8.jpg']
a10=['https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/6.jpg']
a11=['https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/5.jpg']
a12=['https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/6.jpg']
a13=['https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/6.jpg']
a14=['https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/6.jpg']
a15=['https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/5.jpg']
a16=['https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/7.jpg']
a17=['https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/6.jpg']
a18=['https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/7.jpg']
a19=['https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/5.jpg']
a20=['https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/6.jpg']
a21=['https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/9.jpg']
a22=['https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/9.jpg']
a23=['https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/6.jpg']
a24=['https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/9.jpg']
a25=['https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/6.jpg']
a26=['https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/6.jpg']
a27=['https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/7.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/8.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/9.jpg']
a28=['https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/6.jpg']
a29=['https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/6.jpg']
a30=['https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/6.jpg']
a31=['https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/6.jpg']
a32=['https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/7.jpg']
a33=['https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/5.jpg']
a34=['https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/6.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/7.jpg']
a35=['https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/6.jpg']



pics_set=[['https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/5.jpg']]




# images_list = [
#     a1,
# a2,
# a3,
# a4,
# a5,
# a6,
# a7,
# a8,
# a9,
# a10,
# a11,
# a12,
# a13,
# a14,
# a15,
# a16,
# a17,
# a18,
# a19,
# a20,
# a21,
# a22,
# a23,
# a24,
# a25,
# a26,
# a27,
# a28,
# a29,
# a30,
# a31,
# a32,
# a33,
# a34,
# a35,
# ]

pics_set=[['https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233817/02/49010/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231857/06/02370/5.jpg'], ['https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/231843/06/50640/5.jpg']]

import os

# os.mkdir('./images/abc') #! 1回限りで良い

# for i, image_datas in enumerate(pics_set):
#     for y, image_data in enumerate(image_datas):
#         r = requests.get(image_data, headers = headers, timeout=3)
#         sleep(1)
#         # image_file = open(f'./images/2nd_20220221/{str(i)}'/str(i+1), 'wb')
#         # image_file = open(f'./images/2nd_20220221/{str(i+2)}' +'-'+ str(y+1)+'.png', 'wb')
#         image_file = open(f'./images/abc/{str(i+2)}' +'-'+ str(y+1)+'.png', 'wb')
#         image_file.write(r.content)
#         image_file.close()

for i, image_datas in enumerate(pics_set):
    for y, image_data in enumerate(image_datas):
        r = requests.get(image_data, headers = headers, timeout=3)
        sleep(1)
        # image_file = open(f'./images/2nd_20220221/{str(i)}'/str(i+1), 'wb')
        image_file = open(f'./images/2nd_20220221/{str(i+2)}' +'-'+ str(y+1)+'.png', 'wb')
        # image_file = open(f'./images/abc/{str(i+2)}' +'-'+ str(y+1)+'.png', 'wb')
        image_file = open(f'./abc/{str(y+1)}.png', 'wb')
        image_file.write(r.content)
        image_file.close()

#- for test
# image_data = a35[-1]
# print(a35[-1])
# r = requests.get(image_data)
# sleep(1)
# image_file = open('./images/2nd_20220221/' + str(1) +'.png', 'wb')
# image_file.write(r.content)
# image_file.close()
