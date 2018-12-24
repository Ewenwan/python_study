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
    print('行号\t\t姓名\t\t年龄\t\t性别\t\t手机号')
    print('----------------------------------')
    conner = sqlite3.connect("test.db")
    cursor = conner.cursor()
    cursor.execute("""
        SELECT * FROM students;
    """)
    student_list = cursor.fetchall()  # [(1,小明,),0]
    for index, student in enumerate(student_list):
        print(f'{index+1}\t\t{student[1]}\t\t{student[2]}\t\t{student[3]}\t\t{student[4]}')


def add_students():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()
    new_name = input('请输入姓名:'),
    new_age = int(input('请输入年龄:'))
    new_sex = input('请输入性别')
    insert_sql = f"""insert into students(name,age,sex)VALUES ("new_name","new_age","new_sex")"""
    cursor.execute(insert_sql)
    connect.commit()
    cursor.close()
    connect.close()


def get_count():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()
    select_sql = 'select * from students '
    res = cursor.execute(select_sql)
    count = res.fetchone()[0]
    return count


def test(number):
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()
    select_sql = f"select * from students WHERE id={number }"
    res = cursor.execute(select_sql)
    result = res.fetchall()
    return len(result)


def update_students():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()
    count = get_count()
    if count != 0:
        # 修改之前先把所有的学员信息先查询出来
        show_students()
        select_number = int(input('请输入要修改的学员的编号：'))
        while test(select_number) == False:
            select_number = int(input('输入的学员编号错误，请重新输入:'))
        # 知道了要修改的学员的编号，然后进行修改。
        new_name = input('请输入修改后的姓名:')
        new_age = int(input('请输入修改后的年龄：'))
        new_sex = input('请输入新的性别：')
        new_phone = int(input('请输入新的手机号'))
        update_sql = f"""update students set name={new_name},age={new_age},sex={new_sex},phone={new_phone} where id={select_number}    """

        cursor.execute(update_sql)
    else:
        print('学员信息为空，无法修改')
    connect.commit()
    cursor.close()
    connect.close()


def delete_students():
    connect = sqlite3.connect("test.db")
    cursor = connect.cursor()
    count = get_count()
    if count != 0:
        print('1-删除指定学员的信息')
        print('2-删除所有学员信息')
        select_number = int(input('请输入要操作的序号：'))
        while select_number != 1 and select_number != 2:
            select_number = int(input('请重新输入你要操作的序号:'))
        # 如果用户选择的是1，说明用户想要删除指定的学员信息
        if select_number == 1:
            show_students()
            number = int(input('请输入要删除的学员编号：'))
            while test(number) == False:
                number = int(input('学员编号输入错误，请重新输入要删除的学员编号：'))
            delete_sql = f"delete from students where id ={number}"
        else:
            delete_sql = 'delete from student'
        cursor.execute(delete_sql)
    else:
        print('学员信息为空')
    connect.commit()
    cursor.close()
    connect.close()


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
