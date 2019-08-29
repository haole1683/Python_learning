Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyDecriptor:
	def __get__(self,instance,owner):
		print('getting...'，self,instance,owner)
		
SyntaxError: invalid character in identifier
>>> class MyDecriptor:
	def __get__(self,instance,owner):
		print('getting...'，self,instance,owner)
		
SyntaxError: invalid character in identifier
>>> class MyDecriptor:
	def __get__(self,instance,owner):
		print('getting...',self,instance,owner)
	def __set__(self,instance,value):
		print('setting...',self,instance,value)
	def __delete__(self,instance):
		print('deleting...',self,instance)

		
>>> class Test:
	x = MyDecriptor()

	
>>> ##描述符,MyDecriptor就是描述符类
>>> 
>>> test = Test()
>>> test.x
getting... <__main__.MyDecriptor object at 0x000002130ACF4548> <__main__.Test object at 0x000002130ACE2B08> <class '__main__.Test'>
>>> test
<__main__.Test object at 0x000002130ACE2B08>
>>> Test
<class '__main__.Test'>
>>> test.x = 'X_man'
setting... <__main__.MyDecriptor object at 0x000002130ACF4548> <__main__.Test object at 0x000002130ACE2B08> X_man
>>> del test.x
deleting... <__main__.MyDecriptor object at 0x000002130ACF4548> <__main__.Test object at 0x000002130ACE2B08>
>>> 
=============================== RESTART: Shell ===============================
>>> class NyProperty:
	def __init__(self,fget = None,fset = None,fdel = None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
	def __get__(self,instance,owner):
		return self.fget(instance)
	def __set__(self,instance,value):
		return self.fset(instance,value)
	def __del__(self,instance):
		self.fdel(instance)

		
>>> 
>>> class C:
	def __init__(self):
		self._x = None
	def getX(self):
		return self._x
	def setX(self,value):
		self._x = value
	def delX(self):
		del self.x
	x = MyProperty(getX,setX,delX)

	
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    class C:
  File "<pyshell#44>", line 10, in C
    x = MyProperty(getX,setX,delX)
NameError: name 'MyProperty' is not defined
>>> class MyProperty:
	def __init__(self,fget = None,fset = None,fdel = None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
	def __get__(self,instance,owner):
		return self.fget(instance)
	def __set__(self,instance,value):
		return self.fset(instance,value)
	def __del__(self,instance):
		self.fdel(instance)

		
>>> class C:
	def __init__(self):
		self._x = None
	def getX(self):
		return self._x
	def setX(self,value):
		self._x = value
	def delX(self):
		del self.x
	x = MyProperty(getX,setX,delX)

	
>>> c = C()
>>> c.x = 'x-man'
>>> c.x
'x-man'
>>> c._x
'x-man'
>>> del c.x
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    del c.x
AttributeError: __delete__
>>> class MyProperty:
	def __init__(self,fget = None,fset = None,fdel = None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
	def __get__(self,instance,owner):
		return self.fget(instance)
	def __set__(self,instance,value):
		return self.fset(instance,value)
	def __delete__(self,instance):
		self.fdel(instance)

		
>>> class C:
	def __init__(self):
		self._x = None
	def getX(self):
		return self._x
	def setX(self,value):
		self._x = value
	def delX(self):
		del self.x
	x = MyProperty(getX,setX,delX)

	
>>> c= C()
>>> c.x = 'X-man'
>>> c.x
'X-man'
>>> c._x
'X-man'
>>> del c.x
Exception ignored in: <function MyProperty.__del__ at 0x000002ABCAED51F8>
TypeError: __del__() missing 1 required positional argument: 'instance'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    del c.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)
  File "<pyshell#57>", line 9, in delX
    del self.x
  File "<pyshell#55>", line 11, in __delete__
    self.fdel(instance)

=============================== RESTART: Shell ===============================
>>> 
============ RESTART: D:/Python/2019-8-13-Property-Temperture.py ============
>>> temp = Temperature()
>>> temp.cel
26.0
>>> temp.cel = 30
>>> temp.fah
86.0
>>> temp.fah = 100
>>> temp.cel
37.77777777777778
>>> 
