from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user

from apps.models.post import Post
from extensions import db
from apps.models import User
from forms import PostForm

mainbp = Blueprint('mainbp',__name__)

@mainbp.route('/',methods=['GET','POST'])
def index():
    # db.create_all()
    form = PostForm()
    page = request.args.get('page',1)
    pagination = Post.query.order_by(Post.posttime.desc()).paginate(page=int(page),per_page=5,error_out=False)
    # posts = Post.query.order_by(Post.posttime.desc()).all()
    posts = pagination.items
    if form.validate_on_submit():
        content = form.content.data
        post = Post(content=content,uid=current_user.id)
        db.session.add(post)
        flash('post ok!')
        return redirect(url_for('postbp.post'))
    return render_template('app/main/index.html',form=form,posts=posts,pagination=pagination)
