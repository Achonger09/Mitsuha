#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client
import hashlib
import urllib
import random
import json
import time

class transport(object):

    def __init__(self):
        print("trabsport init")
        self.SLEEPTIME = 1
        self.NONE = "result is None"
        self.DICTERR = "result dict Error"
        result_key = dict()
        result_key["from"] = "from"
        result_key["to"] = "to"
        result_key["trans_result"] = "trans_result"
        self.result_key = result_key
        trans_result_key = dict()
        trans_result_key["src"] = "src"
        trans_result_key["dst"] = "dst"
        self.trans_result_key = trans_result_key
        self.appid = '20200130000378770'  # 填写你的appid
        self.secretKey = '7StJaENtnjcS9x1A6BJO'  # 填写你的密钥
        self.httpClient = None
        self.myurl = '/api/trans/vip/translate'
        self.server = "api.fanyi.baidu.com"

    def get_url(self,query,fromLang='auto',toLang='zh'):
        salt = random.randint(32768, 65536)
        sign = self.appid + query + str(salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = self.myurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(query) + '&from=' + fromLang + '&to='\
                + toLang + '&salt=' + str(salt) + '&sign=' + sign
        return myurl

    def do_transe(self,url):
        try:
            httpClient = http.client.HTTPConnection(self.server)
            httpClient.request('GET', url)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            return result
        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()

    def get_transport_result(self,result):
        print("result: "+str(result))
        if len(result) == 0:
            return self.NONE
        if isinstance(result,dict):
            if self.result_key["trans_result"] in result:
                trans_result = result[self.result_key["trans_result"]]
                des_list = map(lambda x:x[self.trans_result_key["dst"]],trans_result)
                des_result = ','.join(des_list)
                return des_result
            else:
                return self.DICTERR
        else:
            return self.DICTERR

    def transport_signal(self,query,toLang="zh"):
        #print("222"+toLang)
        url = self.get_url(query,toLang=toLang)
        result_json = self.do_transe(url)
        result = self.get_transport_result(result_json)
        print("result:"+result)
        return result

    def transport_word(self,query,toLang="zh"):
        if self.is_chinese(query):
            toLang = "en"
        #print("##"+toLang)
        if isinstance(toLang ,list):
            print("yes")
            result_list = list()
            for lang in toLang:
                time.sleep(self.SLEEPTIME)
                result_tmp = self.transport_signal(query,lang)
                result_list.append("%s:%s" %(lang,result_tmp))
            result = "\n".join(result_list)
            return result
        else:
            #print("111 :"+ toLang)
            result =  self.transport_signal(query,toLang)
            return result

    def is_chinese(self,query):
        for ch in query:
            print(ord(ch))
            if  ord(ch) > 122:
               return True
        return False