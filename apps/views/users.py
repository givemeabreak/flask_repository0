import os

from flask import Blueprint, render_template, redirect, url_for, current_app, flash, app
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message

from apps.models import User
from extensions import db, mail, photos
from forms import RegisterForm, LoginForm, UploadForm, ProfileForm

userbp = Blueprint('userbp', __name__)


@userbp.route('/')
def index():
    return 'userbp index'


@userbp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = User.query.filter(User.password == password, User.username == username, User.confirmed == True).first()
        if user:
            login_user(user, remember=remember)
            return redirect(url_for('mainbp.index'))
        else:
            return 'user does not exist'
    return render_template('app/users/login.html', form=form)


@userbp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()

        check_url = url_for('userbp.activate', token=new_user.generate_token(), _external=True)
        send_email(check_url, new_user)
        return redirect(url_for('mainbp.index'))
    return render_template('app/users/register.html', form=form)


@userbp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('mainbp.index'))


@userbp.route('/activate/<token>/')
def activate(token):
    id = User.check_token(token)
    if id:
        user = User.query.get(id)
        user.confirmed = True
        db.session.commit()
        return 'sucess'
    return 'fail'


def send_email(check_url, new_user):
    msg = Message(
        subject='请激活邮箱',
        recipients=[new_user.email],
        body='body 验证',
        html='html 点击 <a href="' + check_url + '">此处</a> 验证',
        sender=current_app.config['MAIL_USERNAME']
    )
    mail.send(msg)


@userbp.route('/change_icon/', methods=['GET', 'POST'])
def change_icon():
    form = UploadForm()
    url = url_for('static',filename=User.query.get(current_user.id).icon)
    if form.validate_on_submit():
        flash('upload ok')
        file = form.file.data
        filepath = photos.save(file, name=file.filename)
        url = photos.url(filepath)
        print(url)
        user = User.query.get(current_user.id)
        user.icon = os.path.join('uploads',filepath)
        db.session.commit()
    return render_template('app/users/change_icon.html', form=form,url=url)


@userbp.route('/profile/')
@login_required
def profile():
    form = ProfileForm(username=current_user.username,email=current_user.email)
    return render_template('app/users/profile.html',form=form)