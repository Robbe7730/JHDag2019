from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "JongeHeldenDag2019"
db = SQLAlchemy(app)

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Party {id}> {name}: {score}"

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Party, db.session))

@app.route('/')
def root():
    parties = Party.query.all()
    total = sum([p.score for p in parties])
    return render_template("index.html", parties=parties, total=total)
