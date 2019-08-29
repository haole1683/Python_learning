Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> teacher = '小甲鱼'
>>> print(teacher)
小甲鱼
>>> teacher = '老甲鱼'
>>> print(teacher)
老甲鱼
>>> first = 3
>>> second =
SyntaxError: invalid syntax
>>> second = 8
>>> third = first + second
>>> print(third)
11
>>> myteacher = '小甲鱼'
>>> youteacher = ' 黑鱼'
>>> ourteacher = myteacher + youteacher
>>> print(ourteacher)
小甲鱼 黑鱼
>>> fishc
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    fishc
NameError: name 'fishc' is not defined
>>> first
3
>>> 5+8
13
>>> '5'+'8'
'58'
>>> 'I love fish'
'I love fish'
>>> 'I love you "
SyntaxError: EOL while scanning string literal
>>> ##字符串有引号
>>> 'Let \'s go'
"Let 's go"
>>> 'Let "'"s go
SyntaxError: EOL while scanning string literal
>>> 'Let "'"s go'
SyntaxError: EOL while scanning string literal
>>> str = 'C:\mow'
>>> str = 'C:\now'
>>> print(str)
C:
ow
>>> str = 'C:\\now'
>>> print(str)
C:\now
>>> ##原始字符串
>>> ##只需要在原始字符串加上一个r
>>> str = r'C:\now'
>>> print(str)
C:\now
>>> str
'C:\\now'
>>> str = r'C:/now/now'
>>> str
'C:/now/now'
>>> str = r'C:\now\now'
>>> str
'C:\\now\\now'
>>> ##长字符串，两个双引号
>>> str = """"你是傻屌
你是傻屌
你是傻屌
""""
SyntaxError: EOL while scanning string literal
>>> ##原始字符
>>> ##长字符串就需要用到三重引号字符串
>>> str = """
你是傻逼
你是傻逼
你是傻
"""
>>> print(str)

你是傻逼
你是傻逼
你是傻

>>> 
