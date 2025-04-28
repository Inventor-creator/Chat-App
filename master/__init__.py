from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import text
import os


basedir = os.path.abspath(os.path.dirname(__file__))

filename = "chats.db"
var = "sqlite:///" + os.path.join(basedir, filename)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = var
app.config['SECRET_KEY'] = 'thisisasecretkey'




bcrypt = Bcrypt(app)

db = SQLAlchemy()
login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)


login_manager.login_view = "login"



app.app_context().push()

