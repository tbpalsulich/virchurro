import sqlite3
from flask import Flask, request, g, redirect, url_for, abort, render_template
from werkzeug.exceptions import abort
import secrets

app = Flask(__name__)
app.config.from_object(secrets)

# http://stackoverflow.com/a/9011133
def random_string(length):
    import random
    import string

    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for _ in range(length))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    c = g.db.cursor()
    slug = random_string(6)
    c.execute('insert into entries (slug, song) values (?, ?)', [slug, request.form['song']])
    g.db.commit()
    return redirect(url_for("get", slug=slug))

@app.route("/<slug>")
def get(slug):
    song = g.db.execute('SELECT song FROM entries WHERE slug=?', [slug]).fetchone()
    if song is None: abort(404)
    return render_template("churro.html", song=song[0])

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
