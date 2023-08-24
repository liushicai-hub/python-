import re
show_if = 'GigabitEthernet0/0  10.1.20.1 YES unset up    up'
re_result = re.match('([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+[A-Z]{1,3}\s+\w+\s+\w+\s+(\w+)$',show_if).groups()
# print(re_result)
if_name = re_result[0]
if_ip = re_result[1]
if_state = re_result[2]

print(f'Interface:{if_name:<20} IP address:{if_ip:<20} State:{if_state:<20}')
