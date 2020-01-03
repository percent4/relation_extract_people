# -*- coding: utf-8 -*-
# time: 2019-08-13 11:16
# place: Sanya, Hainan

from collections import defaultdict
from pprint import pprint


# 构建人物关系、id字典
with open('data/relation2id.txt', 'r', encoding='utf-8') as g:
    content = [_.strip() for _ in g.readlines()]

relation_id_dict = {}
id_relation_dict = {}
for line in content:
    relation, id = line.split()
    relation_id_dict[relation] = int(id)
    id_relation_dict[int(id)] = relation

# pprint(relation_id_dict)
# pprint(id_relation_dict)


# 读取人物关系文本，处理成文本-关系字典
def get_text_relation_dict(txt_type):
    with open('data/%s.txt'%txt_type, 'r', encoding='utf-8') as f:
        content = [_.strip() for _ in f.readlines()]

    train_data_dict = {}
    for item in content:
        parts = item.split('\t')
        # 替换原文中出现的人名
        person1 = parts[0]
        person2 = parts[1]
        origin_text = parts[3]
        origin_text = origin_text.replace(person1, '$'*len(person1))
        origin_text = origin_text.replace(person2, '$'*len(person2))
        text = person1 + '*' + person2 + '*' + origin_text
        relation = relation_id_dict[parts[2]]

        train_data_dict[text] = relation

    keys = []
    vals = []
    for _ in list(train_data_dict.keys()):
        lst = []
        for char in _:
            if char == '*':
                item = 'SEP'
            elif char == '$':
                item = 'UNK'
            else:
                item = char
            lst.append(item)
        keys.append(lst)
        # keys.append([char for char in _])
        vals.append(train_data_dict[_])

    return keys, vals


# 测试
if __name__ == '__main__':
    keys, vals = get_text_relation_dict('train')
    print(keys)


