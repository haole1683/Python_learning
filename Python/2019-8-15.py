import urllib.request as ur
import urllib.parse as up

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}

data['i']:'I love fish '
data['from']:'AUTO'
data['to']:'AUTO'
data['smartresult']:'dict'
data['client']:'fanyideskweb'
data['salt']:'15658264372324'
data['sign']:'d03fae20fbcd82ee1caee60426678b4a'
data['ts']:'1565826437232'
data['bv']:'bbb3ed55971873051bc2ff740579bb49'
data['doctype']:'json'
data['version']:'2.1'
data['keyfrom']:'fanyi.web'
data['action']:'FY_BY_CLICKBUTTION'

data = up.urlencode(data).encode('utf-8')
##encode 将uncion变成指定编码形式，这里就是变成utf - 8形式


response = ur.urlopen(url,data)

html = response.read().decode('utf-8')##将其他编码形式变成uniciion形式

print(html)
