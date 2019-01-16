import pygal
from config import PYGAL_CHART_IMG


# 图表
# 高频top20 bar；积极频次10；用户评论活跃时间；商品购买比例；
# 消极频次  差评率仅占2%，消极词语往往连成句子，不容易被字典判断出来。
# 三个月购买量趋势  无法完成，两天评论量都一百页了，最多采集一百页。

word_frequency = [('不错', 156), ('电视', 138), ('买', 102), ('小米', 92), ('送货', 59), ('非常', 58), ('安装', 51), ('挺', 49), ('清晰', 48), ('快', 46), ('满意', 43), ('很快', 40), ('喜欢', 40), ('服务', 39), ('东西', 39), ('师傅', 37), ('性价比', 37), ('说', 33), ('高', 32), ('速度', 32), ('物流', 30), ('价格', 25), ('质量', 23), ('比较', 22), ('便宜', 21), ('支持', 21), ('产品', 20), ('没', 20), ('收到', 20), ('问题', 19)]
line_chart = pygal.Bar()
x_labels = [word[0] for word in word_frequency]
y_values = [{'value': word[1], 'color':'green'} for word in word_frequency]
# line_chart.x_label_rotation = 20  # 中文短字旋转后效果并不好
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, x_labels)
line_chart.add('频次', y_values)
# line_chart.render()   # 当前目录下生成svg
line_chart.render_in_browser()  # 需要lxml包
line_chart.render_to_file(PYGAL_CHART_IMG)