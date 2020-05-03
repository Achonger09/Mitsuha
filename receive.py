#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

class receive(object):
    def parse_xml(web_data):
        #print("in parse_xml")
        #print("len: %d" % len(web_data))
        if len(web_data) == 0:
            return None
        #print("####" + str(web_data,encoding = "utf-8"))
        xmlData = ET.fromstring(str(web_data,encoding = "utf-8"))
        #print("xmlData:"+ str(xmlData))
        msg_type = xmlData.find('MsgType').text
        #print("msg_type:"+msg_type)
        if msg_type == 'text':
            #print("is text")
            return TextMsg(xmlData)
        elif msg_type == 'image':
            return ImageMsg(xmlData)

class Msg(object):
    def __init__(self, xmlData):
        print("Msg init")
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text
        #print("T,F,C,M,M:%s,%s,%s,%s,%s" %(self.ToUserName,self.FromUserName,self.CreateTime,self.MsgType,self.MsgId))

class TextMsg(Msg):
    def __init__(self, xmlData):
        #print("msg init")
        Msg.__init__(self, xmlData)
        #print("before content")
        #print("Content encode:"+str(xmlData.find('Content').text.encode("utf-8")))
        self.Content = xmlData.find('Content').text.encode("utf-8")
        self.Content = str(self.Content,encoding = "utf-8")
        #print("Content:"+ self.Content)


class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text