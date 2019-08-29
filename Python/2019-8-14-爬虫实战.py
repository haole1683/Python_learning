Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: D:/Python/2019-8-14-download-a-cat.py ===============
>>> 
=============== RESTART: D:/Python/2019-8-14-download-a-cat.py ===============
>>> response.geturl()
'http://placekitten.com/g/500/600'
>>> response.info()
<http.client.HTTPMessage object at 0x000001C3AC742488>
>>> print(response.info())
Date: Wed, 14 Aug 2019 00:54:34 GMT
Content-Type: image/jpeg
Transfer-Encoding: chunked
Connection: close
Set-Cookie: __cfduid=d0047bb2e232ec7ab79589bec68bd4ecd1565744074; expires=Thu, 13-Aug-20 00:54:34 GMT; path=/; domain=.placekitten.com; HttpOnly
Access-Control-Allow-Origin: *
Cache-Control: public, max-age=86400
Expires: Thu, 15 Aug 2019 00:54:34 GMT
CF-Cache-Status: HIT
Age: 62085
Vary: Accept-Encoding
Server: cloudflare
CF-RAY: 505ef54fbf59ddc3-SIN


>>> ##包含远程服务器的head信息
>>> 
>>> response.getcode()
200
>>> 
