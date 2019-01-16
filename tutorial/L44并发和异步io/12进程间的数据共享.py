# 进程间数据共享
# 由于进程间的资源相互独立，需要队列queue、管道pipe、中介manager几种方式。

# 队列：先进先出。好像买饭排队，后面增加人，前面的人得到饭后离开队列。场景，生产者消费者模型，某些算法，批量发送广告邮件。

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello',])

if __name__ == '__main__':
    q = Queue()     # 主进程
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()



# (课下)管道pipe、中介manager