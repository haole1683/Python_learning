Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.requst
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import urllib.requst
ModuleNotFoundError: No module named 'urllib.requst'
>>> import urllib.request
>>> 
>>> import urllib.request as ur
>>> response = ur.urlopen('http://www.fishc.com')
>>> html = response.read()
>>> print(html)
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta name="keywords" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4|\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Python\xe6\x95\x99\xe5\xad\xa6|Web\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|\xe5\x85\xa8\xe6\xa0\x88\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|C\xe8\xaf\xad\xe8\xa8\x80\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe6\x95\x99\xe5\xad\xa6|Win32\xe5\xbc\x80\xe5\x8f\x91|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux\xe6\x95\x99\xe5\xad\xa6">\n<meta name="description" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4\xe4\xb8\xba\xe5\xa4\xa7\xe5\xae\xb6\xe6\x8f\x90\xe4\xbe\x9b\xe6\x9c\x80\xe6\x9c\x89\xe8\xb6\xa3\xe7\x9a\x84\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6\xe3\x80\x82">\n<meta name="author" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4">\n<title>\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4-\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Python\xe6\x95\x99\xe5\xad\xa6|Web\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|\xe5\x85\xa8\xe6\xa0\x88\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|C\xe8\xaf\xad\xe8\xa8\x80\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe6\x95\x99\xe5\xad\xa6|Win32\xe5\xbc\x80\xe5\x8f\x91|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux\xe6\x95\x99\xe5\xad\xa6</title>\n<link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">\n<link rel="stylesheet" href="css/styles.css">\n<script src="js/jq.js"></script>\n<script src="js/fishcEgg.js"></script>\n<script>\n        $(document).ready(function() {\n            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;\n\n            createStoryJS({\n                type:       \'timeline\',\n                width:      \'auto\',\n                height:     windowHeight,\n                source:     \'data.json\',\n                start_at_end:true,                          //OPTIONAL START AT LATEST DATE\n                embed_id:   \'my-timeline\'\n            });\n\n            // \xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe5\x88\xa4\xe6\x96\xad\xef\xbc\x8c\xe5\xa6\x82\xe6\x9e\x9c\xe6\x98\xafIE\xe5\xbc\xb9\xe5\x87\xba\xe6\x8f\x90\xe7\xa4\xba\xe6\xa1\x86\n            function getExplore(){\n                var Sys = {};\n                var ua = navigator.userAgent.toLowerCase();\n                var s;\n                (s = ua.match(/rv:([\\d.]+)\\) like gecko/)) ? Sys.ie = s[1] :\n                    (s = ua.match(/msie ([\\d\\.]+)/)) ? Sys.ie = s[1] :\n                        (s = ua.match(/edge\\/([\\d\\.]+)/)) ? Sys.edge = s[1] :\n                            (s = ua.match(/firefox\\/([\\d\\.]+)/)) ? Sys.firefox = s[1] :\n                                (s = ua.match(/(?:opera|opr).([\\d\\.]+)/)) ? Sys.opera = s[1] :\n                                    (s = ua.match(/chrome\\/([\\d\\.]+)/)) ? Sys.chrome = s[1] :\n                                        (s = ua.match(/version\\/([\\d\\.]+).*safari/)) ? Sys.safari = s[1] : 0;\n                // \xe6\xa0\xb9\xe6\x8d\xae\xe5\x85\xb3\xe7\xb3\xbb\xe8\xbf\x9b\xe8\xa1\x8c\xe5\x88\xa4\xe6\x96\xad\n                if (Sys.ie) alert(\'\xe8\xaf\xb7\xe4\xbd\xbf\xe7\x94\xa8\xe9\x9d\x9eIE\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe6\x89\x93\xe5\xbc\x80\xe6\x9c\xac\xe4\xb8\xbb\xe9\xa1\xb5\');\n\n            }\n            getExplore();\n\n        });\n    </script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/timelinejs/2.36.0/js/storyjs-embed.js"></script>\n</head>\n<body>\n<a href=\'http://fishc.taobao.com\' target=\'_blank\' style="position: absolute;z-index: 99999;"><img style="position: fixed; top: 15px; right: 0; border: 0;" src="img/fork.png" alt="Support Thanks"></a>\n<div id="my-timeline"></div>\n<script>\n    window.onload = function(){\n        $(".storyjs-embed.sized-embed").css("padding-top","0");\n        $(".vco-storyjs .vco-feature .vco-slide").css("padding-top","0");\n    };\n\n</script>\n</body>\n</html>'
>>> html = html.decode('utf-8')
>>> print(html)
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="keywords" content="鱼C工作室|免费编程视频教学|Python教学|Web开发教学|全栈开发教学|C语言教学|汇编教学|Win32开发|加密与解密|Linux教学">
<meta name="description" content="鱼C工作室为大家提供最有趣的编程视频教学。">
<meta name="author" content="鱼C工作室">
<title>鱼C工作室-免费编程视频教学|Python教学|Web开发教学|全栈开发教学|C语言教学|汇编教学|Win32开发|加密与解密|Linux教学</title>
<link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">
<link rel="stylesheet" href="css/styles.css">
<script src="js/jq.js"></script>
<script src="js/fishcEgg.js"></script>
<script>
        $(document).ready(function() {
            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;

            createStoryJS({
                type:       'timeline',
                width:      'auto',
                height:     windowHeight,
                source:     'data.json',
                start_at_end:true,                          //OPTIONAL START AT LATEST DATE
                embed_id:   'my-timeline'
            });

            // 浏览器判断，如果是IE弹出提示框
            function getExplore(){
                var Sys = {};
                var ua = navigator.userAgent.toLowerCase();
                var s;
                (s = ua.match(/rv:([\d.]+)\) like gecko/)) ? Sys.ie = s[1] :
                    (s = ua.match(/msie ([\d\.]+)/)) ? Sys.ie = s[1] :
                        (s = ua.match(/edge\/([\d\.]+)/)) ? Sys.edge = s[1] :
                            (s = ua.match(/firefox\/([\d\.]+)/)) ? Sys.firefox = s[1] :
                                (s = ua.match(/(?:opera|opr).([\d\.]+)/)) ? Sys.opera = s[1] :
                                    (s = ua.match(/chrome\/([\d\.]+)/)) ? Sys.chrome = s[1] :
                                        (s = ua.match(/version\/([\d\.]+).*safari/)) ? Sys.safari = s[1] : 0;
                // 根据关系进行判断
                if (Sys.ie) alert('请使用非IE浏览器打开本主页');

            }
            getExplore();

        });
    </script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/timelinejs/2.36.0/js/storyjs-embed.js"></script>
</head>
<body>
<a href='http://fishc.taobao.com' target='_blank' style="position: absolute;z-index: 99999;"><img style="position: fixed; top: 15px; right: 0; border: 0;" src="img/fork.png" alt="Support Thanks"></a>
<div id="my-timeline"></div>
<script>
    window.onload = function(){
        $(".storyjs-embed.sized-embed").css("padding-top","0");
        $(".vco-storyjs .vco-feature .vco-slide").css("padding-top","0");
    };

</script>
</body>
</html>
>>> 
