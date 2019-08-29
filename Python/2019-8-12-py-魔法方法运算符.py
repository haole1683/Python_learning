Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(dir)
<class 'builtin_function_or_method'>
>>> type(int)
<class 'type'>
>>> type(help)
<class '_sitebuiltins._Helper'>
>>> type(list)
<class 'type'>
>>> class C:
	pass

>>> type(c)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
>>> type(C)
<class 'type'>
>>> a = int('123')
>>> a
123
>>> b = int('456')
>>> b
456
>>> a+ b
579
>>> class New_int(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

	
>>> a = New_int(4)
>>> b = New_int(5)
>>> a + b
-1
>>> a - b
9
>>> class Try_int(int):
	def __add__(self,other):
		return self + other
	def __sub__(self,other):
		return self - other

	
>>> a = Try_int(3)
>>> b = Try_int(4)
>>> a + b
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a + b
  File "<pyshell#26>", line 3, in __add__
    return self + other
  File "<pyshell#26>", line 3, in __add__
    return self + other
  File "<pyshell#26>", line 3, in __add__
    return self + other
  [Previous line repeated 991 more times]
RecursionError: maximum recursion depth exceeded
>>> 9 + 9
18
>>> class Try_int(int):
	def __add__(self,other):
		return int(self) + int(other)
	def __sub__(self,other):
		return int(self) - int(other)

	
>>> a = Try_int(3)
>>> b = Try_int(5)
>>> a + b
8
>>> 
