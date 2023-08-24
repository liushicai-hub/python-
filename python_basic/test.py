# import re
# show_if = 'GigabitEthernet0/0  10.1.20.1 YES unset up    up'
# re_result = re.match('([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+[A-Z]{1,3}\s+\w+\s+\w+\s+(\w+)$',show_if).groups()
# # print(re_result)
# if_name = re_result[0]
# if_ip = re_result[1]
# if_state = re_result[2]
#
# print(f'Interface:{if_name:<20} IP address:{if_ip:<20} State:{if_state:<20}')
#


# import re
# show_ip_int = '''
# Vlan13                 10.13.32.1       YES NVRAM  up                    up
# Vlan14                 10.13.4.1       YES NVRAM  up                    up
# Vlan15                 10.13.115.1       YES NVRAM  up                    up
# Vlan16                 10.13.6.1       YES NVRAM  up                    up
# '''
#
# a = show_ip_int.strip().split('\n')
#
# for line in a:
#   re_result= re.match('\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(\w+)',line).groups()
#   print(re_result)


#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


# department1 = 'Security'
# department2 = 'Python'
# depart1_m = 'cq_bomb'
# depart2_m = 'qinke'
# COURSE_FEES_SEC = 456789.12456
# COURSE_FEES_Python = 1234.3456
#
#
# line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!' % (department1,depart1_m,COURSE_FEES_SEC)
# line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!' % (department2,depart2_m,COURSE_FEES_Python)
#
# #line1 = 'Department1 name:{0:<10} Manager:{1:<10} COURSE FEES:{2:<10.2f} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
# #line2 = 'Department2 name:{0:<10} Manager:{1:<10} COURSE FEES:{2:<10.2f} The End!'.format(department2,depart2_m,COURSE_FEES_Python)
#
# length = len(line1)
# print('='*length)
# print(line1)
# print(line2)
# print('='*length)



#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import re

ifconfig_result = 'eno33554944: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n        inet 202.100.1.138  netmask 255.255.255.0  broadcast 202.100.1.255\n        inet6 fe80::20c:29ff:fe8d:5cb6  prefixlen 64  scopeid 0x20<link>\n        ether 00:0c:29:8d:5c:b6  txqueuelen 1000  (Ethernet)\n        RX packets 0  bytes 0 (0.0 B)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 33  bytes 4290 (4.1 KiB)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'

re_findall_result =  re.findall('([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',ifconfig_result)

print('MAC地址为:',re_findall_result[0])