Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> 
=================== RESTART: D:/Python/2019-8-18-OOX-2.py ===================
Traceback (most recent call last):
  File "D:/Python/2019-8-18-OOX-2.py", line 35, in <module>
    download__mm();
NameError: name 'download__mm' is not defined
>>> 
=================== RESTART: D:/Python/2019-8-18-OOX-2.py ===================
Traceback (most recent call last):
  File "D:/Python/2019-8-18-OOX-2.py", line 35, in <module>
    download__MM();
NameError: name 'download__MM' is not defined
>>> 
=================== RESTART: D:/Python/2019-8-18-OOX-2.py ===================
>>> 
Traceback (most recent call last):
  File "D:/Python/2019-8-18-OOX-2.py", line 35, in <module>
    download__MM();
NameError: name 'download__MM' is not defined
>>> 
=================== RESTART: D:/Python/2019-8-18-OOX-2.py ===================
Traceback (most recent call last):
  File "D:/Python/2019-8-18-OOX-2.py", line 35, in <module>
    download_MM();
  File "D:/Python/2019-8-18-OOX-2.py", line 26, in download_MM
    page_num = int(get_page(url))
  File "D:/Python/2019-8-18-OOX-2.py", line 7, in get_page
    response = ur.uropen(url)
AttributeError: module 'urllib.request' has no attribute 'uropen'
>>> 
=================== RESTART: D:/Python/2019-8-18-OOX-2.py ===================
Traceback (most recent call last):
  File "D:/Python/2019-8-18-OOX-2.py", line 35, in <module>
    download_MM();
  File "D:/Python/2019-8-18-OOX-2.py", line 22, in download_MM
    os.mkdir(folder)
FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'OOXX'
>>> 
=================== RESTART: D:/Python/2019-8-18-OOX-2.py ===================
Traceback (most recent call last):
  File "D:/Python/2019-8-18-OOX-2.py", line 35, in <module>
    download_MM();
  File "D:/Python/2019-8-18-OOX-2.py", line 26, in download_MM
    page_num = int(get_page(url))
  File "D:/Python/2019-8-18-OOX-2.py", line 7, in get_page
    response = ur.urlopen(url)
  File "D:\Python\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "D:\Python\lib\urllib\request.py", line 523, in open
    req = meth(req)
  File "D:\Python\lib\urllib\request.py", line 1240, in do_request_
    raise URLError('no host given')
urllib.error.URLError: <urlopen error no host given>
>>> 
