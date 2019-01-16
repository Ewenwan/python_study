import requests
import time
from datetime import datetime
import logging
import json
import random
from config import *
from model import Comment, CrawlLog, Product




class Category(object):
    @classmethod
    def get_third_category_product_list(cls, app=None, category_name='', page=0, item_per_page=0):
        """ name下包括多个referenceId，referenceId由referenceName和color决定
        首页的list接口不好分析，Product表信息不全，所以查询comment表找关系。"""
        category1 = category2 = category3 = 0
        for c in CATEGORY:
            if c['name'] == category_name:
                category1, category2, category3 = c['category']
                sql= '''select c."referenceName", c."referenceId", min(c."referenceImage") as "referenceImage", c."productColor",c."productSize" from product as p inner join comment as c on p.product_id=c."referenceId"
                        where p.category1=737 and p.category2=794 and p.category3=798
                        group by c."referenceName", c."referenceId",c."productColor", c."productSize"
                        order by min(c.comid);
                     '''
                comment_objs = Product.raw(sql)

                product_list = [{'name':'', 'image':'', 'types':[{'product_id':0,'color':'','size':''}]} ]
                for obj in comment_objs:
                    last_product_name = product_list[-1].get('name', '')
                    if obj.referenceName != last_product_name:
                        product_list.append(dict(name=obj.referenceName, image=PRODUCT_IMAGE_PREFIX+obj.referenceImage, types=[]))
                    product_list[-1]['types'].append(dict(product_id=obj.referenceId, color=obj.productColor, size=obj.productSize))
                product_list = product_list[1:]
        app.logger.debug('third_category_product_list {}'.format(product_list.__str__()))
        return product_list