Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = list()
>>> a
[]
>>> b = 'I love fish C '
>>> b = llist(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b = llist(b)
NameError: name 'llist' is not defined
>>> b = list(b)
>>> b
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'f', 'i', 's', 'h', ' ', 'C', ' ']
>>> c = (1,2,3,5,8)
>>> c = list(c)
>>> c
[1, 2, 3, 5, 8]
>>> max(c)
8

>>> max(b)
'v'
>>> max('你傻吊吗')
'吗'
>>> min('你傻吊吗')
'你'
>>> tuple1 = (1,2,3,4,5,6,7,8,9)
>>> max(tuple)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    max(tuple)
TypeError: 'type' object is not iterable
>>> max(tuple1)
9
>>> 
>>> number = {1,2,3,4,5,34,2}
>>> number
{1, 2, 3, 4, 5, 34}
>>> number.append('d')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    number.append('d')
AttributeError: 'set' object has no attribute 'append'
>>> number.add('d')
>>> max(number)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    max(number)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> tupe2 = (1,2,3,4)
>>> sum(tupe2)
10
>>> numbers.pop()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    numbers.pop()
NameError: name 'numbers' is not defined
>>> number.pop()
1
>>> number
{2, 3, 4, 5, 34, 'd'}
>>> sum(tupe2,8)
18
>>> chars = '12345678'
>>> sum(chars)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    sum(chars)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> chars = 'fkkafndsa'
>>> sorted(chars)
['a', 'a', 'd', 'f', 'f', 'k', 'k', 'n', 's']
>>> ##sorted()  排序
>>> reversed(chars)##reversed倒置
<reversed object at 0x00000278901D8188>
>>> ##返回的一个迭代器
>>> list(reversed(number))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(reversed(number))
TypeError: 'set' object is not reversible
>>> numbers = {1，3，6,4,2,4,6,8,9,10}
SyntaxError: invalid character in identifier
>>> numbers = {1,2,4,3,5,6}
>>> numbers
{1, 2, 3, 4, 5, 6}
>>> fd
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    fd
NameError: name 'fd' is not defined
>>> list(reversed(numbers))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(reversed(numbers))
TypeError: 'set' object is not reversible
>>> numbers
{1, 2, 3, 4, 5, 6}
>>> reversed(numbers)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    reversed(numbers)
TypeError: 'set' object is not reversible
>>> numbers = [1,4,6,7,4,3]
>>> numbers
[1, 4, 6, 7, 4, 3]
>>> sorted(numbers)
[1, 3, 4, 4, 6, 7]
>>> list(reversed(numbers))
[3, 4, 7, 6, 4, 1]
>>> list(reversed(sorted(numbers)))
[7, 6, 4, 4, 3, 1]
>>> 
>>> ##直接用reversed(numbers)会生成一个迭代器，需要用list再次将其输出
>>> ##sorted()排序
>>> 
>>> ##enumerate
>>> enumerate(numbers)
<enumerate object at 0x0000027890161F98>
>>> list(enumerate(numbers))
[(0, 1), (1, 4), (2, 6), (3, 7), (4, 4), (5, 3)]\
>>> ##这个bif作用就是讲每一额元素生成一个元组，而且第一位是索引
>>> 
>>> ##同样直接使用的话会产生迭代器
>>> 
>>> ##zip
>>> a = [1,2,3,4,5,6,7,8]
>>> b = [4,5,6,7,8]
>>> zip(a,b)
<zip object at 0x00000278901F31C8>
>>> list(zip(a,b))
[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
>>> ##将两个元组对应索引位置对应生成一个元组
>>> 
>>> 
