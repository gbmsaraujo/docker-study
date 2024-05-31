from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/send-name",methods=['GET', 'POST'])
def send_name():
    name_input = request.form['input-name']
    return render_template("home.html", name=name_input)