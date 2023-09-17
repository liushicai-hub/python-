import paramiko  #导入第三方库
import time   #导入时间库
import getpass

username = input('Username: ')
password = getpass .getpass('Password: ')

f = open("ip_list.txt" ,'r')
for line in f.readlines():
 ip = line.strip()
 ssh1 = paramiko.SSHClient()   #定义SSH会话通道名字为  ssh1
 ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #定义默认的密钥处理策略
 ssh1.connect(hostname=ip,username=username,password=password,timeout=5,allow_agent=False,look_for_keys=False)   #建立SSH会话连接
 command = ssh1.invoke_shell()
 command.send("configure terminal\n")
 command.send("do show ip int br\n")
 command.send("end")
 time.sleep(15)   # 等待暂停15秒
 output = command.recv(65536)

# command. recv ( 中的 65535 代表 截取 65535 个字符的回 显 内容，这也是 Paramiko 一次能截取的最大 回显 内容数。另外，内容数。另外，
# 与 Telnetlib 类似，在 Python 3 中， Paramiko 截取的回 显 内容格式为字节型字符串，需要
# 用 decode(" ascii 将其解析为 ASCII 编码，否则打印出来的 output 的内容格式会很难看
 print(output.decode("ascii"))
ssh1.close()   #关闭连接