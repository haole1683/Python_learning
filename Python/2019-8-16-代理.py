import urllib.request as ur
import random


url = 'http://45.32.164.128/ip.php'

#推荐这个http://45.32.164.128/ip.php，直接返回ip，找了好久找到了
#这个网站不行的，试试这个http://ip.chinaz.com/getip.aspx
#这里给个地址： https://www.kuaidaili.com/free/
#2018-07  新的查ip地址  http://ip.chinaz.com/getip.aspx
#亲测可用查IP：www.soshoulu.com/
#2018-8-7 分享一个ip:121.69.70.182:8118

iplist = ['58.247.127.145:53281','58.247.127.145:53281','119.57.108.89:53281','119.90.126.106:7777','124.205.155.152:9090']

proxy_support = ur.ProxyHandler({'http':'189.112.246.145:8080'})

opener = ur.build_opener(proxy_support)
opener.addheaders =[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36; 360Spider')]

ur.install_opener(opener)

response = ur.urlopen(url)
html = response.read().decode('utf-8')

print(html)
