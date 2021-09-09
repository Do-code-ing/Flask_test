from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Test")


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        return render_template("report.html", searching_by=word)
    return redirect("/")


app.run(debug=True)
