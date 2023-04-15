import time
from B00_DeviceCredentials import DeviceInfo
from B02_SshClient import SshClient
from B03_RecordToFile import SaveLog
import datetime
from random import choice
import string


Now = str(datetime.datetime.now())[0:19].replace(' ','_') #get datetime now


def random_password():
    length = 4
    first1 = choice(string.ascii_letters).upper()
    first2 = str(choice(string.digits))
    first4 = choice(string.ascii_letters).lower()
    first3 = choice('!@')
    last = ''.join(choice(string.ascii_letters + string.digits) for i in range(length))
    return first1 + first2 + first3 + first4 + last


def AddUser(Shell,UserName1,Password1):
    CLIs = [
        'terminal length 0',
        'terminal monitor',
        'config terminal',
        f'username {UserName1} password {Password1}',
        'end'
    ]

    for CLI in CLIs:
        Shell.send(CLI.encode() + b'\n')
        time.sleep(0.5)
        SysLog = Shell.recv(9999).decode()
        print(SysLog)
        SaveLog(DeviceName + '_AddUser_' + Now + '.txt', SysLog)
    Shell.close()
    ssh.close()


if __name__ == '__main__':
    for Device in DeviceInfo:
        DeviceName = DeviceInfo[Device]['DeviceName']
        HostIP = DeviceInfo[Device]['HostIP']
        UserName = DeviceInfo[Device]['UserName']
        Password = DeviceInfo[Device]['Password']

        H = SshClient(HostIP, UserName, Password)
        ssh = H[0]
        Shell = H[1]

        UserName1 = UserName + '1024'
        Password1 = random_password()

        AddUser(Shell, UserName1, Password1)

