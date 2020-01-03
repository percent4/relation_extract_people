# -*- coding: utf-8 -*-
# place: Sanya, Hainan

#import os
# 使用第一张与第三张GPU
#os.environ["CUDA_VISIBLE_DEVICES"] = "1,2,3"

import kashgari
from kashgari.embeddings import BERTEmbedding
from pre_process import get_text_relation_dict
from kashgari.tasks.classification import DPCNN_Model

# kashgari.config.use_cudnn_cell = True

# 获取数据
train_x, train_y = get_text_relation_dict('train')
valid_x, valid_y = get_text_relation_dict('val')
test_x, test_y = get_text_relation_dict('test')

# 词向量嵌入
bert_embed = BERTEmbedding('chinese_wwm_ext_L-12_H-768_A-12',
                           task=kashgari.CLASSIFICATION,
                           sequence_length=100)

# 训练模型
model = DPCNN_Model(bert_embed)
model.fit(train_x, train_y, valid_x, valid_y, batch_size=8, epochs=30)

# 评估模型
model.evaluate(test_x, test_y)

# 保存模型
model.save('text_classification_model')