import requests,re
from 模块.UA import UserAgent
from lxml import etree

class MUban():
    def __init__(self,url):
        self.html = self.request_url(url)
        self.parse_html()

    def request_url(self,url):
        headers = {
            'User-Agent': UserAgent()
        }
        html = requests.get(url,headers=headers).content.decode('utf-8')
        tree = etree.HTML(html)
        #tree = re.findall(r'',html)
        return tree

    def parse_html(self):
        diqu_link = self.html.xpath('//div[@class="sub_nav section_sub_nav"]//a/@href')
        diqu_name = self.html.xpath('//div[@class="sub_nav section_sub_nav"]//a/@title')

        with open('链家.txt','a',encoding='utf-8') as f:

            for i,j in zip(diqu_link,diqu_name):
                f.write('*************************{}**********************'.format(j)+'\n')

                if i[:5] != 'https':url = 'https://bj.lianjia.com'+i
                else:url = i

                for page in range(1,60):
                    f.write('####################第{}页#################'.format(page)+'\n')

                    urls = url + 'pg{}/'.format(page)
                    f.write(urls+'\n')

                    diqu_liebiaos = self.request_url(urls)
                    li = diqu_liebiaos.xpath('//div[@class="info clear"]')

                    for houseinfo in li:
                        housename = houseinfo.xpath('./div[@class="title"]/a/text()')[0]
                        f.write('房屋名称：'+housename+'\n')
                        houseinfo1 = houseinfo.xpath('./div[@class="address"]/div//text()')
                        houseinfo1 = '/'.join(houseinfo1)
                        f.write(houseinfo1+'\n')
                        houseinfo2 = houseinfo.xpath('./div[@class="flood"]//text()')
                        houseinfo2 = ''.join(houseinfo2)
                        f.write(houseinfo2+'\n')
                        houseinfo3 = houseinfo.xpath('./div[@class="followInfo"]//text()')
                        f.write(''.join(houseinfo3[:3])+'\n')
                        f.write('/'.join(houseinfo3[3:-5])+'\n')
                        f.write('/'.join(houseinfo3[-5:])+'\n\n\n')


if __name__ == '__main__':
    url = 'https://bj.lianjia.com/ershoufang/'
    MUban(url)