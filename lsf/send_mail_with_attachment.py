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
mail_pass = '42412klkjjh23kj4lk'

sender = '375540509@qq.com'
receivers = ['jiankong@npool.com','devops@npool.com','nicholas.liu@npool.com']


#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = '375540509@qq.com'   #发送者
message['To'] = '刘少锋'   #接收者
# 邮件标题
subject = 'POST账户余额不足告警'
message['Subject'] = Header(subject, 'utf-8')

MAIL_CONTENT='''

'''
#邮件正文内容
def mail_content(MAIL_CONTENT):
    message.attach(MIMEText(f'{MAIL_CONTENT}', 'plain', 'utf-8'))

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
    # add_attachment()
    mail_content(MAIL_CONTENT)
    send_mail()

