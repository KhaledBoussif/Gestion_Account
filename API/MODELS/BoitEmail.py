from website import db
from sqlalchemy.sql import func
from pytz import timezone
from website.SERVICE.Service import dumpM


class BoitEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_email = db.Column(db.String(150), nullable=False)

    def dump(self):
        return dumpM(self)
