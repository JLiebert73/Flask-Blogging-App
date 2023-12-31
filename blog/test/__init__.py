from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from collections import deque
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '9837d1708e71d4883c16a5736184613e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

url_stack=deque()

from test import routes
