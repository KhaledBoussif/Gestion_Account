import json
from configparser import ConfigParser
from sqlalchemy import create_engine


import pdb


def dump(self):
    return {self.id: {'id': self.id,
                      'Email': self.Email,
                      'Nom': self.Nom,
                      'Prenom': self.Prenom,
                      'Adresse': self.Adresse,
                      'PNP': self.PNP}}


def dumpM(self):
    return {self.id: {'id': self.id,
                      'mail': self.mail,
                      'date': self.date,
                      'user_id': self.user_id,
                      'user_email': self.user_email}}


def GetUsersJSON(users):
    return json.dumps([o.dump() for o in users], indent=1)


def GetOneUserJSON(user):
    return json.dumps(user.dump(), indent=1)


def creat_engine_db():
    config = get_config()
    return create_engine(f'sqlite:///website/{config["DataBase_Info"]["DB_NAME"]}', echo=False)


def commit_db_user(db, N_user=""):
    if N_user != "":
        db.session.add(N_user)
        # pdb.set_trace()
    db.session.commit()


def commit_db_mail(db, New_Mail):
    if New_Mail != "":
        db.session.add(New_Mail)
    db.session.commit()


def commit_db_user_delete(db, user=""):
    if user != "":
        db.session.delete(user)
    db.session.commit()


def commit_db_mail_delete(db, mail=""):
    if mail != "":
        db.session.delete(mail)
    db.session.commit()


def get_config():
    config = ConfigParser()
    config.read('config.ini')
    return config


def upload_file(URL):
    config = get_config()
    open(config["Files"]["URL"], 'wb').write(open(URL, 'rb').read())
