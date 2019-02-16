安装python解释器
===
##目标
安装成功python解释器


##准备
1.windons资源管理器
显示文件后缀名和显示隐藏文件。后缀：.txt、.word、.py

##（了解）版本选择
Python 3.7.0
三位数字分别表示 大版本、小版本、小小版本
我们用的是python3版本
小小版本数字尽量大


b表示beta测试版本：rc待发布版本；什么都不加的是正式版本。我们选择的是正式版本。

我们选择较新又正式的版本。

Windows  x86表示32位。x86-64或amd64表示64位。

wed-based在线安装；executable 可执行安装程序.exe;zip压缩包。我们选择.exe.

最终选择为python3.6.-x86-64.exe

##安装
1、打开exe
2、勾选“add  python  to  path”、选择自定义安装
3、optional  features 全选
4、advanced ooption  勾选 “add python to environment variables”。
install安装，成功后close对话框。

##安装目录下的文件夹的作用
-document  文档、说明书
-library   库
-Scripts 脚本
-python.exe   python解释器的入口
-python。exe 编译

##helloworld
1、双击python.exe  打开python交互式命令行。命令行：非图形化的控制界面。交互式：事实运行我们键入的代码，特点以“>>>”开头。
2、键入“print（“hello  world”）”，回车。注意需要英文字符。

##cmd与环境变量
1、打开Windows的终端（cmd）。
win7用户  开始/附件/命令提示符；win10用户  开始/Windows系统/命令提示符

快捷键win+r开始运行。输入“cmd”回车 打开命令行。


##（了解）环境变量
1.windows的环境变量就是一些配置，系统启动时会加载这些配置。
2。环境变量的系统变量是全局的。用户变量是个性化的。
3.环境变量path有一点像桌面快捷方式。里面记录着一些路径，分号分隔，当我们在命令行当中执行一个xxx.exe程序的时候，系统会查找这些路径，有这个程序的时候，就会调用。
4.如果python安装时没有添加环境变量，为了使用方便需要手动添加。
5.安装完python解释器或修改后需要重启电脑生效。（课下）不重启电脑环境变量生效。


##windows  cmd终端与python解释器
1.windows  cmd终端：跟windows操作系统有关，比如ping命令。特点是“路径>”.
2.python交互式终端：专门运行python代码命令的。特点是“>>>”.
3.windows终端键盘键入“python”进入python终端。
python终端 键入“exit()”退回到windows终端。


##（重点）两种运行代码的方式
1.交互式解释器。优点反馈快。缺点是不适合编辑大型文件。
2.在.py文件中编辑我们的代码。运行方式：windows终端下。
“python hello.py”。优点适合编辑大型文件。