import sys
import os

# PLATFORM = sys.platform
#
# if 'linux' not in PLATFORM:
#     print('not linux')
# else:
#     print(PLATFORM)

# x = input('enter a str:')
# print(x)
# print('='*50)
# y = sys.stdin.readline()
# print(y)
# print('='*50)

# Path = os.getcwd()  #当前工作目录实例化为Path
# x = os.listdir(Path)  #获取Path目录下的所有文件和子文件夹
# FileAbsList = []
#
# for File in x:
#     Abs = os.path.join(Path,File) #将目录和文件名拼接成文件的绝对路径
#     FileAbsList.append(Abs)
#
# print(FileAbsList)

# Path = "home//cisco\\aaaaa\\aaa"

# Path1 = os.path.normpath(Path)
# print(Path1)
# os.rmdir(Path1)

import datetime
# from datetime import datetime
now = datetime.datetime.now()
today = datetime.date.today()
print(now,today)


