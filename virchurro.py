import random
import string

from flask import Flask, request, redirect, url_for, abort, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

import secrets

app = Flask(__name__)
app.config.from_object(secrets)
db = SQLAlchemy(app)

# Create our database model
class Churro(db.Model):
    __tablename__ = "churros"
    slug = db.Column(db.String(6), primary_key=True)
    song = db.Column(db.String(120))

    def __init__(self, slug, song):
        self.slug = slug
        self.song = song

    def __repr__(self):
        return '<Slug %s>' % self.slug
def random_string(length):
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for _ in range(length))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    slug = random_string(6)
    churro = Churro(slug, request.form['song'])
    db.session.add(churro)
    db.session.commit()
    return redirect(url_for("get", slug=slug))

@app.route("/<slug>")
def get(slug):
    churro = db.session.query(Churro).get(slug)
    if churro is None: abort(404)

    return render_template("churro.html", song=churro.song)

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
