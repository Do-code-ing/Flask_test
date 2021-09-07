from flask import Flask

app = Flask("Test")


@app.route("/")
def home():
    return "Hello! Welcome to flask."


@app.route("/<username>")
def potato(username):
    return f"Hello your name is {username}"


app.run()
