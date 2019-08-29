Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##
>>> ##拾遗
>>> 
>>> class Turtle:
	def __init__(self,x):
		self.num = x
class Fish:
	
SyntaxError: invalid syntax
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-4.py ===============
>>> pool = Pool(1,2)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pool = Pool(1,2)
  File "D:/Python/2019-8-10-类和对象：面向对象编程-4.py", line 12, in __init__
    self.fish = Fish(y)
  File "D:/Python/2019-8-10-类和对象：面向对象编程-4.py", line 7, in __init__
    self,x = x
TypeError: cannot unpack non-iterable int object
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-4.py ===============
>>> pool = Pool(1,3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    pool = Pool(1,3)
  File "D:/Python/2019-8-10-类和对象：面向对象编程-4.py", line 12, in __init__
    self.fish = Fish(y)
  File "D:/Python/2019-8-10-类和对象：面向对象编程-4.py", line 7, in __init__
    self,x = x
TypeError: cannot unpack non-iterable int object
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-4.py ===============
>>> pool = Pool(4,5)
>>> pool.print_num()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pool.print_num()
  File "D:/Python/2019-8-10-类和对象：面向对象编程-4.py", line 15, in print_num
    print('水池里有乌龟 %d 只，小鱼 %d 条' % (self.num,turtle.x))
AttributeError: 'Pool' object has no attribute 'num'
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-4.py ===============
>>> pool = Pool(1,4)
>>> pool.print_num()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    pool.print_num()
  File "D:/Python/2019-8-10-类和对象：面向对象编程-4.py", line 15, in print_num
    print('水池里有乌龟 %d 只，小鱼 %d 条' % (turtle.num,fish.x))
NameError: name 'turtle' is not defined
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-4.py ===============
>>> pool =Pool(2,3)
>>> pool.print_num()
水池里有乌龟 2 只，小鱼 3 条
>>> class C:
	count = 0

	
>>> a = C()
>>> b= C()
>>> a.count
0
>>> a.count += 10
>>> a.count
10
>>> b.count
0
>>> C.count += 100
>>> a.count
10
>>> b.count
100
>>> class C:
	def x(self):
		print('x')

		
>>> c = C()
>>> c
<__main__.C object at 0x0000023D1FBFA508>
>>> c.x
<bound method C.x of <__main__.C object at 0x0000023D1FBFA508>>
>>> c.x()
x
>>> c.x = 1
>>> c.x
1
>>> c.x()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c.x()
TypeError: 'int' object is not callable
>>> ##如果属性的名字和方法相同，属性会覆盖方法
>>> 
