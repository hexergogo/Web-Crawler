import requests
from lxml import etree

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

with open('xpath糗百.txt','a',encoding='utf-8') as f:

    for i in range(10):
        url = 'https://www.qiushibaike.com/hot/page/{}/'.format(i)
        req = requests.get(url,headers=headers).content.decode('utf-8')
        content = etree.HTML(req)
        words = content.xpath('//div[@class="article block untagged mb15 typs_long"]|//div[@class="article block untagged mb15 typs_hot"]|//div[@class="article block untagged mb15 typs_old"]')

        for j in words:
            f.write('***************************************************'+'\n')

            #用户名
            try:
                user = j.xpath('./div[@class="author clearfix"]/a[2]//text()')[1].replace('\n','')
            except:
                f.write('匿名用户' + '\n')
            else:
                f.write(user + '\n')

            #内容
            content = j.xpath('./a[1]//text()')
            contents = ''.join(content).replace('\n','')
            f.write(contents + '\n')

            #图片
            pic = j.xpath('./div[@class="thumb"]//img/@src')
            if pic:
                f.write('图片链接：'+'https:'+pic[0]+'\n')
                reimg = requests.get(url='https:'+pic[0],headers=headers).content
                with open('xpath糗百/{}'.format(pic[0][-14:]),'wb') as f2 :
                    f2.write(reimg)

            #点赞与评论数
            like = j.xpath('.//span[@class="stats-vote"]//text()')
            likes = ''.join(like)
            re = j.xpath('.//span[@class="stats-comments"]//text()')
            res = str(re[4])+str(re[5])
            f.write(likes+'   '+res+'\n')

            #热评
            comment = j.xpath('./a[2]//text()')
            if comment:
                comments = ''.join(comment).replace('\n', '')
                f.write('神评：' + comments + '\n')
            else:
                f.write('无神评' + '\n')




