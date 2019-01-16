import logging

# 介绍
# 记录信息。跟print相比较，功能更为强大，不但可以输出到终端（标准输出），还可以写入文件（相当于with open）。但是格式更规整（时间、做了什么事、正确错误信息）；消息分不同级别，在开发的debug模式显示更多信息，在生产环境显示较少信息；方便日后查阅和分析。

# **消息等级**
"""
严重程度从低到高
debug、info、warning、error以及critical

debug: 用户的请求 ip地址 响应状态码 某一个变量的值  执行的sql ， debug信息最细，适合本地调试，不适合生产环境。
info: 普通线上日志级别。 记录用户访问路由、接口名、报错信息。 方便网站进行分析，分析出用户所在地，哪个页面访问量大，哪个方法出现了错误。
warning：警告，不影响程序运行但不建议。 比如使用了某些快过时的语法，未进行一些设置。
error：程序运行错误。 语法错误 1/0  1+'1', 异常，运行时错误 执行sql时报错。
critical：系统崩溃，无法正常运行。
"""

# **基本例子 输出到文件 、终端
import logging
logger = logging.getLogger(__name__)    # 实例化
logger.setLevel(level = logging.INFO)   # 设置日志级别 ，大于等于这个级别的信息才会输出。
handler = logging.FileHandler("log.txt")    # 设置文件操作器，保存的文件路径
handler.setLevel(logging.INFO)              # 文件操作器的日志写入级别
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   # 设置时间格式
handler.setFormatter(formatter)             # 时间设置载入到文件操作器中

console = logging.StreamHandler()           # 设置另一个操作器 ，标准输出流，以同时打印到屏幕
console.setLevel(logging.INFO)              # 标准输出流的日志级别

logger.addHandler(handler)                  # 文件操作器和标准输出流操作器 插入到logger对象上
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")

# 加载配置
# 把设置抽离到json或yaml文件中

# （了解）回滚、过期删除


# （了解）收集日志，整理、数据可视化




# 参考教程
# https://www.cnblogs.com/liujiacai/p/7804848.html
# https://www.cnblogs.com/CJOKER/p/8295272.html