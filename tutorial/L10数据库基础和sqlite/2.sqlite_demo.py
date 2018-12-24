# （重点）sqlite示例   创建表，写数据
import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()
# cursor.execute("""CREATE TABLE student(
#                         id INT PRIMARY KEY,
#                         name VARCHAR(10)
#                 ); """)

cursor.execute("""
    INSERT INTO student (id, name) VALUES (2, "小明");
""")

cursor.close()
connect.commit()
connect.close()







"""
（了解）数据库驱动：数据库有自己本身的软件构造和操作语言，数据库暴露出操作接口，方便跟其它各种编程语言对接。编程语言到数据库的对接中介 叫驱动。所以我们用python操作数据库要使用驱动。

步骤：
1. 引入驱动包
2. 连接数据库，得到会话。   中大型数据库需要先用户名、密码验证，再创建数据库，再连接数据库；而轻量级的sqlite省略了前面的过程直接连接，如果这个数据库不存在的话，会新生成一个库，数据保存在一个单db文件中。
(了解)sqlite3.connect(':memory:')
数据库会创建在内存中，脚本正常运行，只不过看不到具体数据库
3. 生成游标。  游标：游标是对数据库某一行某一格进行增删改查的操作者，就好像操作excel表格时的鼠标。
4. 插入一些数据。  注意主键id列不能重复。
5. 关闭游标。   这一步可以省略。
6. 提交 commit。   除了查询，增加、修改、删除操作都需要在执行sql提交，否则不生效，好像平时用软件保存时的确认对话框。
7. 断开会话连接，释放资源。





"""

"""
可能的异常：
1. 唯一约束错误，主键重复。 sqlite3.IntegrityError: UNIQUE constraint failed: student.id
2. 表已存在重复创建。sqlite3.OperationalError: table student already exists
"""
