#建好亚洲文件夹
import requests,os
from lxml import etree
#亚
# url='http://94srs.com/94xx/01/yazhoutupian/'

url='http://94srs.com/94xx/01/jbtaotu/'

req=requests.get(url=url).content.decode('gb18030')
tree=etree.HTML(req)
url_data=tree.xpath('//a[@class="title"]/@href')
k=1
for i in url_data:
    url='http://94srs.com'+i
    req1=requests.get(url=url).content.decode('gb18030')
    tree1=etree.HTML(req1)
    img=tree1.xpath('//div[@class="container"]//img/@src')[1:]
    for j in img:
        img_data=requests.get(url=j).content
        with open('爬爬网/套图/{}.jpg'.format(k),'wb') as fq:
            fq.write(img_data)
            k+=1