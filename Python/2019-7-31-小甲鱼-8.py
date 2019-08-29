while True:
    score = int(input('请输入分数'))
    if score >= 90 and score <=100:
        print('A')
    elif 80 <= score < 90:##elif相当于C中else if
        print('B')
    elif 60 <= score <80:
        print('C')
    elif 0 <= score <60:
        print('D')
##因此针对于if-else 中

##条件表达式（三元操作符）
##x if 条件 else y
small = x if x < y else y


##assert 断言
##如果后面条件为假的时候，程序会自动崩溃并抛出AsserttionError异常
##例如 assert 3>4
##一般来说我们可以用Ta在程序之中置入检查点，当需要程序中的某一个条件一定为真的时候
##才能让程序正常工作的话，那么assert关键字就会非常有用
