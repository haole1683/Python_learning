Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class C:
	def __init__(self,size = 10)
	
SyntaxError: invalid syntax
>>> class C:
	def __init__(self,size = 10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size = value
	def delSize(self):
		del self.size
	x = property(getSize,setSize,delSize)

	
>>> c = C()
>>> c.x = 1
>>> c.x
1
>>> c.size
1
>>> del c.x
>>> ## 属性访问1
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> class C:
	def __getattribute__(self,name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self,name):
		print('getattr')
	def __setattr__(self,name,value):
		print('setattr')
		super.__setattr__(name,value)
	def __delattr__(self,name)
	
SyntaxError: invalid syntax
>>> class C:
	def __getattribute__(self,name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self,name):
		print('getattr')
	def __setattr__(self,name,value):
		print('setattr')
		super.__setattr__(name,value)
	def __delattr__(self,name):
		print('delattr')
		super().delattr__(name)

		
>>> c = C()
>>> c.x
getattribute
getattr
>>> c.x = 1
setattr
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c.x = 1
  File "<pyshell#32>", line 9, in __setattr__
    super.__setattr__(name,value)
TypeError:  expected 2 arguments, got 1
>>> class C:
	def __getattribute__(self,name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self,name):
		print('getattr')
	def __setattr__(self,name,value):
		print('setattr')
		super().__setattr__(name,value)
	def __delattr__(self,name):
		print('delattr')
		super().delattr__(name)

		
>>> c = C()
>>> c.x  = 1
setattr
>>> c.
SyntaxError: invalid syntax
>>> c.y
getattribute
getattr
>>> del c.x
delattr
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    del c.x
  File "<pyshell#37>", line 12, in __delattr__
    super().delattr__(name)
AttributeError: 'super' object has no attribute 'delattr__'
>>> class C:
	def __getattribute__(self,name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self,name):
		print('getattr')
	def __setattr__(self,name,value):
		print('setattr')
		super().__setattr__(name,value)
	def __delattr__(self,name):
		print('delattr')
		super().__delattr__(name)

>>> 
>>> c= C()
>>> c.x
getattribute
getattr
>>> c.x = 1
setattr
>>> del c.x
delattr
>>> 
================ RESTART: D:/Python/2019-8-12-py-魔法方法属性操作2.py ================
>>> r1 = Reacangle(4,5)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    r1 = Reacangle(4,5)
NameError: name 'Reacangle' is not defined
>>> r1 = Reatangle(4,5)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    r1 = Reatangle(4,5)
NameError: name 'Reatangle' is not defined
>>> 
================ RESTART: D:/Python/2019-8-12-py-魔法方法属性操作2.py ================
>>> r = Rectangle(4,5)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    r = Rectangle(4,5)
  File "D:/Python/2019-8-12-py-魔法方法属性操作2.py", line 3, in __init__
    self.width = width
  File "D:/Python/2019-8-12-py-魔法方法属性操作2.py", line 11, in __setattr__
    self.name = value
  File "D:/Python/2019-8-12-py-魔法方法属性操作2.py", line 11, in __setattr__
    self.name = value
  File "D:/Python/2019-8-12-py-魔法方法属性操作2.py", line 11, in __setattr__
    self.name = value
  [Previous line repeated 988 more times]
  File "D:/Python/2019-8-12-py-魔法方法属性操作2.py", line 7, in __setattr__
    if name == 'square':
RecursionError: maximum recursion depth exceeded in comparison
>>> 
================ RESTART: D:/Python/2019-8-12-py-魔法方法属性操作2.py ================
>>> r1 = Rectangle(4,5)
>>> r1.getArea()
20
>>> r1.square = 10
>>> r1.width
10
>>> r1.height
10
>>> r1.getArea()
100
>>> r1.__dict__
{'width': 10, 'height': 10}
>>> 
================ RESTART: D:/Python/2019-8-12-py-魔法方法属性操作2.py ================
>>> r1 = Rectangle(4,5)
>>> r1.getArea()
20
>>> 
