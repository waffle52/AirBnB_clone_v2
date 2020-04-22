#!/usr/bin/python3
""" Script to start a Flask Web App """
from flask import Flask
from flask import render_template

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
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def py_display(text='is cool'):
    return ('Python {}'.format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def n_display(n):
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def temp(n):
    return render_template('5-number.html', num=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
