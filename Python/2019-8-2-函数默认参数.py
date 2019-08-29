Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def MyFirstFunction(name):
	'nmsl'
	print(name)

	
>>> MyFirstFunction()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    MyFirstFunction()
TypeError: MyFirstFunction() missing 1 required positional argument: 'name'
>>> MyFirstFunction('sfdas')
sfdas
>>> MyFirstFunction.__doc__
'nmsl'
>>> help(MyFirstFunction)
Help on function MyFirstFunction in module __main__:

MyFirstFunction(name)
    nmsl

>>> print.__doc__
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
>>> ##函数文档
>>> ##介绍该函数等
>>> ##使用 __doc__以访问
>>> 
>>> def SaySome(name,words)
SyntaxError: invalid syntax
>>> def SaySome(name,words):
	print(name + 'dfsf' +words)

	
>>> def SaySome(name = 'nui',words = 'dsf'):
	print(name + 'dfsf' +words)

	
>>> SaySome()
nuidfsfdsf
>>> SaySome('苍')
苍dfsfdsf
>>> 
>>> 
>>> ##收集参数
>>> def test(*params):
	print('参数长度是',len(params))
	print('第二个参数是'params[1])
	
SyntaxError: invalid syntax
>>> def test(*params):
	print('参数长度是',len(params))
	print('第二个参数是',params[1])

	
>>> test(1,34,'sff',343)
参数长度是 4
第二个参数是 34
>>> ##任意个实参都可以
>>> 
>>> def test(*collect,exp):
	print('参数长度是',len(params))
	print('第二个参数是',params[1])

	
>>> d
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> def test(*collect,exp):
	print('参数长度是',len(collect))
	print('第二个参数是',collect[1])

	
>>> test(1,2,3)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    test(1,2,3)
TypeError: test() missing 1 required keyword-only argument: 'exp'
>>> def test(*collect,exp = 8):##如果想要使用额外的参数（exp）就需要给这个默认参数加上默认值，否则会报错
	print('参数长度是',len(collect))
	print('第二个参数是',collect[1])

	
>>> test()
参数长度是 0
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    test()
  File "<pyshell#41>", line 3, in test
    print('第二个参数是',collect[1])
IndexError: tuple index out of range
>>> test(1,2,3)
参数长度是 3
第二个参数是 2
>>> 
