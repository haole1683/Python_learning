Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = 'I love you'
>>> str1[:6]
'I love'
>>> str1
'I love you'
>>> str1[]
SyntaxError: invalid syntax
>>> str1[5]
'e'
>>> str[:6] + '插入的字符串' + str[6:]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str[:6] + '插入的字符串' + str[6:]
TypeError: 'type' object is not subscriptable
>>> str1[:6] + '插入字符串' + str1[6:]
'I love插入字符串 you'
>>> str = str[1:]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str = str[1:]
TypeError: 'type' object is not subscriptable
>>> str1 = str1[1:]
>>> str1
' love you'
>>> ##字符串的奇葩内置函数
>>> str2 = 'wakakak'
>>> str2.capitalize()
'Wakakak'
>>>  ##首字母大写
>>> 
>>> str2.casefold()
'wakakak'
>>> ##字符串变小写
>>> ##但是要注意这里仅是返回一份修改完的字符串，而str2本身并未修改
>>> 
>>> str2.center(5)
'wakakak'
>>> 
>>> str2.count('lo')
0
>>> str2.count('wa')
1
>>> str2.endswith('ak')
True
>>> str2 = 'I \t love \t you'
>>> str2
'I \t love \t you'
>>> str3 = 'I love\t'
>>> str3
'I love\t'
>>> str2
'I \t love \t you'
>>> str1
' love you'
>>> str1.find('love')
1
>>> 
