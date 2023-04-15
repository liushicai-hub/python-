from A16_modules import A1,A2

x = int(input('enter x:'))
y = int(input('enter y:'))

z1 = A1(x, y)  #x and y is 实参
z2 = A2(x, y)
print(z1,z2)

'''def f(a):
    print('start')
    print(id(a))
    a = 'groot'
    print(id(a))
    return a

b = 'saiban'
print(id(b))
x = f(b)
print(id(x))
'''

'''def f(a):
    print('start')
    a.append('groot')
    print(a)
    print(id(a))
    a = ['xiaobai']
    print(a)
    return a

b = ['saiban']
print(id(b))
x = f(b)
print(id(x))'''

