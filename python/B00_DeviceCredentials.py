DeviceInfo = {
    'Sw1':
        {'DeviceName': 'Sw1', 'HostIP': '203.0.113.12', 'UserName': 'saiban', 'Password': 'saiban'},
    'CSR1':
        {'DeviceName': 'CSR1', 'HostIP': '203.0.113.11', 'UserName': 'saiban', 'Password': 'saiban'}
}



if __name__ =='__main__':
    pass
    for Device in DeviceInfo:
        DeviceName = DeviceInfo[Device]['DeviceName']
        HostIP = DeviceInfo[Device]['HostIP']
        UserName = DeviceInfo[Device]['UserName']
        Password = DeviceInfo[Device]['Password']