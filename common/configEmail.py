#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/3/15 17:54
#Author:Chao
'''
1-读取配置，调用readconfig
2-创建邮件连接配置（host，username）
3-创建邮件内容（添加附件，report）
4-调用发送邮件的方法
'''
import smtplib
from email.mime.text import MIMEText
from common.readConfig import readConfig
class sendEmail(object):
    # -------------------------------------------------配置邮件属性------------------------------------------------
    r = readConfig()
    # 发送方邮箱
    sender = r.getEmail("sender")
    # 收件人邮箱，多个可以用list，单个如下
    # msg_to = ['**','**']
    receiver = r.getEmail("receiver")
    # 发送方邮箱账号
    username = r.getEmail("mail_user")
    # 发送方邮箱密码
    password = r.getEmail("mail_pass")
    # 发送方邮箱的服务器
    smtpserver = r.getEmail("mail_host")
    # -------------------------------------------------定义邮件最终配置信息------------------------------------------------
    def config_email(self):
        # 邮件主题
        subject = "邮件标题"
        # 邮件内容
        content = "邮件的内容"
        # 生成一个MIMEText对象（还有一些其他参数）
        self.msg = MIMEText(content)
        # 放入邮件主题
        self.msg['Subject'] = subject
        # 放入发件人
        self.msg['From'] = self.sender
        # 放入收件人
        self.msg['To'] = self.receiver
#-------------------------------------------------建立连接发送邮件------------------------------------------------
    def send_email(self):
        self.config_email()
        try:
            # 实例化smtp对象
            s = smtplib.SMTP()
            # 链接smtp服务器
            s.connect(self.smtpserver)
            # 登录
            s.login(self.username, self.password)
            # 发送邮件
            s.sendmail(self.sender, self.receiver, self.msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as msg:
            print(msg)
if __name__ == '__main__':
    r = sendEmail()
    r.send_email()