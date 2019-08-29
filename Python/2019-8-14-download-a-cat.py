import urllib.request as ur

response = ur.urlopen('http://placekitten.com/g/500/600')
cat_img = response.read()


##另一种方式，urlopen实则执行这两句
#req = urllib.request.Request('http://placekitten.com/g/500/600')
#response = urllib.request.urlopen(req)
#cat_img = response.read()



##图片也是文件也是二进制写成的，将所搜到的数据写入jpg格式文件
with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
    
