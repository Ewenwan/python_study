# coding:utf-8
__author__ = 'trc'
def create_counter(n):
    """生成一条序列"""
    print('create counter..')
    while n<4:
        yield n
        print('increment',n)
        n += 1

# cnt = create_counter(2)
# print(cnt,type(cnt))
# try:
#     print(next(cnt))
#     print('====')
#     print(next(cnt))
#     print(next(cnt))
# except Exception as c:
#     print('StopIterion 没有新值生成了','\ndone')

# 生成器对象 、 next取值、无新对象生成、这些操作麻烦，所以出现了
# for item  in 生成器对象
for i in create_counter(1):
    print(i)