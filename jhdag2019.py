from flask import Flask, render_template
app = Flask(__name__)

parties = {
        "Partij a": 7,
        "Partij b": 75
}

@app.route('/')
def root():
    total = sum(parties.values())
    return render_template("index.html", parties=parties, total=total)
