# stu_dict = {'name':'小明','age':10, 'sex':'男','height':160}
# print(stu_dict.values())    # 值
# print(stu_dict.keys())      # 键
# print(stu_dict.items())     # 键值对
# stu_dict['weight'] = 50
# print(stu_dict)
# # stu_dict['weight'] = 40
# # print(stu_dict['weight'])
# del stu_dict['name']
# print(stu_dict)
# stu_dict.pop('age')
# print(stu_dict)


# student = [
#     {'name':'小明','age':10,'sex':'male'},
#     {'mame':'小红','age':12,'sex':'female'},
#     {'mame':'小李','age':12,'sex':'male'}
#           ]
# print(student[0])
# a = student[0]['name']
# print(a)



# weather_info = {
#     'success':'ok,' ,
#     'status_code':200,
#     'city_list':[
#                 {'name':'郑州','temp':'28','wet':30},
#                 {'name':'洛阳','temp':'25','wet':40},
#                ]
# }
# print(weather_info['city_list'])

# c = [1,2,3,4,5,6,1,3,6]
# new_c = []
# for i in c:
#     print(i)
#     if i not in new_c:
#         new_c.append(i)
# print(new_c)
#
#
#
# a = [1,2,3,4,5,6,1,3]
# new_list = []
# for i in a:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)





# def get_max(num1,num2,num3):
#     # if num2 > num1:
#     #     return num2
#     # else:
#     #     return num1
#     max = num1
#     if num2 > num3:
#         max = num2
#         return max
#     else:



# get_max(1,3)



# def get_max2(num1,num2,num3):
#     max = num1
#     if num2 > num3:
#         if max >= num2:
#             max = max
#         else:
#             max = num2
#         return max
#     else:
#             if max >= num3:
#                 max = max
#             else:
#                 max = num3
#             return max
#
# print(get_max2(3,1,5))

# list1 = [1,2,-3,-4,5,-8]
# def get_max3():
#     max3 = list1[0]
#     for i in list1:
#         if i > max3:
#             max3 = i
#
#     return max3
# print(get_max3())
#
# age = 20
# if age > 18:
#     print('年龄大于18是成人')
# else:
#     print('未成年')

# score = -1
# if score < 0 or score > 100:
#     print('分数不合法')
# elif score < 60:
#     print('不及格')
# elif 60 < score < 70:
#     print('及格')
# elif 70 < score < 90:
#     print('良')
# elif score >= 90:
#     print('优秀')
# else:
#     print('请输出整数')
#




# def yuan(r):
#     a=3.14*r*r
#     print(a)
# yuan(2)
# def zheng(b):
#     t=b*b*b
#     print(t)
# zheng(2)
# def qiu(y):
#     i=(4/3)*3.14*y*y*y
#     print(i)
# qiu(2)
#
#
#
#
#
#
#
#
#
# with open('D:\\pycharmprojects\\tutorial\L7本地文件读写\\chinese_utf-8.txt','r',encoding='utf-8')as f:
#     content = f.read()
#     print(content)
#
#
#
#
#
#
#
# with open('D:\\pycharmprojects\\tutorial\L7本地文件读写\\chinese_utf-8.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)




 # 导入random模块
import random

# 导入Image,ImageDraw,ImageFont模块
from PIL import Image, ImageDraw, ImageFont

# 定义使用Image类实例化一个长为120px,宽为30px,基于RGB的(255,255,255)颜色的图片
img1 = Image.new(mode="RGB", size=(120, 30), color=(255, 255, 255))

# 实例化一支画笔
draw1 = ImageDraw.Draw(img1, mode="RGB")

# 定义要使用的字体
font1 = ImageFont.truetype("ariali.ttf", 28)

for i in range(5):
    # 每循环一次,从a到z中随机生成一个字母或数字
    # 65到90为字母的ASCII码,使用chr把生成的ASCII码转换成字符
    # str把生成的数字转换成字符串
    char1 = random.choice([chr(random.randint(65, 90)), str(random.randint(0, 9))])

    # 每循环一次重新生成随机颜色
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 把生成的字母或数字添加到图片上
    # 图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
    draw1.text([i * 24, 0], char1, color1, font=font1)

# 把生成的图片保存为"pic.png"格式
with open("pic.png", "wb") as f:
    img1.save(f, format="png")
#












