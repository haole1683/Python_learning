Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1 = {}
>>> dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict1.fromkeys((1,2,3),'Number')
{1: 'Number', 2: 'Number', 3: 'Number'}
>>> dict1.fromkeys((1,2,3),('one','two','there'))
{1: ('one', 'two', 'there'), 2: ('one', 'two', 'there'), 3: ('one', 'two', 'there')}
>>> ##它会默认把后面元组的值全部赋值给前面的数字
>>> dict1.fromkeys((1,3),'数字')
{1: '数字', 3: '数字'}
>>> dict1 = dict1.fromkeys(range(32),'赞')
>>> dict1
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> for eachkey in dict1.keys():
	print(eachkey)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
>>> for eachvalue in dict1.values():
	print(eachvalue)

	
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
>>> ##keys()和values（分别是该字典的所有键和所有值)
>>> for eachItem in dict1.Items():
	print(eachItem)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for eachItem in dict1.Items():
AttributeError: 'dict' object has no attribute 'Items'
>>> for eachItem in dict1.items():
	print(eachItem)

	
(0, '赞')
(1, '赞')
(2, '赞')
(3, '赞')
(4, '赞')
(5, '赞')
(6, '赞')
(7, '赞')
(8, '赞')
(9, '赞')
(10, '赞')
(11, '赞')
(12, '赞')
(13, '赞')
(14, '赞')
(15, '赞')
(16, '赞')
(17, '赞')
(18, '赞')
(19, '赞')
(20, '赞')
(21, '赞')
(22, '赞')
(23, '赞')
(24, '赞')
(25, '赞')
(26, '赞')
(27, '赞')
(28, '赞')
(29, '赞')
(30, '赞')
(31, '赞')
>>> ##items：所有项
>>> 
>>> print(dict1[32])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(dict1[32])
KeyError: 32
>>> 
>>> ##get
>>> dict1.get(32)
>>> print(dict1.get(32))
None
>>> dict.get(32,'木有')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict.get(32,'木有')
TypeError: descriptor 'get' requires a 'dict' object but received a 'int'
>>> dict1.get(32,'木有')
'木有'
>>> dict1.get(31,'木有')
'赞'
>>> ##如果有的话就会打印出已存在的值，没有则打印'木有'
>>> 31 in dict1
True
>>> 32 in dict1
False
>>> ##索引一个key是否在字典之中还可以使用这种方法
>>> ##但是要注意这里查找的是键而不是值
>>> 
>>> ##清空一个字典
>>> dict1.clear()
>>> dict1
{}
>>> a = {鸡 = 'ni'}
SyntaxError: invalid syntax
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> ##dic的copy是浅拷贝
>>> a = {1:'one',2:'two',3:'Three'}
>>> b = a.copy()
>>> c = 1
>>> c = a
>>> id(a)
2178593672872
>>> id(b)
2178593672552
>>> id(c)
2178593672872
>>> c[4] = 'four'
>>> a
{1: 'one', 2: 'two', 3: 'Three', 4: 'four'}
>>> b
{1: 'one', 2: 'two', 3: 'Three'}
>>> a.pop(2)
'two'
>>> a.popitem()
(4, 'four')
>>> ##pop弹出就没有了
>>> a
{1: 'one', 3: 'Three'}
>>> a.setdefault('shabi':'dadf')
SyntaxError: invalid syntax
>>> a.setdefault('shabi':'dadf')
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> a.setdefault(shabi:'dadf')
SyntaxError: invalid syntax
>>> a.setdefault('shabi')
>>> a
{1: 'one', 3: 'Three', 'shabi': None}
>>> a.setdefault(5,'废物')
'废物'
>>> a
{1: 'one', 3: 'Three', 'shabi': None, 5: '废物'}
>>> ##字典没有顺序的概念
>>> 
>>> b = {'小白':'dog'}
>>> a.update(b)
>>> a
{1: 'one', 3: 'Three', 'shabi': None, 5: '废物', '小白': 'dog'}
>>> ##up更新字典之中数据
