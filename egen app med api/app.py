from flask import Flask, render_template
from cryptomap import hent_posisjoner

posisjoner = hent_posisjoner()

app = Flask(__name__)

@app.route("/")
def index():
    navn = "CRYPTO MAPS"
    return render_template("index.html", navn=navn, posisjoner=posisjoner)

@app.route("/tyskland")
def tyskland():
    sted = "tyskland"
    return render_template("tyskland.html", sted=sted)

@app.route("/spania")
def spania():
    sted = "spania"
    return render_template("spania.html", sted=sted)


