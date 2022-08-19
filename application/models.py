from email.policy import default
from application import db
from datetime import datetime


class Boq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return self.id

