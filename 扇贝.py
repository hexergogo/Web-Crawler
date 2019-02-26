import requests,re
with open('扇贝.txt','a',encoding='utf-8') as f:
    for i in range(4):
        url = 'https://www.shanbay.com/wordlist/110521/232414/?page={}'.format(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        req = requests.get(url,requests).text
        words =  re.findall(r'<tr class="row">(.*?)</tr>',req,re.S)
        for j in words:
            word = re.findall(r'<strong>(.*?)</strong>',j)
            trans = re.findall(r'<td class="span10">(.*?)</td>',j,re.S)
            f.write('* '+word[0]+' *\n')
            f.write(trans[0].replace('\n','')+'\n\n')