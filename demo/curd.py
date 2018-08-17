# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
import elasticsearch

def createESDatabase(idxName):
    ## 创建索引（数据库）
    es.indices.create(
        index = idxName,
        ignore = 400,
        body = {
            'index': {
                'number_of_replicas': 0
            }
        }
    )

class ElasticSearchClient(object):
    @staticmethod
    def get_es_servers():
        es_servers = [{
            "host": "localhost",
            "port": "9200"
        }]
        es_client = elasticsearch.Elasticsearch(hosts=es_servers)
        return es_client

class SearchData(object):
    index = 'room'
    doc_type = 'text'

    @classmethod
    def search(cls, field, query, search_offset, search_size):
        # 设置查询条件
        es_search_options = cls.set_search_optional(field, query)
        # 发起检索。
        es_result = cls.get_search_result(es_search_options, search_offset, search_size)
        # 对每个结果, 进行封装。得到最终结果
        final_result = cls.get_highlight_result_list(es_result, field)
        return final_result

    @classmethod
    def get_highlight_result_list(cls, es_result, field):
        result_items = es_result['hits']['hits']
        final_result = []
        for item in result_items:
            item['_source'][field] = item['highlight'][field][0]
            final_result.append(item['_source'])
        return final_result

    @classmethod
    def get_search_result(cls, es_search_options, search_offset, search_size):
        es_result = ElasticSearchClient.get_es_servers().search(
            index=cls.index,
            doc_type=cls.doc_type,
            body=es_search_options,
            from_=search_offset,
            size=search_size
        )
        return es_result

    @classmethod
    def set_search_optional(cls, field, query):
        es_search_options = {
            "query": {
                "match": {
                    field: {
                        # "query": query,
                        # "slop": 10
                        "query": query
                    }
                }
            },
            "highlight": {
                "fields": {
                    "*": {
                        "require_field_match": True,
                    }
                }
            }
        }
        return es_search_options

if __name__ == '__main__':
    es = Elasticsearch('127.0.0.1:9200')

    idxName = 'wether'

    # 创建数据库
    #createESDatabase(idxName)

    # 插入数据
    typeName = 'summer'
    # body = {'country':'中国','city':'西安','mood':'晴','temperature':'30'}
    body = {'country':'china','city':'xian','mood':'晴','temperature':'30'}
    # es.index(index = idxName,doc_type = typeName,body = body)

    body = {'country': '美国', 'city': '洛杉矶', 'mood': '阴', 'temperature': '25'}
    # es.index(index=idxName, doc_type=typeName, body=body)

    body = {'country': '英国', 'city': '伦敦', 'mood': '雨', 'temperature': '20'}
    # es.index(index=idxName, doc_type=typeName, body=body)

    # 查找数据
    # rst = es.get(index = idxName,doc_type=typeName,id = '2V0O-GQB5RtwR_TSeO6c')
    # print(type(rst))
    # print(rst)

    # 更新数据
    '''这块暂时有问题 !!!'''
    # body = {'country': '美国', 'city': '洛杉矶', 'mood': '阴', 'temperature': '25'}
    # body = {'city': '华盛顿'}
    # es.update(index = idxName,doc_type = typeName,id = '2V0O-GQB5RtwR_TSeO6c',body = body)

    """
        条件查找    
    """
    # 全部查找
    query = {'query':{'match_all':{}}}

    # 精确查找 和分词有关
    query = {'query':{'term':{'temperature':'25'}}}
    query = {'query':{'term':{'mood':'阴'}}}
    query = {'query':{'term':{'country':'中国'}}}
    query = {'query':{'term':{'country':'china'}}}

    #
    query = {'query':{'range':{'temperature':{'lt':30}}}}
    query = {'query': {'range': {'temperature': {'gt': 30}}}}

    # rst = es.search(index = idxName,doc_type = typeName,body = query)

    # print(len(rst['hits']['hits']))
    # print(rst['hits']['hits'])
    # print(rst['hits']['hits'][0])

    """
        条件删除
    """
    """
    query = {'query': {'match': {'sex': 'famale'}}}# 删除性别为女性的所有文档

    query = {'query': {'range': {'age': {'lt': 11}}}}# 删除年龄小于11的所有文档

    es.delete_by_query(index='indexName', body=query, doc_type='typeName')
    """


    # frst = SearchData().search('question','卫生间',0,30)
    # frst = SearchData().search('question','空调',0,30)
    # frst = SearchData().search('question','碗',0,30)
    # print('查询到的句子数：',len(frst))
    # for obj in frst:
        # for k,v in obj.items():
        #     print(k,v)
        # print(obj['question'])
        # print('--------------')

    idxName = 'room'
    typeName = 'text'
    searchOption = {
        'query':{
            'match':{
                # 'question':{'query':'卫生间'}
                'question': {'query': '电脑'}
            }
        }
    }
    srst = es.search(index = idxName,doc_type = typeName,body = searchOption)
    srst = srst['hits']['hits']
    print(len(srst),type(srst))
    for source in srst:
        tmp = source['_source']['question']
        print(tmp)




