# -*- coding: utf-8 -*-
# place: Sanya, Hainan

import kashgari
from pre_process import id_relation_dict

# 加载模型
loaded_model = kashgari.utils.load_model('text_classification_model')

#text = '韩庚卢靖姗昨天有个热搜，韩庚和卢靖姗结婚了，将在31日举行婚礼。'
while 1:
    text = input("Enter people and sentence:")

    lst = []
    persons, origin_text = text.split('*')[0:2], text.split('*')[2]
    for _ in persons:
        origin_text = origin_text.replace(_, '$'*len(_))
    text = '*'.join(persons + [origin_text])

    for char in text:
        if char == '*':
            item = 'SEP'
        elif char == '$':
            item = 'UNK'
        else:
            item = char
        lst.append(item)

    x = [lst]
    print(x)
    #x = [[_ for _ in text]]
    label = loaded_model.predict(x)
    print('预测人物关系:%s' % id_relation_dict[int(label[0])])