from ncclient import manager
from B00_DeviceCredentials import DeviceInfo
import pprint

DeviceName = DeviceInfo['CSR1']['DeviceName']
HostIP = DeviceInfo['CSR1']['HostIP']
UserName = DeviceInfo['CSR1']['UserName']
Password = DeviceInfo['CSR1']['Password']
netconf_port = 830

with manager.connect(host=HostIP, port=netconf_port,
                     username=UserName,
                     password=Password,
                     hostkey_verify=False,
                     device_params={'name': 'csr'},
                     allow_agent=False,
                     look_for_keys=False) as m:
    c = m.get_config(source='running').data_xml #获取running confg并用xml编码方式解读
    print(c)
    print(type(c))
    with open("{}.xml".format(DeviceName), 'w') as f:
        f.write(c)  #将xml文本写入文件
    for capability in m.server_capabilities:  #获取设备能力及遍历打印能力
        print(capability)
        with open(f'{DeviceName}_capabillity.txt', mode='a+') as capability_file:
            capability_file.write(capability)
            capability_file.write('\n')
