import math
import random



PI = math.pi  # 实例化圆周率
print(PI)

x = pow(2, 8)  # 计算乘方
y = 2 ** 8  # 计算乘方
print(x == y)

a = abs(1 - 3)  #绝对值
print(a)

b1 = 5
b2 = 6
b = sum([b1, b2])  # 求元组或者列表的和
print(b)

c = [1, 2, 3, 4, 5]
print(min(c), max(c))  # 打印列表中的最小值和最大值

d = random.random()  # 随机生成一个n，0<= n <1.0
print(d)

e = random.randint(1, 100)  # 随机产生一个整数n，1<=n<=100
print(e)

f = 'abcdefg'
g = random.choice(f)  # 从f对象中随机选取一个元素
print(g)

'''
编写脚本，从0-9随机产生两个整形变量并分别定义变量标识符为 x1 , y1；
打印出两个随机整形的值；
打印出两个随机整形执行不同比较运算的结果；
自行选择逻辑运算符，使用三元表达式打印，当x大于y时输出True，当x小于y时输出False；
'''
# 作业解析
x1 = random.randint(0, 9)
y1 = random.randint(0, 9)
print(x1, y1)

if x1 < y1:
    print('x1<y1')
elif x1 > y1:
    print('x1>y1')
elif x1 == y1:
    print('x1=y1')

print((x1>y1) or not (x1<y1))

