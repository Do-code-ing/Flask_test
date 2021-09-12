from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file
from collections import deque

app = Flask(__name__)
app.url_map.strict_slashes = False

db = {}  # fake DB
records = deque()


def record_control(word):
    global records
    if word in records:
        stack = []
        while records:
            record = records.pop()
            if record == word:
                continue

            stack.append(record)

        records.append(word)
        while stack:
            records.append(stack.pop())
    else:
        records.appendleft(word)
        if len(records) > 8:
            records.pop()


@app.route("/")
def home():
    return render_template("home.html", js="home", records=records)


@app.route("/result")
def result():
    word = request.args.get("word")
    if word:
        record_control(word)
        word = word.lower()
        if word not in db:
            jobs = get_jobs(word)
            db[word] = jobs
        return render_template("result.html", css="result", js="result", result_number=len(db[word]), searching_by=word, jobs=db[word], records=records)
    return redirect("/")


@app.route("/reference")
def reference():
    return render_template("reference.html", css="reference", records=records)


@app.route("/more")
def more():
    return render_template("more.html", css="more", records=records)


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


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return redirect("/")


app.run(debug=True)
