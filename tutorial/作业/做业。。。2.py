# student_list = ['小王','小红','小李']
# while True:
#     print('1_查询学员姓名')
#     print('2_添加学员姓名')
#     print('3_修改学员姓名')
#     print('4_删除学员姓名')
#     print('0-退出程序')
#     num = int(input('请输入0到4的操作指令'))
#     if num ==1:
#         name1 = input('请输入要添加的学生姓名')
#         student_list.append(name1)
#         print(student_list)




student_list = ['小王','小红','小李']
while True:
    print("""
    欢迎使用学生管理系统
    1_查询学员姓名
    2_添加学员姓名
    3_修改学员姓名
    4_删除学员姓名
    0-退出程序
    """)

    num = int(input('请输入操作编号: '))

    if num == 1:
        print('行号\t\t姓名')
        print('-------------------')
        for i in range(0, len(student_list)):
            print(i + 1, '\t\t', student_list[i])
    elif num == 2:
        new_name = input('请添加姓名')
        student_list.append(new_name)
        # student_list.append(input('请添加新姓名：'))
        print('添加成功')
    elif num == 3:
        #修改
        print('行号\t\t姓名')
        print('-------------------')
        for i in range(0, len(student_list)):
            print(i + 1, '\t\t', student_list[i])

        stu_num = int(input('修改第几个：'))
        student_list[stu_num-1] = input('修改后的名字：')
        print('修改成功')
    elif num == 4:
        # 删除
        print("""删除> 请输入子操作编号：
                  1)按学生编号删除
                  2）删除全部学生(谨慎)
        """)
        stu_num = int(input('请选择子操作：'))
        if num == 1:
            stu_num = int(input('请选择子操作:'))
            student_list.pop(stu_num -1)
            print('删除成功')
        elif num == 2:
            confirm = input('确认删除全部?(T/N)')
            if confirm == 'Y'or confirm == 'y':
                student_list.clear()
                print('删除全部成功')
    elif num == 0:
        print('谢谢使用')
        break

