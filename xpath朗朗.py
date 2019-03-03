import requests
from lxml import etree
response = requests.get(url='http://www.langlang2017.com').content.decode('utf-8')
tree = etree.HTML(response)
# li_list = tree.xpath('//div[@class="banner_box"]/ul/li')
# for li in li_list:
#     src = li.xpath('./img/@src')
#     alt = li.xpath('')
#     print(src[0],alt[0])
# meta = tree.xpath('//meta/@content')
meta = tree.xpath('//div[@class="beian"]//text()')
print(meta)

