file = open('test1024.txt','r+')
test = '\nale'
file.write(test)
t = file.readlines()
print(t)
print(t[1])
