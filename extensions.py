from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_moment import Moment

db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate(db=db)
mail = Mail()
lm = LoginManager()
photos = UploadSet('photos',IMAGES)
moment = Moment()


def extension_init(app):
    db.init_app(app)  # 可以先不初始化
    bootstrap.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)

    lm.init_app(app)
    lm.login_view='userbp.login'
    lm.login_message='login required!!'
    lm.session_protection='strong'

    configure_uploads(app, upload_sets=photos)

    moment.init_app(app)