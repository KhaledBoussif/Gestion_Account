from configparser import ConfigParser
from flask import request
import pandas
from website.SERVICE.Service import creat_engine_db, get_config, upload_file
from sqlalchemy import create_engine

import pdb

config = get_config()
engine = creat_engine_db()


def getURLfilefunction():
    URL = request.args.get('CSV')
    upload_file(URL)
    df = pandas.read_csv(config["Files"]["URL"])
    with engine.begin() as connection:
        df.to_sql('user', connection, if_exists='append', index=False)

    return format("file Uploaded !")
