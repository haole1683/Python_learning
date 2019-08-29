Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myGen():
	print('生成器被执行')
	yield 1
	yield 2

	
>>> myG = myGen()
>>> next(myG)
生成器被执行
1
>>> next(myG)
2
>>> next(myG)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    next(myG)
StopIteration
>>> for i in myGen():
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in myGen():
	print (i)

	
生成器被执行
1
2
>>> def fibs():
	a = 0
	b = 1
	while True:
		a,b = b,a + b
		yield a

		
>>> for each in fibs():
	if each > 100:
		break
	print(each,end = '')

	
1123581321345589
>>> a = [i for i in range(100) if not( i % 2) and i %3]
>>> a
[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]
>>> b = {i:i%2 == 0 for i in range(10)}
>>> 
>>> b
{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
>>> c = {i for i in [1,1,2,3,4,5,5,6,7,8,3,2,1]}
>>> c
{1, 2, 3, 4, 5, 6, 7, 8}
>>> d = 'i for i in '
>>> f
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> d
'i for i in '
>>> e = (i for i in range(10))
>>> e
<generator object <genexpr> at 0x000001BDE78FE448>
>>> next(e)
0
>>> next(e)
1
>>> next(e)
2
>>> for each in e :
	print(e)

	
<generator object <genexpr> at 0x000001BDE78FE448>
<generator object <genexpr> at 0x000001BDE78FE448>
<generator object <genexpr> at 0x000001BDE78FE448>
<generator object <genexpr> at 0x000001BDE78FE448>
<generator object <genexpr> at 0x000001BDE78FE448>
<generator object <genexpr> at 0x000001BDE78FE448>
<generator object <genexpr> at 0x000001BDE78FE448>
>>> for each in e:
	print(each)

	
>>> sum(i for i in range(100) if i % 2)
2500
>>> 
>>> 
