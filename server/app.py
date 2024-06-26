#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:name>')
def print_string(name):
    print(name)
    return f'{name}'

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(f'{i}' for i in range(parameter )) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h1>Error: Division by zero!</h1>'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return '<h1>Error: Division by zero!</h1>'
    else:
        return '<h1>Error: Invalid operation!</h1>'
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)