mongodb
===
## 介绍
mongodb是一个流行的nosql数据库，not only sql，介于非关系型和关系型数据库之间。
比sqlite重，比mysql轻。入门单独低但教程较少，个人程序员和创业公司用的多点。

优点：
1. 读性能高。数据存储在内存中，通过一定策略定期持久化到硬盘。在内存中操作，读操作性能高。
2. 存储结构简单。键值对、字典结构直接存。开发效率高。
3. 可扩展性强，灵活
缺点：
1. 内存开销昂贵
2. 没有事务，不能达到数据强制一致性
3. 不适合较复杂的数据结构

## 选择下载包
官网/get MongoDB/选择版本平台。
exe方便些
zip控制力强。下面以.zip演示。
## 安装
1. 解压zip包
2. 新建c:/programfiles/MongoDB 文件夹
3. 软件根目录下新建 /data/  和 /log/mongod.log
4. 软件根目录下新建 mongod.conf
```
# mongod.conf

# for documentation of all options, see:
#   http://docs.mongodb.org/manual/reference/configuration-options/

# Where and how to store data.
storage:
  dbPath: C:\Program Files\MongoDB\Server\4.0.4\data
  journal:
    enabled: true
#  engine:
#  mmapv1:
#  wiredTiger:

# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path:  C:\Program Files\MongoDB\Server\4.0.4\log\mongod.log

# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1


#processManagement:

#security:

#operationProfiling:

#replication:

#sharding:

## Enterprise-Only Options:

#auditLog:

#snmp:

```
## 开启服务
1. 管理员ps> mongod --config "C:\Program Files\MongoDB\Server\4.0.4\mongod.conf"
可能出现的错误，log文件notfound 经检查路径没错，需要删除原来的log，重新运行服务，服务会自动新建一个新的log文件。
2. ps> mongo          直接登录，默认没有管理员账户和密码。

## mongodb与关系型数据库对比
1. 存储方式。mysql 表格。mongo  json。
2. 什么是json？
json是一种通用的数据传出格式，键值对、字符串。
python字典 {'name':'小红', 'age':13, 'score':90 } ,但这个格式其它计算机其它编程不认识python的键值对格式。需要一个种不同计算机不同语言间传输的通用格式，json。json是键值对形式的字符串。
```json
{
"name": "小红",
"age": 13,
"score":90,
"phone":["66350887", "13733177777"]
}
```
字符串必须要双引号。值可以为字符串、数字、列表、更小的json串
3. database库schema   
4. 表table     集合collection
5. 行row       文档document    
## 驱动

## 示例
