Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##构造和析构
>>> 
>>> class Rectangle:
	def __init(self,x,y):
		self.x = x
		self.y = y
	def getPeri(self):
		return (self.x + self.y) * 2
	def getArea(self):
		return self.x * self.y

	
>>> rect = Rectangle(3,4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    rect = Rectangle(3,4)
TypeError: Rectangle() takes no arguments
>>> class Rectangle:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def getPeri(self):
		return (self.x + self.y) * 2
	def getArea(self):
		return self.x * self.y

	
>>> rect = Rectangle(3,4)
>>> rect.getArea()
12
>>> rect.getPeri()
14
>>> ##__init__返回的是None
>>> 
>>> class A:
	def __init__(self):
		return 1

	
>>> a = A()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a = A()
TypeError: __init__() should return None, not 'int'
>>> 
>>> 
>>> 
