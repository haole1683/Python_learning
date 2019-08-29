Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##内嵌函数和闭包
>>> count = 5
>>> def MyFun():
	count = 10
	print(count)

	
>>> MyFun()
10
>>> count
5
>>> def MyFun():
	global count
	count = 10
	print(10)

	
>>> MyFu
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    MyFu
NameError: name 'MyFu' is not defined
>>> MyFun()
10
>>> count
10
>>> ##使用global 关键字就可以实现在函数内部修改全局变量
>>> 
>>> def fun1():
	print('fun1() used')
	def fun2():
		print('fun()2 used')
	fun2()

	
>>> fun()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    fun()
NameError: name 'fun' is not defined
>>> fun1()
fun1() used
fun()2 used
>>> 
>>> ##Python支持函数嵌套
>>> 
>>> ##这种功能只能在妇女
>>> ##上句删掉
>>> ##这种功能只能在fun1()中调用fun2()，但是如果在其他地方调用就不好使
>>> 
>>> fun2()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    fun2()
NameError: name 'fun2' is not defined
>>> 
\
>>> def Funx(x):
	def FunY(y):
		return x * y
	return FunY

>>> 
>>> ##闭包
>>> 
>>> def FunX(x):
	def FunY(y):
		return x * y
	return FunY

>>> i = FunX(8)
>>> 
>>> i
<function FunX.<locals>.FunY at 0x0000026368E8A8B8>
>>> i(5)
40
>>> FunX(3)(5)
15
>>> FunY(5)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    FunY(5)
NameError: name 'FunY' is not defined
>>> ##闭包即内部函数调用外部函数变量
>>> 
>>> def Fun1():
	x = 5
	def Fun2():
		x *= x
		return x
	return Fun2()

>>> Fun1()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    Fun1()
  File "<pyshell#63>", line 6, in Fun1
    return Fun2()
  File "<pyshell#63>", line 4, in Fun2
    x *= x
UnboundLocalError: local variable 'x' referenced before assignment
>>> def Fun1():
	x = [5]
	def Fun2():
		x[0] *= x[0]
		return x[0]
	return Fun2()

>>> Fun1()
25
>>> ##这种方式是使用列表进行访问，不会进行报错
>>> 
>>> ##除此之外还可以使用nonlocal
>>> 
>>> def Fun1():
	x = 5
	def Fun2():
		nonlocal x
		x *= x
		return x
	return Fun2()

>>> Fun1()
25
>>> ##及说明这里x不是局部变量
