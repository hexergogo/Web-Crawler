import requests,re
url = 'https://maoyan.com/board'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
req = requests.get(url,headers).text


movies = re.findall(r'<dd>.*?</dd>',req,re.S)
with open('猫眼电影txt','a',encoding='utf-8') as f:
    for i in movies:
        #筛选规则
        rank = re.findall(r'<i.*?>(.*?)</i>',i)
        title = re.findall(r'<a.*?>(.*?)</a>',i)
        actor = re.findall(r'<p class="star">(.*?)</p>',i,re.S)
        time = re.findall(r'<p class="releasetime">(.*?)</p>',i)
        img = re.findall(r'src="(https.*?)"',i)
        #写入
        f.write('*******'+'排名：'+rank[0]+','+'评分：'+rank[1]+rank[2]+'*******'+'\n')
        f.write('电影名称:《'+title[0]+'》'+'\n')
        f.write(actor[0].strip()+'\n')
        f.write(time[0]+'\n')
        f.write('海报:'+img[0]+'\n\n\n')




