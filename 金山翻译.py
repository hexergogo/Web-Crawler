from urllib import parse,request
import json


class Translate():
    def __init__(self,word):
        self.word = word
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        self.data = {'f': 'auto','t': 'auto','w': self.word}
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'

    def reptile(self,):
        data_str = parse.urlencode(self.data)
        req = request.Request(url=self.url, headers=self.headers, data=bytes(data_str, encoding='utf-8'))
        response = request.urlopen(req).read().decode('utf-8')
        str = json.loads(response)
        return str

    def show(self):
        re = self.reptile()
        fy = re['content']
        if re['status'] == 0:
            word_mean = re['content']['word_mean']
            print('单词：' + self.word)
            print('美[{}]'.format(fy['ph_en']), end='  ')
            print('英[{}]'.format(fy['ph_am']))
            for i in word_mean:
                print(i)

        if re['status'] == 1:
            print('英语为：'+fy['out'])



while True:
    word = input('请输入单词：')
    a = Translate(word)
    a.show()




