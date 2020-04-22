#!/usr/bin/python3
""" Script to """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    return 'Hello HBNB!\n'


@app.route('/hbnb')
def hbnb_display():
    return 'HBNB\n'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
