# bootstrap
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo1')
def demo1():
    return render_template('demo1.html')

@app.route('/nav')
def nav():
    return render_template('nav.html')

if __name__ == '__main__':
    app.run()


"""
作业：网上找一个bootstrap模板，修改为个人简历。
提示 1（别找太复杂的）  2先改静态  
官方提供的模板（简单）
"""