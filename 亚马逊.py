import requests
from lxml import etree

class YMX():
    def __init__(self,url,page):
        self.http = self.getHttp(url,page)
        self.parse_html()


    def getHttp(self,url,page):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        data = {
            'pageNumber':page
        }
        http = requests.get(url,headers=headers,params=data).content.decode('utf-8')
        tree = etree.HTML(http)
        return tree

    def parse_html(self):
        reviews = self.http.xpath('//div[@class="a-section celwidget"]')
        for review in reviews:
            reviewer = review.xpath('.//span[@class="a-profile-name"]/text()')[0]
            score = review.xpath('.//span[@class="a-icon-alt"]/text()')[0][:3]
            title = review.xpath('.//a[@data-hook="review-title"]/text()')[0]
            content = review.xpath('.//span[@data-hook="review-body"]/text()')[0]
            f.write('******************************'+'\n'+'用户：'+reviewer+'\n'+'评分：'+score+'\n'+'标题：'+title+'\n'+'评价内容：'+content+'\n\n')

if __name__ == '__main__':
    page = int(input('请输入需要爬取几页：'))
    with open('亚马逊.txt', 'a+', encoding='utf-8') as f:
        for i in range(1,page+1):
            url = 'https://www.amazon.com/product-reviews/B077J3RQLK/ref=cm_cr_getr_d_paging_btm_prev_{}?'.format(i)
            YMX(url,i)
