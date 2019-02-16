import time
import json
from flask import Flask, render_template

app = Flask(__name__)

ARTICLE_CONTENT = """
前后端分离开发。。。
巴啦啦巴啦啦巴拉巴拉
巴啦啦巴啦啦巴拉巴拉
巴啦啦巴啦啦巴拉巴拉
巴啦啦巴啦啦巴拉巴拉
"""
COMMENT_LIST = [
    '好顶赞',
    '巴拉巴拉是什么意思？',
    '路过。。',
    '路过2。。',
    '路过3。。',
]
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/article_sync/<int:article_id>')
def article_sync(article_id=1):
    """ flask django本来的方式 """
    # 优点 只用后端语言加基础前端知识就能开发出
    # 缺点 当有新评论时不知道，只能刷新网页，但会全部刷新浪费加载时间。
    # 用sleep模拟请求图片资源和网络的加载时间（3s ，这部分时间可能较长且影响体验）和读数据库时间（0.5）和浏览器解析渲染时间（0.5）。
    time.sleep(4)

    return render_template('article.html', article=ARTICLE_CONTENT, comment_list=COMMENT_LIST)

@app.route('/article_async/<int:article_id>')
def article_async(article_id=1):
    """ 跟上面的函数一样，只不过专门提供前端js发起的请求 """
    time.sleep(1)   # 读数据库时间（0.5）和浏览器解析渲染时间（0.5）。
    return json.dumps(COMMENT_LIST)


if __name__ == '__main__':
    app.run()
