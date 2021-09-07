from flask import Flask

app = Flask("Test")


@app.route("/")
def home():
    return "Hello! Welcome to flask."


@app.route("/contact")
def potato():
    return "Contact me."


app.run()
