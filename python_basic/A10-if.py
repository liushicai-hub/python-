"""
通俗的理解就是，通过多条语句的执行，得到预期的结果，
将共同完成某一个目标的代码放在一起形成一个代码组；
"""
"""
prefix = '10.1.1.'
prefix_len = '/24'

ip_list = []
for i in range(1, 9):
    ip = prefix + str(i) + prefix_len
    ip_list.append(ip)

print(ip_list)
"""

import random

a = random.randint(0, 100)
b = random.randint(0, 100)

if a == b:
    Result = 'a=b'
elif a < b:
    Result = 'a<b'
elif a > b:
    Result = 'a>b'
else:
    Result = 'I am groot'

print(a, b, Result)
