# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl


class JobuiPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = '赶集网职位爬取'
        self.sheet.append(['公司', '岗位', '地址', '其他信息'])

    def process_item(self, item, spider):
        line = [item['company_name'], item['job_title'], item['location'], item['description']]
        self.sheet.append(line)
        return item

    def close_spider(self,spider):
        self.wb.save('./jobui.xlsx')
        self.wb.close()

