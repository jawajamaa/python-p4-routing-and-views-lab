#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
# replace <param> with variable string?
@app.route('/print/<parameter>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<parameter>')
def count(integer):
    for i in range(integer):
        print(f'{i}\n')

@app.route('/math/<num1><operation><num2>')
def math(num1, operation, num2):
    num1, operation, num2

if __name__ == '__main__':
    app.run(port=5555, debug=True)
