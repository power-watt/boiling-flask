from . import db

class Sleep_time(db.Model):
    __tablename__ = 'sleep_time' # db table name

    id = db.Column(db.Integer, primary_key=True)
    go_to_bed = db.Column(db.DateTime,)
    wake_up   = db.Column(db.DateTime,)

    def __repr__(self):
        return f'<id:{self.id}, go_to_bed:{self.go_to_bed}, wake_up:{self.wake_up}>'
