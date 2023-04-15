import paramiko
import time
from B00_DeviceCredentials import DeviceInfo
import datetime
from B03_RecordToFile import SaveLog


Now = str(datetime.datetime.now())[0:19].replace(' ','_') #get datetime now
DeviceName = DeviceInfo['Sw1']['DeviceName']
HostIP = DeviceInfo['Sw1']['HostIP']
UserName = DeviceInfo['Sw1']['UserName']
Password = DeviceInfo['Sw1']['Password']


def SshClient(SshHostIp, UserName, Password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(SshHostIp, port=22, username=UserName, password=Password, timeout=5, compress=True, allow_agent=False,
                look_for_keys=False)
    Shell = ssh.invoke_shell()
    Shell.recv(9999)
    return ssh,Shell


if __name__ == '__main__':
    CLIs = [
        'terminal length 0',
        'terminal monitor',
        'show cdp neighbors | begin Device ID'
    ]


    H = SshClient(HostIP, UserName, Password)
    ssh = H[0]
    Shell = H[1]


    for CLI in CLIs:
        Shell.send(CLI.encode() + b'\n')
        time.sleep(0.5)
        SysLog = Shell.recv(9999).decode()
        print(SysLog)
        SaveLog(DeviceName + '_VerifyCDP_' + Now + '.txt', SysLog)
        if 'cdp' in CLI:
            NbrName = SysLog.splitlines()[2].split()[0]
            print('='*80 + '\n'+
                  NbrName + '\n'+
                  '='*80)
    Shell.close()
    ssh.close()

