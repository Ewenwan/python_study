# python字典dict 和通用结构json  相互转化


import json


student_list=[
    {'no':'1','name':'小莽','age':'13'},
{'no':'2','name':'小田','age':'19'},
{'no':'3','name':'小李','age':'17'}
]

student_json="""
{
"student_list":[
    {"no":"1","name":"小莽","age":"13"},
{"no":"2","name":"小田","age":"19"},
{"no":"3","name":"小李","age":"17"}
],
 "school_name":"智游",
 "address":"经开第十六大街"
}
"""
# 对象转json
stu_json=json.dumps(student_list,indent=4 )
print(type(stu_json),stu_json )
"""
json.dumps(数据对象 indent=4格式化输出) 返回json格式字符串。
形如\u5c0f是中文的unicode编码。计算机传输的本质是二进制信息。
"""
# json转对象
stu_obj=json.loads(student_json)
print(stu_obj)
for stu in stu_obj['student_list']:
    print(f'学生的名字系{stu["name"]}')
# json.dump() json.load() 这两个方法的参数是文件
# json.dumps() json.loads() 这两个方法的参数是变量
with open('7.天气接口返回数据.json',encoding='utf-8') as file:
    weather_obj=json.load(file)
    print(weather_obj)



# 面试题
