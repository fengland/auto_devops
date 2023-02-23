#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

class SendMail:
    def __init__(self,receivers):
        # 第三方SMTP服务
        self.mail_host = 'smtp.qq.com'
        self.mail_user = '375540509@qq.com'
        self.mail_pass = 'xuhadtxwcmxibhgc'
        self.sender = '375540509@qq.com'
        self.receivers = receivers

        # 创建一个带附件的实例
        self._message = MIMEMultipart()
        self._message['From'] = '375540509@qq.com'
        self._message['To'] = 'all'

        # 邮件标题
        self.subject = 'fault_sector_count ALERT'
        # self._message['Subject'] = Header(self.subject,'utf-8')

        # 邮件正文
        self.MAIL_CONTENT = """
        """
    def mail_subject(self,subject):
        self.subject=subject
        self._message['Subject'] = Header(self.subject, 'utf-8')
    def mail_receivers(self,receivers):
        self.receivers=receivers

    def mail_content(self,MAIL_CONTENT):
        self._message.attach(MIMEText(f'{MAIL_CONTENT}', 'plain', 'utf-8'))

    # 添加附件
    def add_attachment(self,attachment_name):
        part = MIMEApplication(open(attachment_name, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=attachment_name)
        self._message.attach(part)

    # 发送邮件
    def send_mail(self):
        smtpObj = smtplib.SMTP()
        smtpObj.connect(self.mail_host, 25)
        smtpObj.login(self.mail_user, self.mail_pass)
        smtpObj.sendmail(self.sender, self.receivers, self._message.as_string())
        smtpObj.quit()

if __name__ == '__main__':
    # add_attachment()
    aleo_sendmail=SendMail()
    aleo_sendmail.mail_content("test message")
    aleo_sendmail.add_attachment('account.info')
    aleo_sendmail.send_mail()