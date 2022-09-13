from flask import Flask, render_template, request

app = Flask(__name__)

todos = ["Meet Karina", "Sana", "Found OnePiece"]


@app.route("/")
def run():
    name = request.args.to_dict()["name"]
    return render_template("index.html", name=name, todos=todos)


# 이름 띄우기
# 목록 표시
