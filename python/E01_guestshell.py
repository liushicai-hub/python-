"""
要求：
写一个python脚本，名字为qytang666.py，存在 guestshell 当前进入目录下；
通过 cli 库查看设备上的vrf；
创建一个列表，里面包含每个vrf的基本信息：1、vrf名字；2、该vrf所开启的地址族（ipv4 or ipv6 or both）
每个vrf的基本信息为字典；
使用vrf名字及其开启的地址族作为依据遍历字典；
在屏幕上输出这些vrf及其对应开启地址族的直连路由表；

from cli import *
cli_vrf_info_out = execute('show vrf | in ipv').split('\n')
vrf_info_list = []
for line in cli_vrf_info_out:
    split_line = line.split()
    vrf_name = split_line[0]
    if 'ipv4' in split_line[2]:
        split_line[2]=split_line[2].replace('ipv4', 'ip')
    address_family = split_line[2].split(',')
    vrf_info_dict = {"enabled_address_family":address_family,"name":vrf_name}
    vrf_info_list.append(vrf_info_dict)
for i in range(len(vrf_info_list)):
    name = vrf_info_list[i]["name"]
    for addr_family in vrf_info_list[i]["enabled_address_family"]:
        print('='* 50)
        executep('show %s route vrf %s connect' % (addr_family,name))
"""

