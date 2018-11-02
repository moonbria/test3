from datetime import datetime
from flask_script import Manager

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy

from nerverthanless import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/nerverthanless"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "chicya"
db = SQLAlchemy(app)


Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    visit_url = db.Column(db.String(256))
    visit_time = db.relationship("VisitLog", backref="user", lazy="dynamic")


class VisitLog(BaseModel, db.Model):
    __tablename__ = "visit"
    id = db.Column(db.Integer, primary_key=True)
    visit_url = db.Column(db.String(256))
    visit_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    success = db.Column(db.Enum("True", "False"),default="False")
    tells_id = db.Column(db.Integer, default=0)
    onetell = db.relationship("AfterStory", backref="visit", lazy="dynamic")


class AfterStory(BaseModel, db.Model):
    __tablename__ = "tells"
    id = db.Column(db.Integer, primary_key=True)
    tells = db.Column(db.String(256))

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    tel1 = AfterStory(tells="1")
    db.session.add(tel1)
    db.session.commit()
    manager.run()