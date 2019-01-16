import requests
import time, datetime
import logging
import json
import random
from config import COMMENT_REQUEST, COMMON_REQUEST
from model import Comment, CrawlLog

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
logger.addHandler(console)

#
# params = {
#     'productId': 4609652,
#     'page': 0,      # 页码从0开始
#     'pageSize': 10,
#     'sortType': 6,
#     'score': 0,
#     'isShadowSku': 0,
#     # 'fold': 1
# }
#
# for page in range(0, 100):      # jd限制最大请求100页
#     params['page'] = page
#     resp_raw = requests.get(url=COMMENT_REQUEST['url_product_detail'],
#                         params=params, headers=COMMENT_REQUEST['headers'])
#
#     if resp_raw.status_code == 200:
#         # 字符串转对象方便操作
#         resp = json.loads(resp_raw.text)
#         comments = resp['comments']
#         logger.info('当前抓取：{} \n' '返回码：{} \n' '本次条数：{}'.format(resp_raw.url, resp_raw.status_code, len(comments)))
#         # 持久化
#         if comments:
#             comments_value_list = []
#             for comment in comments:
#                 # 判断抓取的评论日期
#                 # if CrawlLog.select().where(comment['creationTime'] <= CrawlLog.create_datetime):
#                 #     logger.info('{}之前日期的评论已抓取过，停止抓取'.format(comment['creationTime']))
#                 # 写评论
#                 try:
#                     row = Comment.create(**comment, _create_time=datetime.datetime.now()) # 官方文档提供了多种批量insert方法，鉴于数据量很小就采用简单循环方式
#                     logger.debug('插入comment表成功，返回行id{}'.format(row._pk))
#                     # try:
#                     #     with database.atomic():
#                     #         Feed.create(**d)
#                     # except peewee.IntegrityError:
#                     #     print('Skipping duplicate')
#                 except Exception as e:
#                     logger.error('写comment表失败，exception:{}'.format(e))
#                 # 写进度
#                 # CrawlLog.insert(**dict(datetime=datetime.now()))
#
#
#         # 无评论跳出
#         if comments is None:
#             logger.info('comments空，跳出循环，第{}页'.format(page+1))
#             break
#         # 持久化评论
#         # 持久化抓取进度
#     elif resp_raw.status_code == 304:
#         # 据说访问过频繁导致304，停顿21s或40s后再访问
#         logger.error('status_code304''url:{}'.format(resp.url))
#         time.sleep(40)   # 防反爬
#         continue
#     else:
#         logger.error('状态码：{}'.format(resp.status_code))
#
#     # 测试 暂时取几页跳出
#     if page == 100:
#         break
#
#     # 页码加1
#     page += 1
#     time.sleep(random.randint(3,5))   # 防反爬

if __name__ == '__main__':
    rs= Comment.select().where(Comment.id == 11483048118).first()
    print(rs)
# psql的一个坑，一个语句错误，下面的死锁都错，解决办法自动commit或用事务
# try:
                            #     with database.atomic():
                            #         Feed.create(**d)
                            # except peewee.IntegrityError:
                            #     print('Skipping duplicate')
# 传入字典设置实例属性
# for i in ['userProvince','userLevelName']:
#     setattr(comments, i, '1')
# print(comments.userProvince)
