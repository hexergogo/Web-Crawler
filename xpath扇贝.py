import requests
from lxml import etree
with open('xpath扇贝.txt','a',encoding='utf-8') as f:
    for i in range(4):
        url = 'https://www.shanbay.com/wordlist/110521/232414/?page={}'.format(i)
        req = requests.get(url).text
        content = etree.HTML(req)
        words = content.xpath('//tr[@class="row"]')

        for j in words:
            word = j.xpath('.//strong/text()')
            trans = j.xpath('./td[@class="span10"]/text()')

            f.write('* '+word[0]+' *\n')
            f.write(trans[0].replace('\n','')+'\n\n')

