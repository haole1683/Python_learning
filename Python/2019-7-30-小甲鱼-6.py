Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 0.0000000000000000000000000025
>>> print(a)
2.5e-27
>>> 15000000000000000000
15000000000000000000
>>> 1.5e11
150000000000.0
>>> ##e计法
>>> True + True
2
>>> True + False
1
>>> True * False
0
>>> ##Type Transpration
>>> a = '520'
>>> b = int(a)
>>> b
520
>>> b= int('xiaojiayu')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b= int('xiaojiayu')
ValueError: invalid literal for int() with base 10: 'xiaojiayu'
>>> a = 5.99
>>> c = int(a)
>>> c
5
>>> 
>>> a = '520'
>>> b = float(a)
>>> b
520.0
>>> a =520
>>> b = float (a)
>>> b
520.0
>>> a = 5.99
>>> b = str(a)
>>> b
'5.99'
>>> c = str(5e19)
>>> c
'5e+19'
>>> str = 'I love fishc'
>>> c =str(5e19)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c =str(5e19)
TypeError: 'str' object is not callable
>>> ##注意此处str已经被赋予值了，之后使用str转换就会默认是定义的str，而非是转换的str函数
>>> ##str   int  float  将对应数据转化为所需要的数据

>>> ##获取关于类型的信息：type
>>> a = '520'
>>> type(a)
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type(3.44)
<class 'float'>
>>> ##isinstance  传入两个类型，判断两个是否为同意类型
>>> a = '小甲鱼'
>>> isinstance(a,1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    isinstance(a,1)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(a,1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    isinstance(a,1)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(a,2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    isinstance(a,2)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(a,int)
False
>>> isinstance(1,int])
SyntaxError: invalid syntax
>>> isinstance(1,int)
True
>>> 
