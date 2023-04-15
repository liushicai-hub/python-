import subprocess
from B00_DeviceCredentials import DeviceInfo


def Ping(HostIP,File):
    cmd = ['ping', HostIP, '-c', '5']  # stop ping until get 5 replys
    result = subprocess.call(cmd, stdout=open(File, 'a'), stderr=open(File, 'a'))
    print('echo reply is '+str(result))
    if result == 0:
        print('ping OK')
    else:
        print('ping Failed')
    return result


if __name__ == '__main__':
    for Device in DeviceInfo:
        DeviceName = DeviceInfo[Device]['DeviceName']
        HostIP = DeviceInfo[Device]['HostIP']
        File = f'{DeviceName}_B08_ping.txt'

        Ping(HostIP, File)
