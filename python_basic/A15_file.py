File = 'saiban.txt'

'''Content = ['saiban','xiaobai','groot']

f = open(File,mode='w')
for i in Content:
    f.write(i+'\n')
f.close()'''

f = open(File,mode='r')
# x = f.readlines()
# print(x)
for i in f:
    print(i,end='')
f.close()
