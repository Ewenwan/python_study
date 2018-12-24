# 高阶函数，闭包，装饰器(后期讲，现在只需认识)


def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1)+ n

print(factorial(100))
