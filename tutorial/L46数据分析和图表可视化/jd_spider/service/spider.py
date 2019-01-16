import requests
import time
from datetime import datetime
import json
import random
from config import COMMENT_REQUEST, COMMON_REQUEST
from model import Comment, CrawlLog


class Crawler(object):
    @classmethod
    def crawl_comment(cls, app=None, product_id=0, page_start=0):
        """ 抓评论
        :arg
        :return '抓取完成详见日志'
        """
        success_num = 0
        app.logger.debug('开始抓取评论，product_id:{}'.format(product_id))

        # url默认参数
        params = {
            'productId': product_id,     # 7位数字
            'page': page_start,           # 页码从0开始
            'pageSize': 10,
            'sortType': 6,
            'score': 0,         # 0 全部评价
            'isShadowSku': 0,
            # 'fold': 1
        }

        # 循环页数，jd限制最大请求最近100页
        for page in range(page_start, 100):
            params['page'] = page
            resp_raw = requests.get(url=COMMENT_REQUEST['url_product_detail'],
                                params=params, headers=COMMENT_REQUEST['headers'])

            if resp_raw.status_code == 200:
                resp = json.loads(resp_raw.text)    # 字符串转对象方便操作
                comments = resp['comments']
                app.logger.info('本次请求start，抓取：{} \n' 'page{}、 条数{} , 返回码：{}'.format(resp_raw.url, page+1, len(comments), resp_raw.status_code))

                # 持久化
                app.logger.info('持久化..')
                if comments:
                    write_num = 0
                    for comment in comments:
                        # 判断是否抓取过，是的话请求下一页或跳出循环，可能会少爬几条

                        if Comment.select().where(Comment.id == comment['id']).first() is not None:
                            app.logger.warning('comment.id={} creationTime={}的评论已抓取过,跳过'.format(comment['id'], comment['creationTime']))
                            continue
                        try:
                            # 写评论
                            row = Comment.create(**comment, _create_time=datetime.now()) # 官方文档提供了多种批量insert方法，鉴于数据量很小就采用简单循环方式
                            success_num += 1
                            write_num += 1
                            app.logger.debug('本次请求end，插入comment表，成功条数{}，返回行id{}'.format(write_num, row._pk))
                            # 写日志
                            crawl_log = dict(success=True, req_url=resp_raw.url, product_id=product_id, page=page+1,
                                               status_code=resp_raw.status_code, resp_content=resp_raw.text,
                                               create_datetime=comment.get('creationTime', ''), craw_datetime=datetime.now())
                            CrawlLog.create(**crawl_log)
                        except Exception as e:
                            app.logger.error('异常exception:{}.\n comment creationTime{}'.format(e, comment['creationTime']))
                            # 写日志
                            crawl_log = dict(success=False, req_url=resp_raw.url, product_id=product_id, page=page + 1,
                                             status_code=resp_raw.status_code, resp_content=resp_raw.text,
                                             create_datetime=comment.get('creationTime', ''),
                                             craw_datetime=datetime.now())
                            CrawlLog.create(**crawl_log)

                # 无评论跳出
                else:
                    app.logger.info('第{}页comments空，跳出循环，\n 抓取终止'.format(page+1))
                    # 写日志
                    crawl_log = dict(success=False, req_url=resp_raw.url, product_id=product_id, page=page,
                                     status_code=resp_raw.status_code, craw_datetime=datetime.now())
                    break
            elif resp_raw.status_code == 304:
                # 据说访问过频繁导致304，停顿21s或40s后再访问
                app.logger.error('status_code304''url:{}'.format(resp.url))
                # 写日志
                crawl_log = dict(success=False, req_url=resp_raw.url, product_id=product_id, page=page,
                                 status_code=resp_raw.status_code, resp_content=resp_raw.text,
                                 create_datetime=datetime.now(),
                                 craw_datetime=datetime.now())
                time.sleep(40)   # 防反爬
                continue
            else:
                app.logger.error('产品id{}，url{}抓取请求失败，状态码：{}'.format(product_id, resp.url, resp.status_code))

            # 测试 暂时取几页跳出
            if page == 100:
                break

            # 页码加1
            page += 1
            time.sleep(random.randint(3,5))   # 防反爬

        app.logger.info('本次共请求{}页，成功写入评论{}条'.format(100-page_start, success_num))
        return '抓取完成，详见日志'



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



# for i in ['userProvince','userLevelName']:
#     setattr(comments, i, '1')
# print(comments.userProvince)
