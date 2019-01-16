# grequests
# 由gevent requests合并组成的异步请求包。封装程度较高，不需要关注协程书写。
# pip install grequests

import grequests
import requests
import time

urls = [
    'http://h.hiphotos.baidu.com/image/h%3D300/sign=f2db86688ccb39dbdec06156e01709a7/2f738bd4b31c87018e9450642a7f9e2f0708ff16.jpg',
    'http://e.hiphotos.baidu.com/image/h%3D300/sign=c422d4ad98cad1c8cfbbfa274f3f67c4/83025aafa40f4bfb0f815ad60e4f78f0f63618db.jpg',
    'https://cms-bucket.nosdn.127.net/2019/01/03/7dab883ca11c414a9098b71f7c66e56d.jpeg',
    'http://www.baidu.com',
    'http://www.douban.com',
    'http://www.github.com'
    # 'http://www.google.com'
]

# 同步
# start_time = time.time()
# for url in urls:
#     try:
#         resp = requests.get(url)
#         print(resp.status_code)
#         if resp.status_code == 200:
#             print(resp.text)
#     except Exception as e:
#         print(e)
# end_time = time.time()
# print(end_time - start_time)


# 异步请求
# url列表准备成一个个requests请求对象，以生成器返回，这个生成式每次返回一个requests.get(url) 对象。这时还未真正请求。get()方法与requests包的get()方法一致，可以加params、timeout等参数。
start_time = time.time()
rs = (grequests.get(url) for url in urls)
# 同时请求
# map()方法 接收上面的生成器，每次取出一个requests.get(url)请求，接收response，最终返回所有response。非阻塞所有请求同时发送，并不会因为某一个请求没有得到response还停止其它工作。resp_list已最慢请求为准，默认40s超时
resp_list = grequests.map(rs)
# 拿到所有请求响应后就可以方便地循环取值，resp的顺序与urls一致。
for resp in resp_list:
    if resp is None:
        print(resp.url, '请求失败')
    else:
        print(resp.status_code)
        print(resp.content)
end_time = time.time()
print(end_time - start_time)


"""
urls = [1,2,3,4]
a = [url for url in urls]
print(a,type(a))        # [1,2,3,4]   <class list>

b = (url for url in urls)
print(type(b))      # <generator>
相当于 
def foo():
    for url in urls:
        yield url
b = foo()
"""

"""
可能的报错：
MonkeyPatchWarning或RecursionError。原因https://github.com/gevent/gevent/issues/1016.
解决import requests放import grequests后面。
"""