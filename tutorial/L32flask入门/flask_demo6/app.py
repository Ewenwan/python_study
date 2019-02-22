# flask-WTF插件。  后端代码翻译成html代码
# (不建议用这个插件，因为学习成本不低，中间需要转换思维，还不如直接html)
from flask import Flask, render_template, url_for
from forms import Login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'skljdba223'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        email = form.data['email']
        password = form.password.data
        nickname = form.nickname.data
        print(email)
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run()
