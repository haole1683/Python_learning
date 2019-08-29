Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##列表
>>> ##一个打了激素的数组
>>> ##创建一个普通列表
>>> member = {'小甲鱼','小布丁','黑恶'}
>>> member
{'小甲鱼', '黑恶', '小布丁'}
>>> number = {1,2,3,4,5}
>>> number
{1, 2, 3, 4, 5}
>>> 
>>> ##混合列表
>>> mix = {1,'小甲鱼'，3.01，[1,2,3]}
SyntaxError: invalid character in identifier
>>> mix = [1,'傻逼',3.12,[1,2,3]]
>>> 
>>> ##k空列表
>>> empty = []
>>> empty
[]
>>> ##向列表添加元素
>>> member.append('傻逼是')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    member.append('傻逼是')
AttributeError: 'set' object has no attribute 'append'
>>> member.add('傻逼是你')
>>> member
{'小甲鱼', '黑恶', '小布丁', '傻逼是你'}
>>> len(member)
4
>>> member.append
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    member.append
AttributeError: 'set' object has no attribute 'append'
>>> member.append('dd')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    member.append('dd')
AttributeError: 'set' object has no attribute 'append'
>>> member.add('宋爸爸')
>>> member.extend(['ni','基你妹太'])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    member.extend(['ni','基你妹太'])
AttributeError: 'set' object has no attribute 'extend'
>>> 
