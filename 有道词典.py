from urllib import request,parse
import json,time,hashlib

def jiami(pw):
    md5 = hashlib.md5()
    md5.update(bytes(pw,encoding='utf-8'))
    result = md5.hexdigest()
    return result


def translate(word,ts,salt,sign):
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': '5933be86204903bb334bf023bf3eb5ed',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }

    data_str = parse.urlencode(data)
    ContentLength = len(data_str)

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': ContentLength,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=42474381@10.168.1.241; JSESSIONID=aaawRmNTElH3Q4_wUlzKw; OUTFOX_SEARCH_USER_ID_NCOO=1959109122.590772; ___rl__test__cookies=1550905970008',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    req = request.Request(url=url, data=bytes(data_str, encoding='utf-8'), headers=headers)
    content = request.urlopen(req).read().decode('utf-8')
    str = json.loads(content)
    return str


if __name__ == '__main__':
    while True:
        word = input('请输入单词：')
        salt = int(time.time() * 10000)
        ts = int(time.time() * 1000)
        value = "fanyideskweb" +word+ str(salt) + "p09@Bn{h02_BIEe]$P^nG"
        sign = jiami(value)
        re = translate(word,ts,salt,sign)

        try:
            if re['smartResult']['type'] == 1 :
                for i in re['smartResult']['entries']:
                    if i:
                        print(i[:-4])
        except:
            print(re['translateResult'][0][0]['tgt'])







