#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText#专门发送正文
from email.mime.multipart import MIMEMultipart#发送多个部分
from email.mime.application import MIMEApplication#发送附件
from email.mime.image import MIMEImage

class HandleEmail(object):

    def __init__(self,host,port=25):
        self.host = host      # 设置发件服务器地址
        self.port =port       # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
        print("init")

    def init_email(self,sender = None,password = None,receiver = None,subject = None,context = "",
                   image = None,attach_image = None,attach_file = None):
        self.sender,self.receiver = sender,receiver
        self.password = password
        self.mail_from,self.mail_to = sender,receiver
        self.subject,self.context = subject,context
        self.image = image
        self.attach_image,self.attach_file = attach_image,attach_file

    def product_msg(self):
        msg = MIMEMultipart()
        msg["Subject"] = self.subject
        msg["From"] = self.mail_from
        msg["To"] = self.mail_to
        if self.image :
            message_html = MIMEText("<p>%s</p><img src=\"cid:images\">" %self.context , 'html', 'utf8')
            msg.attach(message_html)
            data = open(self.image, 'rb')
            message_img = MIMEImage(data.read())
            data.close()
            message_img.add_header('Content-ID', 'images')
            msg.attach(message_img)
        else:
            message_html =  MIMEText("<p>%s</p>" % self.context, 'html', 'utf8')
            msg.attach(message_html)
        if self.attach_image:
            with open(self.attach_image, 'rb') as f:
                msgImage = MIMEImage(f.read())
                msgImage.add_header('Content-ID', '<image1>')
                msg.attach(msgImage)
        if self.attach_file:
            part_attach = MIMEApplication(open(self.attach_file,"rb").read())
            part_attach.add_header("Content-Disposition","attachment",filename = self.attach_file)
            msg.attach(part_attach)
        return msg

    def send_email(self,msg):
        smtp = smtplib.SMTP()
        smtp.connect(self.host,self.port)
        smtp.login(self.sender, self.password)  # 登陆邮箱
        smtp.sendmail(self.sender, self.receiver, msg.as_string())  # 发送邮件！
        print("邮件发送成功!")

    def email_me(self,title = "Test",context = "Context",image=None,attach_file=None):
        print("email me")
        sender = receiver = "18851009517@139.com"
        password = "ZYC199299zyc"
        self.init_email(sender = sender,password = password,receiver = receiver,subject=title,
                        context = context,image = image,attach_image=None,attach_file=attach_file)
        msg = self.product_msg()
        print("get msg")
        self.send_email(msg)

