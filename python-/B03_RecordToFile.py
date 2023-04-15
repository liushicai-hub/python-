def SaveLog(FileName,Content):
    with open(FileName,mode='a') as f:
        f.write(Content)


if __name__ == '__main__':
    Content = 'test1024'
    SaveLog('test1024.txt',Content)

