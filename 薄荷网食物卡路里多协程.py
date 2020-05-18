from gevent import monkey

monkey.patch_all()
import gevent, requests, csv
from bs4 import BeautifulSoup
from gevent.queue import Queue

work = Queue()

# 前3个常见食物分类的前3页的食物记录的网址：
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)

# 第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1, 4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)


# 请写出crawler函数和启动协程的代码：
def crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    while not work.empty():
        url = work.get_nowait()

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        food_list = soup.find_all('li', class_='item clearfix')
        for food in food_list:
            name = food.find_all('a')[1]['title']
            href = food.find_all('a')[1]['href']
            link = 'http://www.boohee.com' + href
            calorie = food.find('p').text

            print(name)
            print(link)
            print(calorie)


tasks_list = []
for x in range(2):
    task = gevent.spawn(crawler)
    tasks_list.append(task)

gevent.joinall(tasks_list)