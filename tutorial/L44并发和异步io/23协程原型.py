# coding:utf-8
__author__ = 'trc'

import time

def coroutine(task):
    print('start')
    time.sleep(2)
    print('end')
    yield 'a'


if __name__ == '__main__':
    c1 =coroutine('c1')
    c2 =coroutine('c2')

    next(c1)
    next(c2)