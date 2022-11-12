#!/usr/bin/python3
#a script that starts a Flask web application with /hbnb

from flask import Flask

app = Flask(_name_)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    "displays the message, hello hbnb"
    return "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays 'HBNB' """
    return 'HBNB'

if __name__ == "__main__":
    "starting flask web"
    app.run(host='0.0.0.0', port=5000)