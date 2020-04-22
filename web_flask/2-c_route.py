#!/usr/bin/python3
""" Script to start a Flask Web App """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_display():
    return 'HBNB'


@app.route('/c/<text>')
def c_display(text):
    return 'C {}'.format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)