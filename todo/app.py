from flask import Flask, render_template, request

app = Flask(__name__)

todos = ["Meet Karina", "Sana", "Found OnePiece"]


@app.route("/")
def run_base():
    return render_template("base.html")


@app.route("/head")
def run_head():
    return render_template("head.html")


@app.route("/todos")
def run_todos():
    # name = request.args.to_dict()["name"]
    name = request.args.get("name", "None")
    return render_template("index.html", name=name, todos=todos)


# 이름 띄우기
# 목록 표시
