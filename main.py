from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mayaO'

@app.route('/')
def hello():
    return "World!"