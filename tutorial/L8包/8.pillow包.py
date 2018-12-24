# pillow包
# pillow：(了解)（python image library）是一个有关图像图片处理的包，这个包底层用的C C++，但PIL包是python2下使用。所以有更新了一个适合python3版本的、基于PIL包的新包pillow。
# 像素：1440*900 1080p  ， 显示器图像的最小色彩单位。

from PIL import Image,ImageFilter

im = Image.open('demo.jpg')
print(im.size)
width,height = im.size
print(width,height)
# 缩放
im.thumbnail( (100, 100) )
# 保存为新图片
im.save('demo2.jpg','jpeg')
# 旋转
im2 = im.rotate(90)
im2.show()      # 临时打开
# 滤镜
im3 = im.filter(ImageFilter.GaussianBlur.BLUR)
im3.show()
# 保存
