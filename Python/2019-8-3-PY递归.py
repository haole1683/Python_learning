Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list(map(lambda x: x * 2 ,range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> ##map相当于迭代器中每一个元素拿出来进行lambda表达式运算
>>> ##递归
>>> def recursion():
	return recursion()

>>> recursion
<function recursion at 0x000002253DB1FD38>
>>> recursion()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    recursion()
  File "<pyshell#5>", line 2, in recursion
    return recursion()
  File "<pyshell#5>", line 2, in recursion
    return recursion()
  File "<pyshell#5>", line 2, in recursion
    return recursion()
  [Previous line repeated 991 more times]
RecursionError: maximum recursion depth exceeded
>>> import sys
>>> sys.setrecursionlimit(1000000)
>>> ##设置递归深度
>>> 
>>> def factorial(n):
	result = n
	for each in range(1,n):
		result *= i
	return result

>>> factorial(5)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    factorial(5)
  File "<pyshell#17>", line 4, in factorial
    result *= i
NameError: name 'i' is not defined
>>> def factorial(n):
	result = n
	for each in range(1,n):
		result *= each
	return result

>>> factorial(5)
120
>>> factorial(10)
3628800
>>> def factorial(n):
	if n == 1 return 1
	
SyntaxError: invalid syntax
>>> def factorial(n):
	if n == 1: return 1
	else: return n *factorial(n-1)

	
>>> factorial(4)
24
>>> 
