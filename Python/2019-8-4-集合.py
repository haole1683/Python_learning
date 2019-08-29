Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = {}
>>> type(num)
<class 'dict'>
>>> num2 = {1,2,3,4,5}
>>> type(num2)
<class 'set'>
>>> num2 = {1,2,3,4,5,6,5,4,3,2,1}
>>> num2
{1, 2, 3, 4, 5, 6}
>>> ##集合里的元素是唯一的，所有重复元素会清理
>>> num2[2]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num2[2]
TypeError: 'set' object is not subscriptable
>>> ##但是集合是无序的，无法用索引
>>> set1 = set([1,2,3,4,5,5])
>>> set1
{1, 2, 3, 4, 5}
>>> ##利用链表创建集合
>>> num1 = [1,2,3,4,5,3,1,0]
>>> num1
[1, 2, 3, 4, 5, 3, 1, 0]
>>> temp = []
>>> for each in num1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5, 0]
>>> num1 = list(set(num1))
>>> 
>>> num1
[0, 1, 2, 3, 4, 5]
>>> ##去除重复的元素
>>> ##但是结果没有顺序情况，结果是无序的
>>> ##用 in not in
>>> ##判断是否在一个集合
>>> 1 in num1
True
>>> 90 in num1
False
>>> 1 not in num1
False
>>> num2
{1, 2, 3, 4, 5, 6}
>>> num2.add(9）
	 
SyntaxError: invalid character in identifier
>>> num2.add(90

	 )
>>> num2
{1, 2, 3, 4, 5, 6, 90}
>>> ##添加新元素
>>> num2.remove(1)
>>> ##去除新元素
>>> ##去除元素
>>> num2.add(88)
>>> num2
{2, 3, 4, 5, 6, 88, 90}
>>> 
>>> ##不可变集合
>>> num3 = frozenset([1,5,3,2])
>>> num3.add(2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    num3.add(2)
AttributeError: 'frozenset' object has no attribute 'add'
>>> ##frozenset就会相当于const不可修改
>>> 
