from datetime import datetime
from elasticsearch import Elasticsearch

# 连接elasticsearch,默认是9200
es = Elasticsearch()

# 创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
# 这个索引可以现在创建，也可以在后面插入数据的时候再临时创建
# es.indices.create(index='my-index')
# {u'acknowledged':True}


# 插入数据,(这里省略插入其他两条数据，后面用)
# es.index(index="my-index", doc_type="test-type", id=1, body={"any": "data01", "timestamp": datetime.now()})
# {u'_type':u'test-type',u'created':True,u'_shards':{u'successful':1,u'failed':0,u'total':2},u'_version':1,u'_index':u'my-index',u'_id':u'1}
# 也可以，在插入数据的时候再创建索引test-index
# es.index(index="test-index", doc_type="test-type", id=2, body={"any": "data", "timestamp": datetime.now()})
# es.index(index="test-index", doc_type="test-type", id=3, body={"any": "data2", "timestamp": datetime.now()})

## 获取整条数据
res = es.get(index="test-index", doc_type="test-type", id=3)
print(res)
