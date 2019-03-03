from urllib import request
import json

types = {'剧情':11,'戏剧':24,'动作':5,'爱情':13,'科幻':17,'动画':25,'悬疑':10,'惊悚':19,'恐怖':20,'纪录片':1,'短片':23,'情色':6,'同性':26,'音乐':14,'歌舞':7,'家庭':28,'儿童':8,'传记':2,'历史':4,'战争':22,'罪犯':3,'西部':27,'奇幻':16,'冒险':15,'灾难':12,'武侠':29,'古装':30,'运动':18,'黑色电影':31}

with open('豆瓣全.txt','a+',encoding='utf-8') as f:
    for k1,v1 in types.items():
        f.write('-----------------{}-----------------'.format(k1)+'\n')
        url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start=0&limit=10000000'.format(v1)
        req = json.loads(request.urlopen(url).read().decode('utf-8'))
        for i in req:
            for k,v in i.items():
                if k == 'rating':
                    f.write('********'+'星级为'+str(int(v[1])/10)+','+'评分为'+str(v[0])+',')
                if k == 'rank':
                    f.write('排名:第'+str(v)+'名'+'********'+'\n')
                if k == 'cover_url':
                    f.write('封面地址为：'+v+'\n')
                if k == 'types':
                    f.write('类型为：')
                    for type in v:
                        f.write(type+'、')
                    f.write('\n')
                if k == 'title':
                    f.write('电影名称：《'+v+'》'+'\n')
                if k == 'url':
                    f.write('详情地址：'+v+'\n')
                if k == 'release_date':
                    f.write('上映时间：'+v+'\n')
                if k == 'actors':
                    f.write('演员：')
                    for actors in v:
                        f.write(actors+'、')
                    f.write('\n')
            f.write('\n\n')



