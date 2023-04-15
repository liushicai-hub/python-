import telnetlib
import time
from B00_DeviceCredentials import DeviceInfo

DeviceName = DeviceInfo['Sw1']['DeviceName']
HostIP = DeviceInfo['Sw1']['HostIP']
UserName = DeviceInfo['Sw1']['UserName']
Password = DeviceInfo['Sw1']['Password']


def TNClient(DeviceName, HostIP, UserName, Password):
    tn = telnetlib.Telnet(HostIP)  # 实例化telnet连接对象
    tn.read_until(b'Username:')  # 读取回显，直到这个字符串
    tn.write(UserName.encode('ascii') + b"\n")  # 以字节码方式输入密码并回车
    tn.read_until(b'Password:')  # 读取回显，直到这个字符串
    tn.write(Password.encode('ascii') + b"\n")  # 以字节码方式输入密码并回车
    tn.read_until('{}#'.format(DeviceName).encode('ascii'))  # 读取到指定字节码
    tn.write('terminal length 0'.encode('ascii') + b"\n")
    tn.read_until('{}#'.format(DeviceName).encode('ascii'))
    tn.write('show run'.encode('ascii') + b"\n")
    time.sleep(0.5)  # 给计算机一点计算和通信的时间
    RuningCfg = DeviceName + '\n' + tn.read_very_eager().decode('ascii').replace('\r\n', '\n')  # 回忆回车和换行
    tn.close()
    print(RuningCfg)


if __name__ == '__main__':
    TNClient(DeviceName, HostIP, UserName, Password)

