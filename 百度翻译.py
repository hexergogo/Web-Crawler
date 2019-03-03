from urllib import request,parse
import json
def translate(word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    data = {
        'kw':word
    }
    url = 'https://fanyi.baidu.com/sug'
    data_str = parse.urlencode(data)
    req = request.Request(url=url,data=bytes(data_str,encoding='utf-8'),headers=headers)
    response = request.urlopen(req).read().decode('utf-8')
    str = json.loads(response)
    return str

if __name__ == '__main__':
    while True:
        word = input('请输入单词：')
        re = translate(word)
        data = re['data']
        for i in data:
            for k,v in i.items():
                if k == 'k':
                    print('单词: '+v)
                else:
                    print('翻译: '+v)
            print()


