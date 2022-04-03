from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)



db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = "Don't do that, Just log in"
login.login_message_category = 'danger'

from app.blueprints.auth import auth
app.register_blueprint(auth)

from app.blueprints.blog import blog
app.register_blueprint(blog)


from app import routes, models, forms

# login = LoginManager(app)
