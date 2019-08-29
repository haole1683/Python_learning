Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##迭代器
>>> for i in 'FishC':
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in 'FishC':
	print (i)

	
F
i
s
h
C
>>> links = {'鱼C工作室':'http://www.fishc.com',\}
	 
SyntaxError: unexpected character after line continuation character
>>> links = {'鱼C工作室':'http://www.fishc.com',\
	 '鱼C论坛':'http://bbs.fish.com',\
	 '鱼C博客':'http://blog.fishc.com',\
	 '支持小甲鱼':'http://fishc.taobao.com'}'
SyntaxError: EOL while scanning string literal
>>> links = {'鱼C工作室':'http://www.fishc.com',\
	 '鱼C论坛':'http://bbs.fish.com',\
	 '鱼C博客':'http://blog.fishc.com',\
	 '支持小甲鱼':'http://fishc.taobao.com'}
>>> for each in links:
	print('%s -> %s' % (each ,links[each]))

	
鱼C工作室 -> http://www.fishc.com
鱼C论坛 -> http://bbs.fish.com
鱼C博客 -> http://blog.fishc.com
支持小甲鱼 -> http://fishc.taobao.com
>>> ##iter
>>> ##next
>>> 
>>> string = 'FishC'
>>> it = iter(string)
>>> next(it)
'F'
>>> next(it)
'i'
>>> 
>>> next(it)
's'
>>> next(it)
'h'
>>> next(it)
'C'
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    next(it)
StopIteration
>>> string = 'FishC'
>>> it = iter(string)
>>> while True:
	try :
		each = next(it)
	except StopIteration:
		break
	print(each)

	
F
i
s
h
C
>>> for each in string:
	print(each)

	
F
i
s
h
C
>>> class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a +self.b
		return self.a

	
>>> fibs = Fibs()
>>> for each in fibs:
	print(each)

	
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
1346269
2178309
3524578
5702887
9227465
14930352
24157817
39088169
63245986
102334155
165580141
267914296
433494437
701408733
1134903170
1836311903
2971215073
4807526976
7778742049
12586269025
20365011074
32951280099
53316291173
86267571272
139583862445
225851433717
365435296162
591286729879
956722026041
1548008755920
2504730781961
4052739537881
6557470319842
10610209857723
17167680177565
27777890035288
44945570212853
72723460248141
117669030460994
190392490709135
308061521170129
498454011879264
806515533049393
1304969544928657
2111485077978050
3416454622906707
5527939700884757
8944394323791464
14472334024676221
23416728348467685
37889062373143906
61305790721611591
99194853094755497
160500643816367088
259695496911122585
420196140727489673
679891637638612258
1100087778366101931
1779979416004714189
2880067194370816120
4660046610375530309
7540113804746346429
12200160415121876738
19740274219868223167
31940434634990099905
51680708854858323072
83621143489848422977
135301852344706746049
218922995834555169026
354224848179261915075
573147844013817084101
927372692193078999176
1500520536206896083277
2427893228399975082453
3928413764606871165730
6356306993006846248183
10284720757613717413913
16641027750620563662096
26925748508234281076009
43566776258854844738105
70492524767089125814114
114059301025943970552219
184551825793033096366333
298611126818977066918552
483162952612010163284885
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    print(each)
KeyboardInterrupt
>>> for each in fibs:
	if each < 20
	
SyntaxError: invalid syntax
>>> fibs = Fibs()
>>> for each in fibs:
	if each < 20:
		print(each)
	else
	
SyntaxError: invalid syntax
>>> for each in fibs:
	if each < 20:
		print(each)
	else:
		break

	
1
1
2
3
5
8
13
>>> class Fibs:
	def __init__(self,n = 10):
		self.a = 0
		self.b = 1
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a +self.b
		if self.a > self.n:
			raise StopIteration
		return self.a

	
>>> fibs = Fibs()
>>> for each in fibs:
	print(each)

	
1
1
2
3
5
8
>>> fibs = Fibs(100)
>>> for each in fibs:
	print(each)

	
1
1
2
3
5
8
13
21
34
55
89
>>> 
