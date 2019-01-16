from config import DB
from peewee import *

database = PostgresqlDatabase(DB['database'],
                              user=DB['user'],
                              password=DB['password'],
                              host=DB['host'],
                              port=DB['port'],
                              autocommit=True   # 爬虫是循环插入 一条失败后认为当前事务已坏后面的都会失败。所以autocommit或放到事务中。
                              )

class BaseModel(Model):
    class Meta:
        database = database

class Comment(BaseModel):
    """
    所有评论表
    ttps://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv51570&productId=4609652&score=0&sortType=6&page=0&pageSize=10&isShadowSku=0&fold=1
    一些字段意思靠猜，比较重要的字段 content days productColor referenceId
    为方便赋值属性名与返回数据key一致
    postgre数据库默认小写，查询字段含大写字母时加双引号
    """
    comid = AutoField() # Auto-incrementing primary key.
    _create_time = DateTimeField()

    afterDays = IntegerField()  # 评论距离现在几天
    anonymousFlag = BooleanField() # 匿名评论
    content = TextField()
    creationTime = DateTimeField()
    days = IntegerField()  # 购买几天后评论？类似字段afterays
    firstCategory = IntegerField()
    guid = CharField(max_length=100)    # 评论uid
    id = BigIntegerField()     # 用户id或评论id？
    integral = BooleanField()   # 评论完整未折叠？
    isMobile = BooleanField()   # 是否手机用户
    isReplyGrade = BooleanField()   # 回复别人的评论？
    isTop = BooleanField()      # 置顶评论
    mobileVersion = CharField()     # app版本
    nickname = CharField()      # 用户昵称
    orderId = IntegerField()    # 订单id
    plusAvailable = IntegerField    # plus会员状态码？
    productColor = CharField(default='', null=True)      # 商品类型或颜色
    # productSales = []     # 不知道意思一个list
    productSize = CharField()    # 商品尺寸
    recommend = BooleanField()  # 推荐广告商品
    referenceId =  IntegerField() # 每种color和size组合都不一样，相当于sku。爬其中一个id时其它同级别商品的款式颜色组合也会爬下来。但它的父级id并不知道。
    referenceImage = CharField()
    referenceName = CharField()   # 产品名称。每种referenceId都有一样的name
    referenceTime = DateTimeField()     # 商品上架时间？
    referenceType = CharField()     # 商品类型
    referenceTypeId = BigIntegerField()
    replyCount = IntegerField()     # 回复这个评论的评论数
    score = IntegerField()          # 点赞数
    secondCategory = IntegerField() # 二级目录
    status = IntegerField()     # 状态正常的评论？
    thirdCategory = IntegerField    # 三级目录
    title = CharField(null=True, default='')    # 标题是referenceId的父级，极少为空
    topped = CharField()    # 置顶评论
    usefulVoteCount = IntegerField()    # 认为有用点赞
    uselessVoteCount = IntegerField()   # 认为无用点踩
    userClient = IntegerField()    # 发表评论时的设备 id
    userClientShow = CharField()    # 发表评论时的设备 描述
    userExpValue = IntegerField(null=True)   # 用户经验值
    userImage = CharField()     # 头像url
    userImageUrl = CharField()  # 头像url
    userImgFlag = BooleanField()    # 是自定义头像
    userLevelColor = CharField()    # 会员等级 铜牌金牌
    userLevelId = IntegerField()    # 会员等级 id   62金牌
    userLevelName = CharField()     # 会员等级 名称
    userProvince = CharField()      # 用户省份
    viewCount = IntegerField()      # 浏览量


# class Product

class CrawlLog(BaseModel):
    """
    抓取进度
    """
    req_url = CharField()  # 请求url
    product_id = BigIntegerField()     # 参数 商品id
    page = IntegerField()   # 参数 那一次的页码 因为会变动意义不大
    page_num = IntegerField(default=10) # 每页条数
    status_code = IntegerField()    # 状态码
    resp_content = TextField(null=True)      # 返回内容
    create_datetime = DateTimeField(null=True)   # 评论创建时间
    success = BooleanField()    # 抓取成功
    craw_datetime = DateTimeField()     # 抓取时间


class Product(BaseModel):
    """
    商品
    """
    category1 = IntegerField()  # 一级目录
    category2 = IntegerField()  # 二级目录
    category3 = IntegerField()  # 三级目录
    product_id = BigIntegerField(unique=True)
    price = FloatField()
    crawl_comment_num = IntegerField() # 爬去评论数
    emotion_score = IntegerField(default=0)     # 根据积极词频率算出的得分


# creating tables
def create_tables():
    with database:
        database.create_tables([Comment, CrawlLog, Product])


if __name__ == '__main__':
    # 建表
    create_tables()



