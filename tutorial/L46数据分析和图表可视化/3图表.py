# 图表
# 常见的图表：条状图、饼状图、点状分布。
# 作用和场景：1. 直观整理信息 ， 支付宝年度账单，阿里云服务器控制台，管理后台。2. 好看、项目出彩。
# 常用图表包：
# 1. pillow、opencv，偏底层，是一些图标包的依赖包。
# 2. matplotlib，知名的图表库，广泛用于图表绘制和科学计算。功能完善，文档复杂。
# 3. chart.js echart，图标库最终要渲染到浏览器中，不少图表库基于js，在python web框架中只要把数据渲染到js图表示例的响应位置，也可以使用js图表库。
# 4. pygal后端pythont图表库，包含常见图表类型，虽然种类不及matplotlib
import pygal

bar = pygal.Bar()
bar.add('等级(单位十位',[11,23,55,59,66,89,156])
bar.render_to_file('3bar.svg')
bar.render_to_png('3bar.png')