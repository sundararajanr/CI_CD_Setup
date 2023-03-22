from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome Sundar Rajan 22/2023 update!!!'
