Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 定制容器
>>> ## 容器不可变：只需要定义__len__(),和__getitem__()
>>> 
>>> class CountList:
	def __init__(self,*args):
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.value)),0)
	def __len__(self):
		return len(self,values)
	def __getitem__(self,key):
		self.count[key] += 1
		return self.value[key]

	
>>> c1 = CountList(1,3,5,7,9)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c1 = CountList(1,3,5,7,9)
  File "<pyshell#13>", line 4, in __init__
    self.count = {}.fromkeys(range(len(self.value)),0)
AttributeError: 'CountList' object has no attribute 'value'
>>> class CountList:
	def __init__(self,*args):
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.values)),0)
	def __len__(self):
		return len(self,values)
	def __getitem__(self,key):
		self.count[key] += 1
		return self.values[key]

	
>>> c1 = CountList(1,3,5,7,9)
>>> c2 = CountList(2,4,6,8)
>>> c1[1]
3
>>> c2[1]
4
>>> c1[1] +c1[1]
6
>>> c1[1] + c2[1]
7
>>> c1.count
{0: 0, 1: 4, 2: 0, 3: 0, 4: 0}
>>> c1[1]
3
>>> c1
