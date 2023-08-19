a = [1, 2, ['a', 'b', 'c'], 'saiban', 5]
print(a[3])
print(a)
print(a[-1])

a.append('alex')
print(a)
a.remove(2)
del a[2]

#如果列表有多个2 会remove第一个
'''
定义两个列表：
a1= ['groot', 'saiban’]
b1= ['mieba', 'jd']
对这两个列表进行拼接
使用下标弹出 ‘jd’ 元素
'''

# 作业解析
a1= ['groot', 'saiban']
b1= ['mieba', 'jd']
c1 = a1+b1
print(c1)
c1.pop(3)
print(c1)
