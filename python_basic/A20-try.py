x = ['aaa','bbb''ccc']
File = 'saiban.txt'
try:
    print('try')
    f = open(File,mode='w')
    f.write(x)
    f.close()
    # print('result',r)
except Exception as e:
    print('except',e)
else:
    print('else')
finally:
    print('finaly')

