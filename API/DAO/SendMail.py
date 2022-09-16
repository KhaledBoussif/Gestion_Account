from website.DAO.CRUD import getAllUsersfunction, getMailbyIdfunction
from email.message import EmailMessage
from website.MODELS.BoitEmail import BoitEmail
from website.SERVICE.Service import commit_db_mail, get_config
from website import db
import smtplib


import pdb


config = get_config()


def SendMailfunction():

    users = getAllUsersfunction()

    for user in users:
        # pdb.set_trace()
        if getMailbyIdfunction(user.id) is None and user.PNP:
            msg_Content = 'Bonjour Monsieur ' + user.Nom + ' ' + user.Prenom + \
                ',\n\nVous êtes le bienvenue sur notre site ! \n\nCordialement,\n' + \
                config["Mail_Info"]["EMAIL_ADDRESS"]
            msg = EmailMessage()
            msg['Subject'] = 'Validation'
            msg['From'] = config["Mail_Info"]["EMAIL_ADDRESS"]
            msg['To'] = user.Email
            msg.set_content(msg_Content)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(config["Mail_Info"]["EMAIL_ADDRESS"],
                           config["Mail_Info"]["EMAIL_PASSWORD"])
                smtp.send_message(msg)
                New_Mail = BoitEmail(mail=msg_Content,
                                     user_email=user.Email, user_id=user.id)
                commit_db_mail(db, New_Mail)

            result = "Email Sended !!"
        else:
            result = "Email not Send !!"
    return format(result)
