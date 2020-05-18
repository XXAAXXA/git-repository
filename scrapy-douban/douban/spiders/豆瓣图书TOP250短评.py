import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domain = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0', 'https://book.douban.com/top250?start=25']

    def parse(self,res):
        soup = BeautifulSoup(res.text, 'html.parser')
        books = soup.find_all(class_='pl2')
        for book in books:
            book_link = book.find('a')['href']
            comments_link = book_link + 'comments/hot?p=1'

            yield scrapy.Request(comments_link, callback=self.comment_parse)  # 进入下个页面

    def comment_parse(self,res):
        soup = BeautifulSoup(res.text, 'html.parser')
        name = soup.find(id='content').find('h1').text
        comments = soup.find_all(class_='comment-item')

        for comment in comments:
            item = DoubanItem()
            item['name'] = name
            item['user_id'] = comment.find('a')['title']
            item['content'] = comment.find('p').text

            yield item

