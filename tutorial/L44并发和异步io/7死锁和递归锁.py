# 死锁
# 加锁后还可能出现一种特殊情况。 线程A和线程B互相需要等待对方资源，结果都干等着不运行。

# 需求：两个人分别做“西兰花”和“红烧肉”，每个人都需要“锅”和“铲子”才能炒菜。
# 只能一个人先做饭，然后第二个再做，下面用程序表达这个过程

import threading, time

class XiLanHua_Thread(threading.Thread):
    def run(self):
        mutexFlag_C = mutex_C.acquire(True)
        if mutexFlag_C:
            print(self.name + '拿到了铲子')

            time.sleep(1)
            mutexFlag_G = mutex_G.acquire(True)
            if mutexFlag_G:
                print(self.name + '拿到了锅')
                # 开始做饭
                mutex_G.release()
            mutex_C.release()
            print(self.name + '使用完成了')

class HongShaoRou_Thread(threading.Thread):
    def run(self):
        mutexFlag_G = mutex_G.acquire(True)
        if mutexFlag_G:
            print(self.name + '拿到了锅')

            time.sleep(1)
            mutexFlag_C = mutex_C.acquire(True)
            if mutexFlag_C:
                print(self.name + '拿到了铲子')
                # 开始做饭
                mutex_C.release()
            mutex_G.release()
            print(self.name + '使用完成了')

if __name__ == '__main__':
    mutex_C = threading.RLock()      # 铲子锁
    mutex_G = threading.RLock()      # 锅锁

    t1 = XiLanHua_Thread()
    t2 = HongShaoRou_Thread()
    t1.start()
    t2.start()

"""
运行程序，结果卡死。两人都拿到了一个资源，但第二个资源都在对方手里，但由于自己的功能未完成，导致自己拿的资源没释放。两个线程并不聪明，不会把自己的资源先借给对方，而是两方一直等待对方。

避免这种情况发生，改为递归锁。threading.Lock()改为threading.Rlock()
"""
"""
既然用户可以在代码中自由加锁控制，确保线程安全，那么为什么还有GIL？
因为GIL处于解释器层面，轮询查看有没有待销毁的垃圾，相当于执行某一项功能的线程。如果垃圾回收功能的线程跟代码功能的线程混在一块，容易出现数据冲突和安全问题，所以发明者分开设计了。
整体流程详见 8线程整体示意图.png
"""