from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Cricket",
    "Football",
    "Vollyball",
    "Badminton",
    "100 m run"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register",methods=["POST"])
def register():
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    return render_template("success.html",name=request.form.get("name"))