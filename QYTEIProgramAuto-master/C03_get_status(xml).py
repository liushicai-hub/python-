from ncclient import manager
from B00_DeviceCredentials import DeviceInfo
from C101_NETCONF_get_status import *
import xml.etree.ElementTree as ET
import ipaddress

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

# 获取acl配置
# print(m.get(get_acl))

# 获取ospf邻居状态数据 并掌握分析xml文本的能力
OspfNbrInfo = m.get(get_OspfNbr)
# print(type(OspfNbrInfo), '\n', OspfNbrInfo)
XML = OspfNbrInfo.data_xml  # 将返回数据存储为XML文本
# print(type(XML), '\n', XML)
Tree = ET.fromstring(XML)  # 将文本以etree形式实例化到变量Tree
# print(type(Tree), '\n', Tree)
# for i in Tree.iter():  # 使用for循环遍历etree的所有标签
    # print(type(i),i)
    # print(i.tag)  # 打印xml标签tag

# 经分析，得到邻居router-id的标签为 "{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper}nbr-id"
NbrIdTag = "{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper}nbr-id"  # 实例化这个tag的文本
NbrIdText = Tree.findtext(".//" + NbrIdTag)  # 查找并实例化这个tag对应的文本

# print(type(NbrIdText), NbrIdText)  # 打印出邻居的router-id，但是总觉得不对劲
RID = int(NbrIdText)  # 转成整形
FinalNbrID = ipaddress.ip_address(RID)
print(type(FinalNbrID),FinalNbrID)
