# coding:utf-8
__author__ = 'trc'

n = 0
def consumer():
    r = ''
    while True:
        global n
        n =yield r
        if not n:
            return
        print(f'消费者{n}')
        r ='200 ok'
def produce(c):
    c.send(None)
    global n
    while n<5:
        n +=1
        print(f'生产者{n}')
        r =c.send(n)
        print(f'消费者返回{r}')
    c.close()

c = consumer()
produce(c)