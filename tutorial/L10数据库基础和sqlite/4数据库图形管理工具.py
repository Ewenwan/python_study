# 数据库图形管理工具
"""
## 常用数据库图形管理工具
1. navicat系列    navicat for sqlite
优点navicatForMysql用户多 表多的时候界面方便，缺点一是付费二是体验一般。
2. datagrip     ，jetbrains出品，优点一个软件连接多个数据库；操作习惯跟pycharm类似；pycharm pro集成。缺点用户少；驱动不好下。

"""

"""
（了解）datagrip操作方法（pycharm集成database工具为例子）：
1. pycharm左下角图标调出工具栏，打开pycharm右侧Database工具。
2. 点加号-DataSource数据源-sqlite  。
3. 弹出的对话框选择 drivers-sqlite(Xerial)  
4. 点击download sqlite-jdbc[latest]  
5. 如果网速不好的话 下载sqlite-jdbc-3.20.1.jar 。对话框+号-custom jars 从本地安装
6. 驱动安装成功后点击apply应用

7. 点击对话框 project data source ，开始配置连接数据库的实例
8. File路径点击 ...图标，选择要连接的.db文件。
9. 点test connection， seccessful为成功
10. 点击ok退出。看到连接的数据库实例下有表。


（了解）
JDBC：java操作数据库的驱动包。因为pycharm 、datagrip是用java开发的。
"""

"""
（了解）database工具使用：
展开目录，找到 表。
schemas 模型，理解为大的仓库，默认有一个仓库main，main仓库下是我们建的表。
sqlite_masters是数据库系统内置表，不用关注它，不能删除。
不用关注collations文件夹。
双击表查看表数据。
图形化界面 加减号增加修改数据，注意修改完需要submit提交。
点击console图标，打开sql命令行工具，可以在里面写sql语句，点击execute按钮执行，得到结果集。
选中库，右键new-table，可视化界面创建表。
实例右键 database-tools - manage shown schema  
工具会自动提交。
"""

"""
作业一（课下）:课下下载navicat for sqlite，破解，连接数据库
作业二（课下): 课下下载datagrip ，破解，连接数据库 。http://www.jetbrains.com/datagrip/?fromMenu
作业三：连接上sqlite数据库，尝试新建表、新建字段、删除表。
"""
