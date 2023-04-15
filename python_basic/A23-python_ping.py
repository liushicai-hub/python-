import subprocess
import sys

SysPlatform = sys.platform

File = 'ping.txt'
target = '203.0.113.11'
# target = '6.6.6.6'
if 'win' in SysPlatform:
    cmd = ['ping','-n','3',target]
elif 'linux' in SysPlatform:
    cmd = ['ping','-c','3',target]
else:
    print('???')

ping_result = subprocess.call(cmd,stdout=open(File,'w'),stderr=open(File,'w'))


if ping_result == 0:
    print('ping OK')
else:
    print('ping Failed')

