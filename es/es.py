from elasticsearch import Elasticsearch

es_object = Elasticsearch()


def create_index():
    # index settings
    settings = {
        "mappings": {
            "user": {
                "properties": {
                    "first_name": {
                        "type": "text"
                    },
                    "last_name": {
                        "type": "text"
                    },
                    "about": {
                        "type": "text"
                    },
                    "age": {
                        "type": "integer"
                    },
                }
            }
        }
    }

    try:
        if not es_object.indices.exists("users"):
            es_object.indices.create(index="users", body=settings)
            print('Created Index')
        else:
            print("users already exists")
    except Exception as ex:
        print(str(ex))


# 写入数据Inserting a document:
# 可以在不创建index,type的情况下直接insert 文档
def insert():
    body1 = {
        "first_name": "John",
        "last_name": "Smith",
        "age": 25,
        "about": "I love to go rock climbing"
    }

    body2 = {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 32,
        "about": "I like to collect rock albums"
    }

    body3 = {
        "first_name": "Douglas",
        "last_name": "Fir",
        "age": 35,
        "about": "I like to build cabinets"
    }
    res1 = es_object.index(index="users", doc_type='user', id=1, body=body1)
    res2 = es_object.index(index="users", doc_type='user', id=2, body=body2)
    res3 = es_object.index(index="users", doc_type='user', id=3, body=body3)


# 检索所有文档Retrieving all Document:
def queryall():
    # rt1 = es_object.search(index="users") #检索index下所有文档
    # rt2 = es_object.search(index="users",doc_type="user") #检索index/type下所有文档
    rt3 = es_object.get(index="users", doc_type="user", id=1)  # 检索index/type下所有文档
    print(rt3)


# 这是一个elasticsearch的简单查询,要求匹配 名字为”Smith”
def querybylastname():
    condition = {
        "query": {
            "match": {"last_name": "Smith"}
        }
    }
    rt1 = es_object.search(index="users", body=condition)
    print(rt1)


# 搜索姓氏为 Smith 的雇员，但这次我们只需要年龄大于 30 的
def querybylastname_age():
    condition = {
        "query": {
            "bool": {
                "must": {"match": {"last_name": "smith"}
                         },
                "filter": {
                    "range": {
                        "age": {"gt": 30}
                    }
                }
            }
        }
    }
    rt1 = es_object.search(index="users", body=condition)
    print(rt1)


if __name__ == '__main__':
    # create_index() #创建index及mapping(表结构)
    # insert() #插入数据
    queryall()  # 查询所有
# querybylastname()
# querybylastname_age()
