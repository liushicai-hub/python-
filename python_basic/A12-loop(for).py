#for循环通常用于遍历任何的可迭代对象（比如：列表、元组、字符串）

x = [1,2,3,4,5,6,7,8,9,0]

for i in x:
    print(i)
print('-'*60)
for i in range(6):
    print(i , x[i])
print('-'*60)
for i in range(1,3):
    print(i ,x[i])
print('-'*60)
for i in range(0,10,2):
    print(i ,x[i])
print('-'*60)

"""

作业，完成以下代码
x = [0,1,2,3,4]
for i in x:
    print(i+1)
    
i = Sum = 0

while i <= 10:
    Sum += i
    i = i + 1
print(Sum)

"""
