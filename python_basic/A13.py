'''
Choice = input('[1] saiban \n'
               '[2] xiaobai \n'
               '[3] groot \n'
               'enter your choice:')

if Choice == '1':
    print(11111)
elif Choice == '2':
    print(22222)
elif Choice == '3':
    print(33333)
else:
    print('I am groot.')
'''

'''a = {1:111,'a':'saiban',2:222,3:333}
for i in a:
    print(i)'''

#迭代器与生成器
'''def range(n):
    print('begin to ......')
    i = 0
    while i < n:
        print('before yield...')
        yield i
        i += 1
        print('after yield...')

x = range(2)
print('-'*50)
print(next(x))
print('-'*50)
print(next(x))
print('-'*50)
print(next(x))'''

File = 'saiban.txt'

f = open(File,mode='r')
# f.write('saiban and groot are friends.')
print(f.read())
f.close()
