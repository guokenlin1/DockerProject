from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users, methods=['GET']) 
def users_get():
    return 'Here are all of the users'

@app.route('/users, methods=['POST'])
def users_post():    
    return 'Thanks for creating a new user'

@app.route('/greeting, methods=['GET'])
def get_greeting():
    return jsonify('Hello world!')
