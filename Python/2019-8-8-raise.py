Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> raise
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise
RuntimeError: No active exception to reraise
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> raise ZeroDivisionError
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    raise ZeroDivisionError
ZeroDivisionError
>>> raise ZeroDivisionError('除数为0异常')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    raise ZeroDivisionError('除数为0异常')
ZeroDivisionError: 除数为0异常
>>> 
