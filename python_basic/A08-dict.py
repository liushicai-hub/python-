"""
字典  vs  json【java script object notation， java脚本对象表示法】
轻量级数据库

key value pair  键 值 对
范例：
一个人 —— 字典
眼睛颜色 ： 黑色
皮肤颜色 ： 黄色
身高 ： 170CM

花括号定义字典
键值对的语法：冒号分隔，一个键值对为字典的一个元素，逗号分隔元素，一个字典中所有的键必须唯一，值可以是任意对象，键必须是不可变对象（元组、字符串、数字）；
"""

#字典的定义
DeviceInfo = {'HostName': 'CSR1',
              'MgmtIP': '203.0.113.11',
              'UserName': 'saiban',
              'Password': 'saiban',
              'EnablePass': 'saiban',2333:6666}

#字典的检索
print(DeviceInfo['Password'])
#字典元素的修改
DeviceInfo['Password'] = 'groot'
print(DeviceInfo['Password'])

#字典元素的删除
print(DeviceInfo)
del DeviceInfo[2333]
print(DeviceInfo)

#字典元素的追加
DeviceInfo['vendor'] = 'cisco'
print(DeviceInfo)

a = {'name':'saiban','age':18,'height':170}
"""
作业
定义一个字典
修改名字为 ‘groot’
修改年龄为24
增加新的键值对 体重 ‘weight’ 70KG
打印字典
"""
