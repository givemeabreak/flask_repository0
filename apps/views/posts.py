from flask import Blueprint, flash, redirect, url_for
from flask_login import login_required

postbp = Blueprint('postbp',__name__)

@postbp.route('/')
def index():
    return 'postbp index'


@postbp.route('/post/')
@login_required
def post():
    return redirect(url_for('mainbp.index'))