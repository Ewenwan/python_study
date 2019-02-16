🦄Gunicorn
===
## 介绍
django自带的单进程单线程服务无法满足多人同时访问的性能。

Gunicorn“green unicorn绿色独角兽”是一个被广泛使用的高性能的Python WSGI UNIX HTTP服务器，移植自Ruby的独角兽（Unicorn ）项目,使用pre-fork worker模式，具有使用非常简单，轻量级的资源消耗，以及高性能等特点。

Gunicorn 服务器作为wsgi app的容器，能够与各种Web框架兼容（flask，django等）,得益于gevent等技术，使用Gunicorn能够在基本不改变wsgi app代码的前提下，大幅度提高wsgi app的性能。
### (了解)原理
参考 [原理](https://blog.csdn.net/jailman/article/details/78496522)
worker
### (不重要)gunicorn WSGI vs uWSGI
https://ivan-site.com/2012/10/gevent-gunicorn-vs-uwsgi/

## 安装
[官网](https://gunicorn.org/#quickstart)
pip3 install gunicorn

## 简单启动
cd /home/yangzheng/jbt_blog/
`gunicorn -w 1 -b 0.0.0.0:8000 jbt_blog.wsgi:application`

## 多进程启动
### 配置
yourproject/gunicorn.conf
```
bind = '0.0.0.0:8000'
workers = 2
daemon = False
proc_name = 'app'   # 进程名
loglevel='info'
#chdir = '/home/yangzheng/jbt_blog/jbt_blog'  #gunicorn要切换到的目的工作目录

#accesslog = "/home/log/gunicorn_access.log"      #访问日志文件
#errorlog = "/home/log/gunicorn_error.log"        #错误日志文件
accesslog = "-"  #访问日志文件，"-" 表示标准输出
errorlog = "-"   #错误日志文件，"-" 表示标准输出
```
worker数量建议cpu核心数*2+1。
配置nginx时，需要将此bind地址写入nginx配置文件中。
daemon = True  下面启动就不用nohup关键字了。

以配置方式启动: cd到项目根目录;`gunicorn -c gunicorn.conf jbt_blog.wsgi`
### nohup和&
目前一个问题是退出程序后命令随之结束无法访问。
参考 https://blog.csdn.net/hl449006540/article/details/80216061
经常连用nohup command & 来让程序一直在后台运行。
### 启动
cd /home/yangzheng/jbt_blog
nohup gunicorn -c gunicorn.conf ttt.wsgi &
### 终止
结束后台运行的程序以释放端口
ps -ef | grep gunicorn  可以看到多个worker进程
kill [pid]


## 参考
https://www.cnblogs.com/nanrou/p/7026802.html
https://blog.csdn.net/y472360651/article/details/78538188
