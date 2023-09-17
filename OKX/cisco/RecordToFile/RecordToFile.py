def SaveLog(FileName,Content):
    with open(FileName,mode='a+') as f:
        f.write(Content)
        print(f.readlines())

    # file = open('test1024.txt', 'r+')
    # t = file.readlines()
    # print(t)

if __name__ == '__main__':
    Content = 'test1024'+'\n'+'tttt'+'\n'+'eeee'
    SaveLog('test1024.txt',Content)

# a+ additional , w+ rewrite, r+ replace  no + meaning only read or write mode


'''
r   以只读方式打开文件，r 模式只能打开已存在的文件。如果文件不存 在，则会报错
w   打开文件并只用于写入。如果文件已经存在，则原有内容将被删除覆盖；如果文件不
存在，则创建新文件
a   以追加方式打开文件。如果文件已经存在，则原有内容不会被删除覆盖，新内容将添
加在原有内容后面；如果文件不存在，则创建新文件
r+   以读写方式打开文件，r+ 模式只能打开已存在的文件。如果文件不存在，则会报错
w+   以读写方式打开文件。如果文件已经存在，则原有内容将被删除覆盖；如果文件不存
在，则创建新文件
a+  以读写方式打开文件。如果文件已经存在，则原有内容不会被删除覆盖，新内容将添
加在 原有内容后面；如果文件不存在，则创建新文件
'''





