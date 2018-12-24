students = [
    {'name': '小明', 'age': 10, 'sex': 'male'},
    {'name': '小红', 'age': 12, 'sex': 'female'},
    {'name': '小李', 'age': 12, 'sex': 'male'}
]

class Student():
    #暴露接口，操作变量student_list增删改查，只关注学生类的数据结构。不包含其余的业务逻辑。
    # 类方法或静态方法
    def show_student(self):
        pass

    def __init__(self,name,age):
        #self.name = name
        #先拼字典{'name':'小明','age':10,'sex':'male'}
        #student_list.append()
        pass

    def update(self):
        pass

    def delete(self):
        pass
