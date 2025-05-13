from master import db
from flask_login import UserMixin
from master import app

class Users(db.Model , UserMixin):
    __tablename__ = 'Users'
    
    def __init__(self , userId , username):
        self.userId = userId
        self.username = username
    
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text)

    def get_id(self):
        return self.userId
    



class chatRooms(db.Model):
    __tablename__ = 'chatRooms'
    
    chatRoomId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chatRoomName = db.Column(db.Text)



class messages(db.Model):
    __tablename__ = 'messages'
    
    messageId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chatRoomId = db.Column(db.Integer , db.ForeignKey("chatRooms.chatRoomId"))
    sentByUserId = db.Column(db.Integer, db.ForeignKey('Users.userId'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    repliedTo = db.Column(db.Integer, db.ForeignKey('messages.messageId'))

    # Relationship for replied message


class userInChatRoom(db.Model):
    __tablename__ = 'userInChatRoom'

    userId = db.Column(db.Integer, db.ForeignKey('Users.userId'), primary_key=True)
    chatRoomId = db.Column(db.Integer, db.ForeignKey('chatRooms.chatRoomId'), primary_key=True)






with app.app_context():
    db.create_all()