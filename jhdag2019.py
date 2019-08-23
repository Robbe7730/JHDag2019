from flask import Flask, render_template
app = Flask(__name__)

parties = {
        "Partij a": 25,
        "Partij b": 75
}

@app.route('/')
def root():
    return render_template("index.html", parties=parties)
