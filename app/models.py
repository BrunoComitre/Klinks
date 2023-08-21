from dataclasses import dataclass
from datetime import datetime
from inspect import TPFLAGS_IS_ABSTRACT
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


@dataclass
class Links(db.Model):
    id: int
    vulnerability: str
    tag: str
    added_on_date: str

    id = db.Column(db.Integer, primary_key=True)
    vulnerability = db.Column(db.String(255),unique=True, nullable=False)
    tag = db.Column(db.String(255),unique=True, nullable=False)
    added_on_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        return f'Task ID: {self.id} - {self.vulnerability}'
