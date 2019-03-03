import requests,re,json,os
from lxml import etree
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Cookie': 'UM_distinctid=16929e66d927ca-053ca77f094186-1333062-1fa400-16929e66d938d7; CNZZDATA1274771516=719982047-1551184008-http%253A%252F%252Fwww.jdlingyu.com%252F%7C1551184008; Hm_lvt_4c0b4bd72dc090c1c4a836b68d5c4d4b=1551186168; Hm_lpvt_4c0b4bd72dc090c1c4a836b68d5c4d4b=1551187475'
}

for page in range(15,37):
    url = 'http://www.jdlingyu.mobi/wp-admin/admin-ajax.php?action=zrz_load_more_posts'
    data = {
    'type': 'catL1182', #'catL1181(日本写真13)'  'catL1182（国产套图）' ‘catL1183（cos套图7）’
    'paged': page
    }
    req = requests.request('post',url=url,data=data,headers=headers).content
    req = json.loads(req)['msg']
    links = re.findall(r'<a target="_blank" href="(.*?)"',req)
    for i in links:
        req = requests.get(url=i,headers=headers).content
        tree = etree.HTML(req)
        imgs = tree.xpath('//div[@id="content-innerText"]//img/@src')
        for j in imgs:
            img = requests.get(url=j,headers=headers).content
            with open('绝对领域/国内套图/{}'.format(j[-29:].replace('/','')),'wb') as f:
                f.write(img)