from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib import parse
from configparser import ConfigParser
import os


# ============ 加载数据库配置 ================
def uri_encode(origin_str: str) -> str:
    return parse.quote_plus(origin_str)

configParser = ConfigParser()
configParser.read("%s/config/database.ini" % Flask.app.root)
db_config = dict(configParser.items(Flask.app.env))

driver = db_config['driver']
username = uri_encode(db_config['username'])
password = uri_encode(db_config['password'])
host = db_config['host']
port = db_config['port']
database = db_config['database']
pool = int(db_config['pool'])
timeout = db_config['timeout']


# ============ 创建数据库连接池 ==================
Flask.app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s:%s/%s' % (driver, username, password, host, port, database)
Flask.app.config['SQLALCHEMY_POOL_SIZE'] = pool
Flask.app.config['SQLALCHEMY_POOL_TIMEOUT'] = timeout
Flask.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #if Flask.app.env == 'production' else True
Flask.app.config['SQLALCHEMY_ECHO'] = False#True if Flask.app.config['debug'] == 'True' else False
Flask.app.mysqldb = SQLAlchemy(Flask.app)
