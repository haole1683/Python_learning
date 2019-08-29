Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Ball:
	def setName(self,name):
		self.name = name
	def kick(self):
		print('who')

		
>>> a = Ball()
>>> a.setName('A')
>>> b = Ball()
>>> b.setName('B')
>>> c = Ball()
>>> class Ball:
	def setName(self,name):
		self.name = name
	def kick(self):
		print('who kick %s' % self.name)

		
>>> c.setName('C')
>>> a.kick()
who
>>> b.kick()
who
>>> c.kick()
who
>>> class Ball:
	def __init__(self,name):##类似于构造函数
		self.name = name
	def kick(self):
		print('我叫%s' % self.name)

		
>>> b = Ball('沙发读书')
>>> b.kick()
我叫沙发读书
>>> 
>>> class Person:
	name = '小甲鱼'

	
>>> p = Persom()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    p = Persom()
NameError: name 'Persom' is not defined
>>> p = Persom()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    p = Persom()
NameError: name 'Persom' is not defined
>>> p = Person()
>>> p.name
'小甲鱼'
>>> class Person:
	__name = '小甲鱼'

	
>>> p = Person()
>>> p.name
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    p.name
AttributeError: 'Person' object has no attribute 'name'
>>> ##python之中 name mangling 名字改编，名字重整机制
>>> ##python 中定义私有变量只需要在变量名或函数名前加上“__”双下划线，那么这个函数或者变量名就变成了私有的
>>> class Person:
	__name = '小甲鱼'
	def getname(self):
		return self.__name

	
>>> p = Person()
>>> p.name
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    p.name
AttributeError: 'Person' object has no attribute 'name'
>>> p.getname()
'小甲鱼'
>>> p = _Person__name
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    p = _Person__name
NameError: name '_Person__name' is not defined
>>> p._Person__name
'小甲鱼'
>>> ##伪私有
>>> 
