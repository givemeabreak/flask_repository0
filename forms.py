from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, PasswordField, StringField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, Email


class PostForm(FlaskForm):
    content = TextAreaField('发言', render_kw={'placeholder':'请输入文字'},validators=[DataRequired('不能为空'), Length(max=100, min=5, message='长度5-100！')])
    submit = SubmitField('提交')

class RegisterForm(FlaskForm):
    username = StringField('用户名',render_kw={'placeholder':'请输入用户名'},validators=[DataRequired('不能为空')])
    password = PasswordField('密码',render_kw={'placeholder':'请输入密码'},validators=[DataRequired('不能为空')])
    repeat = PasswordField('确认密码',render_kw={'placeholder':'请输入确认密码'},validators=[DataRequired('不能为空'),
                                                                                  EqualTo('password','密码不一致')])
    email = StringField('邮箱',render_kw={'placeholder':'输入邮箱地址'},validators=[DataRequired('不能为空'),Email('not an email')])
    submit = SubmitField('注册')

class LoginForm(FlaskForm):
    username = StringField('用户名', render_kw={'placeholder': '请输入用户名'}, validators=[DataRequired('不能为空')])
    password = PasswordField('密码', render_kw={'placeholder': '请输入密码'}, validators=[DataRequired('不能为空')])
    remember = BooleanField('remember me')
    submit = SubmitField('login')


class UploadForm(FlaskForm):
    file = FileField('upload icon',validators=[DataRequired('please select an icon')])
    submit = SubmitField('tijiao')


class ProfileForm(FlaskForm):
    username = StringField('用户名',render_kw={'disabled':True})
    email = StringField('邮箱',render_kw={'disabled':True})