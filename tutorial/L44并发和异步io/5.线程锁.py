# coding:utf-8
__author__ = 'trc'
import time
import threading

num =100
def sub():
    global num
    temp =num
    time.sleep(0.001)
    num =temp-1
l =[]
for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()  #子线程执行完在执行猪线程 确保执行100次sub函数

print(num)