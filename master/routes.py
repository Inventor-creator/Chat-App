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
        print(userObj)
        login_user(userObj)
    
        return redirect(url_for('room',userid = temp ))
    
    return render_template("login.html" , form = form)

    

@login_required
@app.route("/room/<int:userid>" , methods = ["GET" ,"POST"])
def room(userid):
    #select users only from that chatroom to improve efficiency to render
    users = db.session.execute(text("SELECT * FROM Users")).fetchall()
    messages = schema.messages.query.all()
    print(users)
    return render_template('sampleChatBlocks.html' , users = users , messages = messages , userid = userid)




