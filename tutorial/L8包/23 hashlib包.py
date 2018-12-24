# 哈希 hash
# hash ：概括摘要机密算法。一般的加密，比如a-z对应数字1-26，abc的密文为1 abcde的密文为12345。而hash是“摘要”算法，不管1kb的txt文件还是几个G的视频最终都会生成一个固定长度的字符串。
# 常用加密算法：md5  sha128 sha256
# 优点：文件轻度修改最终摘要大幅变化。
"""
场景
1. 校验文件，保证文件被第三方修改。确保下载文件没加入广告或恶意程序。
2. 校验接口参数。api平台app_key和sign签名，如果传输过程中有误或被中间人截取请求修改，那么签名会不匹配，服务器检测到丢弃。
3. 字典，hash表，散列表。hash值作为键名供快速访问。、
4. 把密码以字符串形式存入 黑客就算攻击进去也取得不了密码
"""
import hashlib

md5 = hashlib.md5()
#md5.update('一些文本，特 加密的文件块'.encode('utf-8'))
#md5.update('追加更新内容后的摘要'.encode('utf-8'))
# print(md5.digest())    #'\xbdc\x9c'
md5.update('123'.encode('utf-8'))
print(md5.hexdigest()) # ad81920056cb4ae02e4a01a8b913a1bf
"""
update  比较大的文件可以分为很多块  多次调用update（）
参数为二进制，待摘要信息是字符串的haul先编码
hex digest 生成十六进制 摘要字符串
"""
"""
攻击：穷举 对撞
hash加密并不是绝对安全的
有些喜欢用容易被猜到的密码。
admin 
password
123456
有攻击者根据弱密码字典（10万个弱密码）通过代码生成md5加密，存入一张数据库表。
如果这个黑客窃取了网站的用户表，即使用户表字码存的是密文，跟自己生成的md5做对比，如果对上了，当时就把你钱盗完了
"""
# 小作业 百度 判断输入的字符串是英文还是中文
#作业2：（选做）搜索更多关于hash的知识，算法原理，穷举对撞攻击，加salt的文章。
# 安全性 1  加混合字符串 俗称加盐 salt
salt ='adc'
md5 = hashlib.md5()
md5.update(('password'+salt).encode('utf-8'))
print('md5'+'&'+salt+'&'+md5.hexdigest()) # ad81920056cb4ae02e4a01a8b913a1bf
#  安全性性2  多循环几次  23次已经比较安全
md5 = hashlib.md5()
md5.update('password'.encode('utf-8'))
str1=md5.hexdigest()
md5.update(str1.encode('utf-8'))
str2=md5.hexdigest()
md5.update(str2.encode('utf-8'))
str3=md5.hexdigest
print(str3)
if str3.isgidit:
    print('是纯数字')
else:
    print('不是')
if  str3.isalpha:
    print('是纯')
else:
    print('不是')

"""
加盐后，黑客想要攻击，需要每个弱密码加盐在生成字符串，10万个弱密码。
加盐后没一个盐1*10万行，10*10万行，黑客就很烦
"""
