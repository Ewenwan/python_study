# pip3
"""
pip ：python instsll package ,python三方包管理工具。安装python解释器时已自带。目录已添加到环境变量中。

包管理工具：包是别人写好的代码。经常有这种情况，比如爬虫框架功能的A包，里面引用了负责解析网页的B包，B包引用了更加基础底层的C包，包关系成树装引用。B包依赖C包。直接使用A包，运行报错缺少B包，缺少依赖包。
为了解决依赖包问题，包管理工具出现，主要功能：管理、下载、上传包。解决依赖，安装一个包时会把相关的依赖包都安装好。

pypi：https://pypi.org/  是查找、安装、发布python包的一个平台。pip工具默认从pypi下载包。
"""
"""
pip list     # 输出安装过的三方包的列表。
pip search 关键字    # 搜索包含关键字的包名。
pip install  包名    # (常用)安装包。 安装包的本质是从pypi下载，解压复制到C:\Python36\Lib\site-packages 下。默认安装包的最新版本。
pip install requests==2.19.0   #安装指定版本的包
pip nuintall 包名      # 卸载包

"""

"""
批量备份和安装
pip freeze > requirement.txt        # 讲解释器中的包和版本导出到一个文件中
pip install < requirement.txt       # 根据requirement.txt 的信息批量安装对应版本的包。
"""


"""
pip安装速度慢的问题：
因为服务器在国外，为了改善这个问题，国内一些厂商或大学做了pypi网站的镜像。
国内的镜像站豆瓣源、网易源。
常用国内源：
豆瓣：http://pypi.douban.com/simple/ 
清华：https://pypi.tuna.tsinghua.edu.cn/simple

临时：pip install -i http://pypi.douban.com/simple/ pillow
永久修改（推荐)：C:/Users/用户名 下，新建pip文件夹下新建pip.ini写入下面两行
[global]
index-url = https://pypi.douban.com

"""

"""
python虚拟解释器环境。
场景：公司不同时期的多个开发项目，使用的python大版本和各个包的版本不尽相同。
每个项目要求有一套让自己成功运行的解释器。一个程序员可能同时开发多个项目。电脑上需要有多套python解释器跟项目一一对应。
解决：我们电脑现在只有一套python解释器，已它基础，虚拟出几个解释器的备份。
老的教材中要先安装virtualenv (虚拟enviorment环境)，因为使用较多，所以py3.4起官方直接内置了venv包。

(cmd)python -m venv 虚拟环境名       # 创建虚拟环境
创建完发现虚拟环境具备python.exe pip.exe active.bet，Lib库中除了pip包是空的，就好像刚重装完电脑系统。
(cmd) cd 虚拟环境名/Scripts
(cmd) activate.bat                  # 激活虚拟环境
激活虚拟环境后可以pip install跟项目配合的包，python app.py。如果有多个项目，就生成多个虚拟环境一一搭配。好处，实现了项目环境隔离。

"""

"""
可能出现的错误：
1. 红字错误。没有适合系统的安装包。跟C C++相关的库。
1. 拒绝访问 。 权限问题，使用管理员权限的终端运行。
2. 最后黄字警告。 pip版本升级提示，可以忽略。
3. 黄字警告。 pip所在的目录没有添加的环境变量中。
3. requirement already satisfied 。之前已经成功安装过此包了。
4. cache   缓存。之前已经下载过安装包，再次安装时不会再从网上下载。
"""
"""
另外安装方法：
1. 源码安装。从github  包的主页/releases  找到source code。解压 cd到解压后的根目录。
python setup.py install
优点：适合任何操作系统和python版本。缺点：有些包源代码调用了c++代码，但本机没有c++编译器，编译报错。
2. wheel文件安装。wheel文件是有人已经安装好c++编译器，根据操作系统和python版本编译好这种平台上课运行的2进制。
pip 安装好的包实际上就是平台为我们准备好的适合当前操作系统和python版本的。wheel文件
pypi

"""

