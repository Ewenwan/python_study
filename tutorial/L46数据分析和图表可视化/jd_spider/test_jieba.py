import os
import re
import jieba
import jieba.analyse
import pygal
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
from model import *
from dict.degree_dict.degree_dict import DEGREE_ALL
from config import PATH_ROOT, PATH_FONT, WORD_CLOUD_IMG, PYGAL_CHART_IMG

# referenceName相当于商品标题，下面有多种productId=referenceId，爬去一个productId会把所属referenceName下的referenceId的评论都爬下
comment_obj = Comment.select(Comment.referenceName).where(Comment.referenceId == 4609652).first()
referenceName = comment_obj.referenceName
comment_objs = Comment.select().where(Comment.referenceName == referenceName, Comment.content.is_null(False))

# 所有评论内容放到一个字符串中
comment_all = ''
for comment_obj in comment_objs:
    comment_all = comment_all + comment_obj.content
# print(comment_all)

# 分词
cut_words = list(jieba.cut(comment_all, cut_all=False))       # 注意迭代器的不同之处
# print(cut_words[:50])
if not cut_words:
    print('error:jieba cut_words空')

# 过滤停用词
comment_words_clean = []
stop_words = []
with open('./dict/stop_words_zh.txt', encoding='utf-8') as file:
    for line in file.readlines():
        stop_words.append(line.strip())
for word in cut_words:      # for in 和remove连用时注意隔过去元素的问题
    if word not in stop_words and word.strip() != '':
        comment_words_clean.append(word)

# tl算法算分词权重
# tags = jieba.analyse.extract_tags(comment_all,topK=20, withWeight=True) # TF-IDF 算法的关键词抽取

# 统计词频
comment_counter = Counter(comment_words_clean)
word_topn = comment_counter.most_common(100)  # [(word1,10)(w2, 8)]
print(word_topn)

# 词云
word_cloud = WordCloud(max_words=50,
                       font_path=PATH_FONT,     # 不加这一句显示口字形乱码
                       background_color='white',
                       width=600, height=400, margin=0, max_font_size=100,
                       stopwords=STOPWORDS)
word_cloud_text = ' '.join(comment_words_clean)
word_cloud.generate_from_text(word_cloud_text)
word_cloud.to_file(os.path.join(WORD_CLOUD_IMG))

# 积极消极词     # 这里采取简单处理，复杂的参考https://www.cnblogs.com/hd-zg/p/6959971.html
## 分句子
# comment_sentence = []
# for comment_obj in comment_objs:
#     content = comment_obj.content
#     sentence = re.split('\,|，|。|\.|!|！', content)
#     comment_sentence.extend(sentence)
## 程度
# digree_sign = 1 # 肯定1   否定 -1 # 不好处理暂不考虑
digree = 1  # 轻 1\# 中轻 1.5\# 更 2\# 最 2.5\# 非常 3\# 超出 3.5
for word in word_topn:
    if word[0] in DEGREE_ALL:
        print(111)
        digree = digree + 1*word[1]
digree_avg = 1+ digree / len(word_topn)

positive_word_list = []
negative_word_list = []
with open(os.path.join(PATH_ROOT, 'dict/emotion_dict/pos_all_dict.txt'), encoding='utf-8') as file:
    for line in file.readlines():
        positive_word_list.append(line.strip())     # 注意strip('\n')
with open(os.path.join(PATH_ROOT, 'dict/emotion_dict/neg_all_dict.txt'), encoding='utf-8') as file:
    for line in file.readlines():
        negative_word_list.append(line.strip())
positive_word = []
negative_word = []
# 先统计高频词再判断是否落在字典里，节省资源
word_topk = Counter(cut_words).most_common(100)
for word in word_topk:
    if word[0] in positive_word_list:
        positive_word.append(word)
    elif word[0] in negative_word_list:
        negative_word.append(word)
    else:
        pass
print(positive_word)
print(negative_word)    # 只能跑出来数据
## 积极消极词top
## 期望评分  （积极词*出现次数-消极词*出现次数）* 程度指数 /评论数量  程度指数= 程度词*出现数量
emotion_score = 0
for word in positive_word:
    emotion_score += word[1]
k = 100 # 值太小乘个系数
emotion_score = round((emotion_score * digree_avg)/len(comment_objs), 2) * k
print(digree_avg,emotion_score)





