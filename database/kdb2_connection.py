from qpython import qconnection

# 创建与kdb+数据库的连接
q = qconnection.QConnection(host='localhost', port=8090)
q.open()

# 执行查询
result = q.sendSync('select from sp')

# 处理查询结果
for row in result:
    print(row)

# 关闭连接
q.close()
