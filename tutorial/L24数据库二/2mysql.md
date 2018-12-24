mysql
===
file 文件 edit 编辑 view看法 query 查询 tools工具
server 服务器
## 介绍
流行的关系型数据库。
describe pet; 展示表
## 安装
### 选择安装包
www.mysql.com / download（下载）/ community（社区版）/ mysql server(服务器)
打开下载页后  operating system（选择操作系统）  选microsoft windows（微软windows系统）
- msi microsoft windows installer 也就是.exe安装包。好处 有安装向导，自动添加环境变量，自动生成配置文件，自动注册windows服务。
- zip archive  也就是.zip压缩包。包含mysql主要文件，但跟windows结合部分 环境变量、服务就需要手动建立。好处是版本最新，控制力强。本课使用.zip。
点download，点no thanks不登录就开始下载。
### 安装
1. 新建文件夹C:\Program Files\MySQL    允许权限
2. .zip安装包解压至刚才新建的文件夹。报解压错误，原因无权限。解决先解压到D盘，然后剪切至目录，弹窗时允许权限。

## 开启服务
1. 介绍mysql工程的主要文件夹和文件作用。
- bin文件夹。可执行二进制程序。客户端mysql.exe, 服务端mysqld.exe， 备份mysqldump.exe
- data。存放具体的数据。
2. my.ini 。 数据库服务启动时的默认配置文件，定义了mysql目录，引擎，字符集，日志等关键信息。需要手动建立。
3. 初始化data文件夹和生成root密码。 mysqld --defaults-file=C:\my.ini --initialize --console
成功后注意记住生成的随机root密码。data文件夹下可以看到许多文件。
可能出现的错误--initialize specified but the data directory has files in it. Aborting.解决删除data下文件。管理员cmd下重新命令。
4. 开启服务  mysqld --console   。出现3306等字样成功，窗口不要关闭。
可能出现的错误，找不到data路径，检查第2、3步。
管道命名错误，极少人出现，需要my.ini添加配置enable-named-pipe。
5. 客户端登录 mysql -u root -p刚才生成的密码
可能出现的错误 ERROR 2003 (HY000): Can't connect to MySQL server on 'localhost' (10061)   说明服务器没有启动。
6. 登录进去后改密码。 ALTER USER "root"@"localhost" IDENTIFIED  BY "新密码";     
\q退出后可以用mysql -u root -p 重新登录。
7. 注册windows服务  mysqld --install MySQL80 --defaults-file="C:\my.ini"
### exe安装
可能会出现缺少c++ runtime distribute情况。
### 卸载
win删除服务  管理员cmd sc delete 服务名
## sql操作

## 驱动

## 示例


## 作业
1. （课下）很多公司仍在使用5.x版本。安装mysql5.x版本，启动5.x版本服务器，新建student表，进行insert拆入操作，值要包含中文。会报错。上网搜索原因，修改配置文件。
2. ：由于很多公司还使用navicat，课下尝试用它来连接，由于mysql8.0登录验证新增加密方式，navicat无法直接连接。网上百度解决方案（把密码验证方式修改为旧方式）
3. ：预习更多的sql语法http://www.w3school.com.cn/sql/sql_join_full.asp

