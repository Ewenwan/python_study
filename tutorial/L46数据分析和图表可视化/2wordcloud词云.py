# wordcloud词云
# 作用：根据词汇和词频生成一张美观的词汇组成的图片，用于数据可视化。经常与jieba包一起使用。
# matplotlib:绘图库
# 官方仓库(注意)guhttps://github.com/amueller/word_cloud    pip install wordcloud
from matplotlib import pyplot
from wordcloud import WordCloud

string ="""双卡 双待 就 按了 跨 世纪 的萨 达就开 始了 肯德 基啥 代理 四大 皆空"""
string2 ='s dsa d adf dsfd sfdsf ds fdsf fd dff sddfsW'
font ='msyhbd.ttc'
wc = WordCloud(font_path=font,#如果是中文必须要添加这个
    background_color='green',
    width=1000,
   height=800,
  max_font_size=300,
  min_font_size=50).generate(string)

wc.to_file('love.png')
