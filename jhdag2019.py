from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "JongeHeldenDag2019"
db = SQLAlchemy(app)

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Party {self.id}> {self.name}: {self.score}"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def dateString(self):
        return self.created_date.strftime("%H:%M")

    def __repr__(self):
        return f"<Message {self.id}> {self.title}: {self.content[:32]}"

admin = Admin(app, name='Jonge Heldendag 2019', template_mode='bootstrap3')
admin.add_view(ModelView(Party, db.session))
admin.add_view(ModelView(Message, db.session))

@app.route('/')
def root():
    parties = Party.query.all()
    total = sum([p.score for p in parties])
    messages = Message.query.order_by(Message.created_date.desc()).all()
    print(messages)
    return render_template("index.html", parties=parties, total=total, messages=messages)
