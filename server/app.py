#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:string>")
def print_string(string):
    print(f"{string}")
    return f"{string}"

@app.route("/count/<int:integer>")
def count(integer):
    count = f""
    for i in range(integer):
        count += f"{i}\n"
    return count

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "Please enter one of the following operations: + - * div %"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
