import collections
import pprint
from ncclient import manager
from B00_DeviceCredentials import DeviceInfo
from C101_NETCONF_get_status import *
import ipaddress
import xmltodict  # 连接网络，安装对应的第三方库
import xml.dom.minidom

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

# 获取ospf邻居状态数据
OspfNbrInfo = m.get(get_OspfNbr)
# 打印结果，但是不好看
# pprint.pprint(OspfNbrInfo)
# 将结果漂亮的打印出来
# print(xml.dom.minidom.parseString(OspfNbrInfo.xml).toprettyxml())
# 将返回的xml文本转成有序的字典
Data = xmltodict.parse(OspfNbrInfo.xml)["rpc-reply"]["data"]
# Data = xmltodict.parse(OspfNbrInfo.xml)

# print(type(Data), Data)

# 定义函数，用于从有序字典中查找我们想要的数据
def GetFromOrderDict(dict):
    global x  # 定义全局变量x
    for i in dict:  # 遍历传入的有序字典
        print(type(dict[i]), dict[i])
        if i == 'nbr-id':  # 如果遍历对象为我们需要的数据键
            # print(type(dict[i]),dict[i])
            x = dict[i]
            break  # 打断循环
        elif type(dict[i]) == collections.OrderedDict:  # 如果遍历对象的值为有序字典
            GetFromOrderDict(dict[i])  # 执行自我迭代
    return x  # 返回该键的值


Result = ipaddress.ip_address(int(GetFromOrderDict(Data)))
print(Result)

# 获取设备状态数据
# Status = m.get(get_if)
# 打印结果，但是不好看
# pprint.pprint(Status)
# 将结果漂亮的打印出来
# print(xml.dom.minidom.parseString(Status.xml).toprettyxml())
# 将返回的xml文本转成有序的字典
# Data = xmltodict.parse(Status.xml)["rpc-reply"]["data"]
# print(Data)
# print(type(Data))
# 从中取出接口的有序字典,主要尝试理解和掌握有序字典
# Interfaces = Data['interfaces']['interface']
# print(Interfaces)
# for i in Interfaces:
#     print(i['name'])


# 遍历有序字典及取值办法
# for interface in Interfaces:
#     print(interface['name'], ' enable status is ', interface['enabled'])
