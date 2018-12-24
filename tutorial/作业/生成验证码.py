#
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
#
# im1 = Image.open('biu.jpg')
# im1.thumbnail((300,300))
# im1.save('biu2.jpg','jpeg')
# im=Image.open('biu2.jpg')
#
# # 返回随机大写字母
# def random_char():
#     return chr(random.randint(65,90))
#
# # 返回随机rgb色值
# def random_color():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
# # 返回随机浅色
# def random_color2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
#
# # 字体对象，字体，字号
# def random_font():
#     return ImageFont.truetype('arial.ttf', random.randint(30,60))
#
# # 绘制对象
# draw = ImageDraw.Draw(im)
#
#
# # 生成文字
# for t in range(0, 4):
#         draw.text((45*t+15, 35), random_char(), font=random_font(),fill=random_color2())
#
# # 生成验证码图片
# im.save('背景变化版.jpg', 'jpeg')
# print('保存成功')




