import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from B08_ping import Ping
from B00_DeviceCredentials import DeviceInfo
# 为保护隐私，我的用户名和密码存在了一个python模块里
from Secret import UserName, Password, receivers

# 定义邮件内容
EmailContent = '报告主人，你的喵需要喝水！'


# 定义发送邮件的函数
def sent_email(receivers, EmailContent, File):
    sender = UserName
    # 三个参数：第一个为邮件正文文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEMultipart()  # 实例化一个带附件的邮件
    message.attach(MIMEText(EmailContent, 'plain', 'utf-8'))  # 邮件正文
    message['From'] = formataddr(['邮件来自塞班', sender])  # 给定发送者
    message['To'] = formataddr(['塞班的爸爸', receivers])  # 给定接收者
    message['Subject'] = Header('欢迎加入喵星', 'utf-8')  # 定义邮件主题

    # 构造附件，传送 test.txt 文件
    att = MIMEText(open(File, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="DeviceReport.txt"'
    message.attach(att)

    smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)  # 使用ssl
    smtpObj.login(UserName, Password)  # 邮箱登录信息
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮件
    smtpObj.quit()
    print('邮件发送成功')


if __name__ == '__main__':
    File = 'B09_ping_DeviceReport.txt'

    for Device in DeviceInfo:
        DeviceName = DeviceInfo[Device]['DeviceName']
        HostIP = DeviceInfo[Device]['HostIP']
        with open(File,mode='a') as f:
            f.write(f'\n\n{DeviceName} ping report \n')
        Ping(HostIP, File)

    # 发送邮件
    sent_email(receivers, EmailContent, File)
