from tkinter.tix import DirList
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
print(repr(now))

date = now.strftime('%Y%m%d%H%M%S')
print(date)  #example 20211104173728 秒まで

date = now.strftime('%Y%m%d%H%M')
print(date)  #example 202111041737 分まで

a='https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/7.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/8.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232560/04/62538/9.jpg'
b='https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233888/00/94276/5.jpg'
c='https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24024/5.jpg'
d='https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234071/00/75454/6.jpg'
e='https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233822/03/74488/6.jpg'
f='https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233278/18/24031/6.jpg'
g='https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231978/06/33277/6.jpg'
h='https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232072/09/35368/6.jpg'
i='https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/7.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233317/03/07098/8.jpg'
j='https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234120/01/43462/6.jpg'
k='https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234078/00/67526/5.jpg'
l='https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232937/08/42378/6.jpg'
m='https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233979/01/50786/6.jpg'
n='https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233436/01/46398/6.jpg'
o='https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/01/85479/5.jpg'
p='https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/27088/7.jpg'
q='https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232070/05/85385/6.jpg'
r='https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/231908/08/93210/7.jpg'
s='https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233750/02/45579/5.jpg'
t='https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233438/03/97367/6.jpg'
u='https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/7.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/8.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232682/10/50702/9.jpg'
v='https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/7.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/8.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233913/01/50070/9.jpg'
w='https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234172/01/04899/6.jpg'
x='https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/7.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/8.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232494/05/31249/9.jpg'
y='https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232478/04/75307/6.jpg'
aa='https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/80984/6.jpg'
bb='https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/7.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/8.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232927/04/87082/9.jpg'
cc='https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/234047/01/04203/6.jpg'
dd='https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233783/01/42968/6.jpg'
ee='https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233468/04/67418/6.jpg'
ff='https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232051/06/98107/6.jpg'
gg='https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/230003/23/29956/7.jpg'
hh='https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233833/02/02275/5.jpg'
ii='https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/6.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/232840/06/55353/7.jpg'
jj='https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/6.jpg'

# jjj = '|'.join(jj)
jjj = jj.split('|')
print(jjj)
# ['https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/6.jpg']

list = [a,b,c,d,
e,f,g,h,
i,j,
k,
l,
m,
n,
o,
p,
q,
r,
s,
t,
u,
v,
w,
x,
y,
aa,
bb,
cc,
dd,
ee,
ff,
gg,
hh,
ii,
jj,]

d_list = []

for i,el in enumerate(list):
    abc =el.split('|')
    d_list.append({
        'picUrl':abc
    })

df = pd.DataFrame(d_list)
print(d_list[-1])
# {'picUrl': ['https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/1.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/2.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/3.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/4.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/5.jpg', 'https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/6.jpg']}

print('time================',d)

#! change the file name every time
df.to_excel(f'2nd_["jpg,jpg"]_{date}.xlsx', index=False)
