#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import hashlib
import reply
from receive import *
from transport import *
from handle_message import *


class Handle(object):

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "wechatToken" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            print("token :%s,timestamp:%s,nonce:%s" %(token, timestamp, nonce))
            list.sort()
            list_str = ''.join(list)
            hashcode = hashlib.sha1(list_str.encode("utf8")).hexdigest()
            #sha1 = hashlib.sha1()
            #map(sha1.update, list)
            #hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: %s,%s", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except (Exception ) as ar:
            return ar
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is %s" % webData)   #后台打日志
            recMsg = receive.parse_xml(webData)
            #print(str(isinstance(recMsg, Msg)))
            #print(str(recMsg.MsgType))
            print("recMsg instanceof receive.Msg :%s, recMsg.MsgType:%s" %(str(isinstance(recMsg, Msg)),str(recMsg.MsgType)))
            if isinstance(recMsg, Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    handle_mess = HandleMessage()
                    print(recMsg.Content)
                    content = handle_mess.handle_message(recMsg.Content)
                    print("##########:"+content)
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    print("toUser:%s,fromUser:%s,info:%s" %(str(toUser),str(fromUser), str(recMsg.Content).encode("utf-8")))
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print("暂且不处理")
                return reply.Msg().send()
        except Exception as ar:
            return ar
