# mysql驱动
# 引题：已经学习了sql语法，sqlite驱动操作sqlitre数据库，datagrip的jdbc java驱动操作mysql。所以我们要找python操作mysql驱动
"""
驱动选择：
1. MySQLDB。已经有C驱动mysql的成熟包，Mysqldb包python对这个c驱动包封装。优点是效率高，py2环境和众多项目中使用。
缺点windows 下pip安装报错。可以去网上找对应平台编译后的.whl安装(也可能出错)。最终解决去mysql官网下载对应平台的connector.msi安装。
2.mysql-connector。 python书写。 类似mysqldb但不依赖c语言驱动。
3. pymysql。纯python写的。缺点效率稍低。优点安装方便，完全兼容mysql的语法。市场占有越来越高。

"""
import pymysql.cursors

connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='trc',
             db='test' ,)

#cursorclass=pymysql.cursors.DictCursor  charset='utf-8mb4'
print(connection)

try:
    with connection.cursor() as  cursor:
        sql="""select * from shirt"""
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for row in result:
            print(f'小红有一个{row[2]}的{row[1]}')
    with connection.cursor() as cursor:
        sql = """INSERT INTO shirt values(%s,%s,%s,%s)"""
        affected_rows=cursor.execute(sql,(None,'裙子','红',100))
        print(affected_rows)
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()



