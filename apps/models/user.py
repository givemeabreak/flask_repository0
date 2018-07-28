from flask import current_app
from flask_login import UserMixin

from extensions import db, lm
from itsdangerous import TimedJSONWebSignatureSerializer as JWS


class User(UserMixin,db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(32),nullable=False,unique=True)
    password = db.Column(db.String(128),nullable=False,unique=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    confirmed = db.Column(db.Boolean(),default=False)                  # 邮箱是否验证
    icon = db.Column(db.String(50),default='/uploads/default.jpg')

    posts = db.relationship('Post',backref='user',lazy='dynamic')
    collections = db.relationship('Post',backref=db.backref('users'),lazy='dynamic',secondary='collection')

    def generate_token(self):
        jws = JWS(current_app.config['SECRET_KEY'], expires_in=600)
        token = jws.dumps({'id': self.id})
        return token

    def is_collected(self,pid):
        for post in self.collections:
            if post.id == pid:
                return True
        return False

    @staticmethod
    def check_token(token):
        jws = JWS(current_app.config['SECRET_KEY'])
        try:
            data = jws.loads(token)
        except:
            return False #'token wrong,register fail'
        else:
            id = data.get('id')
            if User.query.get(id) is None:
                return False #'user did not exist'
            else:
                return id #'register ok'


@lm.user_loader
def get_user(id):
    return User.query.get(id)