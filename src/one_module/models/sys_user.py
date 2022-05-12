from flask import Flask
db = Flask.app.mysqldb

class SysUser(db.Model):
    __tablename__ = "sys_user"

    id = db.Column(db.String, primary_key=True)

    

    pass