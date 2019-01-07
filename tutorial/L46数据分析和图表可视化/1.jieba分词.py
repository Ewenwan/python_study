# jieba分词
# 这个包的主要作用是把一句话 按照词汇分隔，为后面的词频统计和图片展示打基础

import pymysql
import jieba
results =jieba.cut('潘世瑶是个大傻逼',cut_all=False)
word_list=[]
for r in results:
    print(r)
    word_list.append(r)
print(word_list)

# for  r in results:
#     print('生成器值可以用一次')

print(results) #<generator object Tokenizer.cut at 0x00000278731 750A0>
"""
生成器generator, 参考L4/L5小节。
跟列表相比：
1. 都是可迭代的，被for循环。range(0,10)返回的就是生成器。
2. generator优点用一个取一个，占内存低。
3.  循环后才能看到数据不太直观：数据只能取用一次，如果想
"""
