Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = ['我急你太美']
>>> assert len(my_list) > 0
>>> my_list.pop()
'我急你太美'
>>> assert len(my_list) > 0
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    assert len(my_list) > 0
AssertionError
>>> my_list.fishc
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    my_list.fishc
AttributeError: 'list' object has no attribute 'fishc'
>>> ##尝试访问位置对象方法火属性异常
>>> my_list = [1,2,3]
>>> my_list[3]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_list[3]
IndexError: list index out of range
>>> ##访问超出索引
>>> 
>>> my_dict = {'one':1,'two':2}
>>> my_dict{'one'}
SyntaxError: invalid syntax
>>> my_dict['one']
1
>>> my_dict['three']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    my_dict['three']
KeyError: 'three'
>>> ##keyerror 异常：字典之中不存在要访问的值
>>> 
>>> my_dict.get('four')
>>> fishc
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fishc
NameError: name 'fishc' is not defined
>>> ##尝试访问一个不存在的变量
>>> 
>>> ##osError
>>> ##有很多
>>> 
>>> print 'fafdsfas'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('fafdsfas')?
>>> 
>>> 1 + '1'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    1 + '1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> ##TypeError 不同类型之间无效操作
>>> 
>>> 4/0
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    4/0
ZeroDivisionError: division by zero
>>> ##ZeroDivisionError  除数为零
>>> 
>>> 
