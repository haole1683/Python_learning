import urllib.request as ur
import urllib.parse as up
import json
import time

while True:
    content = input('请输入翻译内容(输入‘q!’退出程序)')
    if content == 'q!':
        break;
    
    url = "http://fanyi.youdao.com/translate"


    data = {}

    data['type']:'AUTO'
    data['i']  = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'

    data = up.urlencode(data).encode('utf-8')
    ##encode 将uncion变成指定编码形式，这里就是变成utf - 8形式

    req = ur.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')

    response = ur.urlopen(req)


    html = response.read().decode('utf-8')##将其他编码形式变成uniciion形式


    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print(target)
    time.sleep(5)

    ##隐藏修改header
    ##通过Request的headers 的参数
    ##通过Request.add_header()方法修改

    ##代理
