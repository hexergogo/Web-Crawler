import requests,re
with open('果壳.txt','a',encoding='utf-8') as f:
    for i in range(1000):
        url = 'https://www.guokr.com/ask/highlight/?page={}'.format(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        req = requests.get(url,requests).text
        link = re.findall(r'<a target="_blank" href="(https://www.guokr.com/question/.*?)"',req)
        for j in link:
            title = re.findall(r'<a target="_blank" href="{}">(.*?)</a>'.format(j),req,re.S)
            f.write('文章标题：'+title[0].replace('\n','')+'\n')
            f.write('文章链接:'+j+'\n\n')

