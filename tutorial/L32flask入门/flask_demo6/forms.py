from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Login(FlaskForm):
    email = StringField('注册邮箱', validators=[Email()], render_kw={'placeholder': '请填写邮箱'})
    password = PasswordField('密码', validators=[DataRequired()])
    nickname = StringField('昵称', validators=[Length(1, 10, message='输入长度必须在1-10个字符')])
    submit = SubmitField('提交')

# Email验证有问题，后端form.validate_on_submit()返回了错误，但前端没有渲染出来。