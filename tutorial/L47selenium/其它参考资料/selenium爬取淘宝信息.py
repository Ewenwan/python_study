# coding:utf-8
# __author__ = 'Gao'
import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.taobao.com/')

# 获取输入框，输入 “笔记本电脑”
driver.find_element_by_id('q').send_keys(u'笔记本电脑')

# 定位搜索按钮
driver.find_element_by_class_name('btn-search').click()

# 循环爬取前两页商品信息
for page in xrange(1, 3):
    print '正在获取第{}页数据...'.format(page)

    # 定期将滚动条进行向上滚动
    # (1, 11, 2): 从1开始循环，每隔两次循环一次，x的值[1,3,5,7,9]
    for x in xrange(1, 11, 2):
        # 根据x循环的值以及整个页面的高度，计算需要滚动的比例
        i = float(x)/10
        print 'i == ',i
        # document.documentElement.scrollHeight: 获取可滚动页面的整体高度
        # document.documentElement.scrollTop：每次滚动距离最上边的高度
        js = "document.documentElement.scrollTop = document.documentElement.scrollHeight * %f"%i

        driver.execute_script(js)

        # 浏览器每滚动一次，休眠一下，让后面的代码下载商品信息
        time.sleep(3)

    # 获取包含商的div
    shops_list = driver.find_elements_by_class_name('grid-item')
    for one_shop in shops_list:
        with open('shop.txt', 'a') as f:
            f.write(one_shop.text.encode('utf-8'))
            f.write('\n')


    # 定位到下一页，并点击
    driver.find_element_by_link_text(u'下一页').click()

print('数据爬取完毕！')
driver.quit()

# selenium爬取小说，自然风光图片，豆瓣电影，自动登录知乎。
