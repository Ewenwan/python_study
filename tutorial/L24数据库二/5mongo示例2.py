from pymongo import MongoClient
from pprint import pprint   # 格式化输出json

class Connect(object):
    @staticmethod
    def get_connection():
        # return MongoClient("mongodb://'127.0.0.1':27017/test")   url写法
        return MongoClient('localhost', 27017)

    # "mongodb://$[username]:$[password]@$[hostlist]/$[database]?authSource=$[authSource]"

print(Connect.get_connection())
client = Connect.get_connection()
db = client.test
# 建立inventory的集合并插入一条文档
db.inventory.insert_one(
    {
        "item": "帆布",
        "quantity": 100,
        "tags": ["棉布"],
        "size": {"height": 28, "weight": 35.5, "uom": "cm"}
    }
)
result_set1 = db.inventory.find({})
for item in result_set1:
    pprint(item)

# 带条件的查询
from bson.son import SON
db.inventory.insert_many([
    {"item": "journal",
     "qty": 25,
     "size": SON([("h", 14), ("w", 21), ("uom", "cm")]),
     "status": "A"},
    {"item": "notebook",
     "qty": 50,
     "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
     "status": "A"},
    {"item": "paper",
     "qty": 100,
     "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": SON([("h", 22.85), ("w", 30), ("uom", "cm")]),
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size" : SON([("h", 10), ("w", 15.25), ("uom", "cm")]),
     "status": "A"}])
# 带条件查询
result_set2 = db.inventory.find({"status": "D"})
for item in result_set2:
    pprint(item)
result_set3 = db.inventory.find({"size.h": 8.5})
# 带操作符的   lt (less than)
result_set4 = db.inventory.find({"qty": {"$lt": 45}})
# 多个条件逗号隔开
result_set5 = db.inventory.find({"status": "A", "qty": 45})

# 更新数据
db.inventory.update_one(
    {"item": "postcard"},       # 条件
    {"$set": {"qty": 50}}       # 设置新值
)

# 删除
db.inventory.delete_one({"status": "D"})    # 参数是条件

# 删除集合
db.inventory.drop()


# 参考
# 一篇中文博客https://www.cnblogs.com/yzrw/p/8286696.html
# 更多复杂查询参考文档https://docs.mongodb.com/guides/或百度。