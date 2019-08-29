Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class int(int):
	def __add__(self,other):
		return int.__sub__(self,other)

	
>>> a = int('4')
>>> a
4
>>> b = int('5')
>>> 
>>> b
5
>>> a + b
-1
>>> 
=============================== RESTART: Shell ===============================
>>> class Nint(int):
	def __radd(self,other):
		return int.__sub__(other,self)

	
>>> a = Nint(1)
>>> b = Nint(2)
>>> a + b
3
>>> b + a
3
>>> 1 + b
3
>>> class Nint(int):
	def __radd__(self,other):
		return int.__sub__(other,self)

	
>>> aa = Nint(1)
>>> bb = Nint(4)
>>> aa + bb
5
>>> 6+ bbv
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    6+ bbv
NameError: name 'bbv' is not defined
>>> 6+bb
2
>>> 
=============================== RESTART: Shell ===============================
>>> class Nint(int):
	def __rsub__(self,other)
	
SyntaxError: invalid syntax
>>> class Nint(int):
	def __rsub__(self,other):
		return int.__sub__(self,other)

	
>>> a = Nint(4)
>>> 6-a
-2
>>> a
4
>>> -a
-4
>>> +a
4
>>> a = -a
>>> a
-4
>>> +a
-4
>>> 
