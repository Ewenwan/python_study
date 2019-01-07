# coding:utf-8
__author__ = 'trc'

import pymysql
import jieba
from  wordcloud import WordCloud
connect =pymysql.connect(user='root',password='trc', db='jddd')
cursor = connect.cursor()
cursor.execute("""select content from jdjd""")
comment = cursor.fetchall()
print(comment)
list1 = []
for i in comment:
    list1.append(i[0])
# print(list1)
str1 = ''.join(list1)
print(str1)

results =jieba.cut(str1,cut_all=False)
word_list=[]
for r in results:
    word_list.append(r)
print(word_list)
www =' '.join(word_list )
print(www)
font ='msyhbd.ttc'
wc = WordCloud(font_path=font,#如果是中文必须要添加这个
    background_color='green',
    width=1000,
   height=800,
  max_font_size=300,
  min_font_size=50).generate(www)

wc.to_file('京东评论.png')



