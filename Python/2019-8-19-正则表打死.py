Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.search(r'FishC','I love FishC.com')
<re.Match object; span=(7, 12), match='FishC'>
>>> #search()方法用于在字符串之中搜索正则表达式模式第一次出现的位置
>>> 
>>> ##起始从0开始
>>> 
>>> 'I love CifhC.com'.find('Ci')
7
>>> re.search(r'.','I love FishC.com!')
<re.Match object; span=(0, 1), match='I'>
>>> # . 号表示除了换行符任何一个字符
>>> 
>>> re.search(r'Fish.','I love FishC.com')
<re.Match object; span=(7, 12), match='FishC'>
>>> 
>>> re.search(r'FishC\.','I love FishC.com')
<re.Match object; span=(7, 13), match='FishC.'>
>>> # 如果想匹配 . 则加上反斜杠
>>> 
>>> re.search(r'\d','I love 12FishC.com')
<re.Match object; span=(7, 8), match='1'>
>>> # \d 则表示任何数字
>>> re.search(r'\d\d\d','I love 1245FishC.com')
<re.Match object; span=(7, 10), match='124'>
>>> 
>>> 
>>> re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.111.124')
<re.Match object; span=(0, 15), match='192.168.111.124'>
>>> # 尝试匹配ip地址
>>> 
>>> # 但是会出现问题
>>> re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.111.14')
>>> 
>>> 
>>> 
>>> re.search(r'[aeiou]','I love FishC.com')
<re.Match object; span=(3, 4), match='o'>
>>> # []用括号  字符类中只要匹配任何一个字符就算匹配
>>> 
>>> # 但是正则表达式开启大小写敏感模式
>>> re.search(r'[aeiouAEIOU]','I love FishC.com')
<re.Match object; span=(0, 1), match='I'>
>>> # 正则表达式任意一个匹配成功就算成功
>>> 
>>> # 还可以表示范围
>>> re.search(r'[a-z]','I love FishC')
<re.Match object; span=(2, 3), match='l'>
>>> re.search(r'[1-9]','I lovedfsa111 FishC')
<re.Match object; span=(10, 11), match='1'>
>>> # [a-z]  [1-9]这种的
>>> 
>>> re.search(r'[1-5]','9393')
<re.Match object; span=(1, 2), match='3'>
>>> 
>>> 
>>> # 限定重复匹配次数
>>> re.search(r'ab[3]c','abbbc')
>>> re.search(r'ab{3}c','abbbc')
<re.Match object; span=(0, 5), match='abbbc'>
>>> # {}表示重复次数
>>> 
>>> # 但是如果手一抖，d多了就无法匹配
>>> re.search(r'ab[3]c','abbbbbc')
>>> 
>>> #如果想匹配范围
>>> re.search(r'ab{3,10}c','abbbbbbc')
<re.Match object; span=(0, 8), match='abbbbbbc'>
>>> # 可以匹配b的个数的范围
>>> 
>>> re.search(r'[0-255]',188)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    re.search(r'[0-255]',188)
  File "D:\Python\lib\re.py", line 183, in search
    return _compile(pattern, flags).search(string)
TypeError: expected string or bytes-like object
>>> re.search(r'[0-255]','188')
<re.Match object; span=(0, 1), match='1'>
>>> re.search(r'[0-2][0-5][0-5]','188')
>>> # 注意正则表达式是按照字符串类型来匹配，只有0-9
>>> 
>>> # 想要匹配0-255之内的数字应该这么写
>>> re.search(r'[01]\d\d|2[0-4]|25[0-5]','188')
<re.Match object; span=(0, 3), match='188'>
>>> # 此处 | 相当于或
>>> # 上面写错了
>>> re.search(r'[01]\d\d|2[0-4]\d25[0-5]','188')
<re.Match object; span=(0, 3), match='188'>
>>> # 000-099 + 100 - 199 + 200 - 209 + 210 - 219 + 220 - 229 + 230 - 239 + 240 - 249 +250 - 255
>>> 
>>> re.search(r'[01]\d\d|2[0-4]\d|25[0-5]\.{3}([01]\d\d)|2[0-4]\d|25[0-5]','163.168.4.1')
<re.Match object; span=(0, 3), match='163'>
>>> re.search(r'([01]\d\d|2[0-4]\d|25[0-5]\.){3}([01]\d\d)|2[0-4]\d|25[0-5]','163.168.4.1')
>>> # 小括号表示整体
>>> 
>>> re.search(r'([01]{01}\d\d|2[0-4]\d|25[0-5]\.){3}([01]\d\d)|2[0-4]\d|25[0-5]','163.168.4.1')
>>> re.search(r'(25[0-5]|2[0-4]\d|[01]{0,1}\d{0,1}\d)\.){3}(25[0-5]|2[0-4]\d|[01]{0,1}\d{0,1}\d','186.235.62.3')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    re.search(r'(25[0-5]|2[0-4]\d|[01]{0,1}\d{0,1}\d)\.){3}(25[0-5]|2[0-4]\d|[01]{0,1}\d{0,1}\d','186.235.62.3')
  File "D:\Python\lib\re.py", line 183, in search
    return _compile(pattern, flags).search(string)
  File "D:\Python\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "D:\Python\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "D:\Python\lib\sre_parse.py", line 944, in parse
    raise source.error("unbalanced parenthesis")
re.error: unbalanced parenthesis at position 39
>>> re.search(r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d,','135.201.30.3')'
SyntaxError: EOL while scanning string literal
>>> re.search(r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d,','135.201.30.3')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    re.search(r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d,','135.201.30.3')
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
  File "D:\Python\lib\sre_parse.py", line 819, in _parse
    source.tell() - start)
re.error: missing ), unterminated subpattern at position 120
>>> re.search(r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d,','135.201.30.3')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    re.search(r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d,','135.201.30.3')
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
  File "D:\Python\lib\sre_parse.py", line 819, in _parse
    source.tell() - start)
re.error: missing ), unterminated subpattern at position 120
>>> 
