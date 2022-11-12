#!/usr/bin/python3
#a script to start a Flask web application

from flask import Flask

app = Flask(_name_)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    #returns hello hbnb!
    return "Hello HBNB!"
    
if __name__ == "__main__":
    "running flask web"
    app.run(host='0.0.0.0', port=5000)

