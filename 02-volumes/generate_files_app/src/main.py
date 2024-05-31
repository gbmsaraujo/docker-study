from flask import Flask, render_template, request, redirect, url_for
import os
import shutil

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return redirect(url_for('hello'))

    title = request.form["title"]
    text = request.form["text"]

    temp_path = os.path.join(os.path.abspath("./src/temp"), f"{title.lower()}.txt")
    final_path = os.path.join(os.path.abspath("./src/feedback"), f"{title.lower()}.txt")

    with open(temp_path, "w") as temp_file:
        temp_file.write(text)

    if os.path.exists(final_path):
        return render_template("exists.html")
    else:
        shutil.copy(temp_path, final_path)

    return render_template("home.html")

@app.route("/feedback/<name>", methods=["GET"])
def feedback(name:str):
    if not os.path.exists(f"./src/feedback/{name}.txt"):
        return "Arquivo não existe"
    
    with open(f"./src/feedback/{name}.txt", "r") as file:
        return file.read()