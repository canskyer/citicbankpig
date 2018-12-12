#!/use/bin/python3
#-*- coding:utf-8 _*-
"""
@version: v1.0
@author: luoyongcan
@contact: canskyer@foxmail.com
@software: PyCharm
@file: 涂猪.py
@time: 2018/12/11 13:47
"""
import requests
import time
import json
import urllib3
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def zhuli(cookie,reqbody,idlist):
    # 填写你自己的cookies
    cookie=cookie.strip()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'Referer': 'https://servicewechat.com/wx13b9861d3e9fcdb0/10/page-frame.html',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                             ' Mobile/16B92 MicroMessenger/6.7.4(0x1607042c) NetType/4G Language/zh_CN',
               'Accept': '*/*', 'Content-Type': 'application/json;charset=utf-8',
               'Cookie': cookie}

    # reqbody = json.loads(reqbody)
    # reqbody['wx_nickname'] = 'sss'
    # r = requests.post('https://s.creditcard.ecitic.com/citiccard/gwapi/winterpig/assistance/enjoy', data=reqbody,
    #                   headers=headers, verify=False)
    # print(r.text)

    for i in idlist:
        print('原来的'+reqbody)
        data = json.loads(reqbody)
        data['wx_nickname'] = 'sss'
        data['unionidDst'] = i
        data = '%s' % data
        print('新' + data)
        r = requests.post('https://s.creditcard.ecitic.com/citiccard/gwapi/winterpig/assistance/enjoy', data=data, headers=headers,verify=False)
        print(r.text)
        time.sleep(1)

if __name__ == "__main__":
    pass
