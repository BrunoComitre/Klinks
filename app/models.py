from dataclasses import dataclass
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


@dataclass
class Links(db.Model):
    id: int
    page_title: str
    link: str
    added_on_date: str

    id = db.Column(db.Integer, primary_key=True)
    page_title = db.Column(db.String(255),unique=True, nullable=False)
    link = db.Column(db.String(255),unique=True, nullable=False)
    added_on_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        return f'Task ID: {self.id} - {self.page_title}'
