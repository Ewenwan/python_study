# 参考 [一个socket例子演示异步IO演化](https://blog.csdn.net/sinat_38682860/article/details/80847674)
import time
# 伪代码
def coroutine(c):
    # 请求一个网址
    # 下载图片，写数据库，代码运算假设消耗一些时间。
    time.sleep(10)
    # 遇到阻塞，挂起，跳转到主线代码中（第23行)
    c.switch()
    # 注册事件
    c.register(name=c, signal='Done')
    yield resp

# 事件在内存中占据一片公共区域
def loop():
    pass

def save_img():
    pass

if __name__ == '__main__':
    c1 = coroutine()
    c2 = coroutine()
    c3 = coroutine()

    next(c1)
    next(c2)

    # 查看事件循环
    while True:
        if event_list:
            resp1 = c1.send()
            save_img(resp1.content)

# 同步循环因为IO阻塞，运行完一个再运行第二个下载，在IO时间长的情况下耗费大量时间。
# for i in ['www1', 'www2',...]:
#     coroutine()
# 改进：IO非阻塞，事件循环。
"""
事件循环：查询某一支任务有没有完成
回调函数（callback）： 上例中的save_img()函数。回头再调用，先把函数功能放那，回调函数的需要参数，参数又需要其它函数来获取。回调函数等待参数准备好后再执行。 比喻：小区有个小卖铺，你告诉老板想要一包方便面（回调函数定义），老板说没货了需要去进货（IO等待时间），货到了我再打电话通知你（回调函数返回结果）。
"""




