Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '%c' % 97
'a'
>>> '%c %c %C' % (97,98,99)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    '%c %c %C' % (97,98,99)
ValueError: unsupported format character 'C' (0x43) at index 7
>>> '%c %c %c' % (97,98,99)
'a b c'
>>> '%c'  %  100
'd'
>>> ##%c格式化输出字符或ASCii码
>>> 
>>> '%s' % '你是傻屌'
'你是傻屌'
>>> ##格式化字符串
>>> 
>>> ##格式化整数
>>> '%d + %d = %d' % (4,5,4+5)
'4 + 5 = 9'
>>> 
>>> ##格式化无符号八进制 %o
>>> '%o' %10
'12'
>>> '%x' %10
'a'
>>> '%X' %10
'A'
>>> ##x十六进制
>>> 
>>> '%f' %27.332323
'27.332323'
>>> 
>>> ##%e为科学计数法
>>> '%e' % 1354564541
'1.354565e+09'
>>> 
>>> 
>>> ##格式化操作辅助命令
>>> '%5.2f' % 27.23232233
'27.23'
>>> 
>>> '%.5e' % 21.2323566
'2.12324e+01'
>>> '%4f' % 2
'2.000000'
>>> '%4d' %2
'   2'
>>> 
>>> '%5+d' %3
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    '%5+d' %3
ValueError: unsupported format character '+' (0x2b) at index 2
>>> '%+5d' %3##前面加上+表示输出正数带+
'   +3'
>>> 
>>> '%#0' %10
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    '%#0' %10
ValueError: incomplete format
>>> '%#o' %10
'0o12'
>>> ##%后面加上#X表示八进制输出 o 十进制输出0x
>>> 
>>> '%#x' % 22
'0x16'
>>> ##前面加上0表示用0取代空格
>>> '%010d'  %5
'0000000005'
>>> '%-010d'  %5
'5         '
>>>  '%-010d'  % -5
 
SyntaxError: unexpected indent
>>>  
