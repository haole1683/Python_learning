Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##一些是bif
>>> class A:
	pass

>>> class B(A):
	pass

>>> issubclass(B,A)
True
>>> issubclass(B,B)
True
>>> issubclass(A,B)
False
>>> issubclass(B,object)
True
>>> class C:
	pass

>>> issubclass(B,C)
False
>>> ##判断一个类是否另一个类的基类
>>> 
>>> ##检查是否一个对象属于一个类
>>> ##如果第一个参数不是类，则永远返回false
>>> 
>>> b1 = B()
>>> isinstance(b1,B)
True
>>> isinstance(b1,A)
True
>>> isinstance(b1,C)
False
>>> isinstance(b1,dd)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    isinstance(b1,dd)
NameError: name 'dd' is not defined
>>> 
>>> 
>>> ##hasattr
>>> ##测试一个对象是否有指定的属性
>>> class C:
	def __init__(self,x = 0):
		self.x = x

		
>>> c1 = C()
>>> hasattr(c1,'x')
True
>>> ##一定要有字符串标志
>>> 
>>> ##getattr
>>> getattr(c1,'x')
0
>>> getattr(c1,'s','不存在')
'不存在'
>>> 
>>> ##setattr
>>> ##设定对象指定值，如果不存在，则新建后赋值
>>> setattr(c1,'y','1')
>>> getattr(c1,'y')
'1'
>>> 
>>> delattr(c1,'y')
>>> delattr(c1,'y')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    delattr(c1,'y')
AttributeError: y
>>> ##删除对象中的属性
>>> 
>>> class C:
	def __init__(self,size = 10):
		self.size = size
	def getsize(self):
		return self.size
