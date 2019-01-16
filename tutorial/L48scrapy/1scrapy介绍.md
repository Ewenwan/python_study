scrapy
===
scrapy是一个流行的爬虫框架。架构分层，适合复杂项目并易于扩展。封装异步包，实现并发请求和分布式部署。

### 框架架构介绍
类似 L45封装/baike_spider 项目，将爬虫项目分为几个功能层次。

- 引擎（scrapy engine)
处理整个系统的数据流，触发事务。
- 调度器（scheduler ）
接收引擎发过来的请求，压入队列，去重，决定下一次请求的url。
- 下载器（downloader)
根据url请求网页，下载网页原始内容，并将网页内容返回给spiders。（基于twisted,异步请求）
- 爬虫（spiders)
从网页信息中提取实体信息，返回单个实体item。
也可以提取链接供之后爬取。
- 管道（pipeline)
接收单个实体item，好像生产线一样进行加工。
验证item是否有效，持久化数据（写csv或数据库）。

- 下载中间件、爬虫中间件、调度中间件（middle）
上述主要模块无法满足的更细化或更前置的需求。例如django也有中间件，需求：用户进入视图函数前新建数据库连接、验证用户sessionid，请求后要销毁数据库链接。


### 运行流程
1. 引擎从调度器里去一个url待请求
2. 引擎接收到后封装为一个请求，交给下载器
3. 下载器请求网页，返回response
4. 爬虫解析response得到实体item
5. item交给管道进行处理

### 安装scrapy
scrapy依赖包较多，有些包用c写的需要vc编译器。

方法一：anaconda, 自带上千种编译好的科学计算相关包。优点自带编译后的scrapy。缺点：体积大，下载包300m，安装一个多G。主要是科学计算领域，大多数包用不上，flask django又没有需要新下。miniconda是anaconda的精简版本。版本有限。缺少.net会导致无报错失败。
方法二(推荐)：pip install scrapy   哪些包报错需要vc编译器的，再单独去发布编译后的包的网站下载对应平台编译后的.whl文件安装。
参考链接： 
1.第三方编译后包的网站 https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted。
2. 图文教程 https://www.1owo.com/python/python/python-scrapy%E5%AE%89%E8%A3%85%E4%B9%8Bwindows%E7%8E%AF%E5%A2%83%E4%B8%8B/


### 创建项目
创建项目 scrapy startproject [项目名]
根据预设模板创建爬虫文件 scrapy genspider [爬虫名] [域名]
运行爬虫 scrapy crawl [爬虫名]

### 参考教程
1. 入门 mingyan  

