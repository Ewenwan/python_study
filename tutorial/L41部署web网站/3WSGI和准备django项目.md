(了解)通用应用网关接口
========
下面概念了解即可，知道有WSGI这么个东西。 
## 引题
django自带的服务器是单线程的，性能低。
所以主流web框架根据统一规定实现了 通用网管接口。 源代码是一个“应用”，应用防止在专门的服务器容器上。
好像java中源代码和tomcat容器的关系。

## 整体部署流程
1. nginx 做为代理服务器：负责静态资源发送（js、css、图片等）、动态请求转发以及结果的回复；
2. uWSGI 做为后端服务器：负责接收 nginx 请求转发并处理后发给 Django 应用以及接收 Django 应用返回信息转发给 nginx；
3. Django 应用收到请求后处理数据并渲染相应的返回页面给 uWSGI 服务器。


## 协议介绍
### CGI
CGI(Common Gateway Inteface): 字面意思就是通用网关接口，我觉得之所以看字面意思跟没看一样是因为这个称呼本身很学术，所以对于通俗的理解就存在一定困难，这里我觉得直接把 Gateway 当作 server 理解就好。

它是外部应用程序与Web服务器之间的接口标准

意思就是它用来规定一个程序该如何与web服务器程序之间通信从而可以让这个程序跑在web服务器上。当然，CGI 只是一个很基本的协议，在现代常见的服务器结构中基本已经没有了它的身影，更多的则是它的扩展和更新。

FastCGI: CGI的一个扩展， 提升了性能，废除了 CGI fork-and-execute （来一个请求 fork 一个新进程处理，处理完再把进程 kill 掉）的工作方式，转而使用一种长生存期的方法，减少了进程消耗，提升了性能。
## WSGI
WSGI的全称是Web Server Gateway Interface（Web服务器网关接口），它不是服务器、python模块、框架、API或者任何软件，只是一种描述web服务器（如nginx，uWSGI等服务器）如何与web应用程序（如用Django、Flask框架写的程序）通信的规范。

server和application的规范在PEP3333中有具体描述，要实现WSGI协议，必须同时实现web server和web application，当前运行在WSGI协议之上的web框架有Bottle, Flask, Django。
## uwsgi
uWSGI
uWSGI是一个全功能的HTTP服务器，实现了WSGI协议、uwsgi协议、http协议等。它要做的就是把HTTP协议转化成语言支持的网络协议。比如把HTTP协议转化成WSGI协议，让Python可以直接使用。

uwsgi
与WSGI一样，是uWSGI服务器的独占通信协议，用于定义传输信息的类型(type of information)。每一个uwsgi packet前4byte为传输信息类型的描述，与WSGI协议是两种东西，据说该协议是fcgi协议的10倍快。

## 协议选择
uwsgi 底层c，但实际效率优势不大。
基于wsgi协议的gunicorn使用配置简单，我们后面以它为例子。


## django整理成接口形式
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/

## 本节目标
1. 知道django项目由application和通用网关接口两部分组成。
2. 网关接口有wsgi、uwsgi等协议。
3. 我们将要采用基于wsgi的服务器工具gunicorn。
