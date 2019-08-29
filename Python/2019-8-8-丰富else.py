try:
    print(int('1234'))
except ValueError as reason:
    print('出错了'+ str(reason))
else:
    print('没毛病')
##else 是当没有异常时执行
    

##with语句

try:
    with open('data.txt','w') as f:
        for each_line in f:
            print (each_line)
except OSError as reason:
    print('出错了' + str(reason))
##使用with后不管with中的代码出现什么错误，都会进行对当前对象进行清理工作。
##例如file的file.close()方法，无论with中出现任何错误，都会执行file.close（）方法
