import paramiko
import time
from B00_DeviceCredentials import DeviceInfo


DeviceName = DeviceInfo['Sw1']['DeviceName']
HostIP = DeviceInfo['Sw1']['HostIP']
UserName = DeviceInfo['Sw1']['UserName']
Password = DeviceInfo['Sw1']['Password']


def SshClient(SshHostIp, UserName, Password,CLIs):
    ssh = paramiko.SSHClient()  # 实例化SSH会话通道
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 定义默认的密钥处理策略
    ssh.connect(SshHostIp, port=22, username=UserName, password=Password, timeout=5, compress=True,
                allow_agent=False,look_for_keys=False)  # 建立SSH会话连接
    Shell = ssh.invoke_shell()  # 实例化交互式shell
    Shell.recv(9999)  # 接收回显
    time.sleep(0.5)
    for CLI in CLIs:  # 以for循环逐个执行cli命令，并接收回显
        Shell.send(CLI.encode() + b'\n')
        time.sleep(0.5)
        SysLog = Shell.recv(9999).decode()
        time.sleep(1)
        print(SysLog)
    Shell.close()
    ssh.close()


if __name__ == '__main__':
    CLIs = [
        'terminal length 0',
        'show running-config'
    ]

    SshClient(HostIP, UserName, Password, CLIs)



