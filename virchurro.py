import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from werkzeug.exceptions import abort
import secrets

app = Flask(__name__)
app.config.from_object(secrets)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<id>")
def get(id):
    return render_template("index.html", id=id)

if __name__ == "__main__":
    app.run(debug=True)
