Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.findall(r'\bFishC\b','FishC.com!Fish_com!(FishC)')
['FishC', 'FishC']
>>> # 这里只匹配了第一个和第三个，第二个的下划线被认为是非单词边界
>>> 
>>> re.findall(r'\w','我爱鱼C工作室,(love_FishC.com)')
['我', '爱', '鱼', 'C', '工', '作', '室', 'l', 'o', 'v', 'e', '_', 'F', 'i', 's', 'h', 'C', 'c', 'o', 'm']
>>> p = re.compile(r'[A-Z]')
>>> type(p)
<class 're.Pattern'>
>>> p.search('I love FIsh,c')
<re.Match object; span=(0, 1), match='I'>
>>> p.findall('I live ')
['I']
>>> re.I
<RegexFlag.IGNORECASE: 2>
>>> re.I
<RegexFlag.IGNORECASE: 2>
>>> 
