# pillow例子2 随机生成验证码
"""
(了解)RGB：red green blue 色光三颜色，(11,225,5)

"""
from PIL import Image, ImageDraw,ImageFont,ImageFilter
import random

# 随机字母
def random_char():
    return chr(random.randint(65,90))
# 随机数字
def random_num():

    return random.randint(0,9)

# 随机字体颜色  稍深
def random_color():
    return (random.randint(150,255),random.randint(150,255),random.randint(150,255))

# 随机背景颜色
def random_color2():
    return (random.randint(30,120),random.randint(30,120),random.randint(30,120))

# 生成空白背景图层
image = Image.new('RGB',size=(240,60),color=(255,255,255))
# 生成绘制对象
draw = ImageDraw.Draw(image)
# 字体对象 ， 字体、 字号
font = ImageFont.truetype('arial.ttf', 36)

# 循环像素并填充颜色
for x in range(0,240):
    for y in range(0,60):
        draw.point(xy=(x, y), fill=random_color2())
# 生成文字
for t in range(0,4):
    draw.text((60*t+20, 10),random_char(), font=font, fill=random_color())
# 加模糊滤镜
image = image.filter(ImageFilter.BLUR)

# 保存
image.save('demo4.jpg','jpeg')



# 作业：追加需求
"""
1. 在github上搜索关键字“生成验证码”，查看学习别人生成验证码的流程。拷贝一份别人的实现并成功运行。
2. 绘制文字时纵坐标更凌乱
3. 添加干扰斜线或虚线
4. 文字扭曲效果，猜测跟滤镜相关，百度“pillow滤镜”“PIL文字 扭曲”
5. 背景干扰点
6. 文字为中文。C:/windows/fonts 文件夹下找找微软雅黑字体。
7. 字体粗细、大小混排。
8. 文字轻度旋转(-30度到30度)
9. 把一张风景图作为实验码的背景。
"""

"""
作业二：表情图和文字合成
用一个变量存储文字
打开素材图image对象
生成绘制对象draw
draw.text() 绘制文字并生成图片
追加：多找几个模板，批量生成多个图片，每次合成的图片放到一个文件夹中。
"""