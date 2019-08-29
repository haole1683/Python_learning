Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("你妈死了")
你妈死了
>>> print "d"你妈死了
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("d"你妈死了)?
>>> print "hiahia"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hiahia")?
>>> ###d
>>> print("ddd");
ddd
>>> print("你妈死了")
你妈死了
>>> print("鸡你太美")
鸡你太美
>>> print "d"你妈死了
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("d"你妈死了)?
>>> print "hiahia"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hiahia")?
>>> print "hiahia"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hiahia")?
>>> printf("nimasile")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    printf("nimasile")
NameError: name 'printf' is not defined
>>> printf("ddddd");
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    printf("ddddd");
NameError: name 'printf' is not defined
>>> print(5+3)
8
>>> 5+3
8
>>> 666666666
666666666
>>> print("well")
well
>>> 123456789+212
123457001
>>> 666666666666*999999999999
666666666665333333333334
>>> 987654321*123456789##support big number caclulattion
121932631112635269
>>> ##d
>>> print("well water"+"river")
well waterriver
>>> ##字符串也可以
>>> 
>>> print("well water"+" river")
well water river
>>> print("你死傻屌")*8
你死傻屌
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("你死傻屌")*8
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> print("鸡你太美"*8)
鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美
>>> print("基你妹太\n"*8)
基你妹太
基你妹太
基你妹太
基你妹太
基你妹太
基你妹太
基你妹太
基你妹太

>>> print("鸡你太美"+8)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print("鸡你太美"+8)
TypeError: can only concatenate str (not "int") to str
>>>
##这里报错是因为字符串与数字根本不是一个类型，没有意义，但是乘以*就有意义
##此外，want to add a " in the string?
##Just do as the follow
print("\"You are a stupid man")



