# coding:utf-8
# __author__ = 'Gao'

import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///C:/Users/Administrator/Desktop/1-17/am/wanmeishijiexiaoshuo/index.htm')

# 先获取第三个class='bg'的div
divs = driver.find_elements_by_css_selector('.bg')
main_div = divs[2]

# 找到序章对应的a标签，并点击进入序章的详情页面
a = main_div.find_element_by_css_selector('a')
a.click()

# 进入到序章详情页面
while True:
    # 定位小说的正文内容
    content = driver.find_elements_by_css_selector('.content p')
    content_string = ''
    for c in content:
        text_string = c.text.encode('utf-8')
        content_string += text_string
    # 定位小说章节标题
    name = driver.find_element_by_css_selector('.bg>h1').text
    print '开始获取{}章节内容...'.format(name.encode('utf-8'))

    # 打开文件将正文内容写入到文件
    with open('novel.txt', 'a') as f:
        f.write(name.encode('utf-8'))
        f.write('\n')
        f.write(content_string)
        f.write('\n\n')

    # 定位下一页的a标签，点击
    try:
        driver.find_element_by_css_selector('a[rel="next"]').click()
    except Exception, e:
        print '下载完成！'
        break



