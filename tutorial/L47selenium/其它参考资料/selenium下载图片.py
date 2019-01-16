# coding:utf-8
# __author__ = 'Gao'

# phantomJS: selenium+phantomJS实现动态网站数据的爬取。该工具被称为幽灵浏览器，也可以像浏览器一样去渲染JS加载的页面，只不过没有界面。运行速度比启动客户端又快一些。

# 注意：phantomJS解析的动态网页源码可能会存在和Firefox()客户端解析的动态网页源码不一样的情况。

# 通过cmd命令 phantomjs -v 查看是否安装成功。出现版本号则可以正常使用了。

# 当使用Phantomjs进行验证码截图时，如果出现整张大图中有验证码，但是截取出来的验证码小图是不显示的，是因为像素问题导致的。
# driver.maximize_window() # 火狐浏览器适用


import time, os
import shutil
from urllib import urlretrieve
from selenium import webdriver


class ImagesDownload(object):
    def __init__(self):
        self.base_url = 'http://www.ivsky.com/tupian/ziranfengguang/'
        self.page = 1
        # 由于图片的下载只需要创建一个浏览器对象即可，将对象的创建放到初始化函数中。
        self.driver = self.get_driver()

    def get_driver(self):
        driver = webdriver.PhantomJS()
        try:
            driver.get(self.base_url + 'index_' + str(self.page) + '.html')
        except Exception,e:
            print '加载首页数据失败，原因：',e
        else:
            print '加载首页数据成功'
            return driver

    def create_directory(self, directory_name):
        if os.path.exists(directory_name):
            print directory_name + u' 目录已经存在了'
            shutil.rmtree(directory_name)
        os.mkdir(directory_name)
        os.chdir(directory_name)

    def dowmload_img(self):
        # 定位到每一张图片元素，取出src图片地址用于下载，取出alt属性用于创建文件夹
        imgs_list = self.driver.find_elements_by_css_selector('.il_img img')
        for img in imgs_list:
            src = img.get_attribute('src').encode('utf-8')
            alt = img.get_attribute('alt')
            self.create_directory(alt)
            urlretrieve(src, 'fengjing.png')
            os.chdir(os.path.pardir)
        # 定位下一页
        try:
            # print self.driver.page_source
            next_page = self.driver.find_element_by_css_selector('.page-next')
            # print next_page
        except Exception, e:
            print '已经是最后一页了'
            # 最后一页：退出浏览器，同时结束当前函数的执行。
            self.driver.quit()
            return
        else:
            # 取出下一页的url
            next_url = next_page.get_attribute('href').encode('utf-8')
            self.driver.get(next_url)
            self.dowmload_img()


if __name__ == '__main__':
    img = ImagesDownload()
    img.dowmload_img()
