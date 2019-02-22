# 路由详解。  url_for()。
from flask import Flask, render_template, url_for

app = Flask(__name__)

# 固定路由
@app.route('/')
@app.route('/index')    # 多个url指向同一方法 。  127.0.0.1:5000/     127.0.0.1:5000/index
def index():
    return render_template('index.html')

@app.route('/service')    # 127.0.0.1:5000/service
def service():
    print(url_for('service'))
    return '服务页面'

@app.route('/about')
def about():
    return '关于我们页面'

# 带参数的路由。优点可以写多个参数
# http://www.xxx.com/product_list?pageno=1
# http://www.xxx.com/product_list?pageno=2
# 路由前面一部分一样，后面部分不一样。优点是利于搜索引擎。
# http://www.xxx.com/product_list/1/
# http://www.xxx.com/product_list/2/
# http://www.xxx.com/product_list
@app.route('/product_list/<int:page_no>')
@app.route('/product_list', defaults={'page_no': 1})       # 参数默认值
def product_list(page_no):
    print(page_no, type(page_no))
    # page_no = int(page_no)
    return '商品1，商品2...'

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5001)
    app.run(port=5001)



"""
路由：
1. 匹配固定地址。
'/' → '//127.0.0.1:5000/    //127.0.0.1:5000   匹配根目录

flask命令行工具：
flask run --port=5000 --host='0.0.0.0'

url_for(endpoint) 函数，构造url：
endpoint端点参数，填写方法名。注意参数对应的是函数名，跟路由的url没关系。
1. 参数是方法名。当ip、port发生变化时，不用前端页面。
2. 参数1静态文件夹名，参数2是filename=''。引用css js之类的静态资源。flask框架会对url进行预处理，前端html页面引用资源时不能写成相对路径。前端url_for()返回结果/static/index.css , flask框架内置相关路由。


匹配可变url：
@app.route('/product_list/<int:page_no>')
[domain]/product_list/2
参数转换器（不重要）：
int:  float:


本节常见错误：
1. template not found 模板未找到，检查.html文件路径和文件名。
2. ValueError: urls must start with a leading slash  路由没有以/开头
3. cli.no app.exception  没有找到app示例。终端设置set FLASK_APP=app.py 。虽然pycharm已自动注入环境变量。问题原因未知，cmd中换端口运行解决。
4. 代码正确情况下css未生效。原因谷歌浏览器缓存，开发者工具里勾选disable cache。或者清空缓存硬性重新加载。 
"""