from apps.models.user import User
from extensions import db



collection = db.Table(
    'collection',
    db.Column('uid',db.Integer, db.ForeignKey('user.id')),
    db.Column('pid',db.Integer, db.ForeignKey('post.id'))
)
