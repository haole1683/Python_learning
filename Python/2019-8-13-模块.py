Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import hello
>>> hi()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    hi()
NameError: name 'hi' is not defined
>>> import hello as h
>>> h.hi()
I love you
>>> hello.hi()
I love you
>>> 
