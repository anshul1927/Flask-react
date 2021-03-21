from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello' methods=['GET'])
def say_hello_world():
    return {'result': "Hello"}


@app.route('/mood/<m>', methods = ['POST'])
def create(m):
    mood = request.json

    print(mood)
    print(m)
    say_hello_world()
