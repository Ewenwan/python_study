# post请求   请求request  上下文context  响应response
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# (常用）传参数的url  。场景：接口
# http://127.0.0.1:5000/product_list?page_no=1&cat=sport
@app.route('/product_list')
def product_list():
    args = request.args
    print(args)
    print(args['page_no'])
    print(args['cat'])
    # 数据库查询 pass
    return '商品1，商品2...'

@app.route('/login')
def login():
    print(request)
    return render_template('login.html')

@app.route('/login_submit', methods=['POST','GET'])
def login_submit():
    form = request.form
    print(form)
    username = form['username']
    password = form['password']
    print(username, password)
    # 跟数据库里的用户表做权限比对或存储信息
    return '表单提交完成'




if __name__ == '__main__':
    app.run()


"""
request:  flask框架中全局变量，存储着跟请求相关信息。

作业1：https://www.1owo.com/categories/flask/  L1-L5
作业2：print(request.method)  ,把/login /login_submit二合一 /login，第一次get请求表单页面，表单信息提交时走post请求。
"""