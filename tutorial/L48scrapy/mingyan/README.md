README
===
[参考教程 scrapy中文网](http://www.scrapyd.cn/doc/140.html)

## 流程
1. 创建项目`scrapy startproject mingyan`
2. 创建爬虫`scrapy genspider mingyan_spider  mingyan.com`
3. 编码 修改mingyan.spiders.mingyan_spider.py
4. 运行`scrapy crawl mingyan_spider`  根目录下生成.html文件