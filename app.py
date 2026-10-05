import os
import subprocess
from flask import Flask, request
from database import execute_query

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args["id"]

    # INTENTIONAL SQL INJECTION DEMO
    query = "SELECT * FROM users WHERE id=" + user_id

    return execute_query(query)


@app.route("/run")
def run_command():
    command = request.args["cmd"]

    # INTENTIONAL COMMAND INJECTION DEMO
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout


@app.route("/calculate")
def calculate():
    expression = request.args["expression"]

    # INTENTIONAL UNSAFE EVAL DEMO
    return str(eval(expression))


@app.route("/profile")
def profile():
    user = request.args.get("user", "guest")

    try:
        return "Profile: " + user
    except:
        pass


def process_items(items=[]):
    # INTENTIONAL MUTABLE DEFAULT ARGUMENT
    items.append("demo")
    return items


unused_variable = os.getenv("THIS_ENVIRONMENT_VARIABLE_IS_NOT_USED")
