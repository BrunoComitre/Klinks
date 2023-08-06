from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


@dataclass
class City(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self):
        return f'Task ID: {self.id} - {self.name}'
