#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:num>')
def count(num):
    string = ""
    for i in range(num):
        string = string + (str(i)+"\n")
    return string

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(int(num1) + int(num2))
    elif operation == "-":
        return str(int(num1) - int(num2))
    elif operation == "*":
        return str(int(num1) * int(num2))
    elif operation == "div":
        return str(int(num1) / int(num2))
    elif operation == "%":
        return str(int(num1) % int(num2))
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
