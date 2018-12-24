# 字符编码
# 引题：在windows资源管理器中新建 含有中文的txt文件，win上的文本文件应用正常打开，但是pytcharm中打开中文乱码
file = open('chinese_gbk.txt','r',encoding='ascii')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

"""
open():  arg1文件名，arg2 模式，encoding 编码。
encoding参数如果没有写，默认随系统，windows系统默认编码为gbk，linux、maci系统上的默认编码为utf-8。

编码 encoding：计算机中存储的是二进制（0,1），我们平时用的看到的是英文字符、中文字符、图片、视频、word文档，所以这些内容需要经过规则转换成二进制才能储存。这个过程叫编码。场景：写文件，传输信息。

解码  decode：解码是编码的逆运算，讲二进制转换为我们平时看到的文字、图片。
本节课讨论纯文本文件的编解码，图片视频word文档的编码规则复杂不讨论。

(了解 为什么二进制)：计算机通过电压高低判断信息，如果电压区间太接近的话（1v 表示1,2v表示2...）,可能由于电压不稳导致数据易出错和检测困难。所以计算机发明者采用二进制表示低电压0和高电压1两种状态。

字节：众多的0、1，为了存储表示方便和更好的可读性，规定每8位二进制数字组成一个字节byte。形如 01010101 。字节是最基本的信息单位。

"""

"""
引题：编码就好像近代战争，传输信息为了保密和易于传输。将原始信息(文明)经过特定规则转换加密信息（密文）。传输密文。友军收到秘闻后按相同规则逆向解读出原始信息。示例'abc'编码→'abc'

编码规则历史:
信息经过编码成二进制再存到硬盘当中。计算机只认识二进制01，基本信息单位是01组成的字节。
首先对容量单位有个大认识，
1byte  = 8bit               一个字节8位 (比特)  形如  01010101   宽带50mbps
1kb = 1000byte              一个几十行的py文件大小为3kb
1Mb = 1000kb                一首mp3歌曲大概5Mb左右
1GB = 1000Mb = 1000000kb    一个电影大概2G左右，固态硬盘大约250G
1TB = 1000G                 一个大容量机械硬盘3Tb

计算机早期内存、硬盘容量小且昂贵。科学家思考，我要在计算机中存储a A 0 1 + 
常见字母、数字、运算符。想出了一套编码方式ascii（美国信息交换标准代码）。
ascii编码：用8位二进制，也就是1byte字节，来表示常见英文大小写、数字定义表示出来。2的8次方一共有256种可能，足够表示出常见字母、数字、运算符、部分特殊符号。例如01100001 代表字母a。

后来计算机渐渐发展，传到了国外，中国、韩国、日本欧洲等。
中国大陆的科学家为了使用计算机，为了存储汉字，也发明了一套编码gbk2312
GB2312：汉字有几万种，一个字节256种排列不够，所以用两个或更多字节存储汉字。这套编码方式可以编两万个汉字。
GB18030：GB2312发现不够用，繁体字特殊字符。所以人们补充新标准，可以编码7万多汉字。
上面两种具体编码方式都属于GBK编码。

与此同时，中国台湾、日本、韩国等等其他国家都研究出了自己国家的编码方式。Erxxx。
全世界有很多套编码方式，自己国家网站和软件可以使用，但跟其他使用时经常由于编解码方式不统一而出现乱码错误，不理软件知识在全世界范围内的沟通交流。编码方式混乱。


出现乱码的原因在于编码和解码不匹配。比如台湾某网站用某编码方式编繁体字，你用电脑打开，电脑默认用gbk解码，由于规则不对应，所以乱码。例如编码规则1  “abc  ...  对应 123...” 编码规则2“abc ...对应567...”,这样信息'abc'经规则1转换后为'123','123'经规则2解码后错误出现乱码。

为了改变这种混乱的编码状况，一个国际组织定义了一套统一的编码方式，Unicode (union)。unicode 编码方式用4到6个字节进行编码。，2的32次方42亿多种可能，可以把所有国家的文字都编码进去，还包括特殊字符（希腊字母、数学字符），还emoji表情图。

但是使用unicode编码后，还有一些问题。一是计算机接收到了4个字节，到底是ascii编码的是4个字符还是unicode编码的1个字母，二是纯英文信息的话，unicode编码占用磁盘体积将是ascii编码的4倍，浪费大。ascii编码的字母a的二进制为01100001，unicode编码兼容ascii编码，字母a第一个字节跟ascii编码一致，其他三个字节填充0，最终unicode编码的a是 00000000  00000000  00000000  01100001。

为了避免上述缺点，提供了几种优化后的存储方式，比如utf-8、utf-16、utf-32。目前最常用的utf-8。
utf-8使用边长1-4个字节存储信息，比如上面unicode编码的a，只存储有用的一个字节，而当遇到中文时，用2-3字节来存储，这样的话既保证兼容，又能以较小的存储空间存储。
unicode是一种编码方式、编码思想，utf-8是unicode一种具体的实现方法。


"""


"""
# py2和py3编码区别
python2 默认ascii编码，如果.py文件中出现中文，系统尝试用ascii去编码范围错误。就汇报超出编码范围错误。
所以要在.py文件第一行需要显示声明编码方式  # encoding='utf-8'-*- encoding:utf-8 -*-

python3 默认unicode编码。程序中字符串其实都先转换成中间产物unicode编码，形如'\u4e2d'。
"""


"""
pycharm相关
设置/editor/file encoding  ,建议保持默认设置或都设置为utf-8。当pycharm打开文件或项目出现乱码时，调整编码方式为gbk或utf-8.
pycharm编辑器中new  file, 用utf-8编码。
"""

"""
编解码错误
1) 文件本身是gbk（windows记事本创建的txt），用utf-8解码
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 position 46
2)文件本身是gbk或 utf-8编码，包含中文，但解码时用ascii
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc8 in position 46: ordinal not in range(128)
3) 尝试用ascii去编码中文，python2中常见错误
UnicodeEncodeError: 'ascii' codec can't encode character '\u4e2d' in position 0: ordinal not in range(128)
"""

"""
关于操作系统：
windows操作系统默认gbk;macOS和linux默认的utf-8。
windows记事本默认gbk；但win上的pycharm
所以平时新建文件建议使用pycharm或sublime。

1）修改源文件：windows记事本另存为的时候可以修改编码为utf-8。
2）修改解码方式：pycharm打开一个gbk文件时会提示reload in gbk。
"""

"""
参考：
1.csdn博客 https://blog.csdn.net/Deft_MKJing/article/details/7946048
2.廖雪峰的教程-编码 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000
"""