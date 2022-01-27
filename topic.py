from utils import *
import pandas as pd

# total 9 topic
df = load_file('data_topic.xlsx')
# initialize
topics = [f'主題{i}' for i in range(1, 10)]
# 各主題數量
topic_num = [0 for i in range(9)]
# 各主題所在index
topic_index = {}

for i in range(1, 10):
    topic = f'主題{i}'
    topic_index[f'主題{i}'] = []
    
    for j in range(len(df)):
        if(pd.isna(df[topic][j])):
            continue
        else:
            topic_num[i-1] += 1
            topic_index[f'主題{i}'].append(j)

print(topic_num)
print(f'已標注資料數量 {sum(topic_num)}')
print(topic_index)




    