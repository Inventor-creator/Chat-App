from master import app
from master import db
from master import login_manager
from master import schema

from sqlalchemy import text
from master import forms

from flask import render_template ,jsonify
from flask import request , url_for , redirect , session 
from flask_login import login_user, login_required, logout_user, current_user 


@login_manager.user_loader
def load_user(user_id):
    return schema.Users.query.get(int(user_id))

@app.route('/logout')
def logout():
    print("logged out user")
    logout_user()
    return redirect(url_for('login'))

@app.route('/' , methods = ['GET' , 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        try:
            temp = db.session.execute(text(f"SELECT userId FROM Users WHERE username = '{user}'")).fetchall()[0][0]
        except:
            print("db issue line 26")
        
        print(temp)

        #login user
        userObj = schema.Users.query.filter_by(username = user).first()
        
        login_user(userObj)
        
        return redirect(url_for('dashboard',userId = temp ))
    
    return render_template("login.html" , form = form)

@login_required
@app.route('/dashboard/user')
def dashboard():
    
    userId = request.args.get('userId')
    userObj = schema.Users.query.filter_by(userId = userId).first()
    #recheck the user 
    if current_user != userObj:
        return "hatt ree gendu"
    username = db.session.execute(text(f"SELECT username FROM Users WHERE userId = '{userId}'")).fetchall()[0][0]
    #get all chatroom in which user is there    
    userChatRooms = db.session.execute(text(f"SELECT chatRooms.chatRoomName FROM userInChatRoom , chatRooms WHERE userInChatRoom.userId = {userId} AND userInChatRoom.chatRoomId = chatRooms.chatRoomId ")).fetchall()
    
    return render_template('dashboardBlocks.html' , user = username , userChatRooms = userChatRooms)


@login_required
@app.route("/room/<int:userid>" , methods = ["GET" ,"POST"])
def room(userid):
    print(request.args.get('something'))
    #select users only from that chatroom to improve efficiency to render
    users = db.session.execute(text("SELECT * FROM Users")).fetchall()
    messages = schema.messages.query.all()
    print(messages[0].chatRoomId)
    return render_template('sampleChatBlocks.html' , users = users , messages = messages , userid = userid)




