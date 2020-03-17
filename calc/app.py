# Put your app in here.
# build a calculator app which takes two url query paramets to get the numbers to calculate with
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/add")
def add():
    print(request.args)
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b = int(b)
    return f"addpage {operations.add(a,b)}"
@app.route("/sub")
def subtract():
    print(request.args)
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b = int(b)
    return f"subtract {operations.sub(a,b)}"
@app.route("/mult")
def multiply():
    print(request.args)
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b = int(b)
    return f"multiply {operations.mult(a,b)}"
@app.route("/div")
def divide():
    print(request.args)
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b = int(b)
    return f"divide {operations.div(a,b)}"
@app.route("/math/<function>")
def math_operation(function):
    print(l_functions)
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b = int(b)
    return f"Wrorks!! {l_functions[function](a,b)}"
l_functions = {
    "add": operations.add,
    "sub": operations.sub,
    "div": operations.div,
    "mult": operations.mult
}
print(l_functions["sub"])