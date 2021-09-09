from flask import Flask, render_template, request, redirect
from scraper import get_jobs

app = Flask("Test")

db = {}  # fake DB


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        if word not in db:
            jobs = get_jobs(word)
            db[word] = jobs
        return render_template("report.html", result_number=len(db[word]), searching_by=word, jobs=db[word])
    return redirect("/")


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        return f"Generate CSV for {word}"
    except:
        return redirect("/")


app.run(debug=True)
