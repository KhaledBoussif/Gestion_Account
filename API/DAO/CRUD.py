import json
from flask import request
from website.MODELS.BoitEmail import BoitEmail
from website.MODELS.User import User
from website import db
from website.SERVICE.Service import commit_db_mail_delete, commit_db_user, commit_db_user_delete

import pdb


def getAllUsersfunction():
    users = User.query.all()
    print(users)
    return users


def getUserByIdfunction():
    ID = request.args.get('ID')
    user = User.query.filter_by(id=ID).first()
    print(user)
    return user


def DeleteUserByIdfunction():
    ID = request.args.get('ID')
    user = User.query.filter_by(id=ID).first()
    mail = BoitEmail.query.filter_by(user_id=ID).first()
    commit_db_user_delete(db, user)
    commit_db_mail_delete(db, mail)
    return format("Delete success !")


def DeleteAllfunction():
    User.__table__.drop(db.engine)
    BoitEmail.__table__.drop(db.engine)
    print("Table deleted !")
    db.create_all()
    commit_db_user(db)
    print("New Table Created !")
    return format("Table Created !")


def AddUserfunction():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        new_user = User(Email=json["Email"], Nom=json["Nom"],
                        Prenom=json["Prenom"], Adresse=json["Adresse"], PNP=json["PNP"])
        # pdb.set_trace()
        commit_db_user(db, new_user)
        return json
    else:
        return 'Content-Type not supported!'
    # user = request.args
    # new_user = User(Email=user["Email"], Nom=user["Nom"],
    #                 Prenom=user["Prenom"], Adresse=user["Adresse"], PNP=user["PNP"])
    # commit_db_user(db, new_user)
    # return format("User Add !")


def UpdateUserfunction():
    useratt = request.args
    user = User.query.filter_by(id=useratt["ID"]).first()
    if useratt["Email"] != "":
        user.Email = useratt["Email"]
    if useratt["Nom"] != "":
        user.Nom = useratt["Nom"]
    if useratt["Prenom"] != "":
        user.Prenom = useratt["Prenom"]
    if useratt["Adresse"] != "":
        user.Adresse = useratt["Adresse"]
    if useratt["PNP"] != "":
        user.PNP = useratt["PNP"]
    commit_db_user(db)
    print("user Updated !")
    return format("User Updated !")


def getMailbyIdfunction(id):
    result = BoitEmail.query.filter_by(user_id=id).first()
    print(result)
    return result
