#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http.client
import hashlib
import urllib
import json

class weather(object):

    def __init__(self):
        self.host= "v.juhe.cn"
        self.url = "/weather/index"
        self.appID = "ff28f76feea513a00a29938bb4457b41"
        self.city_name = "南京"
        self.DICTERROR= "result dict error"
        self.CONNECTERROR = "connect error"
        self.today_format = "日期：%s\n天气：%s\n温度：%s\n城市：%s\n感觉：%s\n建议：%s"
        self.result = {
            "resultcode":"200",
            "reason":"successed!",
            "result":{
                "sk":{
                    "temp":"5",
                    "wind_direction":"西北风",
                    "wind_strength":"2级",
                    "humidity":"52%",
                    "time":"19:26"
                },
                "today":{
                    "temperature":"-2℃~8℃",
                    "weather":"晴",
                    "weather_id":{
                        "fa":"00",
                        "fb":"00"
                    },
                    "wind":"西北风微风",
                    "week":"星期四",
                    "city":"南京",
                    "date_y":"2020年01月30日",
                    "dressing_index":"较冷",
                    "dressing_advice":"建议着厚外套加毛衣等服装。年老体弱者宜着大衣、呢外套加羊毛衫。",
                    "uv_index":"中等",
                    "comfort_index":"",
                    "wash_index":"较适宜",
                    "travel_index":"较不宜",
                    "exercise_index":"较不宜",
                    "drying_index":""
                },
                "future":{
                    "day_20200130":{
                        "temperature":"-2℃~8℃",
                        "weather":"晴",
                        "weather_id":{
                            "fa":"00",
                            "fb":"00"
                        },
                        "wind":"西北风微风",
                        "week":"星期四",
                        "date":"20200130"
                    },
                    "day_20200131":{
                        "temperature":"-1℃~10℃",
                        "weather":"晴转多云",
                        "weather_id":{
                            "fa":"00",
                            "fb":"01"
                        },
                        "wind":"东南风微风",
                        "week":"星期五",
                        "date":"20200131"
                    },
                    "day_20200201":{
                        "temperature":"0℃~12℃",
                        "weather":"多云",
                        "weather_id":{
                            "fa":"01",
                            "fb":"01"
                        },
                        "wind":"东风微风",
                        "week":"星期六",
                        "date":"20200201"
                    },
                    "day_20200202":{
                        "temperature":"3℃~13℃",
                        "weather":"多云转阴",
                        "weather_id":{
                            "fa":"01",
                            "fb":"02"
                        },
                        "wind":"东风微风",
                        "week":"星期日",
                        "date":"20200202"
                    },
                    "day_20200203":{
                        "temperature":"4℃~8℃",
                        "weather":"多云",
                        "weather_id":{
                            "fa":"01",
                            "fb":"01"
                        },
                        "wind":"东风微风",
                        "week":"星期一",
                        "date":"20200203"
                    },
                    "day_20200204":{
                        "temperature":"0℃~12℃",
                        "weather":"多云",
                        "weather_id":{
                            "fa":"01",
                            "fb":"01"
                        },
                        "wind":"东风微风",
                        "week":"星期二",
                        "date":"20200204"
                    },
                    "day_20200205":{
                        "temperature":"-1℃~10℃",
                        "weather":"晴转多云",
                        "weather_id":{
                            "fa":"00",
                            "fb":"01"
                        },
                        "wind":"东南风微风",
                        "week":"星期三",
                        "date":"20200205"
                    }
                }
            },
            "error_code":0
        }

    def get_url(self):
        #city_name_encode = self.city_name.encode("utf-8")
        data = {
            "cityname":self.city_name,
            "key":self.appID
        }
        data_encode = urllib.parse.urlencode(data)
        url_format = "%s?%s" %(self.url,data_encode)
        print(url_format)
        return url_format

    def do_query(self,url):
        try:
            httpClient = http.client.HTTPConnection(self.host)
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

    def format_result(self,result_json):
        print(self.result)
        result_json = self.result
        if not isinstance(result_json,dict):
            return self.DICTERROR
        if not result_json["resultcode"] == "200" or not result_json["error_code"] == 0 :
            reason = result_json["reason"]
            return "%s:%s" %(self.CONNECTERROR,reason)
        result = result_json["result"]
        today = result["today"]
        today_data = today["date_y"]  ##日期
        today_weather = today["weather"]  ##天气
        today_temperature = today["temperature"] ##温度
        city = today["city"]
        dressing_index = today["dressing_index"]
        dressing_advice = today["dressing_advice"]
        future = result["future"]
        today_format = "日期：%s\n天气：%s\n温度：%s\n城市：%s\n感觉：%s\n建议：%s"
        today_show = today_format %(today_data,today_weather,today_temperature,city,dressing_index,dressing_advice)
        return today_show

    def get_today_info(self):
        url = self.get_url()
        #result_json = self.do_query(url)
        result_json=""
        result_info = self.format_result(result_json)
        return result_info


