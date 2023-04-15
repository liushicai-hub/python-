import time
from B00_DeviceCredentials import DeviceInfo
from B02_SshClient import SshClient
from B03_RecordToFile import SaveLog
import datetime


Now = str(datetime.datetime.now())[0:19].replace(' ','_') #get datetime now


def CensorChoiceCLI(CLI=["terminal length 0", "terminal monitor"], Choice='show run'):
    if Choice == 'show run':
        CLIs = CLI + ['show running-config']
    elif Choice == 'cdp':
        CLIs = CLI + ['show cdp neighbor']
    elif Choice == 'interface':
        CLIs = CLI + ['show ip interface brief']
    elif Choice == 'route':
        CLIs = CLI + ['show ip route']
    else:
        CLIs = ['exit']
        print('No meaning chioce')
    return CLIs


if __name__ == '__main__':
    InputChoice = input('show run \n'
                        'cdp \n'
                        'interface \n'
                        'route \n'
                        'Enter your choice:')
    for Device in DeviceInfo:
        DeviceName = DeviceInfo[Device]['DeviceName']
        HostIP = DeviceInfo[Device]['HostIP']
        UserName = DeviceInfo[Device]['UserName']
        Password = DeviceInfo[Device]['Password']

        H = SshClient(HostIP, UserName, Password)
        ssh = H[0]
        Shell = H[1]

        CensorCLIs = CensorChoiceCLI(Choice=InputChoice)

        for CLI in CensorCLIs:
            Shell.send(CLI.encode() + b'\n')
            time.sleep(0.5)
            SysLog = Shell.recv(9999).decode()
            print(SysLog)
            SaveLog(DeviceName+'_'+InputChoice+'_'+Now+'.txt',SysLog)
        Shell.close()
        ssh.close()

