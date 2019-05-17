from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager,create_access_token
import huanghuaye_test.test as hhy

class User():
    def __init__(self,username,password):
        self.username=username
        self.password=password

app=Flask(__name__)
app.config['JWT_SECRET_KEY']='super-secret'
jwt=JWTManager(app)
users={}

@app.route('/huanghuaye_signup',methods=['POST'])
def huanghuaye_signup():
    if not request.is_json:
        return jsonify({'msg':'Missing JSON in request'})
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    if not username:
        return jsonify({'msg':'未填用户名'})
    if not password:
        return jsonify({'msg':'未填密码'})
    if username in users:
        return jsonify({'msg':'此用户名已存在'})
    users[username]=User(username,password)
    return jsonify({'msg':'注册成功！'})

@app.route('/huanghuaye_login',methods=['POST'])
def huanghuaye_login():
    if not request.is_json:
        return jsonify({'msg':'Missing JSON in request'})
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    if (not username) or (not password):
        return jsonify({'msg':'Missing username or password parameter'})
    ye_loginuser=users.get(username,None)
    if not ye_loginuser:
        return jsonify({'msg':'此用户名不存在'})
    elif ye_loginuser.password==password:
        return jsonify(access_token=create_access_token(identity=username))
    else:
        return jsonify({'msg':'密码错误！'})

app.register_blueprint(hhy.test_hhy)

if __name__=='__main__':
    app.run()