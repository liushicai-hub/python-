from ncclient import manager
from B00_DeviceCredentials import DeviceInfo
import pprint
from C100_NETCONF_CONFIGs import *

DeviceName = DeviceInfo['CSR1']['DeviceName']
HostIP = DeviceInfo['CSR1']['HostIP']
UserName = DeviceInfo['CSR1']['UserName']
Password = DeviceInfo['CSR1']['Password']
netconf_port = 830


# 定义函数，用于建立netconf会话
def netconf_connect(HostIP, port, UserName, Password):
    return manager.connect(host=HostIP, port=netconf_port,
                           username=UserName,
                           password=Password,
                           hostkey_verify=False,
                           device_params={'name': 'csr'},
                           allow_agent=False,
                           look_for_keys=False)


# 实例化netconf会话
m = netconf_connect(HostIP, netconf_port, UserName, Password)
# 推送配置数据，目标为running-config，配置内容为config
# m.edit_config(target='running',config=config_interface)
# m.edit_config(target='running',config=DNS)
for CFG in CfgList:
    m.edit_config(target='running', config=CFG)
