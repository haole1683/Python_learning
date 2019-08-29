##隐藏
import urllib.request as ur
import urllib.parse as up
import json

content = input('请输入翻译内容')
url = 'http://fanyi.youdao.com/translate?_osmartresult=dict&smartresult=rule'

head = {}
head['User-Agemt'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

data = {}

data['type']:'AUTO'
data['i']  = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'

data = up.urlencode(data).encode('utf-8')
##encode 将uncion变成指定编码形式，这里就是变成utf - 8形式

req = ur.Request(url,data,head)
response = ur.urlopen(req)


html = response.read().decode('utf-8')##将其他编码形式变成uniciion形式


target = json.loads(html)
target = target['translateResult'][0][0]['tgt']

print(target)
