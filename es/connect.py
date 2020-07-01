from elasticsearch import Elasticsearch

#connect to our ES server
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def connect_elasticsearch():
    # es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # es.ping()对服务器发送ping请求，如果连接上的话返回True
    if es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return es


# 获取当前连接的集群节点信息
def info():
    print(es.cluster.client.info())


# 获取集群目前所有的索引
def getallindex():
    #print(es.cat.indices())
    print(es.indices.get_alias())
    print(es.indices.get_alias().keys())#查询所有index名称



def indexinfo():
    print(es.indices.get("users"))#查询index信息,包含mapping  settings信息
    print(es.indices.get_mapping("users"))# 查看指定index的mapping信息
    print(es.indices.get_settings("users"))# 查看指定index的settings信息

def nodesinfo():
    print(es.cat.indices())

if __name__ == '__main__':
    #connect_elasticsearch()
    #getallindex()
    indexinfo()

