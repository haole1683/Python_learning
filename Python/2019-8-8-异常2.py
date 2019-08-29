file_name = input('请输入需要打开的文件')
f = open(file_name)
print('文件的内容是')
for eachline in f:
    print(eachline)
