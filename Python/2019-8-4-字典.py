Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> brand = ['鸡','你','太','美']
>>> slogan = ]
SyntaxError: invalid syntax
>>> slogan = ['Oh','b','a','b']
>>> print('mei',slogan[brand.index('鸡')])
mei Oh
>>> 
>>> dict1 = {'鸡':'Oh','你':'b','太':'a','美':'y'}
>>> print('鸡二',dict1['鸡'])
鸡二 Oh
>>> ##字典标志性东西：大括号    	key--value  键：值
>>> dict2 = {1:'one',2:'two',3:'There'}
>>> dict2{2}
SyntaxError: invalid syntax
>>>  dict2[2]
 
SyntaxError: unexpected indent
>>> dict2[2]
'two'
>>> dict3 = {}
>>> ##空的
>>> 
>>> dict3 = dict((('F',70),('i',105),('s',115),('h',104)))
>>> dict3 = dict((('F',70),('i',105),('s',115),('h',104)))
>>> ##可以将元组作为参数传入，为什么有这么多括号原因是应为dict的参数只有一个迭代器
>>> dict4 = dict(小甲鱼 = '让变成改变世界',苍井空 = 'AV')
>>> dict4
{'小甲鱼': '让变成改变世界', '苍井空': 'AV'}
>>> ##注意这里小甲鱼和仓井是不能带引号的，这里相当于一个新定义的变量
>>> 
>>> dict4['苍井空'] = '所有AV职业者都要通过学习编程'
>>> dict4
{'小甲鱼': '让变成改变世界', '苍井空': '所有AV职业者都要通过学习编程'}
>>> ##可以这样修改键对应的值
>>> dict4['爱迪生'] = '天才就是99%汗水 + 1%灵感，但是1%的灵感远比99%更重要'
>>> dict4
{'小甲鱼': '让变成改变世界', '苍井空': '所有AV职业者都要通过学习编程', '爱迪生': '天才就是99%汗水 + 1%灵感，但是1%的灵感远比99%更重要'}
>>> 
