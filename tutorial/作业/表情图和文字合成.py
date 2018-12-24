from PIL import Image, ImageDraw, ImageFont
img = Image.open("dami.png")
draw = ImageDraw.Draw(img)#生成绘制对象draw
typeface = ImageFont.truetype('simhei.ttf', 18)

# darw.text()回执文字并生成图片
draw.text((60, 150), "哇，你真好看", fill=(120, 0, 60),
font=typeface)
img.show()
img.save("斗图小组.png")# 保存


