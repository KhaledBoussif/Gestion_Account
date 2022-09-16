from website import db
from website.SERVICE.Service import dump


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email = db.Column(db.String(150), unique=True, nullable=False)
    Nom = db.Column(db.String(150), nullable=False)
    Prenom = db.Column(db.String(150), nullable=False)
    Adresse = db.Column(db.String(150), nullable=False)
    PNP = db.Column(db.Boolean, nullable=False, default=False)
    BoitEmail_id = db.relationship('BoitEmail', backref='user', lazy=True)

    def dump(self):
        return dump(self)
