import requests
from lxml import etree

class Wangyiyun():
    def __init__(self,url):
        self.html = self.request_url(url)
        self.parse_html()

    def request_url(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        html = requests.get(url,headers=headers).content.decode('utf-8')
        tree = etree.HTML(html)
        return tree

    def parse_html(self):
        type_name = self.html.xpath('//div[@class="blk"]//a/text()')
        type_link = self.html.xpath('//div[@class="blk"]//a/@href')
        for i,j in zip(type_name,type_link):
            print('*****************************{}**************************'.format(i))
            type_url = 'https://music.163.com'+j
            type_content = self.request_url(type_url)
            name_types = type_content.xpath('//ul[@class="n-ltlst f-cb"]//a/@href')
            for name_type in name_types:
                name_type_url = 'https://music.163.com'+name_type
                singer_names = self.request_url(name_type_url)
                singer_name_list = singer_names.xpath('//ul[@class="m-cvrlst m-cvrlst-5 f-cb"]//a/text()')
                for name in singer_name_list:
                    print(name,end='   ')
            print()

if __name__ == '__main__':
    url = 'https://music.163.com/discover/artist/'
    Wangyiyun(url)