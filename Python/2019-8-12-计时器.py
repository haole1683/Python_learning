Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class A():
    def __str__(self):
        return '沙雕'


>>> a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = A()
>>> print(a)
沙雕
>>> class B():
	def __repr__(self):
		return '数'

	
>>> b = B()
>>> b
数
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1.start()
计时开始
>>> t
<module 'time' (built-in)>
1
>>> t1.stop()
<__main__.MyTimer object at 0x000002697A9445C8> 总共运行了000007
计时停止
>>> t1.stop()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t1.stop()
TypeError: 'time.struct_time' object is not callable
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1.start()
计时开始
>>> t1
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t1
  File "D:\Python\lib\idlelib\rpc.py", line 621, in displayhook
    text = repr(value)
  File "D:/Python/MyTimer.py", line 26, in __str__
    return self.prompt
AttributeError: 'MyTimer' object has no attribute 'prompt'
>>> t1.stop
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t1.stop
  File "D:\Python\lib\idlelib\rpc.py", line 621, in displayhook
    text = repr(value)
  File "D:/Python/MyTimer.py", line 26, in __str__
    return self.prompt
AttributeError: 'MyTimer' object has no attribute 'prompt'
>>> t1.stop()
总共运行了00001-44 总共运行了00001-44
计时停止
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1
未开始
>>> t1.start()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t1.start()
TypeError: 'int' object is not callable
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1
未开始
>>> t1.start()
计时开始
>>> t1.end()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t1.end()
TypeError: 'int' object is not callable
>>> t1.stop()
总共运行了0000020 总共运行了0000020
计时停止
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MytTimer()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t1 = MytTimer()
NameError: name 'MytTimer' is not defined
>>> t1 = MyTimer()
>>> t1.start()
计时开始
>>> t1.stop()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t1.stop()
  File "D:/Python/MyTimer.py", line 13, in stop
    self._calc();
  File "D:/Python/MyTimer.py", line 22, in _calc
    if lasted[index]:
NameError: name 'lasted' is not defined
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1.start()
计时开始
>>> t1.stop()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t1.stop()
  File "D:/Python/MyTimer.py", line 13, in stop
    self._calc();
  File "D:/Python/MyTimer.py", line 22, in _calc
    if lasted[index]:
NameError: name 'lasted' is not defined
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1.start()
计时开始
>>> t1.stop()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t1.stop()
  File "D:/Python/MyTimer.py", line 13, in stop
    self._calc();
  File "D:/Python/MyTimer.py", line 23, in _calc
    self.prompt += str(self.lasted[index] + self.unit[index])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1  = MyTimer()
>>> 
>>> t1.start()
计时开始
>>> t1.stop()
总共运行了5秒 总共运行了5秒
计时停止
>>> t1
总共运行了5秒
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1
未开始
>>> t1.start()
计时开始
>>> t1.stop()
总共运行了38秒 总共运行了38秒
计时停止
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = Mytimer()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t1 = Mytimer()
NameError: name 'Mytimer' is not defined
>>> t1
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t1
NameError: name 't1' is not defined
>>> t1 = MyTimer()
>>> t1.start()
计时开始
>>> t1.stop()
总共运行了5秒 总共运行了5秒
计时停止
>>> t2 = MyTimer()
>>> t1.start()
计时开始
>>> t2.stop()
提示请先调用start开始计时
>>> t1 + t2
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    t1 + t2
  File "D:/Python/MyTimer.py", line 50, in __add__
    result.append(self.lasted[index] + other.lasted[index])
IndexError: list index out of range
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> t1 = MyTimer()
>>> t1.start()
计时开始
>>> t1.stop()
总共运行了3秒 总共运行了3秒
计时停止
>>> t2 = MyTimer()
>>> t1.start()
计时开始
>>> t1.stop()
总共运行了4秒 总共运行了4秒
计时停止
>>> t1 + t2
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    t1 + t2
  File "D:/Python/MyTimer.py", line 50, in __add__
    result.append(self.lasted[index] + other.lasted[index])
IndexError: list index out of range
>>> 
======================= RESTART: D:/Python/MyTimer.py =======================
>>> 
