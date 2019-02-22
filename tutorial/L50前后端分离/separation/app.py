from flask import Flask, render_template
import time
import json

app = Flask(__name__)

ARTICLE_CONTENT = """
前后端分离开发
巴拉巴拉巴拉巴拉
巴拉巴拉巴拉巴拉
巴拉巴拉巴拉巴拉
巴拉巴拉巴拉巴拉
"""

COMMENT_LIST = [
    '好顶赞',
    '评论2',
    '评论3',
    '评论4',
    '评论5',
    '评论6',
]




@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/article_sync/<int:article_id>')
def article_sync(article_id=1):
    """ 传统同步 """
    # 读取数据库(0.5秒)    网络传输(3)   刷新 浏览器解析html(0.5)
    time.sleep(4)
    return render_template('article.html', article=ARTICLE_CONTENT, comment_list=COMMENT_LIST)

@app.route('/comments')
def comments():
    """ 前后端分离，配合前端js异步请求,获取评论列表 """
    # 测试时需要手动增加评论数据。可以看出局部刷新体验更好。
    # 读取数据库(0.5秒)    网络传输(1)   刷新 浏览器解析html(0.5)
    time.sleep(2)
    print(json.dumps(COMMENT_LIST))
    return json.dumps(COMMENT_LIST)

if __name__ == '__main__':
    app.run()
