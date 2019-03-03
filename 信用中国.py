import requests,re,random,json,os
from urllib import parse

base_url = "https://www.creditchina.gov.cn/api/credit_info_search?"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko)"}
# proxy_list = [
    # {'http':'59.62.167.44:808',"https":'116.209.53.2:9999'},
    # {'http':'115.171.202.213:9000','https':'121.61.27.229:9999'},
    # {'http':'1.192.245.17:9999','https':'221.218.102.254:9000'},
    # {'http':'125.123.139.175:9999','https':'	59.62.165.73:808'},
    # {'https':'61.183.176.122:53281','http':'116.209.53.81:9999'},
    # {'https':'116.209.56.159:9999','http':'60.216.101.46:59351'}
# ]
# proxy = random.choice(proxy_list)
def urltwo(encryStr):
    url_two   = "https://www.creditchina.gov.cn/api/credit_info_detail?encryStr={}".format(encryStr)
    content_two = requests.request('get',url=url_two,headers=headers).content.decode('utf-8')
    try:
        content_two = json.loads(content_two)
        entName = content_two["result"]["entName"]
        creditCode = content_two["result"]["creditCode"]
        dom = content_two["result"]["dom"]
        timestatmp = content_two["timestatmp"]
        regno = content_two["result"]["regno"]
        legalPerson = content_two["result"]["legalPerson"]
        esdate = content_two["result"]["esdate"]
        enttype = content_two["result"]["enttype"]
        regorg = content_two["result"]["regorg"]
        print("- - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - -  -")
        print(entName+'\n'+"统一社会信用代码："+creditCode+'\n'+"地址："+dom+'\n'+'报告查看时间：'+timestatmp)
        print("工商注册号："+regno+'\n'+"法人信息："+legalPerson+'\n'+"成立日期："+esdate+'\n'+"企业类型："+enttype+'\n'+'登记机关：'+regorg)
    except:
        pass

def urlthree(name):
    url_three = "https://www.creditchina.gov.cn/api/pub_permissions_name?name={}&page=1&pageSize=10".format(name)
    content_three = requests.request('get',url=url_three,headers=headers).content.decode('utf-8')
    try:
        content_three = json.loads(content_three)
        if content_three["result"]["results"]!=[]:
            xkWsh = content_three["result"]["results"][0]["xkWsh"]
            xkSplb = content_three["result"]["results"][0]["xkSplb"]
            xkFr = content_three["result"]["results"][0]["xkFr"]
            xkNr = content_three["result"]["results"][0]["xkNr"]
            xkYxq = content_three["result"]["results"][0]["xkYxq"]
            xkJdrq = content_three["result"]["results"][0]["xkJdrq"]
            xkJzq = content_three["result"]["results"][0]["xkJzq"]
            xkDfbm = content_three["result"]["results"][0]["xkDfbm"]
            xkXzjg = content_three["result"]["results"][0]["xkXzjg"]
            xkSjc = content_three["result"]["results"][0]["xkSjc"]
            print("行政许可决定书文号："+xkWsh+'\n'+"审核类型：："+xkSplb+'\n'+"法人代表人姓名："+xkFr+'\n'+'内容许可：'+"营业执照"+'\n'+"许可有效期："+xkYxq)
            print("许可决定日期："+xkJdrq+"         许可截止日期："+xkJzq+'\n'+"地方编码："+xkDfbm+'\n'+"许可机关："+xkXzjg+'\n'+"数据更新时间:"+xkSjc)
            print("- - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print("%s:行政许可为空"%name)
    except:
        pass

def urlfour(name):
    url_four = "https://www.creditchina.gov.cn/api/pub_penalty_name?name={}&page=1&pageSize=10".format(name)
    content_four = requests.request('get',url=url_four,headers=headers).content.decode('utf-8')
    try:
        content_four = json.loads(content_four)
        if content_four["result"]["results"]==[]:
            print("%s：没有行政处罚"%name)
        else:
            cfWsh = content_four["result"]["results"][0]["cfWsh"]
            cfCfmc = content_four["result"]["results"][0]["cfCfmc"]
            cfSy = content_four["result"]["results"][0]["cfSy"]
            cfJg =  content_four["result"]["results"][0]["cfJg"]
            cfXzjg = content_four["result"]["results"][0]["cfXzjg"]
            print("决定书文号："+cfWsh+'\n'+"处罚名称："+cfCfmc+'\n'+"处罚事由："+cfSy+'\n'+"处罚结果"+cfJg+'\n'+"处罚机关："+cfXzjg+'\n')
    except:
        pass

def chinazx(keyword):
    data = {
        "keyword":keyword,
        "templateId":"",
        # "page":"3",
        "pageSize":"10",
            }
    data_str = parse.urlencode(data)
    content = requests.request('get',url=base_url,headers=headers,params=data_str).content.decode('utf-8')
    req = re.findall(r'{"name":.*?}',content)
    for data in req:
        name_all= re.findall(r'"name":"(.*?)"',data)
        encryStr_all= re.findall(r'encryStr":"(.*?)\\n"',data)
        name=name_all[0]
        encryStr = encryStr_all[0]

        urltwo(encryStr)
        urlthree(name)
        urlfour(name)
if __name__ == '__main__':
    keyword = input("请输入要查的公司名:")
    chinazx(keyword)


