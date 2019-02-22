# 文件上传 ;返回cookie; 错误状态码
import os
from flask import Flask, render_template, url_for, request, make_response, abort, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload_submit', methods=['POST'])
def upload_submit():
    file = request.files['file']
    print(file)
    # file.save('static/userfile/001.txt')    # 不建议写相对路径
    # file.save('D:/PycharmProjects/flask_demo4/static/userfile/002.txt')
    # print(os.path.dirname(__file__))    # app.py 所在的文件夹路径 D:\PycharmProjects\flask_demo4
    # save_path = os.path.dirname(__file__) + '/static/userfile/' +
    save_path = os.path.join(os.path.dirname(__file__), 'static/userfile/'  ,file.filename)
    print(save_path)
    file.save(save_path)
    return '保存完成'


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)   # 客户端请求方法
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        print(username, password)
        # 数据库查询比对
        pass
        # 设置cookie
        response = make_response(render_template('index.html'))
        response.set_cookie('username', username)
        return response

# 返回内置错误模板
@app.route('/admin')
def admin():
    # 假设这个路由是管理后台，前来登录的用户权限验证失败
    abort(401)      # 返回内置的错误模板页面


# 返回自定义错误模板
@app.errorhandler(404)
def error404(error):
    # return render_template('error404.html'), 404
    return redirect(url_for('hello_world'), code=302)

# 重定向redirect  。
# 场景：登录成功了，进入我的订单页面；登录失败，重定向到首页或登录页面让用户再次尝试登录。请求的路由发生变化。




if __name__ == '__main__':
    app.run()


"""
作业1：用户上传文件的文件名可能包含非法字符，服务器接收后导致程序崩溃。尝试flask框架中的secure_filename()方法。
"""