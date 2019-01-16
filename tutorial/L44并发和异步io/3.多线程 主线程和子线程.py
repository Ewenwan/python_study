# coding:utf-8
__author__ = 'trc'
import threading
import time

def run(n):
    """倒计时"""
    print('task',n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)
for i in range(3):
    t = threading.Thread(target=run,args=(f't{i}',))
    t.setDaemon(True)
    t.start()

# 主线程
time.sleep(1.5)
# print(threading.active_count())

# t.join()     # 主线程阻塞，让子线程线运行完，失去线程并发意义，但更容易研究一些线程的表现。
# t.setDaemon(True)    # 主线程结束后子线程跟着结束
