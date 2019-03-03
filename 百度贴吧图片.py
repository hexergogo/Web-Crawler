import requests,re

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
'Cookie':'BAIDUID=58418F346970AAD30C04B2731CEC21BE:FG=1; BIDUPSID=58418F346970AAD30C04B2731CEC21BE; PSTM=1550982669; BDUSS=00UG8tTE93VkdIeHhFQkxQWGhGVjFDZWlrVkxJRlNaZVc1aGo1WUtRMTV2cGxjQVFBQUFBJCQAAAAAAAAAAAEAAACRTHER0KZlbXB0eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHkxclx5MXJcem; TIEBAUID=e1100a0da906767012b25593; STOKEN=5bf8d3fb9910178f754baee7571102e9ac1db2ba1509056755b2d9bae073931e; TIEBA_USERTYPE=9be462d3f99b227478ecef1d; BDRCVFR[S_ukKV6dOkf]=mk3SLVN4HKm; delPer=0; PSINO=2; H_PS_PSSID=1436_21104_26350_28415_27542; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1551077097,1551180581; 292637841_FRSVideoUploadTip=1; wise_device=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1551181033'
}

ba = input('请输入贴吧名：')
num = int(input('请输入需要爬取多少页：'))
page = (num-1)*50

url = 'http://tieba.baidu.com/f?'  #？以前的为基础url，？以后的是所需字段
data = {
'kw': ba,
'ie':'utf-8',
'pn': page
}

for i in range(1,num+1):  #对页进行循环第一页-第二页-第三页。。。
    req = requests.get(url,headers=headers,params=data).content.decode('utf-8')  #获取页面html

    divs = re.findall(r'<div class="threadlist_title pull_left j_th_tit ">(.*?)</div>',req,re.S)

    for j in divs:  #j代表每篇帖子
        link = re.findall(r'<a rel="noreferrer" href="(.*?)"',j)[0]  #获取a标签中的链接
        url = 'https://tieba.baidu.com'+link  #拼接链接
        req2 = requests.get(url=url,headers=headers).text  #通过链接获取详情页所有信息
        imgs = re.findall(r'<img class="BDE_Image" src="(.*?)"',req2)

        if imgs:  #有些帖子没有图片，所以需要判断一下
            for k in imgs:  #k代表每一张图片，每个帖子有很多张图片，所以需要通过循环取出每一张
                img = requests.get(url=k,headers=headers).content  #获取图片二进制信息
                with open('酷安吧/{}'.format(k[-10:]),'wb')as f: #用二进制写入的方法写入本地目录酷安吧/图片名
                    f.write(img)  #写入获取的img二进制信息







