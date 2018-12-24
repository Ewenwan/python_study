
"""
python虚拟解释器环境。
场景：公司不同时期的多个开发项目，使用的python大版本和各个包的版本不尽相同。
每个项目要求有一套让自己成功运行的解释器。一个程序员可能同时开发多个项目。电脑上需要有多套python解释器跟项目一一对应。
解决：我们电脑现在只有一套python解释器，已它基础，虚拟出几个解释器的备份。
老的教材中要先安装virtualenv (虚拟enviorment环境)，因为使用较多，所以py3.4
起官方直接内置了venv包。

(cmd)python -m venv 虚拟环境名       # 创建虚拟环境
创建完发现虚拟环境具备python.exe pip.exe active.bet，Lib库中除了pip包是空的，就好像刚重装完电脑系统。
(cmd) cd 虚拟环境名/Scripts
(cmd) activate.bat                  # 激活虚拟环境
激活虚拟环境后可以pip install跟项目配合的包，python app.py。如果有多个项目，就生成多个虚拟环境一一搭配。好处，实现了项目环境隔离。
"""


"""
pip和venv在pycharm中的简便图形化操作。

ile/settings  project/interpreter 切换解释器或创建新的虚拟环境或切换环境或安装包或更改资源。
"""