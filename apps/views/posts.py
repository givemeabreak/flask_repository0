from flask import Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user

from apps.models.post import Post

postbp = Blueprint('postbp',__name__)


@postbp.route('/post/')
@login_required
def post():
    return redirect(url_for('mainbp.index'))


@postbp.route('/switch_collect/<int:pid>/')
@login_required
def switch_collect(pid):
    post = Post.query.get(pid)
    collections = current_user.collections
    if current_user.is_collected(pid):
        collections.remove(post)
        flash('取消收藏')

    else:
        collections.append(post)
        flash('收藏成功')

    return redirect(url_for('mainbp.index'))