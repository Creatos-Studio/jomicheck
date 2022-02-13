from flask import Flask, render_template
from database import database
# from flask_sqlalchemy import SQLAlchemy

from apps.users.views import users
from apps.passwords.views import passwords


def create_app():

    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    database.init_app(app)
    app.register_blueprint(users)
    app.register_blueprint(passwords)

    # @app.route('/about')
    # def about():
        # return render_template('pages/about.html')

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
