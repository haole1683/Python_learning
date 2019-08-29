import urllib.request as ur
import os

def get_page(url):
    req = ur.Request(url)
    req.add_header('User-Ages','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    response = ur.urlopen(url)
    html = response.read().decode('utf-8')

    a = html.find('current-comment-page') + 12
    b = html.finf(']',a)

    print(html[a:b])

def find_img(url):
    pass

def save_img(img_adds):
    pass

def download_MM(folder = 'OOXX',pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url =  'http:http://jandan.net/ooxx'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_img(page_url)
        save_img(img_adds)

if __name__ == '__main__':
    download_MM();
    
