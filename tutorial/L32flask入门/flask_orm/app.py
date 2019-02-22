from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 数据库连接通用接口：是由用户名密码配置信息组成的单行类似网址的URI。
# 数据库驱动名://用户名:密码@服务器ip:端口/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:56tyghbn@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


db.create_all()     # 根据类生成表
if __name__ == '__main__':
    app.run()



"""
python console中插入数据

from app import db
C:\Python36\lib\site-packages\pymysql\cursors.py:170: Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 519")
  result = self._query(query)
from app import User
user1 = User(username='小明', email='xxx@qq.com')
user2 = User(username='小红', email='xxsk@qq.com')
db.session.add(user1)
db.session.add(user2)
db.session.commit()
"""


"""
作业（课外）：
1.字段类型，表连接
2.各种查询 排序 分组 连接
3.表修改和数据迁移
"""