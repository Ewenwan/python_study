student_list = ['小铁', '小莽', '小楞', '小呆']
while True:
            print('1_添加学院名字')
            print('2_修改学员名字')
            print('3_查询学员名字')
            print('4_删除学员名字')
            print('0-退出程序')
            num = int(input('请输入0到4的操作指令'))
            if num == 1:
               name1 = input('请输入要添加的学生名字')
               student_list.append (name1)
               print(student_list)
            elif num == 2:
                name3 = int(input('请输入要修改的学生的序号'))
                name4 = input('请输入要添加的学生的名字')
                student_list[name3] = (name4)
                print(student_list)
            elif num == 3:
                for i in range(0, len(student_list)):
                 print(i, '  ', student_list[i])
            elif num == 4:
                name2 = int(input('请输入要删除的学生的序号'))
                student_list.pop(name2)
                print(student_list)
                break
            else:
                 print('请输入正确的指令')
