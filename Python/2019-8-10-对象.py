Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##对象 = 属性 + 方法
>>> 
==================== RESTART: D:/Python/2019-8-10-对象+类.py ====================
>>> tt = Turtle()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tt = Turtle()
NameError: name 'Turtle' is not defined
>>> tt = Tertle()
>>> tt.climb()
怕就完了
>>> tt.run()
slow
>>> Tertle t
SyntaxError: invalid syntax
>>> 
>>> ##对象实例化
>>> tt = Tertle
>>> tt.climb()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tt.climb()
TypeError: climb() missing 1 required positional argument: 'self'
>>> ##对象实例化
>>> tt = Tertle()
>>> tt.climb()
怕就完了
>>> 
>>> 
>>> list1 = [2,1,3,5,67]
>>> list1.sort()
>>> list1
[1, 2, 3, 5, 67]
>>> class MyList(list):
	pass

>>> list2 = MyList()
>>> list2.append(1)
>>> list2
[1]
>>> list2.sort
<built-in method sort of MyList object at 0x0000026358DDEAE8>
>>> list2.sort()
>>> class A:
	def fun(self):
		print('我是a')

		
>>> class B:
	def fun(self):
		print('我是b')

		
>>> a = A()
>>> b = B()
>>> a.fun()
我是a
>>> b.fun()
我是b
>>> 
