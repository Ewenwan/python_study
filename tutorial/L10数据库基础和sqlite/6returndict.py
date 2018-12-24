# sqlite fetchall() 返回字典形式。

"""
原[(1,'小明')，（2，'小红'）]
需求[{'id':1, 'name':'小明'},{'id':2, 'name':'小红'}]

百度后思路
1. 驱动方法https://www.jb51.net/article/94024.htm   cursor.description()
2. sql语句 http://www.hangge.com/blog/cache/detail_1454.html   PRAGMA table_info([employee]);

"""
import sqlite3
connect  = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

cursor.execute(""" select * from employee;""")
employees = cursor.fetchall()
print(employees)

print(cursor.description)
description = cursor.description
column_name_list = []
for i in description:

    column_name_list.append(i[0])  # 列名
print(column_name_list)

# 结果集拼字典
result = []
for employee in employees:
    employee_dict = {}
    for index in range(0, len(column_name_list)):
        print(len(column_name_list))
        print(column_name_list[index])
        print(employee[index])
        employee_dict[column_name_list[index]] = employee[index]
    print(employee_dict)
    result.append(employee_dict)

    print(dict(zip(column_name_list, employee)))
print(result)

print("=========语法糖写法")
print([dict(zip(column_name_list,employee)) for employee in employees])
