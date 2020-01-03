# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 11:54

from pprint import pprint
import pandas as pd
from sklearn.utils import shuffle
from collections import Counter

# 读取数据集并打乱顺序
df = pd.read_excel('人物关系表.xlsx')
df = shuffle(df, random_state=1234)
pprint(Counter(df['关系']))

# 将数据集分为训练集、验证集、测试集
train_num = int(df.shape[0] * 0.8)
val_num = int(df.shape[0] * 0.1)

train_data = df.iloc[0:train_num, :]
val_data = df.iloc[train_num:train_num+val_num, :]
test_data = df.iloc[train_num+val_num:,:]


# 将数据集写入至txt文件
with open('train.txt', 'w', encoding='utf-8') as f:
    for i in range(train_data.shape[0]):
        line = train_data.iloc[i, :]
        f.write('\t'.join(line.tolist())+'\n')

with open('val.txt', 'w', encoding='utf-8') as g:
    for i in range(val_data.shape[0]):
        line = val_data.iloc[i, :]
        g.write('\t'.join(line.tolist())+'\n')

with open('test.txt', 'w', encoding='utf-8') as h:
    for i in range(test_data.shape[0]):
        line = test_data.iloc[i, :]
        h.write('\t'.join(line.tolist())+'\n')