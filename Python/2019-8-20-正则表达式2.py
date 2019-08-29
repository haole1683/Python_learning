Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.search(r'Fish(C|D)','FishC')
<re.Match object; span=(0, 5), match='FishC'>
>>> 
>>> # | 管道符，表示或
>>> 
>>> re.search(r'Fish(C|D)','FishC')
<re.Match object; span=(0, 5), match='FishC'>
>>> 
>>> re.search(r'^FishC','FishC','I love FishC.com!')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    re.search(r'^FishC','FishC','I love FishC.com!')
  File "D:\Python\lib\re.py", line 183, in search
    return _compile(pattern, flags).search(string)
  File "D:\Python\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "D:\Python\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "D:\Python\lib\sre_parse.py", line 930, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
TypeError: unsupported operand type(s) for &: 'str' and 'int'
>>> re.search(r'^FishC','FishC','I love FishC.com!')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    re.search(r'^FishC','FishC','I love FishC.com!')
  File "D:\Python\lib\re.py", line 183, in search
    return _compile(pattern, flags).search(string)
  File "D:\Python\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "D:\Python\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "D:\Python\lib\sre_parse.py", line 930, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
TypeError: unsupported operand type(s) for &: 'str' and 'int'
>>> re.search(r'^FishC','I love FishC.com!')
>>> # 脱字符  ^ 要求此处F必须出现在字符串的开头
>>> re.search(r'^FishC','FishC.com!')
<re.Match object; span=(0, 5), match='FishC'>
>>> 
>>> re.search(r'^FishC$','love FishC')
>>> re.search(r'^FishC$','love FishC!')
>>> re.search(r'^FishC$','loveFishC!')
>>> re.search(r'^FishC$','loveFishC')
>>> re.search(r'^FishC$','love FishC')
>>> re.search(r'^FishC$','love FishC')
>>> # $以FishC作为结尾匹配
>>> 
>>> re.search(r'(FishC)\1','FishC')
>>> re.search(r'(FishC)\1','FishCFishC')
<re.Match object; span=(0, 10), match='FishCFishC'>
>>> # 相当于复制第几个括号里的内容 re.search(r"(A)(B)(C)/2")就匹配的是ABC本身加上第二个子类就是ABCB
>>> 
>>> re.search(r'.','FishCFishC')
<re.Match object; span=(0, 1), match='F'>
>>> re.search(r'/.','FishCFishC')
>>> re.search(r'\.','FishCFishC')
>>> re.search(r'[.]','FishCFishC')
>>> 
>>> re.search(r'[.]','FishCFish.C')
<re.Match object; span=(9, 10), match='.'>
>>> # []字符类将[]内视为字符
>>> 
>>> re.findall(r'[a-z]','Fish')
['i', 's', 'h']
>>> # - 表示范围
>>> 
>>> re.search(r'[\]','FishCFish.C')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    re.search(r'[\]','FishCFish.C')
  File "D:\Python\lib\re.py", line 183, in search
    return _compile(pattern, flags).search(string)
  File "D:\Python\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "D:\Python\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "D:\Python\lib\sre_parse.py", line 930, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "D:\Python\lib\sre_parse.py", line 426, in _parse_sub
    not nested and not items))
  File "D:\Python\lib\sre_parse.py", line 532, in _parse
    source.tell() - here)
re.error: unterminated character set at position 0
>>> re.search(r'[\n]','FishCFish.C\n')
<re.Match object; span=(11, 12), match='\n'>
>>> 
>>> re.finall(r'[^a-z]','Fish')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    re.finall(r'[^a-z]','Fish')
AttributeError: module 're' has no attribute 'finall'
>>> 
>>> re.search(r'FishC{3}','FishCCC')
<re.Match object; span=(0, 7), match='FishCCC'>
>>> # 匹配C三次
>>> 
>>> re.search(r'FishC{3}','FishCFishCFishC')
>>> re.search(r'(FishC){3}','FishCFishCFishC')
<re.Match object; span=(0, 15), match='FishCFishCFishC'>
>>> # 想要整体匹配加上小括号
>>> 
>>> re.search(r'(FishC){24}','FishCFishCFishC')
>>> re.search(r'(FishC){24}','FishCFishCFishC')
>>> re.search(r'(FishC){2-4}','FishCFishCFishC')
>>> re.search(r'(FishC){2,4}','FishCFishCFishC')
<re.Match object; span=(0, 15), match='FishCFishCFishC'>
>>> # {}中2,4表示匹配FishC 2-4次
>>> 
>>> re.search(r'(FishC){2, 4}','FishCFishCFishC')
>>> # 但是小心不要随表加空格，会被认为是正则表达式匹配
>>> 
>>> s = '<html><title>I love FishC <title><html>'
>>> re.search(r'<.+>',s)
<re.Match object; span=(0, 39), match='<html><title>I love FishC <title><html>'>
>>> # 默认贪婪匹配
>>> 
>>> re.search(r'<.+?>,'5)
SyntaxError: invalid syntax
>>> re.search(r'<.+?>,'s)
SyntaxError: invalid syntax
>>> re.search(r'<.+?>,'s)
SyntaxError: invalid syntax
>>> re.search(r'<.+?>,s)
	  
SyntaxError: EOL while scanning string literal
>>> re.search(r'<.+?>,s)
	  
SyntaxError: EOL while scanning string literal
>>> re.search(r'<.+?>',s)
<re.Match object; span=(0, 6), match='<html>'>
>>> # 在后面加上?表示非贪婪
>>> 
>>> 
