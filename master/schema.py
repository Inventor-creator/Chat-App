from master import db
from flask_login import UserMixin
from master import app





with app.app_context():
    db.create_all()