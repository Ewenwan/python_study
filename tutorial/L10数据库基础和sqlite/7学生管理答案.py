# 学生管理v4 sqlite版
import sqlite3

def create_table():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE students
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex TEXT,
            age INTEGER,
            phone TEXT
        );
    """)
    connect.commit()
    cursor.close()
    connect.close()

def show_students():
    """
    展示学生列表
    """
    print('行号\t\t姓名\t\t年龄\t\t性别\t\t')
    print('----------------------------------')
    conner = sqlite3.connect("test.db")
    cursor = conner.cursor()
    cursor.execute("""
        SELECT * FROM students;
    """)
    student_list = cursor.fetchall()   # [(1,小明,),0]

    for index, student in enumerate (student_list):
        print(f'{index+1}\t\t{student[1]}\t\t{student[2]}\t\t{student[3]}\t\t{student[4]}')


def add_students():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()
    name = input('请输入你要添加的名字')
    sex = input('请输入你要添加的学生的性别')
    age = int(input('请输入你要添加的学生年龄'))
    insert = """INSERT INTO students(name, sex ,age) values ( "%s","%d","%s")"""%(name,sex,age)
    cursor.execute(insert)

def update_students():
    pass
def delete_students():
    sub_select = input("""
    删除>请选择删除子操作
    1. 按学生姓名删除
    2. 全部删除
    """)
    if sub_select == '1':
        stu_name = input('要删除的学生姓名：')
        """ delrte from students where name='{stu_name}'"""
    elif sub_select == '2':
        """ delete from student;"""
        confirm = input('要删除全部学生？(Y/N):')
        if confirm =='Y':
            pass
            # coursor.execute

def main():
    # 主函数，程序入口
    while True:
        print("""
            欢迎使用学生管理系统
            1-查询学员姓名
            2-添加学员姓名
            3-修改学员姓名
            4-删除学员姓名
            0-退出程序
        """)

        num = int(input('请输入操作编码：'))

        if num == 1:
            show_students()
        elif num == 2:
            add_students()
        elif num == 3:
            update_students()
        elif num == 4:
            delete_students()
        elif num == 0:
            break

print(main())




