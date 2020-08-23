# _*_ coding:utf-8 _*_

import os,sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import configparser
from config import setting
from public.models import newReport

def send_email(filePath):
    """
    定义发送邮件
    :param filePath:
    :return: 成功：打印发送邮箱成功；失败：返回失败信息
    """
    f = open(filePath,'rb')
    mail_body = f.read()
    f.close()

    # 添加附件
    con = configparser.ConfigParser()
    con.read(setting.CONFIG_DIR, encoding='utf-8')
    report = newReport(setting.TEST_REPORT)
    sendfile = open(report,'rb').read()

    # --------- 读取config.ini配置文件 ---------------
    HOST = con.get("user", "HOST_SERVER")
    SENDER = con.get("user", "FROM")
    RECEIVER = con.get("user", "TO")
    USER = con.get("user", "user")
    PWD = con.get("user", "password")
    SUBJECT = con.get("user", "SUBJECT")

    # ---------邮件内容设置-------------
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", report))

    msg = MIMEMultipart('related')
    msg.attach(att)
    msgtext = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgtext)
    msg['Subject'] = SUBJECT
    msg['from'] = SENDER
    msg['to'] = RECEIVER

    # -----------发送邮件-------------
    try:
        server = smtplib.SMTP()
        server.connect(HOST)
        server.starttls()
        server.login(USER,PWD)
        server.sendmail(SENDER,RECEIVER,msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as  e:
        print("失败: " + str(e))