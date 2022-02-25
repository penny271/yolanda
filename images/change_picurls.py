# coding: UTF-8
#! 上記をつけないとpandasでエラーが起きることがある

from lib2to3.pgen2.token import ISTERMINAL
import pandas as pd
import glob

# abc = ['https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/1.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/2.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/3.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/4.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/5.jpg|https://cdn2.2ndstreet.jp/img/pc/goods/233866/02/51660/6.jpg']

# for i in abc:
#     i = i.replace('|',',')

# print(i)

item_number = 0

img_list = []

pic_number = 0


# for item_number in range(3):
#     print('############', item_number)
#     container = f'<!-- #{item_number+2} item --><div class="container"><ol class="img-list"><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li><li><img src="../images/2nd_20220221/2-1.png" alt="" ></li></ol></div>'
#     item_number = item_number
#     img_list.append(container)

# print('img_list=========================', img_list)
# img_list = '|'.join(img_list)
# print('img_list=============join後==================',img_list)


for item_number in range(3):
    print('############', item_number)
    if pic_number >11:
        pic_number=1
    else:
        pic_number+=1

    container = f'<!-- #{item_number+2} item --><div class="container"><ol class="img-list"><li><img src="../images/2nd_20220221/{item_number+2}-1.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-2.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-3.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-4.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-5.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-6.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-7.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-8.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-9.png" alt="" ></li><li><img src="../images/2nd_20220221/{item_number+2}-10.png" alt="" ></li></ol></div>'

    item_number = item_number
    img_list.append(container)


print('img_list=========================', img_list)
img_list = '|'.join(img_list)
print('img_list=============join後==================',img_list)
