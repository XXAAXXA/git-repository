import scrapy
from bs4 import BeautifulSoup
from ..items import JobuiItem


class JobuiSpider(scrapy.Spider):
    name = 'jobui'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, res):
        soup = BeautifulSoup(res.text, 'html.parser')
        company_list = soup.find_all(class_='textList')
        for companys in company_list:
            links = companys.find_all('a')
            for link in links:
                href = link['href']
                job_link = 'https://www.jobui.com{}jobs/'.format(href)
                yield scrapy.Request(job_link, callback=self.parse_job)

    def parse_job(self, res):
        soup = BeautifulSoup(res.text, 'html.parser')

        name = soup.find(id='companyH1').text

        jobs = soup.find_all(class_='c-job-list')
        for job in jobs:
            item = JobuiItem()
            item['company_name'] = name
            item['job_title'] = job.find('a').find('h3').text
            item['location'] = job.find_all('span')[0].text
            item['description'] = job.find_all('span')[1].text
            yield item
