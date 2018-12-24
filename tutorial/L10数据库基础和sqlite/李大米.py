# import sqlite3
# connect = sqlite3.connect('test.db')
# cursor = connect.cursor()
#
# # cursor.execute("""
# # # CREATE TABLE  lidami(
# # # id INTEGER primary key ,
# # # name VARCHAR(20),
# # # sex  varchar (20)
# # # )
# # # """)
# # INTEGER 整数类型 primary key 主键 VARCHAR 字符串类型
#
# cursor.execute("""
# INSERT INTO
# # INSERT INTO 插入进去 lidami(id, name, sex) values (2, '田润超', '男')
# # """)
#
#
# connect.commit()


import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

def show_students():
    cursor.execute(""" 
        SELECT * FROM students;
    """)
    students_list = cursor.fetchall()
    print(students_list)

def add_students():
    a = int(input("请输入要插入id号："))
    b = input("请输入要插入的学生姓名：")
    c = input("请输入要插入的学生性别：")
    d = int(input("请输入要插入的学生年龄："))
    e = int(input("请输入要插入的学生电话号码："))
    cursor.execute("""INSERT INTO students(id,name,sex,age,phone) VALUES ('{}','{}','{}','{}','{}');
    """.format(a,b,c,d,e))
    cursor.execute(""" 
        SELECT * FROM students;
        """)
    students1 = cursor.fetchall()
    print(students1)

def update_students():
    show_students()
    # f = input("要修改id的号码：")
    g = input("修改后的新姓名：")
    # h = input("修改后的新年龄：")
    # j = input("修改后的新性别：")
    # k = input("请输入新电话号：")
    cursor.execute("""
    UPDATE students SET name='{}' WHERE id=2;
    """.format(g))
    show_students()

def delete_students():
    print("""
    选项>请输入操作选项：
        1.删除整个表
        2.删除某一行
    """)
    l = int(input("请输入选项选择对应操作："))
    if l == 1:
        cursor.execute("""
            DELETE FROM students;
        """)
    if l == 2:
        m = int(input("请输入要删除的id序号："))
        cursor.execute("""
            DELETE FROM students WHELE id='{}';
        """.format(m))
        show_students()
def main():
    while True:
        print("""
        尊敬的用户，你好！
        欢迎使用学生管理系统
        1-查询学员姓名
        2-添加学员姓名
        3-修改学员姓名
        4-删除学员姓名
        0-退出程序
        以上是该程序的指引

        """)

        n = int(input("请输入一个数字来确定执行何种操作: "))
        if n == 1:
            show_students()
        elif n == 2:
            add_students()
        elif n == 3:
            update_students()
        elif n == 4:
            delete_students()
        elif n == 0:
            break


if __name__ == '__main__':
    main()

cursor.close()
connect.commit()
connect.close()