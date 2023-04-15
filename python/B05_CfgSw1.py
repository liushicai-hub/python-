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
        'config terminal',
        'spann mode r',
        'spann portfast default',
        'vlan 100',
        'name Employees',
        'vlan 12',
        'name ConnectCSR1',
        'interface g0/1',
        'switchport mode access',
        'switchport access vlan 100',
        'interface g0/2',
        'switchport trunk enc d',
        'switchport mode trunk',
        'switchport trunk native vlan 12',
        'interface loopback 0',
        'ip address 10.1.255.1 255.255.255.255',
        'ip ospf 1 area 0',
        'interface vlan 12',
        'no shutdown',
        'ip address 10.1.1.2 255.255.255.252',
        'ip ospf network point-to-point',
        'ip ospf 1 area 0',
        'interface vlan 100',
        'no shutdown',
        'ip address 10.1.100.1 255.255.255.0',
        'ip helper-address 10.1.255.11',
        'ip ospf 1 area 0',
        'router ospf 1',
        'passive-interface vlan100',
        'end',
        'show spanning',
        'show vlan brief',
        'show interface trunk',
        'show ip interface brief',
        'show ip ospf interface brief',
        'show ip protocol',
    ]


    H = SshClient(HostIP, UserName, Password)
    ssh = H[0]
    Shell = H[1]


    for CLI in CLIs:
        Shell.send(CLI.encode() + b'\n')
        time.sleep(0.5)
        SysLog = Shell.recv(9999).decode()
        print(SysLog)
        SaveLog(DeviceName + '_' + Now + '.txt', SysLog)
    Shell.close()
    ssh.close()

