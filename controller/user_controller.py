from app import app
from flask import request
from model.user_model import user_model

user = user_model()
@app.route('/signup')
def signup():
    return user.user_signup_model()

@app.route('/getUsers')
def get_all_user():
    return user.get_user_all()

@app.route('/user/addOne', methods = ['POST'])
def add_one_user():
    return user.add_one_user(request.form)
    
@app.route('/user/update',methods = ['PUT'])
def update_user():
    return user.update_user(request.form)

@app.route('/user/delete/<id>', methods = ['DELETE'])
def delete_user(id):
    return user.delete_user(id)