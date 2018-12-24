# # f = [1,2,3,4]
# f = "wer"
# if isinstance(f,list):
#     if len(f) >= 5:
#         print(f[:2])
#     elif len(f) < 5:
#         print('None')
# else:
#     print('输入错误')

# # 第一题
# def a(x):
#     if len(x) >= 5:
#         print(x[0:2])
#     else:
#         print("None")
# x = [1,2,3,4]
# a(x)



# 第二题

#
# def niupi():
#     demo_list = ['小莽', '小铁', '小哦', '小牛', '小皮']#旧列表
#     mangfu=demo_list[0:5]  #切片把demo_list里面的内容提出来
#     demo_list1 = []   #新列表
#     for i in range(0, len(mangfu)):# for循环 mangfu 的长度
#         if (i % 2) == 0: #判断是否偶数
#             print('哦，牛皮')  #如果是偶数不用输出 这个写个none就可以
#         else:
#              o=demo_list[i] # 现在i是奇数  o把mangfu中奇数部分给提出来
#              demo_list1.append(o) # 添加
#     print(demo_list1) # 输出
# print(niupi())  #def函数输出





#
# def lst():
#     demo_list = ['小莽', '小铁', '小哦', '小牛', '小皮']#旧列表
#     # mangfu=demo_list[0:5]  #切片把demo_list里面的内容提出来
#     demo_list1 = []   #新列表
#     for i in range(0, len(demo_list)):# for循环 mangfu 的长度
#         if (i % 2) == 0: #判断是否偶数
#             print('偶数')  #如果是偶数不用输出 这个写个none就可以
#         else:
#              o=demo_list[i] # 现在i是奇数  o把mangfu中奇数部分给提出来
#              demo_list1.append(o) # 添加
#
#     print(demo_list1) # 输出
# print(lst())  #def函数输出







a = ['小周','小吴','小郑','小王','小李']
b = []
for i in range(1,len(a)):
    if i%2 == 1:
        print(i)
        b.append(a[i])
print(b)