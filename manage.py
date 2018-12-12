#!/use/bin/python3
#-*- coding:utf-8 -*-
#@Author:luoyongcan
#@Time:2018年11月02日13时
#说明:在models那边新增或者修改模型后，命令行CD到这个文件目录下 然后 python manage.py db migrate ,再pyhton manage.py db upgrade
#总结:

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sky import app
from exts import db
from models import Userinfo,Piguser

#绑定app
manager = Manager(app)

#使用Migrate绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()