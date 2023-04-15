import paramiko  #导入第三方库
import time   #导入时间库
ssh1=paramiko.SSHClient()   #定义SSH会话通道名字为  ssh1
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #定义默认的密钥处理策略
ssh1.connect(hostname='203.0.113.11',port=22,username='saiban',password='saiban',timeout=5,allow_agent=False,look_for_keys=False)   #建立SSH会话连接
time.sleep(15)   # 等待暂停15秒
ssh1.close()   #关闭连接
