#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyping
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr
from email.utils import formataddr

def format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,"utf-8").encode(),addr))

url = '93.179.98.182'
# url = 'www.baidu.com'

mail_host = 'smtp.126.com'
mail_user = 'rushiwo'
mail_pass = ''

sender = 'rushiwo@126.com'
receivers = ['rushiwo@126.com']

message = MIMEText('vps ip 可用','plain','utf-8')
message['From'] = format_addr("%s" %(sender))
print(message['From'])
message['To'] = format_addr("%s" %(receivers[0]))
message['Subject'] = Header('vps ip' + url + '可用','utf-8')



while True:

    r = pyping.ping(url)
    if r.ret_code == 0:
        print('ping host :' + url + ' success!\n')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host,25)
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender,receivers,message.as_string())
            smtpObj.quit()
            print('邮件发送成功\n')
        except smtplib.SMTPException as e:
            print('Error: 无法发送邮件\n' + str(e))

        break
    else:
        print('ping host :' + url + ' failed!\n')
    time.sleep(3600)
