"""Session 1: first Flask page."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="My Study Planner")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
