from gevent import monkey
monkey.patch_all()
from bs4 import BeautifulSoup
from gevent.queue import Queue
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
import gevent, requests, openpyxl

url_list = ['http://www.mtime.com/top/tv/top100/']

# requests 头，cookie会过期
headers = {
    'Cookie': '_userCode_=2020491647431658; _userIdentity_=2020491647437823; _tt_=4765DED62DCDDF900C7D0ABB08E463DC; DefaultCity-CookieKey=292; DefaultDistrict-CookieKey=0; __utmz=196937584.1586422064.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); waf_cookie=00c34c67-c8db-4e295e30688a80ba92f90723364c7bc1c9bd; __utma=196937584.127199715.1586422064.1586422064.1586428529.2; __utmc=196937584; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1586422064,1586428529; _ydclearance=088838805fb33ef0f4ae103d-d3e9-46d7-911d-b189169d5c17-1586436704; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1586429505; __utmt=1; __utmt_~1=1; __utmb=196937584.4.10.1586428529',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }

task_list = []  # 多协程任务列表

# 创建excel表格
movie_excel = [['排名', '电影名', '导演', '演员', '简介']]
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '时光电影TOP100'

for page in range(2,11):
    url_list.append('http://www.mtime.com/top/tv/top100/index-{}.html'.format(page))

# 将网址加入队列
work = Queue()
for url in url_list:
    work.put_nowait(url)


# 定义爬虫函数
def crawler():
    while not work.empty():  # 队列不为空时
        url = work.get_nowait()
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        movie_list = soup.find(id='asyncRatingRegion')
        movies = movie_list.find_all('li')

        for movie in movies:
            name = movie.find('a')
            num = movie.find('div')
            info = movie.find_all('p')

            print('No.' + num.text)
            print('电影名' + name['title'])

# 由于有些电影没有导演、演员、简介，所以加入try语句
            try:
                director = info[0].find('a')
                dir_ = ILLEGAL_CHARACTERS_RE.sub(r'', director.text)  # 可能有非法字符
            except Exception:
                dir_ = '无'

            try:
                actor = info[1].find('a')
                actor_ = ILLEGAL_CHARACTERS_RE.sub(r'', actor.text)
            except Exception:
                actor_ = '无'

            try:
                brief = info[2]
                brief_ = ILLEGAL_CHARACTERS_RE.sub(r'', brief.text)
            except Exception:
                brief_ = '无'

            movie_excel.append([num.text, name['title'], dir_, actor_, brief_])


            print('-------------\n')


# 相当于两个爬虫同时进行
for x in range(2):
    task = gevent.spawn(crawler)
    task_list.append(task)

# 执行任务
gevent.joinall(task_list)

for row in movie_excel:
    sheet.append(row)

# 保存excel
wb.save('时光电影TOP100,2.0.xlsx')