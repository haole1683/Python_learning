Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ds(x):
	return 2 * x + 1

>>> de(s)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    de(s)
NameError: name 'de' is not defined
>>> ds(5)
11
>>> lambda x : 2 * x +  1
<function <lambda> at 0x00000150BD84EAF8>
>>> g = lambda x : 2 * x + 1
>>> g(5)
11
>>> def add(x,y):
	return x + y

>>> add(3,4)
7
>>> lambda x , y : x + y
<function <lambda> at 0x00000150BD8AA5E8>
>>> add1 = lambda x ,y :x + y
>>> add1(1,4)
5
>>> 
>>> ##lambda：使用该表达式可以省下定义函数过程
>>> 
>>> ##过滤器 : filter()
>>> 
>>> help(filter())
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    help(filter())
TypeError: filter expected 2 arguments, got 0
>>> help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function or None, iterable) --> filter object
 |  
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> filter(None,[1,0,'false'],True)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    filter(None,[1,0,'false'],True)
TypeError: filter expected 2 arguments, got 3
>>> filter(None,[1,0,'false',True])
<filter object at 0x00000150BD8BDD48>
>>> list(filter(None,[1,0,'false',True]))
[1, 'false', True]
>>> list(filter(None,[1,0,False,True]))
[1, True]
>>> ##把任何非True得元素筛选条件

##map

list(map(lambda x: x * 2 ,range(10)))



