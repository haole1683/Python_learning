Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> p = Parent()
>>> p.hello()
父类funionn 条用
>>> c = Child()
>>> c.hello()
父类funionn 条用
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> c= Chile()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c= Chile()
NameError: name 'Chile' is not defined
>>> c = Child()
>>> c.hello()
正在调用子类
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> f = Fish()
这是Fish
>>> goldfish = GoldFish()
这是Fish
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> goldfish = GoldFish()
这是Fish
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> golafish = GoldFish()
这是金鱼
>>> ##注意这里__init__被重写了，父类的被覆盖了
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> ##解决方案
>>> ##重新调用父类初始化方法
>>> 
>>> goldfish = GoldFish()
这是Fish
这是金鱼
>>> 
>>> ##解决方案2
>>> ##使用super
>>> 
>>> class Fish:
	    def __init__(self):
		print('这是Fish')

class GoldFish(Fish):
    def __init__(self):
        Fish.__init__(self)##重新调用父类初始化方法，注意这里self是子类的实例对象
        print('这是金鱼')
class SHark(Fish):
    def __init__(self):
        print('这是鲨鱼')
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
这是金鱼
>>> go = GoldFish()
这是Fish
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
这是金鱼
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
这是金鱼
>>> gold = GoldFish()
这是Fish
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> gold = GoldFish()
这是Fish
这是金鱼
\
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> c = C()
>>> c.fool()
我是fool 1
>>> c.fool2()
我是fool 2
>>> 
=============== RESTART: D:/Python/2019-8-10-类和对象：面向对象编程-2.py ===============
>>> c = C()
>>> c.fool()
我是fool 1
>>> 
