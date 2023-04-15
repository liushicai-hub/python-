import sys
import time

# while True:
#     time.sleep(1)
#     print(time.asctime(),'\n','I am groot.')

#让电脑自动数羊
# i = 0
# while i<=10:
#     time.sleep(1)
#     i += 1
#     print(str(i),' goat')

#用while循环查找数据的索引下标
# x = ('cisco','huawei','h3c','saiban','xiaobai','groot')
# i = 0
# while x[i] != 'saiban':
#     i += 1
#     print('I can\'t see cat.')
# print(f'saiban\'s index is {str(i)}')

#用while循环计算1-100的总和
Condition = 100
Sum = 0
Counter = 1
while Counter <= Condition:
    Sum += Counter
    print(Sum)
    Counter += 1
    # continue子句，仅仅打断本次循环的后续代码执行；
    if str(Counter)[-1] =='4':
        continue
    # if Sum >=2000:
        # break子句，立刻结束循环，不再执行代码组中的任何后续代码
        # break
    print(Counter)
#else子句，当且仅当表达式结果为False并正常跳出循环时，执行else代码块；
else:
    pass
    print('I am groot.')

print('I am saiban.')

