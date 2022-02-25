#
#to 参考 csv word replacement: https://teratail.com/questions/143036

import pandas as pd
import glob
import datetime

with open('csv_folder/csv_replace_words/test.csv', "r") as f:
    s = f.read()
s = s.replace("ボディーバッグ", "XYZABCDEFG").replace("ボディバッグ", "XYZABCDEFG").replace("ボディーバッグ", "XYZABCDEFG").replace("ボディーバッグ", "XYZABCDEFG").replace("ボディーバッグ", "XYZABCDEFG").replace("ボディーバッグ", "XYZABCDEFG").replace("ボディーバッグ", "XYZABCDEFG").replace("ボディーバッグ", "XYZABCDEFG")

with open('csv_folder/csv_replace_words/test.csv', "w") as f:
    f.write(s)
