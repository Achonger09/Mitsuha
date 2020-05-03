#!/usr/bin/env python
# -*- coding: utf-8 -*-

from transport import *
from weather import *
from handle_email import *

class HandleMessage(object):
    def __init__(self):
        pass

    def handle_message(self,message):
        if message == "天气" or message == "weather":
            we = weather()
            info  = we.get_today_info()
            return info
        elif message.startswith("http"):
            email = HandleEmail("smtp.139.com")
            email.email_me()
        else:
            tr = transport()
            content = tr.transport_word(message)
            return content

