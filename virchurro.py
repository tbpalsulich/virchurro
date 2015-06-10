from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<id>")
def get(id):
    return render_template("index.html", id=id)

if __name__ == "__main__":
    app.run(debug=True)
