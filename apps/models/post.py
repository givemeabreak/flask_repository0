import datetime

from extensions import db


class Post(db.Model):
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    content = db.Column(db.Text(),nullable=False)
    posttime = db.Column(db.DateTime(),default=datetime.datetime.utcnow)
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))

