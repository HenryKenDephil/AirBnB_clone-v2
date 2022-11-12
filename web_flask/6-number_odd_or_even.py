#!/usr/bin/python3
#script to returns html template if n is a number

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


@app.route('/c/<text>', strict_slashes=False)
def c():
    "returns c is fun and replaces underscore"
    return 'c %s' % text.replace('_', '')

@app.route('/python/(<text>)' strict_slashes=False)
def python():
    "display python"
    return 'python %s' % text.replace('_', 'is cool')


@app.route('/number/<int:n>', strict_slashes=False)
def /number/<n>():
    "returning n is a number if it's an integer"
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number(n):
    "returns html page if n is an integer"
    return render_template(5-number.html, value=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even():
    if n % 2 == 0:
        return render_template(6-number_odd_or_even.html, value=n)
    elif n % 2 !=0:
        return render_template(6-number_odd_or_even.html, value=)n    
if __name__ == "__main__":
    "starting flask web"
    app.run(host='0.0.0.0', port=5000)