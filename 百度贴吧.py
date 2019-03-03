from urllib import request,parse

# response = request.urlopen('http://www.jd.com')
# content = response.read()
# html = content.decode('utf-8')
# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# req = request.Request(url='http://www.baidu.com',headers=header)
# html = request.urlopen(req).read().decode('utf-8')
# with open('d:/baidu.html','w',encoding='utf-8') as f:
#     f.write(html)


#

name = input('请输入贴吧名称：')
i=1
while i <= 10:
    num = (i-1)*50
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    data = {
        'ie':'utf-8',
        'kw':name,
        'fr':'search',
        'pn':num
    }
    str = parse.urlencode(data)
    req = request.Request(url='http://tieba.baidu.com/f?{}'.format(str),headers=headers)
    html = request.urlopen(req).read().decode('utf-8')
    with open('{}吧第{}页.html'.format(name,i),'w',encoding='utf-8') as f:
        f.write(html)
    i += 1

    str= parse.urlencode()
