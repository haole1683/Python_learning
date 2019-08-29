Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class CapStr(str):
	def __new__(cls,string):
		string = string.upper()
		return str.__name__(cls,string)

	
>>> a = CapStr('I Love')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a = CapStr('I Love')
  File "<pyshell#4>", line 4, in __new__
    return str.__name__(cls,string)
TypeError: 'str' object is not callable
>>> class CapStr(str):
	def __new__(cls,string):
		string = string.upper()
		return str.__new__(cls,string)

>>> 
>>> a = CapStr('I love')
>>> a
'I LOVE'
>>> ##__init__
>>> 
>>> ##__del__
>>> 
>>> class C:
	def __init__(self):
		print('init')
	def __def__(self):
		print(delf)

		
>>> c1 = C()
init
>>> c2 = c1
>>> c3 = c2
>>> del c2
>>> del c3
>>> del c1
>>> 
>>>  class C:
	def __init__(self):
		print('init')
	def __def__(self):
		print('def')
		
SyntaxError: unexpected indent
>>> class C:
	def __init__(self):
		print('init')
	def __def__(self):
		print('def')

		
>>> c1  = C()
init
>>> c2 = c1
>>> c3 = c2
>>> del c1
>>> del c2
>>> del c3
>>> b = C()
init
>>> 
>>> class C:
	def __init__(self):
		print('init')
	def __del__(self):
		print('def')

		
>>> c1 = C()
init
>>> c2 = c1
>>> c3 = c1
>>> del c1
>>> del c2
>>> del c3
def
>>> 
