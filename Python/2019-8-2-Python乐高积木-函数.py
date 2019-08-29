Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##函数
>>> def MyFirstFunction():
	print('这是我创建的第一个函数')
	print('傻吊玩意')

	
>>> MyFirstFunction()
这是我创建的第一个函数
傻吊玩意
>>> MySecondFunction()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    MySecondFunction()
NameError: name 'MySecondFunction' is not defined
>>> MyFirstFunction()
这是我创建的第一个函数
傻吊玩意
>>> def MySecondFunction(name):
	print('name'+'沙嗲一枚')

	
>>> MySecondFunction('小甲鱼')
name沙嗲一枚
>>> MySecondFunction('鸡你太美')
name沙嗲一枚
>>> def MySecondFunction(name):
	print(name+'沙嗲一枚')

	
>>> MySecondFunction('鸡你太美')
鸡你太美沙嗲一枚
>>> def MySecondFunction(name):
	print('%s煞笔') % name

	
>>> 	MySecondFunction('唧唧')
	
SyntaxError: unexpected indent
>>> MySecondFunction('唧唧')
%s煞笔
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    MySecondFunction('唧唧')
  File "<pyshell#18>", line 2, in MySecondFunction
    print('%s煞笔') % name
TypeError: unsupported operand type(s) for %: 'NoneType' and 'str'
>>> 
>>> def add(num1,num2):
	result = num1 + num2
	print(result)

	
>>> add(1,2)
3
>>> def add(num1,num2):
	print('%d' % num1 + num2)

	
>>> add(2,3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    add(2,3)
  File "<pyshell#29>", line 2, in add
    print('%d' % num1 + num2)
TypeError: can only concatenate str (not "int") to str
>>> def add(num1,num2):
	return num1 + num2

>>> print(add(4,5))
9
>>> 
