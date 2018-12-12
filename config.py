#!/use/bin/python3
#-*- coding:utf-8 -*-
#@Author:luoyongcan
#@Time:2018年10月29日09时
#说明:
#总结:

import os
#调试模式是否开启
DEBUG=True
#密钥 随机24位
SECRET_KEY=os.urandom(24)

#数据库
DIALECT='mysql'
DRIVER='mysqldb'
USERNAME='root'
PASSWORD='root'
HOST='127.0.0.1'
PORT='3306'
DATABASE='zx'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format\
    (DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS=False
