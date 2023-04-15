import paramiko  # 导入第三方库
import time  # 导入时间库

ssh1 = paramiko.SSHClient()  # 定义SSH会话通道名字为  ssh1
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 定义默认的密钥处理策略
ssh1.connect(hostname='203.0.113.11', port=22, username='saiban', password='saiban', timeout=5, allow_agent=False,
             look_for_keys=False)  # 建立SSH会话连接

Shell = ssh1.invoke_shell()  # 实例化一个交互式shell
time.sleep(0.5)  # 给脚本和设备的数据交互一点时间
Syslog = Shell.recv(9999).decode()  # 接收回显并赋予变量标识符
print(Syslog)  # 打印回显变量
Shell.send('terminal length 0 \n'.encode())  # 发送CLI指令
time.sleep(0.5)
Syslog = Shell.recv(9999).decode()
print(Syslog)
Shell.send('show running-config \n'.encode())
time.sleep(1)
Syslog = Shell.recv(9999).decode()
print(Syslog)
time.sleep(15)  # 等待暂停15秒
ssh1.close()  # 关闭连接
