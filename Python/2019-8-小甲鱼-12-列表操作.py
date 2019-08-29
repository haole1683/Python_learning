Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##元组
>>> ##由于和列表是近亲关系，所以使用非常相似
>>> 
>>> 
>>> ##create and 访问 a 元组
>>> tuple1 = (1,2,3,4,5,6,7,8)
>>> tuple
<class 'tuple'>
>>> tuple1
(1, 2, 3, 4, 5, 6, 7, 8)
>>> tuple1[1]
2
>>> ##访问相同
>>> 
>>> tuple1[5:]
(6, 7, 8)
>>> tuple1[:5]
(1, 2, 3, 4, 5)
>>> 
>>> ##拷贝
>>> tuple2 = tuple1[:]
>>> tuple2
(1, 2, 3, 4, 5, 6, 7, 8)
>>> tuple[1]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple[1]
TypeError: 'type' object is not subscriptable
>>> tiple1[1]= 1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tiple1[1]= 1
NameError: name 'tiple1' is not defined
>>> ##元组元素是不可以被修改的
>>> temp = (1)
>>> temp
1
>>> type(temp)
<class 'int'>
>>> temp2 = 2,3,4
>>> type(temp2)
<class 'tuple'>
>>> ##所以判断是否为元组，不在于是否有括号，而在于是否有逗号
>>> ##如果要创建一个空元组，那么是
>>> temp = ()
>>> type(temp)
<class 'tuple'>
>>> ##如果要创建一个只含有一个元素的元组，则要在元素后面加上逗号
>>> temp = (1,)
>>> type(temp)
<class 'tuple'>
>>> type(temp)
<class 'tuple'>
>>> 8 * 8
64
>>> 8 * (8)
64
>>> 8 * (8,)
(8, 8, 8, 8, 8, 8, 8, 8)
>>> ##注意这里就是相当于列表，此处的乘号就相当于重复操作符
>>> 
>>> temp = ('小甲鱼','黑夜','煞笔')
>>> temp = temp[:2] + ('你爸爸',) + temp[2:]
>>> temp
('小甲鱼', '黑夜', '你爸爸', '煞笔')
>>> ##所以想要添加新元素或者删减新元素的操作是这样
>>> ##但是要注意加入的元素一定要按照上述操作进行，括号逗号缺一不可，否则会报错
>>> 
>>> ##删除整个元组
>>> delete tem[
	
SyntaxError: invalid syntax
>>> delete temp
SyntaxError: invalid syntax
>>> del temp
>>> ##手动释放
