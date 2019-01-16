# 创建多线程

# import _thread  # 多线程低层操作包，主要使用threading包
# 创建多线程：方式一 threading.Thread() 生成线程实例然后运行   方式二 class xxx(Thread):  def run() 继承父类重写与run方法。

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

# run(99)      # 单线程运行，忽略参数，是一个普通的
t0 = threading.Thread(target=run,args=('t0',)) #target目标 threading线程
t1 = threading.Thread(target=run,args=('t1',))
t2 = threading.Thread(target=run,args=('t2',))
t0.start()
t1.start()
t2.start()
