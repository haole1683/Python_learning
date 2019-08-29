Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> (3 < 4) and (4 < 5)
True
>>> -3 ** 2
-9
>>> ##注意上面的运算符优先级
>>> ## **优先级高于 -优先级
>>> 
>>> (-3) ** 2
9
>>> ##加上括号则优先级先算括号里的
>>> ##同理
>>> 3 ** -2
0.1111111111111111
>>> ##这里就是相当于 3 ** (-2)
>>> 
>>> ##逻辑运算符
>>> ## and or not
>>> not True
False
>>> not False
True
>>> not 1
False
>>> not 0
True
>>> not 4
False
>>> 
>>> ##综合优先级
>>> ##幂运算(**) >  正负号(+x/-x)  >  算术操作符(*/ / / // + - ) >
>>> ## >比较运算符（> >=...）  > 逻辑运算符 （and or not）
>>> ##此外逻辑运算符之中 not > and >or
