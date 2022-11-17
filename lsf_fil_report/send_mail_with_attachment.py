#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

# 第三方SMTP服务
mail_host = 'smtp.qq.com'
mail_user = '375540509@qq.com'
mail_pass = 'jtoibirxqxmwbiia'

sender = '375540509@qq.com'
receivers = ['jiankong@npool.com','nicholas.liu@npool.com']
#receivers = ['jiankong@npool.com']


#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = '375540509@qq.com'   #发送者
message['To'] = '刘少锋'   #接收者
# 邮件标题
subject = '4个节点概要信息'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('node_ids=[“f01876488”,“f01953944”,"01953959","f079815"]\n\nroot@HK-TGT-DHF-H09-U31-HP380-HX1060-JUMP lsf_fil_report', 'plain', 'utf-8'))

# #添加附件
# part = MIMEApplication(open('f01211859.csv', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="f01211859.csv")
# message.attach(part)
#
# #添加附件2
# part = MIMEApplication(open('f01876488.csv', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="f01876488.csv")
# message.attach(part)


def add_attachment(attachment_name):
    part = MIMEApplication(open(attachment_name, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=attachment_name)
    message.attach(part)

def send_mail():
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()

if __name__ == '__main__':
    add_attachment()
    send_mail()


