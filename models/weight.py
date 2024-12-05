from . import db
import datetime

class Weight(db.Model):
    __tablename__ = 'weight' # db table name

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    weight    = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<id:{self.id}, timestamp:{self.timestamp}, weight:{self.weight}>'
