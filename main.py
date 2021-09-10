from flask import Flask, render_template, request, redirect, send_file
from scraper import get_jobs
from exporter import save_to_file

app = Flask("Test")

db = {}  # fake DB


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def result():
    word = request.args.get("word")
    if word:
        word = word.lower()
        if word not in db:
            jobs = get_jobs(word)
            db[word] = jobs
        return render_template("result.html", result_number=len(db[word]), searching_by=word, jobs=db[word])
    return redirect("/")


@app.route("/reference")
def reference():
    return render_template("reference.html")


@app.route("/more")
def more():
    return render_template("more.html")


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
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(debug=True)
