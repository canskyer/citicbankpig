#!/use/bin/python3
#-*- coding:utf-8 -*-
#@Author:luoyongcan
#@Time:2018年10月29日09时
#说明:
#总结:
import datetime
import json
from flask import Flask, request, render_template
import requests
import urllib3
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import session,redirect,url_for
from exts import db
from models import Userinfo,Piguser
from shuapig import zhuli
from pig import uppig


import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/go',methods=['GET','POST'])
#注册
def go():
    if request.method=='GET':
        return render_template('index.html',message=None)
    else:
        reqhead = request.form.get('reqhead')
        reqbody = request.form.get('reqbody')
        #查找用户的猪ID
        pigflag=reqbody.find('"unionidDst":"')
        if pigflag:
            pigflag+=14
            pigid=reqbody[pigflag:59]
        #查找用户cookies
        flag=reqhead.find('citicbank')
        if flag:
            usercookies = reqhead[flag:flag+291]
            #print('用户的cookies是:'+usercookies)
            if reqhead != None and reqbody != None:
                regtime = datetime.datetime.now().strftime('%Y-%m-%d')
                userinfo = Userinfo(reqhead=usercookies, reqbody=reqbody, regtime=regtime)
                piguser = Piguser(pigid=pigid)

                db.session.add(userinfo)
                db.session.add(piguser)
                db.session.commit()
                idlist = []
                allpiguser = Piguser.query.filter(Piguser.id<200).all()
                for piguser in allpiguser:
                    idlist.append(piguser.pigid)
                #print('开始助力')
                #zhuli(cookie=usercookies,reqbody=reqbody,idlist=idlist)
                return render_template('index.html',message='成功，请耐心等待')
            else:
                return render_template('index.html',message='输出错误，请检查输入内容')

@app.route('/iphelp',methods=['GET'])
def iphelp():
    return render_template('helpiphone.html')

@app.route('/anhelp',methods=['GET'])
def anhelp():
    return render_template('helpandroid.html')

if __name__ == '__main__':
    app.run()
