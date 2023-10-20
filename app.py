from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def hello_world():
    mensagem = "Hello, world"
    return render_template("home.html", mensagem=mensagem)