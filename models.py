#!/use/bin/python3
#-*- coding:utf-8 -*-
#@Author:luoyongcan
#@Time:2018年11月02日13时
#说明: 用法 新增或修改模型后到manage.py那边引入
#总结:
from datetime import datetime
from exts import db

class Userinfo(db.Model):
    __tablename__='userinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reqhead=db.Column(db.String(5000),nullable=False)
    reqbody=db.Column(db.String(5000),nullable=False)
    regtime = db.Column(db.Date, nullable=False)

class Piguser(db.Model):
    __tablename__ = 'piguser'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pigid=db.Column(db.String(1000),nullable=False)