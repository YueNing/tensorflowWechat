#coding=utf-8
import itchat
import requests
import datetime
from itchat.content import *

def dateTime():
    return datetime.datetime.now()


KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'ningwechat-Robot'
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(TEXT)
def tuling_reply(msg):
    if msg.user.UserName == 'filehelper': print ('%s:%s:%s'% (dateTime(), msg.user.UserName, msg['Text']))
    else: print ('%s:%s:%s'% (dateTime(), msg.user.NickName, msg['Text']))
    defaultReply = 'I received:' + msg['Text']
    reply = get_response(msg['Text'])
    print ('%s:Turling: %s'% (dateTime(), reply))
    return reply or defaultReply

itchat.auto_login(hotReload=True, enableCmdQR=True)
itchat.run()