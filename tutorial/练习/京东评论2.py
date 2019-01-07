"""
create table if not exits jd {id integer primary key,
 comment varchar(20),create_time datetime}
insert into jd (id,comment,create_time) values (1,2,3)
select * from jd where id=2
update jd set id =3 where id=2
delete from jd where id=1
"""
import requests
import json
from lxml import etree
from CrawlerUtility import ChromeHeaders2Dict
url= 'http://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv32872&productId=7652139&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
new_list = []
html = requests.get(url).text
# d =json.loads(html[27:-2])
# new_list.append(d)
# print(new_list)
dict = json.loads(html[27:-2])
a=dict['comments']
for i in a:
     comment=i['content']
import pymysql
connect = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='trc',db='jddd')
cursor =connect.cursor()

# cursor.execute("""select * from jdcomment""")
# jdcomments = cursor.fetchall()
# print(jdcomments)

# cursor.execute("""create table  jd(id INTEGER PRIMARY KEY ,comment varchar(500))""")
num =1
for i in a:
     print(i['content'])
     cursor.execute('insert into jd(id,comment) values (%s,%s)',[ num ,i['content']])
     num +=1
connect.commit()
