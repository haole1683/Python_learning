Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> secret = random.randint(1,10)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    secret = random.randint(1,10)
NameError: name 'random' is not defined
>>> import random
>>> secret = random.randint(1,10)
>>> secret
8
>>> import os
>>> os.getcmd()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.getcmd()
AttributeError: module 'os' has no attribute 'getcmd'
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'D:\\Python'
>>> getcwd()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    getcwd()
NameError: name 'getcwd' is not defined
>>> ##getcwd返回当前工作目录
>>> os.chdir('E:\\')
>>> ##改变工作目录
>>> os.getcwd()
'E:\\'
>>> os.listdie('E:\\')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    os.listdie('E:\\')
AttributeError: module 'os' has no attribute 'listdie'
>>> os.listdir'E:\\')
SyntaxError: invalid syntax
>>> os.listdir('E:\\')
['$RECYCLE.BIN', '.temp', '1e3b6c01881321f4e1540eb5f6e06905', 'Adobe', 'Direct X', 'env', 'Games', 'hostd', 'kinggsoft', 'MCBox', 'messages', 'MyDrivers', 'Nier', 'Program Files (x86)', 'ProgramData', 'QLDownload', 'QLDownloadGame', 'QMDownload', 'qqpcmgr_docpro', 'qycache', 'System Volume Information', 'tencent', 'wegame', 'Windows Kits', '大一上', '大一下', '嵌入', '文件', '火线', '联盟', '英雄时刻']
>>> ##列举文件名
>>> os.mkdir('E:\\fa')
>>> os.mkdir('E:\\fa\\af')
>>> ##创建单层目录
>>> 
>>> os.remove('E:\\fa\\af')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.remove('E:\\fa\\af')
PermissionError: [WinError 5] 拒绝访问。: 'E:\\fa\\af'
>>> os.removedirs('E:\\fa\\af')
>>> os.system('cmd')
-1073741510
>>> os.system('calc')
0
>>> os.curdir
'.'
>>> os.listdir(os.curdie)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    os.listdir(os.curdie)
AttributeError: module 'os' has no attribute 'curdie'
>>> os.listdie(os.curdir)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    os.listdie(os.curdir)
AttributeError: module 'os' has no attribute 'listdie'
>>> os.listdir(os.curdir)
['$RECYCLE.BIN', '.temp', '1e3b6c01881321f4e1540eb5f6e06905', 'Adobe', 'Direct X', 'env', 'Games', 'hostd', 'kinggsoft', 'MCBox', 'messages', 'MyDrivers', 'Nier', 'Program Files (x86)', 'ProgramData', 'QLDownload', 'QLDownloadGame', 'QMDownload', 'qqpcmgr_docpro', 'qycache', 'System Volume Information', 'tencent', 'wegame', 'Windows Kits', '大一上', '大一下', '嵌入', '文件', '火线', '联盟', '英雄时刻']
>>> os.name
'nt'
>>> os.path.basename('E:\\Direct X\\DirectX_Repair-V3_8.zip')
'DirectX_Repair-V3_8.zip'
>>> os.path.dirname('E:\\Direct X\\DirectX_Repair-V3_8.zip')
'E:\\Direct X'
>>> os.path.join('A','B','C')
'A\\B\\C'
>>> os.path.split('E:\\Adobe')
('E:\\', 'Adobe')
>>> os.path.splitext('E:\\ProgramData')
('E:\\ProgramData', '')
>>> os.path.getatime('E:\\鸡你太美')
1565139729.5567799
>>> import time
>>> time.gmtime(os.path.getatime('E:\\鸡你太美'))
time.struct_time(tm_year=2019, tm_mon=8, tm_mday=7, tm_hour=1, tm_min=2, tm_sec=9, tm_wday=2, tm_yday=219, tm_isdst=0)
>>> time.localtime(os.path.getatime('E:\\鸡你太美'))
time.struct_time(tm_year=2019, tm_mon=8, tm_mday=7, tm_hour=9, tm_min=2, tm_sec=9, tm_wday=2, tm_yday=219, tm_isdst=0)
>>> time.localtime(os.path.getatime('E:\\鸡你太美'))
time.struct_time(tm_year=2019, tm_mon=8, tm_mday=7, tm_hour=9, tm_min=2, tm_sec=9, tm_wday=2, tm_yday=219, tm_isdst=0)
>>> os.path.ismount('E:\\')
True
>>> 
