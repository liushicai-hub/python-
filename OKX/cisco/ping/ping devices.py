import subprocess
from OKX.cisco.ping.deviceinfo import DeviceInfo


def Ping(HostIP,File):
    cmd = ['ping', HostIP, '-c', '5']  # stop ping until get 5 replys
    result = subprocess.call(cmd, stdout=open(File, 'a'), stderr=open(File, 'a'))
    print('echo reply is '+str(result))
    if result == 0:
        print(' %s ping OK' % DeviceName)
    else:
        print('ping Failed')
    return result


if __name__ == '__main__':
    for Device in DeviceInfo:
        DeviceName = DeviceInfo[Device]['DeviceName']
        HostIP = DeviceInfo[Device]['HostIP']
        # if you want to get a ping file un# below code
        File = f'{DeviceName}_ping.txt'

        Ping(HostIP, File)
