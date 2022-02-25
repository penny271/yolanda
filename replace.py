import pandas as pd
import numpy as np
import datetime

#! I added the below time related things
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
print(repr(now))

d = now.strftime('%Y%m%d%H%M%S')
print(d)  #example 20211104173728 秒まで

d = now.strftime('%Y%m%d%H%M')
print(d)  #example 202111041737 分まで

words_to_replace = pd.read_csv('csv_folder/csv_replace_words/words_to_replace.csv')
# df = pd.read_csv('main_data.csv')
#! change the filename extension from .csv to .xlsx
df = pd.read_excel('main_data.xlsx')

print(words_to_replace)

# load the dataframe to dictionary for easier processing
words_dict = {}
for index, rows in words_to_replace.iterrows():
    if rows["new word"] is not np.nan:
        key = rows["old word"]
        value = rows["new word"]
    else:
        key = rows["old word"]
        value = " "
    words_dict[key] = value

# convert to proper datatypes
df = df.convert_dtypes()


# main function to replace old values with new ones
def helper_function(old):
    if not isinstance(old, str):
        return old
    old = old.split(' ')
    for i in range(len(old)):
        for key in words_dict:
            if key in old[i]:
                print(f'Changed {old[i]} to {words_dict[key]}, {key}')
                old[i] = words_dict[key]
    return ' '.join(old)


# iterate through the dataframe and apply the function to each value
cols = df.columns
for ind, rows in df.iterrows():
    for each_col in df.columns:
        new_val = helper_function(df[each_col][ind])
        df[each_col][ind] = new_val


# write to csv
# OUTPUT_FILENAME = 'final_'+d+'.csv'
OUTPUT_FILENAME = 'final_'+d+'.xlsx'
# df.to_csv(OUTPUT_FILENAME, index=False)
#! change the filename extension from .csv to .xlsx
df.to_excel(OUTPUT_FILENAME, index=False)
