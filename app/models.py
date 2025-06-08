
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
