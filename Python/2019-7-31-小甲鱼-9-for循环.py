Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##Py的 for循环
>>> ##语法
>>> ##for 目标 in 表达式:
>>> ##	循环体
>>> 
>>> favourite = 'FishC'
>>> for i in favourite:
	print(i,end = ' ')

	
F i s h C 
>>> member = ['小甲鱼','小布丁','黑夜','mitu'，'傻逼']
SyntaxError: invalid character in identifier
>>> member = ['小甲鱼','小布丁','黑夜','mitu','傻逼']
>>> for each in member:
	print(each,len(member))

	
小甲鱼 5
小布丁 5
黑夜 5
mitu 5
傻逼 5
>>> for each in member:
	print(each,len(member))
KeyboardInterrupt
>>> for each in member:
	print(each,len(each))

	
小甲鱼 3
小布丁 3
黑夜 2
mitu 4
傻逼 2
>>> ##range()
>>> ##语法:range([strat,] stop[,step=1])
>>> ##这个BIF有参数，其中用中括号括起来两个表示这两个参数是可以选择的
>>> ##step = 1表示第三个参数的值的默认值为1
>>> ##range这个bif
>>> ##作用就是生成一个从start参数的值开始到stop参数的值结束的数字序列
>>> 
>>> range(0,5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(2,9):
	print(i)

	
2
3
4
5
6
7
8
>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9
>>> ##两个关键语句
>>> ##break  continue
>>> 
>>> 
>>> ##!!!!!!!!!!!!!!
>>> ##尝试写出下列语句输出结果
>>> for i in range(10):
	if i % 2 != 0:
		print(i)
		continue
	i+=2
	print(i)

	
2
1
4
3
6
5
8
7
10
9
>>> #注意这里循环进行10次，没一次都从列表之中拿出一个值进行循环体内的操作
>>> ##而非这里i+=2没有影响
>>> ##而是没执行一次for循环，i的值都被从range1里面取出一个数据给覆盖掉了
