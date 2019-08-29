Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [123]
>>> list2 = [234]
>>> list1 > list2
False
>>> list1 = [123,456]
>>> list2 = [234,123]
>>> list1 > list2
False
>>> ##从前面的元素进行比比较，类似于字符串
>>> list3 = [123,456]
>>> (list1 < list2) and (list1 == list3)
True
>>> list4 = list1 + list2
>>> list4
[123, 456, 234, 123]
>>> ##类似于字符串拼接
>>> ##list.extend()
>>> ##但是下列的就是不行的
>>> list1 = list4 + 'dd'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list1 = list4 + 'dd'
TypeError: can only concatenate list (not "str") to list
>>> ##这里由于 + 号两边的类型需要相同，因此不能这样子操作，可以使用append extend
>>> list3
[123, 456]
>>> list * 3
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list * 3
TypeError: unsupported operand type(s) for *: 'type' and 'int'
>>> list3 *3
[123, 456, 123, 456, 123, 456]
>>> ##列表 * 运算（重复运算符）
>>> list3 *= 3
>>> list3
[123, 456, 123, 456, 123, 456]
>>> list3 *=5
>>> list3
[123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456]
>>> 123 in list3
True
>>> 'cc' not in list3
True
>>> list5 = [123,['ji','ni'],456]
>>> list5
[123, ['ji', 'ni'], 456]
>>> 'ji' in list5
False
>>> ##访问列表中的列表元素
>>> 'ji' in list5[1]
True
>>> ##类似于二维数组访问
>>> list5[1][1]
'ni'
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> ##列举列表内置函数
>>> ##常用列表函数
>>> list3.count(123)
15
>>> ##count用于计算一个列表之中一个元素出现多少次
>>> ##
>>> ##index:返回参数在列表中的位置
>>> list3.index(123)
0
>>> list3.index(123,3,7)
4
>>> ##可以有两个参数，上面'3'是开始元素位置,'7'是结束元素位置
>>> list3.index(123,3,15)
4
>>> ##但是只能索引到第一次出现的位置
>>> 
>>> ##reverse 将整个列表全部反转
>>> list3.reverse
<built-in method reverse of list object at 0x00000257EF4CD788>
>>> list3.reverse()
>>> list3
[456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123]
>>> 
>>> ##sort
>>> list6 = [4,2,5,1,9,23,66,444]
>>> list6.sort()
>>> list6
[1, 2, 4, 5, 9, 23, 66, 444]
>>> ##sort 排序
>>> ##如果想要反过来排序
>>> ##sort(reverse = False)
>>> list6.sort(reverse = True)
>>> list6
[444, 66, 23, 9, 5, 4, 2, 1]
>>> 
>>> 
>>> list7 = list6[:]
>>> list7
[444, 66, 23, 9, 5, 4, 2, 1]
>>> lilst8 = list6
>>> lilst8
[444, 66, 23, 9, 5, 4, 2, 1]
>>> list6.sort()
>>> list7
[444, 66, 23, 9, 5, 4, 2, 1]
>>> list8
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list8
NameError: name 'list8' is not defined
>>> lilst8
[1, 2, 4, 5, 9, 23, 66, 444]
>>> list6
[1, 2, 4, 5, 9, 23, 66, 444]
>>> ##关于分片拷贝（类似于深拷贝，浅拷贝）
>>> ##直接使用等号，那么这个新建的小相当于多了一份标签
>>> ##而前一种，就是深拷贝，是额外的空间
>>> 
