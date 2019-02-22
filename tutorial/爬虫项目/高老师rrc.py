from fake_useragent import UserAgent
# 导入进程池的类
# 进程池和线程池
# 全局解释锁：GIL
# IO密集型任务：爬虫(网络请求、数据库读写)，因为GIL在遇到比较耗时的任务时，python解释器会自动释放这个锁，让其它的线程开始工作。
# 计算密集型任务：科学计算(加减乘除等)
from multiprocessing import Pool
import requests, re

class RRCSpider(object):
    ua = UserAgent()

    def __init__(self):
        self.url = 'https://www.renrenche.com/zz/ershouche/p{}/'

    def get_list_page(self, page_num):
        """
        请求列表页
        :param page_num:
        :return:
        """
        print('正在请求第{}页'.format(page_num))
        # 开始利用self.url拼接page_num，构造完整的url地址。
        list_url = self.url.format(page_num)
        try:
            response = requests.get(url=list_url, headers={'User-Agent': self.ua.chrome})
            if response.status_code == 200:
                return response.text
            else:
                print('列表页状态码异常：{}'.format(response.status_code))
                return None
        except Exception as e:
            print('列表页请求失败：{}'.format(e))
            return None

    def parse_list_page(self, list_html):
        """
        解析列表页，提取详情页的Url地址
        :param list_html:
        :return:
        """
        patt = re.compile(r'<li class="span6.*?<a.*?href="(.*?)".*?class="thumbnail"', re.S)
        # findall('a(.*?)b', ''): ['123', '234']
        # findall('a(.*?)bbb(.*?)ccc', ''): [('123', '111'), ()]
        # ['https://xxx', 'https://xxx']
        detail_urls = re.findall(patt, list_html)
        # 如果函数内部有yield关键字，那么这个函数就变成了一个生成器对象。
        # 生成器对象和列表对象
        # 相同点：这两个对象都属于可迭代对象，都能使用for循环进行遍历。
        # 不同点：列表对象是一次性的将40个url地址，同时保存在内存中，所以如果列表的数据量比较大，会导致内存占用过多，影响运行效率。生成器对象它并不会将所有值全部放在内存中，而是等程序遍历这个生成器对象的时候，生成器会动态的获取一个url地址，然后将这一个url放在内存中。
        for detail_url in detail_urls:
            yield detail_url
        # return detail_urls

    def get_detail_page(self, detail_url):
        """
        请求详情页
        :param detail_url:
        :return:
        """
        url = 'https://www.renrenche.com' + detail_url
        try:
            response = requests.get(url=url, headers={'User-Agent': self.ua.chrome})
            if response.status_code == 200:
                return response.text
            else:
                print('详情页状态码异常：{}'.format(response.status_code))
                return None
        except Exception as e:
            print('详情页请求失败：{}'.format(e))
            return None

    def parse_detail_page(self, detail_html, detail_url):
        """
        解析详情页数据
        :param detail_html:
        :return:
        """
        if 'zz/sales' not in detail_url and 'zz' in detail_url:
            patt = re.compile(r'<h1 class="title-name.*?</span>(.*?)</h1>.*?<p class="money.*?首付(.*?)</p>.*?月供(.*?)</p>.*?<li class="kilometre">.*?<strong class="car-summary.*?>(.*?)</strong>.*?<li class="span7">.*?<strong class="car-summary">(.*?)</strong>', re.S)
            data = re.findall(patt, detail_html)
            print(detail_url, data)

    def start(self, num):
        list_html = self.get_list_page(num)
        if list_html:
            urls = self.parse_list_page(list_html)
            # print(urls)
            for detail_url in urls:
                detail_html = self.get_detail_page(detail_url)
                if detail_html:
                    self.parse_detail_page(detail_html, detail_url)

if __name__ == '__main__':
    obj = RRCSpider()

    # 进程池：可以在这个池子中创建指定数量的进程对象，然后将所有的请求任务交给这个池子中的几个进程取执行。100个任务  3个进程，启动时程序会选取3个url交给三个进程执行，剩下的url等待， 等待有空闲的、没有任务的进程执行剩余的任务。
    pool = Pool(3)
    # 将50个url列表页的请求任务放到pool池子中开始执行？
    pool.map(obj.start, [x for x in range(1, 51)])

    # 进程分为主进程和子进程：程序启动的时候，默认就有一个主进程，主进程决定着程序的运行和结束，但是多个进程之间的任务执行是相互之间不影响的，而主进程执行程序的时候，默认不会等待子进程任务的结束，所以主进程会先执行完毕，而子进程的任务比较多，会执行一段时间。

    # 这两句代码就是告诉主进程任务执行完毕之后，要等待子进程中的所有任务执行完毕之后，主进程再退出。
    pool.close()
    pool.join()

    # for x in range(1, 51):
    #     list_html = obj.get_list_page(x)
    #     if list_html:
    #         urls = obj.parse_list_page(list_html)
    #         # print(urls)
    #         for detail_url in urls:
    #             detail_html = obj.get_detail_page(detail_url)
    #             if detail_html:
    #                 obj.parse_detail_page(detail_html, detail_url)
