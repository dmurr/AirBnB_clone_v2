#!/usr/bin/python3
""" Starts a simple flask application """

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays 'C <text>' """
    return 'C %s' % text.replace(" ", "_")

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Displays 'Python <text>' """
    return 'Python %s' % text.replace(" ", "_")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
