students = [{'name': '小明', 'age': 10, 'sex': 'male'},
            {'name': '小红', 'age': 12, 'sex': 'female'},
            {'name': '小李', 'age': 12, 'sex': 'male'}
            ]
while True:
    print('''
    1-查询学员姓名
    2-添加学员姓名
    3-修改学员姓名
    4-删除学员姓名
    0-退出程序
    ''')
    user_num = int(input("请输入您的操作："))
    if isinstance(user_num, int):
        if 0 <= user_num < 5:
            if user_num == 1:
                print('行号','\t\t','姓名','\t\t','年龄','\t\t','性别')
                for i in range(1,len(students)+1):
                    name = students[i-1]['name']
                    age = students[i-1]['age']
                    sex = students[i-1]['sex']
                    print(i,'\t\t',name,'\t\t',age,'\t\t',sex,'\t\t')
            elif user_num == 2:
                add_dict = {}
                add_name = input('请输入要添加的姓名：')
                add_age = input('请输入要添加的年龄：')
                add_sex = input('请输入要添加的性别：')
                add_dict = {'name':add_name,'age':add_age,'sex':add_sex}
                students.append(add_dict)
                print('添加成功')
            elif user_num == 3:
                update_num = int(input('请输入要修改的学生行号：'))
                students[update_num - 1]['name'] = input('请输入修改后的姓名：')
                students[update_num - 1]['age'] = input('请输入修改后的年龄：')
                students[update_num - 1]['sex'] = input('请输入修改后的性别：')
                print("修改成功")
            elif user_num == 4:
                del_num = int(input('请输入要删除的行号：'))
                students.pop(del_num - 1)
                print("删除成功")

            else:
                break
    else:
        print("输入错误")


