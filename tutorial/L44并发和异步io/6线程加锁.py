 # 为了避免多线程对一处公共资源同时读写导致问题。
# 办法：当一个线程操作资源时，声明操作权，这时其它线程无法操作。叫做 加锁。
# 当这个线程对资源操作完毕时，释放操作权， 叫做 解锁。然后其它资源再争夺下一次操作权。
import threading
import time

num = 100

def sub():
    """ 每次减1"""
    global num

    lock.acquire()      # 加锁
    temp = num
    time.sleep(0.001)
    num = temp - 1
    lock.release()      # 解锁

l = []
lock = threading.Lock()     # 实例化
for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    l.append(t)

for t in l:
    t.join()    # 子线程执行完再执行主线程，确保执行100次sub函数

print(num)      # 0


# 加锁后的线程挨个执行，结果正确
# 类似数据中 事务 的思想