from flask import render_template

from apps.views import mainbp, userbp, postbp

blueprints = (
    (mainbp, '/main'),
    (userbp, '/users'),
    (postbp, '/posts'),

)


def register_blueprints(app):
    for bp, prefix in blueprints:
        app.register_blueprint(bp,url_prefix=prefix)

def errors(app):
    @app.errorhandler(404)
    def error404(e):
        return render_template('errors/404.html')