# -*- coding:utf-8 -*-

import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch('127.0.0.1:9200')

def createESDatabase():

    ## 创建索引（数据库）
    es.indices.create(
        index='room',
        ignore=400,
        body={
            'index': {
                'number_of_replicas': 0
            }
        }
    )

if __name__ == '__main__':
    fpath = './data/house.csv'
    df = pd.read_csv(fpath,encoding='utf-8')

    createESDatabase()

    for idx,series in df.iterrows():
        question = series['q']
        answer = series['a']
        roomid = series['roomId']
        category = series['question_category']
        entity = series['entity']

        es.index(
            index='room',
            doc_type='text',
            body={'idx':idx,
                  'question': question,
                  'answer': answer,
                  'roomid': roomid,
                  'category':category,
                  'entity':entity
                  }
        )
        print(idx)