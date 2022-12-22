from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tovari.db"
db = SQLAlchemy(app)


class Tovar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    info = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.id




from app import routes
