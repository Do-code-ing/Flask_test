from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file
from collections import deque

app = Flask(__name__)
app.url_map.strict_slashes = False

db = {}  # fake DB
reference_db = {
    "노마드 코더": [["https://nomadcoders.co/", "Nomad Coders - Clone Startups. Learn to Code."]],
    "1분코딩": [
        ["https://studiomeal.com/archives/197", "이번에야말로 CSS Flex를 익혀보자 - 1분 코딩"],
        ["https://studiomeal.com/archives/533", "이번에야말로 CSS Grid를 익혀보자 - 1분 코딩"]
    ],
    "드림코딩": [["https://www.youtube.com/c/%EB%93%9C%EB%A6%BC%EC%BD%94%EB%94%A9by%EC%97%98%EB%A6%AC", "드림코딩 by 엘리 (Youtube)"]],
    "MDN": [["https://developer.mozilla.org/en-US/", "MDN Web Docs"]],
}
more_db = {
    "Do-Code-Ing": [["https://github.com/Do-code-ing", "Do-Code-Ing GitHub"]],
    "To Do List": [["https://do-code-ing.github.io/Nomad_Vanilla_JS/", "Momentum App"]],
    "Clone Zoom": [["https://do-code-ing.github.io/Nomad_Clone_ZOOM/", "Noom"]],
    "Paint Brush": [["https://do-code-ing.github.io/Nomad_Paint_Brush/", "Paint Brush"]],
    "Movie App": [["https://do-code-ing.github.io/Nomad_Movie_App/", "Movie App"]],
}
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
    return render_template("reference.html", css="reference", db=reference_db, records=records)


@app.route("/more")
def more():
    return render_template("more.html", css="more", db=more_db, records=records)


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
