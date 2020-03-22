from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET']) 
def users_get():
    return 'Here are all of the users'

@app.route('/users', methods=['POST'])
def users_post():    
    return 'Thanks for creating a new user'

@app.route('/greeting<string:name>', methods=['GET'])
def get_greeting(name):
    return jsonify(f"greeting {name}")

greetings = []
@app.route('/greeting', methods = ['POST'])
def add_greeting():
    content = request.json
    newGreeting = "Hello %s" % content['name']
    greetings.append(newGreeting)
    return jsonify({ "greeting" : newGreeting })

@app.route('/')
def get_all_greetings():
    return jsonify(greetings)
