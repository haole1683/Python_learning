Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##列表添加元素
>>> member = ['鸡','你','太','美']
>>> member.append('我')
>>> member.extend(['是练习时长两年半','篮球练习生'])
>>> member
['鸡', '你', '太', '美', '我', '是练习时长两年半', '篮球练习生']
>>> len(member)
7
>>> ##extend添加列表
>>> 
>>> ##insert
>>> member.insert(1,'吐过')
>>> member
['鸡', '吐过', '你', '太', '美', '我', '是练习时长两年半', '篮球练习生']
>>> ##从列表之中获取元素
>>> member[0]
'鸡'
>>> member[1]
'吐过'
>>> ##exchange
>>> temp = member[0]
>>> member = member[1]
>>> member
'吐过'
>>> member = ['鸡','你','太','美']
>>> temp = member[0]
>>> member[0] = member[1]
>>> member[1] = temp
>>> member
['你', '鸡', '太', '美']
>>> ##从列表删除元素
>>> member.remove('太')
>>> member
['你', '鸡', '美']
>>> 
