# switch in SG office level 36
DeviceInfo = {
    'OKSG-36F-POE1':
        {'DeviceName': 'OKSG-36F-POE1', 'HostIP': '10.13.255.21'},
    'OKSG-36F-POE2':
        {'DeviceName': 'OKSG-36F-POE2', 'HostIP': '10.13.255.22'},
    'OKSG-36F-POE3':
        {'DeviceName': 'OKSG-36F-POE3', 'HostIP': '10.13.255.23'},
    'OKSG-36F-POE4':
        {'DeviceName': 'OKSG-36F-POE4', 'HostIP': '10.13.255.24'},
    'SIN-36F-CSW':
        {'DeviceName': 'SIN-36F-CSW', 'HostIP': '10.13.255.1'},
    'Singtel-switch':
        {'DeviceName': 'Singtel-switch', 'HostIP': '10.13.255.25'},
    'Starhub-switch':
        {'DeviceName': 'Starhub-switch', 'HostIP': '10.13.255.25'},
}


if __name__ =='__main__':
    pass
    for Device in DeviceInfo:
        DeviceName = DeviceInfo[Device]['DeviceName']
        HostIP = DeviceInfo[Device]['HostIP']
        UserName = DeviceInfo[Device]['UserName']
        Password = DeviceInfo[Device]['Password']