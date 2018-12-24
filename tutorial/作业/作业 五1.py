# 第一题
# def factorial(n):
#     if n == 0:
#         return 0
#     return factorial(n-1) + n
# print(factorial(100))
#
#

#第二题
# def factorial(n):
#     if n == 1:
#         return 1
#     return factorial(n-1) * n
# print(factorial(1))


#  作业4
def boo(n):
    if n ==1:
        return 1
    elif n == 2:
        return 1
    else:
        return boo(n-1) + boo(n-2)
for i in range(1,8+1):
    print(boo(i),',',end='')
