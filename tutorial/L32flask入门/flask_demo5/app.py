# jinja2 前端模板渲染语法
from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    name = '小李'

    # 假设从数据库取得学生姓名列表
    name_list = ['小明', '小红', '小青']
    stu_list = [
        {'name': '小明', 'age': 13, 'phone': '137000'},
        {'name': '小李', 'age': 13, 'phone': '135000'},
        {'name': '小红', 'age': 13, 'phone': '136000'}
    ]

    # 假设从数据库里取一个字段信息包含html语法
    html_content = """
        <body>
            <h1>python</h1>
        </body>
    """
    return render_template('index.html', name=name, name_list=name_list, stu_list=stu_list, html_content=html_content)

@app.route('/about')
def about():
    return  render_template('about.html')



if __name__ == '__main__':
    app.run()



"""
作业：jinja2  利用for循环和if判断，实现表格的隔行变色。
作业2： 百度"XSS"攻击，了解大致原理。
"""