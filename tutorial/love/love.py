
# 导入相应的Python包
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
# 读取需要可视化的数据 ，这边是以文件的形式存储数据。此处也可以从数据库提取数据的方式
f=open("./oo.txt", encoding="utf-8")
word_space_split=f.read()
# 提取图片，最后的数据以该图片的形状展示
coloring=np.array(Image.open("./love.png"))
my_wordcloud=WordCloud(background_color="white",
			max_words=120,
			mask=coloring,
			max_font_size=40,
			min_font_size=5,
			random_state=42,
			scale=1,
			font_path="./arial.ttf").generate(word_space_split)  # 注：song.ttc  设置展示的图文的字体
image_colors = ImageColorGenerator(coloring)
plt.title=("Distant savior")
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.figure()
plt.axis("off")
plt.show()



